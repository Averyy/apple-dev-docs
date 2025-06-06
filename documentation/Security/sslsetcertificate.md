# SSLSetCertificate(_:_:)

**Framework**: Security  
**Kind**: func

Specifies this connection’s certificate or certificates.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.2+

## Declaration

```swift
func SSLSetCertificate(_ context: SSLContext, _ certRefs: CFArray?) -> OSStatus
```

## Mentions

- [Using the Secure Socket Layer for Network Communication](using-the-secure-socket-layer-for-network-communication.md)

#### Return Value

A result code. See [`Secure Transport Result Codes`](secure-transport-result-codes.md).

#### Discussion

Setting the certificate or certificates is mandatory for server connections, but is optional for clients. Specifying a certificate for a client enables SSL client-side authentication. You must place in `certRefs[0]` a `SecIdentityRef` object that identifies the leaf certificate and its corresponding private key. Specifying a root certificate is optional; if it’s not specified, the root certificate that verifies the certificate chain specified here must be present in the system wide set of trusted anchor certificates.

This function must be called before calling [`SSLHandshake(_:)`](sslhandshake(_:).md), or immediately after [`SSLHandshake(_:)`](sslhandshake(_:).md) has returned `errSSLClientCertRequested` (that is, before the handshake is resumed by calling [`SSLHandshake(_:)`](sslhandshake(_:).md) again).

Secure Transport assumes the following:

- The certificate references remain valid for the lifetime of the session.
- The identity specified in `certRefs[0]` is capable of signing.

The required capabilities of the identity specified in `certRefs[0]`—and of the optional certificate specified in the [`SSLSetEncryptionCertificate(_:_:)`](sslsetencryptioncertificate(_:_:).md) function—are highly dependent on the application. For example, to work as a server with Netscape clients, the identity specified here must be capable of both signing and encrypting. Use the [`SSLCopyDistinguishedNames(_:_:)`](sslcopydistinguishednames(_:_:).md) function to get a list of certificates acceptable to the server.

## Parameters

- `context`: An SSL session context reference.
- `certRefs`: The certificates to set. This array contains items of type  , except for  , which is of type  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sslsetcertificate(_:_:))*