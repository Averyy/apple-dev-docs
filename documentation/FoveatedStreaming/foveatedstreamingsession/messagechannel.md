# FoveatedStreamingSession.MessageChannel

**Framework**: Foveated Streaming  
**Kind**: class  
**Role**: Class

A bidirectional channel for sending and receiving custom data.

**Availability**:
- visionOS 26.4+

## Declaration

```swift
class MessageChannel
```

#### Overview

Use message channels to communicate with the application streaming foveated content to your visionOS app. You can send data with the [`sendMessage(_:)`](./messagechannel/sendmessage%28_%29.md) function and receive data through the [`receivedMessageStream`](./messagechannel/receivedmessagestream.md) async stream.

## Topics

### Structures
- [FoveatedStreamingSession.MessageChannel.ID](./messagechannel/id-swift.struct.md)
  A unique identifier for a message channel.
### Instance Properties
- [var channelStatus: FoveatedStreamingSession.MessageChannel.ChannelStatus](./messagechannel/channelstatus-swift.property.md)
  The state of the message channel.
- [let id: FoveatedStreamingSession.MessageChannel.ID](./messagechannel/id-swift.property.md)
  An identifier for the message channel.
- [let receivedMessageStream: AsyncStream<Data>](./messagechannel/receivedmessagestream.md)
  An async stream that yields data objects each time the channel receives a message.
### Instance Methods
- [func disconnect()](./messagechannel/disconnect%28%29.md)
  Manually disconnects and closes the data channel.
- [func sendMessage(Data) throws](./messagechannel/sendmessage%28_%29.md)
  Sends data to the streaming endpoint on this channel.
### Enumerations
- [FoveatedStreamingSession.MessageChannel.ChannelStatus](./messagechannel/channelstatus-swift.enum.md)
  The status of a message channel.

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [Escapable](../../Swift/escapable.md)
- [Identifiable](../../Swift/identifiable.md)
- [Observable](../../Observation/observable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foveatedstreaming/foveatedstreamingsession/messagechannel)*