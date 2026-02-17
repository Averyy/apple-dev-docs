# receivedMessageStream

**Framework**: Foveated Streaming  
**Kind**: property

An async stream that yields data objects each time the channel receives a message.

**Availability**:
- visionOS 26.4+ (Beta)

## Declaration

```swift
final let receivedMessageStream: AsyncStream<Data>
```

#### Discussion

The async stream ends when the message channel closes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foveatedstreaming/foveatedstreamingsession/messagechannel/receivedmessagestream)*