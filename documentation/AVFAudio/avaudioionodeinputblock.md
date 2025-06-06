# AVAudioIONodeInputBlock

**Framework**: AVFAudio  
**Kind**: typealias

The type that represents a block to render operation calls to get input data when in manual rendering mode.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
typealias AVAudioIONodeInputBlock = (AVAudioFrameCount) -> UnsafePointer<AudioBufferList>?
```

#### Return Value

An [`AudioBufferList`](https://developer.apple.com/documentation/CoreAudioTypes/AudioBufferList) that contains the data to render, or `nil` if no data is available.

#### Discussion

Don’t clear or refill the data in the return value until the framework calls the input block again or the rendering finishes. The format of the buffer list must match the format you specify when registering the block.

## Parameters

- `inNumberOfFrames`: The number of frames the system needs to complete the request.

## See Also

- [func setManualRenderingInputPCMFormat(AVAudioFormat, inputBlock: AVAudioIONodeInputBlock) -> Bool](avaudioinputnode/setmanualrenderinginputpcmformat(_:inputblock:).md)
  Supplies the data through the input node to the engine while operating in the manual rendering mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioionodeinputblock)*