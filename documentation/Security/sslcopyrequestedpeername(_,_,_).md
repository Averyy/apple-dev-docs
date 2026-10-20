# SSLCopyRequestedPeerName(_:_:_:)

**Framework**: Security  
**Kind**: func  
**Role**: Function

Determines the buffer size needed for the peer domain name.

**Availability**:
- iOS 9.0+ - Deprecated in 13.0
- iPadOS 9.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.11+ - Deprecated in 10.15

> **Deprecated**: No longer supported. Use Network.framework.

## Declaration

```swift
func SSLCopyRequestedPeerName(_ context: SSLContext, _ peerName: UnsafeMutablePointer<CChar>, _ peerNameLen: UnsafeMutablePointer<Int>) -> OSStatus
```

```c
OSStatus SSLCopyRequestedPeerName(SSLContextRef context, char *peerName, size_t *peerNameLen);
```

#### Return Value

A result code. See [Secure Transport Result Codes](./secure-transport-result-codes.md).

#### Discussion

Use the `peerNameLen` returned by this function when calling the [`SSLCopyRequestedPeerNameLength(_:_:)`](./sslcopyrequestedpeernamelength%28_,_%29.md) function.

## Parameters

- `context`: An SSL session context reference.
- `peerName`: The fully qualified domain name of the peer—for example, `store.apple.com`. The name is in the form of a C string, except that `NULL` termination is optional.
- `peerNameLen`: On return, points to the length of the peer domain name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sslcopyrequestedpeername(_:_:_:))*