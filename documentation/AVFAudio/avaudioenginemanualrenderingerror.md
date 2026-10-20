# AVAudioEngineManualRenderingError

**Framework**: AVFAudio  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum AVAudioEngineManualRenderingError : OSStatus;
```

## Topics

### Creating a rendering error
- [init?(rawValue: OSStatus)](./avaudioenginemanualrenderingerror/init%28rawvalue%29.md)
### Identifying rendering errors
- [AVAudioEngineManualRenderingError.initialized](./avaudioenginemanualrenderingerror/initialized.md)
  An operation that the system can’t perform because the engine is still running.
- [AVAudioEngineManualRenderingError.invalidMode](./avaudioenginemanualrenderingerror/invalidmode.md)
  An operation the system can’t perform because the engine isn’t in manual rendering mode or the right variant of it.
- [AVAudioEngineManualRenderingError.notRunning](./avaudioenginemanualrenderingerror/notrunning.md)
  An operation the system can’t perform because the engine isn’t running.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Rendering audio manually
- [func enableManualRenderingMode(AVAudioEngineManualRenderingMode, format: AVAudioFormat, maximumFrameCount: AVAudioFrameCount) throws](./avaudioengine/enablemanualrenderingmode%28_,format,maximumframecount%29.md)
  Sets the engine to operate in manual rendering mode with the render format and maximum frame count you specify.
- [enum AVAudioEngineManualRenderingMode](./avaudioenginemanualrenderingmode.md)
  The two modes for manual rendering.
- [func disableManualRenderingMode()](./avaudioengine/disablemanualrenderingmode%28%29.md)
  Sets the engine to render to or from an audio device.
- [func renderOffline(AVAudioFrameCount, to: AVAudioPCMBuffer) throws -> AVAudioEngineManualRenderingStatus](./avaudioengine/renderoffline%28_,to%29.md)
  Makes a render call to the engine operating in the offline manual rendering mode.
- [enum AVAudioEngineManualRenderingStatus](./avaudioenginemanualrenderingstatus.md)
  Status codes that return from the render call to the engine operating in manual rendering mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioenginemanualrenderingerror)*