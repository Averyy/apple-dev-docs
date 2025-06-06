# SSLSetDatagramHelloCookie(_:_:_:)

**Framework**: Security  
**Kind**: func

Sets the cookie value used in the Datagram Transport Layer Security (DTLS) hello message.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.8+

## Declaration

```swift
func SSLSetDatagramHelloCookie(_ dtlsContext: SSLContext, _ cookie: UnsafeRawPointer?, _ cookieLen: Int) -> OSStatus
```

#### Return Value

A result code. See [`Secure Transport Result Codes`](secure-transport-result-codes.md).

#### Discussion

This function should be called only on the server side, and is optional. The default cookie is a zero-length cookie.

## Parameters

- `dtlsContext`: The SSL context associated with the connection.
- `cookie`: The cookie value.
- `cookieLen`: The length of the cookie (up to 32 bytes).


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sslsetdatagramhellocookie(_:_:_:))*