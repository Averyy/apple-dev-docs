# FoveatedStreamingProviderMessageChannel

**Framework**: Foveated Streaming  
**Kind**: class

A message channel between the host app and a streaming provider extension.

**Availability**:
- visionOS 27.0+ (Beta)

## Declaration

```swift
@MainActor
final class FoveatedStreamingProviderMessageChannel
```

#### Overview

Message channels are created by the framework when the host app opens a channel and delivered to the extension via [`openMessageChannel(_:)`](foveatedstreamingextension/openmessagechannel(_:).md). Provider extensions do not construct values of this type directly.

A channel unifies both directions of message flow:

- Messages the host app sends to the extension arrive on [`receivedMessages`](foveatedstreamingprovidermessagechannel/receivedmessages.md).
- Data the extension receives from the streaming endpoint is delivered to the host app via [`send(_:)`](foveatedstreamingprovidermessagechannel/send(_:).md).

## Topics

### Instance Properties
- [var channelStatus: FoveatedStreamingSession.MessageChannel.ChannelStatus](foveatedstreamingprovidermessagechannel/channelstatus.md)
  The current status of this channel.
- [let id: FoveatedStreamingSession.MessageChannel.ID](foveatedstreamingprovidermessagechannel/id.md)
  The identifier of this channel.
- [var receivedMessages: some AsyncSequence<Data, Never>](foveatedstreamingprovidermessagechannel/receivedmessages.md)
  The messages the host app has sent to the extension.
### Instance Methods
- [func close()](foveatedstreamingprovidermessagechannel/close.md)
  Closes the channel and finishes [`receivedMessages`](foveatedstreamingprovidermessagechannel/receivedmessages.md).
- [func send(Data)](foveatedstreamingprovidermessagechannel/send(_:).md)
  Sends data received from the streaming endpoint to the host app.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Escapable](../Swift/Escapable.md)
- [Observable](../Observation/Observable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foveatedstreaming/foveatedstreamingprovidermessagechannel)*