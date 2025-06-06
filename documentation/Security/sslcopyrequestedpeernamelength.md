# SSLCopyRequestedPeerNameLength(_:_:)

**Framework**: Security  
**Kind**: func

Obtains the hostname specified by the client in the ServerName extension (SNI). Server only.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+

## Declaration

```swift
func SSLCopyRequestedPeerNameLength(_ ctx: SSLContext, _ peerNameLen: UnsafeMutablePointer<Int>) -> OSStatus
```

#### Return Value

A result code. See [`Secure Transport Result Codes`](secure-transport-result-codes.md).

## Parameters

- `ctx`: An SSL session context reference.
- `peerNameLen`: The length of the peer name, as retrieved by calling the   function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sslcopyrequestedpeernamelength(_:_:))*