# FoveatedStreamingSession.MessageChannel

**Framework**: Foveated Streaming  
**Kind**: class

A bidirectional channel for sending and receiving custom data.

**Availability**:
- visionOS 26.4+

## Declaration

```swift
class MessageChannel
```

#### Overview

Use message channels to communicate with the application streaming foveated content to your visionOS app. You can send data with the [`sendMessage(_:)`](foveatedstreamingsession/messagechannel/sendmessage(_:).md) function and receive data through the [`receivedMessageStream`](foveatedstreamingsession/messagechannel/receivedmessagestream.md) async stream.

## Topics

### Structures
- [FoveatedStreamingSession.MessageChannel.ID](foveatedstreamingsession/messagechannel/id-swift.struct.md)
  A unique identifier for a message channel.
### Instance Properties
- [var channelStatus: FoveatedStreamingSession.MessageChannel.ChannelStatus](foveatedstreamingsession/messagechannel/channelstatus-swift.property.md)
  The state of the message channel.
- [let id: FoveatedStreamingSession.MessageChannel.ID](foveatedstreamingsession/messagechannel/id-swift.property.md)
  An identifier for the message channel.
- [let receivedMessageStream: AsyncStream<Data>](foveatedstreamingsession/messagechannel/receivedmessagestream.md)
  An async stream that yields data objects each time the channel receives a message.
### Instance Methods
- [func disconnect()](foveatedstreamingsession/messagechannel/disconnect.md)
  Manually disconnects and closes the data channel.
- [func sendMessage(Data) throws](foveatedstreamingsession/messagechannel/sendmessage(_:).md)
  Sends data to the streaming endpoint on this channel.
### Enumerations
- [FoveatedStreamingSession.MessageChannel.ChannelStatus](foveatedstreamingsession/messagechannel/channelstatus-swift.enum.md)
  The status of a message channel.

## Relationships

### Conforms To
- [Copyable](../swift/copyable.md)
- [Escapable](../swift/escapable.md)
- [Identifiable](../swift/identifiable.md)
- [Observable](../observation/observable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foveatedstreaming/foveatedstreamingsession/messagechannel)*