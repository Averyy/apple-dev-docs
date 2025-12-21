# receive(as:)

**Framework**: Network  
**Kind**: method

Receive data from a connection as a fixed width integer.

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
func receive<Value>(as type: Value.Type) async throws -> ApplicationProtocol.Message<Value> where Value : NetworkFixedWidthInteger
```

#### Discussion

This may be called before the connection is ready, in which case the receive request will be enqueued until the connection is ready.

## Parameters

- `type`: The type to use when interpreting the bytes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/networkchannel/receive(as:))*