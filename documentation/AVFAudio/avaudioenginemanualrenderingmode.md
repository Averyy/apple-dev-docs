# AVAudioEngineManualRenderingMode

**Framework**: AVFAudio  
**Kind**: enum

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

#### Overview

By default, the engine connects to an audio device and automatically renders in real time. You can configure it to operate in manual rendering mode, where it doesn’t have a connection to an audio device and renders in response to requests from the client.

## Topics

### Constants
- [AVAudioEngineManualRenderingMode.offline](avaudioenginemanualrenderingmode/offline.md)
  An engine that operates in an offline mode.
- [AVAudioEngineManualRenderingMode.realtime](avaudioenginemanualrenderingmode/realtime.md)
  An engine that operates under real-time constraints and doesn’t make blocking calls while rendering.
### Initializers
- [init?(rawValue: Int)](avaudioenginemanualrenderingmode/init(rawvalue:).md)

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
- [enum AVAudioEngineManualRenderingStatus](avaudioenginemanualrenderingstatus.md)
  Status codes that return from the render call to the engine operating in manual rendering mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioenginemanualrenderingmode)*