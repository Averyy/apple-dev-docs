# Creating an Identity for Local Network TLS

**Framework**: Network

Learn how to create and use a digital identity in your application for local network TLS.

#### Overview

In the context of Transport Layer Security (TLS), a  is a cryptographic asset that contains a certificate and an associated private key for encrypting network traffic sent between a client and a server. Creating a digital identity for iOS or macOS is done so clients can communicate using TLS over the internet or a local network.

In this scenario, a server accepts client connections on a local network. While this article focuses on local network TLS, you can apply many of the concepts for other use cases. For example, setting up TLS with a certificate obtained from third-party Certificate Authority or configuring any system that needs to establish chain of trust to a root certificate.

##### Prepare the Environment

Imagine you’re building an app to handle orders in a restaurant. This app runs on a server device  — like an iPad or Mac — located at the front desk. Out in the restaurant, customers create and send orders to the server to be processed by the server using iOS client devices. In this situation, the server uses a digital identity from a local certificate authority to provide TLS to the clients. The following article explains how to setup both the server and client devices for local network TLS.

To create an identity for local network TLS the first thing you need to do is create and manage a local Certificate Authority (CA). A CA is a trusted entity that issues certificates for use in cryptographic operations. In this case, the CA serves as the trusted source of truth to issue a certificate that is used in a digital identity for TLS. Without this trusted authority, clients won’t be able to verify the issuer of the certificate they are using.

After creating the CA, you need to issue a leaf certificate for the digital identity that is installed on the server. Next, you need to distribute the identity to the server. In the restaurant example, this is either the macOS or iOS device acting as the server. Lastly, you also need to distribute the root certificate to all of the iOS client devices in the restaurant network so that they can establish the chain of trust during the handshake process, and trust evaluation doesn’t need to be overridden.

An overview of how this would work can be described as follows:

1. Create and manage your own certificate authority using the Keychain app on macOS.
2. Distribute the identity to the server. On macOS, either create and use an identity on the same machine the server is running on, or securely distribute the PKCS#12 file to the device Keychain. On iOS, import the PKCS#12 file onto the server device. For example, you could load the PKCS#12 file onto a thumb drive and import it to the iOS server app and save it in the Keychain.
3. On iOS client devices, install the root certificate onto the iOS device to form the chain of trust.

##### Distribute the Identity to the Server

On iOS, the certificate authority owner is faced with the challenge of distributing the identity to the server. After transferring the identity on the server — either through thumb drive or through secure network transfer — save it to the Keychain. To save the identity in the iOS Keychain, use the following:

```swift
let password = <# A password from the Keychain #>
let options = [kSecImportExportPassphrase: password ] as NSDictionary
var rawItems: CFArray?
let status = SecPKCS12Import(data as CFData, // Data from imported Identity.
                             options as CFDictionary,
                             &rawItems)

guard status == errSecSuccess,
      let items = rawItems,
      let dictionaryItems = items as? Array<Dictionary<String, Any>> else {
    // handle error …
}

let secIdentity: SecIdentity = dictionaryItems[0][kSecImportItemIdentity as String] as! SecIdentity

// Notice that kSecClass as String: kSecClassIdentity isn't used here as this is inferred from kSecValueRef.
let identityAddition = [
    kSecValueRef: secIdentity,
    kSecAttrLabel: "ListenerIdentityLabel"
] as NSDictionary

let identityStatus = SecItemAdd(identityAddition as CFDictionary, nil)

guard identityStatus == errSecSuccess else {
    // handle error …
}
// Added identity successfully.
```

To retrieve the identity from the iOS Keychain, use the following:

```swift
func getSecIdentity() -> SecIdentity? {

    // On the query, use kSecClassIdentity to make sure a SecIdentity is extracted.
    let identityQuery = [
        kSecClass: kSecClassIdentity,
        kSecReturnRef: true,
        kSecAttrLabel: "ListenerIdentityLabel"
    ] as NSDictionary
    var identityItem: CFTypeRef?
    let getIdentityStatus = SecItemCopyMatching(identityQuery as CFDictionary, &identityItem)

    guard getIdentityStatus == errSecSuccess else {
        // handle error …
    }
    let secIdentity = identityItem as! SecIdentity
    return secIdentity
}
```

With the local identity accessible from the Keychain, set it to [`NWListener`](nwlistener.md) to serve connections using TLS 1.2+ with the following:

```swift
let tlsOptions = NWProtocolTLS.Options()
let tlsParams = NWParameters(tls: tlsOptions, tcp: .init())

if let secIdentity = getSecIdentity(),
   let identity = sec_identity_create(secIdentity) {
    sec_protocol_options_set_min_tls_protocol_version(
        tlsOptions.securityProtocolOptions, .TLSv12)
    sec_protocol_options_set_local_identity(
        tlsOptions.securityProtocolOptions, identity)
} 
let listener = try NWListener(using: tlsParams, on: 4433)
```

