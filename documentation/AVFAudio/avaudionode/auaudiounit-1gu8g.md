# auAudioUnit

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property

An audio unit object that wraps or underlies the implementation’s audio unit.

**Availability**:
- iOS 11.0+ - Deprecated in 27.0
- iPadOS 11.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 10.13+ - Deprecated in 27.0
- tvOS 11.0+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0

> **Deprecated**: Deprecated in favor of withAUAudioUnit

## Declaration

```swift
@export(implementation)
var auAudioUnit: AUAudioUnit { get }
```

#### Discussion

This provides an [`AUAudioUnit`](../../AudioToolbox/auaudiounit.md) that either wraps or underlies the implementation’s audio unit, depending on how the app packages the audio unit. Apps interact with this to control custom properties, select presets, and change parameters.

Don’t perform operations directly on the audio unit that may conflict with the engine’s state, which includes changing the initialization state, stream formats, channel layouts, or connections to other audio units.

## See Also

### Getting audio node properties
- [func withAUAudioUnit<R, E>((borrowing AUAudioUnit) throws(E) -> R) throws(E) -> R](./withauaudiounit%28_%29.md)
  Provides scoped access to the node’s AUAudioUnit
- [var latency: TimeInterval](./latency.md)
  The processing latency of the node, in seconds.
- [var outputPresentationLatency: TimeInterval](./outputpresentationlatency.md)
  The maximum render pipeline latency downstream of the node, in seconds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudionode/auaudiounit-1gu8g)*