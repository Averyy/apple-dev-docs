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

### Creating a rendering error
- [init?(rawValue: OSStatus)](avaudioenginemanualrenderingerror/init(rawvalue:).md)
### Identifying rendering errors
- [AVAudioEngineManualRenderingError.initialized](avaudioenginemanualrenderingerror/initialized.md)
  An operation that the system can’t perform because the engine is still running.
- [AVAudioEngineManualRenderingError.invalidMode](avaudioenginemanualrenderingerror/invalidmode.md)
  An operation the system can’t perform because the engine isn’t in manual rendering mode or the right variant of it.
- [AVAudioEngineManualRenderingError.notRunning](avaudioenginemanualrenderingerror/notrunning.md)
  An operation the system can’t perform because the engine isn’t running.

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [func enableManualRenderingMode(AVAudioEngineManualRenderingMode, format: AVAudioFormat, maximumFrameCount: AVAudioFrameCount) throws](avaudioengine/enablemanualrenderingmode(_:format:maximumframecount:).md)
  Sets the engine to operate in manual rendering mode with the render format and maximum frame count you specify.
- [enum AVAudioEngineManualRenderingMode](avaudioenginemanualrenderingmode.md)
  The two modes for manual rendering.
- [func disableManualRenderingMode()](avaudioengine/disablemanualrenderingmode.md)
  Sets the engine to render to or from an audio device.
- [func renderOffline(AVAudioFrameCount, to: AVAudioPCMBuffer) throws -> AVAudioEngineManualRenderingStatus](avaudioengine/renderoffline(_:to:).md)
  Makes a render call to the engine operating in the offline manual rendering mode.
- [enum AVAudioEngineManualRenderingStatus](avaudioenginemanualrenderingstatus.md)
  Status codes that return from the render call to the engine operating in manual rendering mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioenginemanualrenderingerror)*