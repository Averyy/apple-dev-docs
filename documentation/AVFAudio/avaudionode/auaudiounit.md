# auAudioUnit

**Framework**: AVFAudio  
**Kind**: property

An audio unit object that wraps or underlies the implementation’s audio unit.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var auAudioUnit: AUAudioUnit { get }
```

#### Discussion

This provides an [`AUAudioUnit`](https://developer.apple.com/documentation/AudioToolbox/AUAudioUnit) that either wraps or underlies the implementation’s audio unit, depending on how the app packages the audio unit. Apps interact with this to control custom properties, select presets, and change parameters.

Don’t perform operations directly on the audio unit that may conflict with the engine’s state, which includes changing the initialization state, stream formats, channel layouts, or connections to other audio units.

## See Also

- [var latency: TimeInterval](avaudionode/latency.md)
  The processing latency of the node, in seconds.
- [var outputPresentationLatency: TimeInterval](avaudionode/outputpresentationlatency.md)
  The maximum render pipeline latency downstream of the node, in seconds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudionode/auaudiounit)*