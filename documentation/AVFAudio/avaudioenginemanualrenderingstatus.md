# AVAudioEngineManualRenderingStatus

**Framework**: AVFAudio  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum AVAudioEngineManualRenderingStatus : NSInteger;
```

## Topics

### Creating a rendering status
- [init?(rawValue: Int)](./avaudioenginemanualrenderingstatus/init%28rawvalue%29.md)
### Interpreting rendering results
- [AVAudioEngineManualRenderingStatus.error](./avaudioenginemanualrenderingstatus/error.md)
  A problem that occurs during rendering and results in no data returning.
- [AVAudioEngineManualRenderingStatus.success](./avaudioenginemanualrenderingstatus/success.md)
  A status that indicates the successful return of the requested data.
- [AVAudioEngineManualRenderingStatus.insufficientDataFromInputNode](./avaudioenginemanualrenderingstatus/insufficientdatafrominputnode.md)
  A condition that occurs when the input node doesn’t return enough input data to satisfy the render request at the time of the request.
- [AVAudioEngineManualRenderingStatus.cannotDoInCurrentContext](./avaudioenginemanualrenderingstatus/cannotdoincurrentcontext.md)
  An operation that the system can’t perform under the current conditions.

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
- [enum AVAudioEngineManualRenderingError](./avaudioenginemanualrenderingerror.md)
  Constants that describe error codes that the framework returns from manual rendering mode methods.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioenginemanualrenderingstatus)*