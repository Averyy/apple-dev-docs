# Conversation.Capabilities

**Framework**: LiveCommunicationKit  
**Kind**: struct  
**Role**: Structure

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

## Overview

Configure conversation capabilites as part of a [`Conversation.Update`](./update.md).

## Topics

### Capabilities
- [static let merging: Conversation.Capabilities](./capabilities/merging.md)
  The conversation can merge with another conversation to create a new conversation.
- [static let pausing: Conversation.Capabilities](./capabilities/pausing.md)
  The conversation is active and can be temporarily paused.
- [static let playingTones: Conversation.Capabilities](./capabilities/playingtones.md)
  The conversation supports playing tone sequences.
- [static let unmerging: Conversation.Capabilities](./capabilities/unmerging.md)
  The conversation is the result of merging two conversations and can be separated into the original conversations.
- [static let video: Conversation.Capabilities](./capabilities/video.md)
  The conversation sends or displays video streams.

## Relationships

### Conforms To
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [Hashable](../../Swift/hashable.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [SetAlgebra](../../Swift/setalgebra.md)

## See Also

### Updating a conversation
- [Conversation.Update](./update.md)
  A type that describes new, changed, or deleted capabilities and attributes of a conversation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/conversation/capabilities)*