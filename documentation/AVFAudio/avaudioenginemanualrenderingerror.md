# AVAudioEngineManualRenderingError

**Framework**: AVFAudio  
**Kind**: enum

Constants that describe error codes that the framework returns from manual rendering mode methods.

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
enum AVAudioEngineManualRenderingError
```

## Topics

### Manual Rendering Errors
- [AVAudioEngineManualRenderingError.initialized](avaudioenginemanualrenderingerror/initialized.md)
  An operation that the system can’t perform because the engine is still running.
- [AVAudioEngineManualRenderingError.invalidMode](avaudioenginemanualrenderingerror/invalidmode.md)
  An operation the system can’t perform because the engine isn’t in manual rendering mode or the right variant of it.
- [AVAudioEngineManualRenderingError.notRunning](avaudioenginemanualrenderingerror/notrunning.md)
  An operation the system can’t perform because the engine isn’t running.
### Initializers
- [init?(rawValue: OSStatus)](avaudioenginemanualrenderingerror/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [enum AVAudioEngineManualRenderingMode](avaudioenginemanualrenderingmode.md)
  The two modes for manual rendering.
- [enum AVAudioEngineManualRenderingStatus](avaudioenginemanualrenderingstatus.md)
  Status codes that return from the render call to the engine operating in manual rendering mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioenginemanualrenderingerror)*