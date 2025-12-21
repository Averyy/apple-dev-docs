# receive(exactly:)

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
func receive(exactly: Int) async throws -> ApplicationProtocol.Message<Data>
```

#### Discussion

This may be called before the connection is ready, in which case the receive request will be enqueued until the connection is ready.

## Parameters

- `exactly`: Receive exactly this number of bytes from the connection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/networkchannel/receive(exactly:))*