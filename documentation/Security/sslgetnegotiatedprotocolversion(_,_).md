# SSLGetNegotiatedProtocolVersion(_:_:)

**Framework**: Security  
**Kind**: func  
**Role**: Function

Obtains the negotiated protocol version of the active session.

**Availability**:
- iOS 5.0+ - Deprecated in 13.0
- iPadOS 5.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.2+ - Deprecated in 10.15

> **Deprecated**: No longer supported. Use Network.framework.

## Declaration

```swift
func SSLGetNegotiatedProtocolVersion(_ context: SSLContext, _ protocol: UnsafeMutablePointer<SSLProtocol>) -> OSStatus
```

```c
OSStatus SSLGetNegotiatedProtocolVersion(SSLContextRef context, SSLProtocol *protocol);
```

## Return Value

A result code. See [Secure Transport Result Codes](./secure-transport-result-codes.md).

## Discussion

This function retrieves the version of the Secure Sockets Layer (SSL) or Transport Layer Security (TLS) protocol negotiated for the session. Note that the negotiated protocol may not be the same as your preferred protocol, depending on which protocol versions you enabled with the [`SSLSetProtocolVersionEnabled`](./sslsetprotocolversionenabled.md) function. This function can return any of the following values:

- `kSSLProtocol2`
- `kSSLProtocol3`
- `kTLSProtocol1`
- `kSSLProtocolUnknown`

## Parameters

- `context`: An SSL session context reference.
- `protocol`: On return, points to the negotiated protocol version of the active session. The value is set to [`SSLProtocol.sslProtocolUnknown`](./sslprotocol/sslprotocolunknown.md) if no SSL session is in progress.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sslgetnegotiatedprotocolversion(_:_:))*