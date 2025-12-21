# receive()

**Framework**: Network  
**Kind**: method

Receive data from a connection.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
func receive() async throws -> ApplicationProtocol.Message<Data>
```

#### Discussion

This may be called before the connection is ready, in which case the receive request will be enqueued until the connection is ready.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/networkchannel/receive()-86md7)*