# receive(atLeast:atMost:)

**Framework**: Network  
**Kind**: method

Receive data from a connection

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
func receive(atLeast: Int = 1, atMost: Int) async throws -> ApplicationProtocol.Message<Data>
```

#### Discussion

This may be called before the connection is ready, in which case the receive request will be enqueued until the connection is ready.

## Parameters

- `atLeast`: The minimum length to receive from the connection,   until the content is complete.
- `atMost`: The maximum length to receive from the connection in a single completion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/networkchannel/receive(atleast:atmost:))*