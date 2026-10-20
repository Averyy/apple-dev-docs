# SSLHandshake(_:)

**Framework**: Security  
**Kind**: func  
**Role**: Function

Performs the SSL handshake.

**Availability**:
- iOS 5.0+ - Deprecated in 13.0
- iPadOS 5.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.2+ - Deprecated in 10.15

> **Deprecated**: No longer supported. Use Network.framework.

## Declaration

```swift
func SSLHandshake(_ context: SSLContext) -> OSStatus
```

```c
OSStatus SSLHandshake(SSLContextRef context);
```

## Mentions

- [Using the Secure Socket Layer for Network Communication](./using-the-secure-socket-layer-for-network-communication.md)

#### Return Value

A result code. See [Secure Transport Result Codes](./secure-transport-result-codes.md).

#### Discussion

On successful return, the session is ready for normal secure communication using the functions [`SSLRead(_:_:_:_:)`](./sslread%28_,_,_,_%29.md) and [`SSLWrite(_:_:_:_:)`](./sslwrite%28_,_,_,_%29.md).

If it finds any problems with the peer’s certificate chain, Secure Transport aborts the handshake. You can use the [`SSLCopyPeerCertificates`](./sslcopypeercertificates.md) function to see the peer’s certificate chain. This function can return a wide variety of result codes, including the following:

- `errSSLUnknownRootCert`—The peer has a valid certificate chain, but the root of the chain is not a known anchor certificate.
- `errSSLNoRootCert`—The peer’s certificate chain was not verifiable to a root certificate.
- `errSSLCertExpired`—The peer’s certificate chain has one or more expired certificates.
- `errSSLXCertChainInvalid`—The peer has an invalid certificate chain; for example, signature verification within the chain failed, or no certificates were found.
- `errSSLClientCertRequested`—The server has requested a client certificate. This result is returned only if you called the [`SSLSetSessionOption(_:_:_:)`](./sslsetsessionoption%28_,_,_%29.md) function to set the `kSSLSessionOptionBreakOnCertRequested` option. After receiving this result, you must call the [`SSLSetCertificate(_:_:)`](./sslsetcertificate%28_,_%29.md) function to return the client certificate, and then call [`SSLHandshake(_:)`](./sslhandshake%28_%29.md) again to resume the handshake. Use the [`SSLCopyDistinguishedNames(_:_:)`](./sslcopydistinguishednames%28_,_%29.md) function to obtain a list of certificates acceptable to the server.
- `errSSLServerAuthCompleted`—The server authentication portion of the handshake is complete. This result is returned only if you called the [`SSLSetSessionOption(_:_:_:)`](./sslsetsessionoption%28_,_,_%29.md) function to set the `kSSLSessionOptionBreakOnServerAuth` option, and provides an opportunity to perform application-specific server verification before calling [`SSLHandshake(_:)`](./sslhandshake%28_%29.md) again to continue.

Note that in macOS prior to version 10.8, you must also explicitly call [`SSLSetEnableCertVerify`](./sslsetenablecertverify.md) to disable verification.

A return value of `errSSLWouldBlock` indicates that the [`SSLHandshake(_:)`](./sslhandshake%28_%29.md) function must be called again until a different result code is returned.

## Parameters

- `context`: An SSL session context reference.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sslhandshake(_:))*