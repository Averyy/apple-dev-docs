# initWithRealtimeSafeReceiverBlock:

**Framework**: AVFAudio  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```objc
- (instancetype) initWithRealtimeSafeReceiverBlock:(AVAudioSinkNodeReceiverBlockRealtimeSafe) block;
```

## Discussion

Identical to initWithReceiverBlock:, but requires a realtime-safe block and is the preferred initializer.

## See Also

### Creating an audio sink node
- [typealias AVAudioSinkNodeReceiverBlock](../avaudiosinknodereceiverblock.md)
  A block that receives audio data from an audio sink node.
- [init(receiverBlock: AVAudioSinkNodeReceiverBlock)](./init%28receiverblock%29.md)
  Creates an audio sink node with a block that receives audio data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosinknode/initwithrealtimesafereceiverblock:)*