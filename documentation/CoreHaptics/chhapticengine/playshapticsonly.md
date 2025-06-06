# playsHapticsOnly

**Framework**: Core Haptics  
**Kind**: property

A Boolean value that indicates whether the engine ignores audio events.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var playsHapticsOnly: Bool { get set }
```

#### Discussion

Setting this property to [`true`](https://developer.apple.com/documentation/swift/true) causes the engine to ignore all audio events, such as [`audioContinuous`](chhapticevent/eventtype/audiocontinuous.md) and [`audioCustom`](chhapticevent/eventtype/audiocustom.md). This also reduces latency of starting haptic playback.

> ❗ **Important**:  Changing the value of this property on a running engine has no effect until you stop and restart the engine.

 Changing the value of this property on a running engine has no effect until you stop and restart the engine.

## See Also

- [var playsAudioOnly: Bool](chhapticengine/playsaudioonly.md)
  A Boolean value that indicates whether the engine ignores haptic events and plays audio events only.
- [var isMutedForAudio: Bool](chhapticengine/ismutedforaudio.md)
  A Boolean value that indicates whether the engine mutes audio.
- [var isMutedForHaptics: Bool](chhapticengine/ismutedforhaptics.md)
  A Boolean value that indicates whether the engine mutes haptics.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehaptics/chhapticengine/playshapticsonly)*