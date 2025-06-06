# AVAudioEngineManualRenderingStatus.cannotDoInCurrentContext

**Framework**: AVFAudio  
**Kind**: case

An operation that the system can’t perform under the current conditions.

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
case cannotDoInCurrentContext
```

#### Discussion

This status guards a real-time render operation when a reconfiguration of the engine’s internal state is in progress. The client can try again later.

## See Also

- [AVAudioEngineManualRenderingStatus.error](avaudioenginemanualrenderingstatus/error.md)
  A problem that occurs during rendering and results in no data returning.
- [AVAudioEngineManualRenderingStatus.success](avaudioenginemanualrenderingstatus/success.md)
  A status that indicates the successful return of the requested data.
- [AVAudioEngineManualRenderingStatus.insufficientDataFromInputNode](avaudioenginemanualrenderingstatus/insufficientdatafrominputnode.md)
  A condition that occurs when the input node doesn’t return enough input data to satisfy the render request at the time of the request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioenginemanualrenderingstatus/cannotdoincurrentcontext)*