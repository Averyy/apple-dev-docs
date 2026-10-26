# AUAudioUnit

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```objc
@property (nonatomic, readonly) AUAudioUnit * AUAudioUnit;
```

#### Discussion

An AUAudioUnit wrapping or underlying the implementation’s AudioUnit.

This provides an AUAudioUnit which either wraps or underlies the implementation’s AudioUnit, depending on how that audio unit is packaged. Applications can interact with this AUAudioUnit to control custom properties, select presets, change parameters, etc.

No operations that may conflict with state maintained by the engine should be performed directly on the audio unit. These include changing initialization state, stream formats, channel layouts or connections to other audio units.

## See Also

### Getting audio node properties
- [var latency: TimeInterval](./latency.md)
  The processing latency of the node, in seconds.
- [var outputPresentationLatency: TimeInterval](./outputpresentationlatency.md)
  The maximum render pipeline latency downstream of the node, in seconds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudionode/auaudiounit-1kkjr)*