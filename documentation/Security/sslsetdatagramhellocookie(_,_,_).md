# SSLSetDatagramHelloCookie(_:_:_:)

**Framework**: Security  
**Kind**: func  
**Role**: Function

Sets the cookie value used in the Datagram Transport Layer Security (DTLS) hello message.

**Availability**:
- iOS 5.0+ - Deprecated in 13.0
- iPadOS 5.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.8+ - Deprecated in 10.15

> **Deprecated**: No longer supported. Use Network.framework.

## Declaration

```swift
func SSLSetDatagramHelloCookie(_ dtlsContext: SSLContext, _ cookie: UnsafeRawPointer?, _ cookieLen: Int) -> OSStatus
```

```c
OSStatus SSLSetDatagramHelloCookie(SSLContextRef dtlsContext, const void *cookie, size_t cookieLen);
```

#### Return Value

A result code. See [Secure Transport Result Codes](./secure-transport-result-codes.md).

#### Discussion

This function should be called only on the server side, and is optional. The default cookie is a zero-length cookie.

## Parameters

- `dtlsContext`: The SSL context associated with the connection.
- `cookie`: The cookie value.
- `cookieLen`: The length of the cookie (up to 32 bytes).


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sslsetdatagramhellocookie(_:_:_:))*