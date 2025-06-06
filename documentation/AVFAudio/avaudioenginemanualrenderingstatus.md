# AVAudioEngineManualRenderingStatus

**Framework**: AVFAudio  
**Kind**: enum

Status codes that return from the render call to the engine operating in manual rendering mode.

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
enum AVAudioEngineManualRenderingStatus
```

## Topics

### Constants
- [AVAudioEngineManualRenderingStatus.error](avaudioenginemanualrenderingstatus/error.md)
  A problem that occurs during rendering and results in no data returning.
- [AVAudioEngineManualRenderingStatus.success](avaudioenginemanualrenderingstatus/success.md)
  A status that indicates the successful return of the requested data.
- [AVAudioEngineManualRenderingStatus.insufficientDataFromInputNode](avaudioenginemanualrenderingstatus/insufficientdatafrominputnode.md)
  A condition that occurs when the input node doesn’t return enough input data to satisfy the render request at the time of the request.
- [AVAudioEngineManualRenderingStatus.cannotDoInCurrentContext](avaudioenginemanualrenderingstatus/cannotdoincurrentcontext.md)
  An operation that the system can’t perform under the current conditions.
### Initializers
- [init?(rawValue: Int)](avaudioenginemanualrenderingstatus/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [enum AVAudioEngineManualRenderingError](avaudioenginemanualrenderingerror.md)
  Constants that describe error codes that the framework returns from manual rendering mode methods.
- [enum AVAudioEngineManualRenderingMode](avaudioenginemanualrenderingmode.md)
  The two modes for manual rendering.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioenginemanualrenderingstatus)*