# SSLCopyRequestedPeerName(_:_:_:)

**Framework**: Security  
**Kind**: func

Determines the buffer size needed for the peer domain name.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+

## Declaration

```swift
func SSLCopyRequestedPeerName(_ context: SSLContext, _ peerName: UnsafeMutablePointer<CChar>, _ peerNameLen: UnsafeMutablePointer<Int>) -> OSStatus
```

#### Return Value

A result code. See [`Secure Transport Result Codes`](secure-transport-result-codes.md).

#### Discussion

Use the `peerNameLen` returned by this function when calling the [`SSLCopyRequestedPeerNameLength(_:_:)`](sslcopyrequestedpeernamelength(_:_:).md) function.

## Parameters

- `context`: An SSL session context reference.
- `peerName`: The fully qualified domain name of the peer—for example,  . The name is in the form of a C string, except that   termination is optional.
- `peerNameLen`: On return, points to the length of the peer domain name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sslcopyrequestedpeername(_:_:_:))*