On macOS, the code is largely the same except if the `NWListener` is running on the same machine that set up the local certificate authority then the app’s code can reference the identity by loading a reference from the [`SecCertificate`](https://developer.apple.com/documentation/Security/SecCertificate) in the Keychain. To retrieve the identity from the Keychain on macOS, use the following:

```swift
func getSecIdentity() -> SecIdentity? {

    var identity: SecIdentity?
    let getquery = [kSecClass: kSecClassCertificate,
        kSecAttrLabel: "certificate_name_in_keychain",
        kSecReturnRef: true] as NSDictionary

    var item: CFTypeRef?
    let status = SecItemCopyMatching(getquery as CFDictionary, &item)
    guard status == errSecSuccess else {
        // handle error …
    }
    let certificate = item as! SecCertificate

    let identityStatus = SecIdentityCreateWithCertificate(nil, certificate, &identity)
    guard identityStatus == errSecSuccess else {
        // handle error …
    }
    return identity
}
```

After loading the identity on macOS, you can use the exact same `NWListener` code on iOS.

##### Configure the Client Devices

For clients that connect to the server, install the root certificate on the client device to avoid overriding trust evaluation. After installing the root certificate on the client device, the client connects to the server using a local network name. When connecting from the client side of the connection, use the following:

```swift
let tlsOptions = NWProtocolTLS.Options()
sec_protocol_options_set_min_tls_protocol_version(
    tlsOptions.securityProtocolOptions, 
    .TLSv12)

let tlsParams = NWParameters(tls: tlsOptions, tcp: .init())

let endpoint = NWEndpoint.hostPort(host: "listener-name.local", port: 4433)
let connection = NWConnection(to: endpoint, using: tlsParams)
```

> **Note**:  If the root certificate from the CA is installed on the device, you can use the code above without implementing [`sec_protocol_options_set_verify_block(_:_:_:)`](https://developer.apple.com/documentation/Security/sec_protocol_options_set_verify_block(_:_:_:)) to override trust evaluation.

 If the root certificate from the CA is installed on the device, you can use the code above without implementing [`sec_protocol_options_set_verify_block(_:_:_:)`](https://developer.apple.com/documentation/Security/sec_protocol_options_set_verify_block(_:_:_:)) to override trust evaluation.

If your client needs to connect over IP, instead of using a local network name, the server needs to use a leaf certificate that lists the IP in the “IP Address” field of the Subject Alternative Name. This also avoids having to override trust evaluation on the client and allows client connections to use the following:

```swift
let tlsOptions = NWProtocolTLS.Options()
sec_protocol_options_set_min_tls_protocol_version(
    tlsOptions.securityProtocolOptions, 
    .TLSv12)

let tlsParams = NWParameters(tls: tlsOptions, tcp: .init())

let endpoint = NWEndpoint.hostPort(host: "x.x.x.x", port: 4433)
let connection = NWConnection(to: endpoint, using: tlsParams)
```

Attempting to connect from a client to a server without the root certificate installed on the client iOS device results in application errors similar to the following:

```None
// [BoringSSL] boringssl_context_error_print(1863) boringssl ctx 0x2813acbe0: 4348594328:error:1000007d:SSL routines:OPENSSL_internal:CERTIFICATE_VERIFY_FAILED
// [BoringSSL] boringssl_session_handshake_incomplete(164) [C1:1][0x1032186d0] SSL library error
```

> **Note**:  The same is true if either the IP Address or DNS Name in the Subject Alternative Name fields are missing in the leaf certificate.

 The same is true if either the IP Address or DNS Name in the Subject Alternative Name fields are missing in the leaf certificate.

To work around this on the client, use `sec_protocol_options_set_verify_block` to perform your own verification checks on the peer’s leaf certificate. This isn’t the recommended path, but could be done in extreme cases. In the following example, [`SecPolicyCreateBasicX509()`](https://developer.apple.com/documentation/Security/SecPolicyCreateBasicX509()) checks against the certificate’s basic x509 policy:

```swift
sec_protocol_options_set_verify_block(tlsOptions.securityProtocolOptions, { (_, trust, completionHandler) in
    let secTrustRef = sec_trust_copy_ref(trust).takeRetainedValue() as SecTrust

    // Cannot do hostname here because of IP.
    let x509Policy = SecPolicyCreateBasicX509()
    SecTrustSetPolicies(secTrustRef, x509Policy)

    var error: CFError?
    if !SecTrustEvaluateWithError(secTrustRef, &error) {
        completionHandler(false)
    }
    // Perfom other certificate-based checks.  

    completionHandler(true)
}, .main)
```

From there the client can set up a handshake using TLS on a local network.

## See Also

- [Security Options](security-options.md)
  Configure security options for TLS handshakes.
- [Privacy Management](privacy-management.md)
  Configure parameters related to user privacy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/creating-an-identity-for-local-network-tls)*