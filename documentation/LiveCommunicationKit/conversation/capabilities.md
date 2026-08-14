# Conversation.Capabilities

**Framework**: LiveCommunicationKit  
**Kind**: struct

A type that describes capabilities of a conversation.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- visionOS 1.1+
- watchOS 10.4+

## Declaration

```swift
struct Capabilities
```

#### Overview

Configure conversation capabilites as part of a [`Conversation.Update`](conversation/update.md).

## Topics

### Capabilities
- [static let merging: Conversation.Capabilities](conversation/capabilities/merging.md)
  The conversation can merge with another conversation to create a new conversation.
- [static let pausing: Conversation.Capabilities](conversation/capabilities/pausing.md)
  The conversation is active and can be temporarily paused.
- [static let playingTones: Conversation.Capabilities](conversation/capabilities/playingtones.md)
  The conversation supports playing tone sequences.
- [static let unmerging: Conversation.Capabilities](conversation/capabilities/unmerging.md)
  The conversation is the result of merging two conversations and can be separated into the original conversations.
- [static let video: Conversation.Capabilities](conversation/capabilities/video.md)
  The conversation sends or displays video streams.

## Relationships

### Conforms To
- [Decodable](../swift/decodable.md)
- [Encodable](../swift/encodable.md)
- [Equatable](../swift/equatable.md)
- [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md)
- [Hashable](../swift/hashable.md)
- [OptionSet](../swift/optionset.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [SetAlgebra](../swift/setalgebra.md)

## See Also

- [Conversation.Update](conversation/update.md)
  A type that describes new, changed, or deleted capabilities and attributes of a conversation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/conversation/capabilities)*