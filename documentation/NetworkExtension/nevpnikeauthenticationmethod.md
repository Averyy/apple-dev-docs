# NEVPNIKEAuthenticationMethod

**Framework**: Network Extension  
**Kind**: enum

Internet Key Exchange (IKE) authentication methods used to authenticate with the IPSec server.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
enum NEVPNIKEAuthenticationMethod
```

## Topics

### Authentication methods
- [NEVPNIKEAuthenticationMethod.none](nevpnikeauthenticationmethod/none.md)
  Do not authenticate with the IPSec server. Note that extended authentication may still be performed if the [`useExtendedAuthentication`](nevpnprotocolipsec/useextendedauthentication.md) property is set. This value is only valid for IKE version 2 (IKEv2)
- [NEVPNIKEAuthenticationMethod.certificate](nevpnikeauthenticationmethod/certificate.md)
  Use a certificate and private key as the authentication credential. The certificate and private key set in the [`identityReference`](nevpnprotocol/identityreference.md) or [`identityData`](nevpnprotocol/identitydata.md) property will be used.
- [NEVPNIKEAuthenticationMethod.sharedSecret](nevpnikeauthenticationmethod/sharedsecret.md)
  Use a shared secret as the authentication credential. The shared secret set in the [`sharedSecretReference`](nevpnprotocolipsec/sharedsecretreference.md) property will be used.
### Initializers
- [init?(rawValue: Int)](nevpnikeauthenticationmethod/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var authenticationMethod: NEVPNIKEAuthenticationMethod](nevpnprotocolipsec/authenticationmethod.md)
  The method used to authenticate the device with the IPSec server. For IKE version 2, when using extended authentication, this authentication method only affects how the client validates the authentication payload presented by the server.
- [var useExtendedAuthentication: Bool](nevpnprotocolipsec/useextendedauthentication.md)
  A flag indicating if extended authentication will be negotiated.
- [var sharedSecretReference: Data?](nevpnprotocolipsec/sharedsecretreference.md)
  A persistent keychain reference to a keychain item containing the IKE shared secret.
- [var localIdentifier: String?](nevpnprotocolipsec/localidentifier.md)
  A string identifying the iOS or macOS device for authentication purposes
- [var remoteIdentifier: String?](nevpnprotocolipsec/remoteidentifier.md)
  A string identifying the IPSec server for authentication purposes


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nevpnikeauthenticationmethod)*