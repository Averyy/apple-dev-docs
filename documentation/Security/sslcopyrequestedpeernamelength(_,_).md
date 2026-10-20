# SSLCopyRequestedPeerNameLength(_:_:)

**Framework**: Security  
**Kind**: func  
**Role**: Function

Obtains the hostname specified by the client in the ServerName extension (SNI). Server only.

**Availability**:
- iOS 9.0+ - Deprecated in 13.0
- iPadOS 9.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.11+ - Deprecated in 10.15

> **Deprecated**: No longer supported. Use Network.framework.

## Declaration

```swift
func SSLCopyRequestedPeerNameLength(_ ctx: SSLContext, _ peerNameLen: UnsafeMutablePointer<Int>) -> OSStatus
```

```c
OSStatus SSLCopyRequestedPeerNameLength(SSLContextRef ctx, size_t *peerNameLen);
```

#### Return Value

A result code. See [Secure Transport Result Codes](./secure-transport-result-codes.md).

## Parameters

- `ctx`: An SSL session context reference.
- `peerNameLen`: The length of the peer name, as retrieved by calling the [`SSLCopyRequestedPeerName(_:_:_:)`](./sslcopyrequestedpeername%28_,_,_%29.md) function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sslcopyrequestedpeernamelength(_:_:))*