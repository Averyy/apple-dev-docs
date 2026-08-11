# receivedMessages

**Framework**: Foveated Streaming  
**Kind**: property

The messages the host app has sent to the extension.

**Availability**:
- visionOS 27.0+ (Beta)

## Declaration

```swift
@MainActor
final var receivedMessages: some AsyncSequence<Data, Never> { get }
```

#### Discussion

The sequence yields each message as the host sends it and finishes when the channel closes.

> **Note**: Intended for a single consumer.  Iterate [`receivedMessages`](foveatedstreamingprovidermessagechannel/receivedmessages.md) from one place only; consuming it concurrently from multiple tasks is not supported.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foveatedstreaming/foveatedstreamingprovidermessagechannel/receivedmessages)*