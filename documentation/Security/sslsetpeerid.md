# SSLSetPeerID(_:_:_:)

**Framework**: Security  
**Kind**: func

Specifies data that is sufficient to uniquely identify the peer of the current session.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.2+

## Declaration

```swift
func SSLSetPeerID(_ context: SSLContext, _ peerID: UnsafeRawPointer?, _ peerIDLen: Int) -> OSStatus
```

#### Return Value

A result code. See [`Secure Transport Result Codes`](secure-transport-result-codes.md).

#### Discussion

Secure Transport uses the peer ID to match the peer of an SSL session with the peer of a previous session in order to resume an interrupted session. If the peer IDs match, Secure Transport attempts to resume the session with the same parameters as used in the previous session with the same peer.

The data you provide to this function is treated as an opaque blob by Secure Transport but is compared byte for byte with previous peer ID data values set by the current application. An example of peer ID data is an IP address and port, stored in some caller-private manner. Calling this function is optional but is required if you want the session to be resumable. If you do call this function, you must call it prior to the handshake for the current session.

You can use the [`SSLGetPeerID(_:_:_:)`](sslgetpeerid(_:_:_:).md) function to retrieve the peer ID data for the current session.

## Parameters

- `context`: An SSL session context reference.
- `peerID`: A pointer to a buffer containing the peer ID data to set.
- `peerIDLen`: The length of the peer ID data buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sslsetpeerid(_:_:_:))*