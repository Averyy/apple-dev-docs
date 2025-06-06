# SSLGetPeerID(_:_:_:)

**Framework**: Security  
**Kind**: func

Retrieves the current peer ID data.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.2+

## Declaration

```swift
func SSLGetPeerID(_ context: SSLContext, _ peerID: UnsafeMutablePointer<UnsafeRawPointer?>, _ peerIDLen: UnsafeMutablePointer<Int>) -> OSStatus
```

#### Return Value

A result code. See [`Secure Transport Result Codes`](secure-transport-result-codes.md).

#### Discussion

If the peer ID data for this context was not set by calling the [`SSLSetPeerID(_:_:_:)`](sslsetpeerid(_:_:_:).md) function, this function returns a `NULL` pointer in the `peerID` parameter, and `0` in the `peerIDLen` parameter.

## Parameters

- `context`: An SSL session context reference.
- `peerID`: On return, points to a buffer containing the peer ID data.
- `peerIDLen`: On return, the length of the peer ID data buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sslgetpeerid(_:_:_:))*