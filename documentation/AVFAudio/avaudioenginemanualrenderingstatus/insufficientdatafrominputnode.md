# AVAudioEngineManualRenderingStatus.insufficientDataFromInputNode

**Framework**: AVFAudio  
**Kind**: case

A condition that occurs when the input node doesn’t return enough input data to satisfy the render request at the time of the request.

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
case insufficientDataFromInputNode
```

#### Discussion

This status only applies to the input node when it provides input data for rendering. The output buffer may contain rendered data from other active sources in the engine’s processing graph. See [`setManualRenderingInputPCMFormat(_:inputBlock:)`](avaudioinputnode/setmanualrenderinginputpcmformat(_:inputblock:).md).

## See Also

- [AVAudioEngineManualRenderingStatus.error](avaudioenginemanualrenderingstatus/error.md)
  A problem that occurs during rendering and results in no data returning.
- [AVAudioEngineManualRenderingStatus.success](avaudioenginemanualrenderingstatus/success.md)
  A status that indicates the successful return of the requested data.
- [AVAudioEngineManualRenderingStatus.cannotDoInCurrentContext](avaudioenginemanualrenderingstatus/cannotdoincurrentcontext.md)
  An operation that the system can’t perform under the current conditions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioenginemanualrenderingstatus/insufficientdatafrominputnode)*