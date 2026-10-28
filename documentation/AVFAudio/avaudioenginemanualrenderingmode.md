# AVAudioEngineManualRenderingMode

**Framework**: AVFAudio  
**Kind**: enum  
**Role**: Enumeration

The two modes for manual rendering.

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
enum AVAudioEngineManualRenderingMode
```

```c
enum AVAudioEngineManualRenderingMode : NSInteger;
```

## Overview

By default, the engine connects to an audio device and automatically renders in real time. You can configure it to operate in manual rendering mode, where it doesn’t have a connection to an audio device and renders in response to requests from the client.

## Topics

### Creating a rendering mode
- [init?(rawValue: Int)](./avaudioenginemanualrenderingmode/init%28rawvalue%29.md)
### Choosing a rendering mode
- [AVAudioEngineManualRenderingMode.offline](./avaudioenginemanualrenderingmode/offline.md)
  An engine that operates in an offline mode.
- [AVAudioEngineManualRenderingMode.realtime](./avaudioenginemanualrenderingmode/realtime.md)
  An engine that operates under real-time constraints and doesn’t make blocking calls while rendering.

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
- [func disableManualRenderingMode()](./avaudioengine/disablemanualrenderingmode%28%29.md)
  Sets the engine to render to or from an audio device.
- [func renderOffline(AVAudioFrameCount, to: AVAudioPCMBuffer) throws -> AVAudioEngineManualRenderingStatus](./avaudioengine/renderoffline%28_,to%29.md)
  Makes a render call to the engine operating in the offline manual rendering mode.
- [enum AVAudioEngineManualRenderingStatus](./avaudioenginemanualrenderingstatus.md)
  Status codes that return from the render call to the engine operating in manual rendering mode.
- [enum AVAudioEngineManualRenderingError](./avaudioenginemanualrenderingerror.md)
  Constants that describe error codes that the framework returns from manual rendering mode methods.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioenginemanualrenderingmode)*