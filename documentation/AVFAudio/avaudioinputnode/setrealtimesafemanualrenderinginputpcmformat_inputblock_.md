# setRealtimeSafeManualRenderingInputPCMFormat:inputBlock:

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
- (BOOL) setRealtimeSafeManualRenderingInputPCMFormat:(AVAudioFormat *) format inputBlock:(AVAudioIONodeInputBlockRealtimeSafe) block;
```

#### Discussion

Identical to setManualRenderingInputPCMFormat:inputBlock:, but requires a realtime-safe input block.

## See Also

### Supplying manual rendering input
- [func setManualRenderingInputPCMFormat(AVAudioFormat, inputBlock: AVAudioIONodeInputBlock) -> Bool](./setmanualrenderinginputpcmformat%28_,inputblock%29.md)
  Supplies the data through the input node to the engine while operating in the manual rendering mode.
- [typealias AVAudioIONodeInputBlock](../avaudioionodeinputblock.md)
  The type that represents a block to render operation calls to get input data when in manual rendering mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioinputnode/setrealtimesafemanualrenderinginputpcmformat:inputblock:)*