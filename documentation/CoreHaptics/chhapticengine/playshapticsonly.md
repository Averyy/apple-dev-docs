# playsHapticsOnly

**Framework**: Core Haptics  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, readwrite) BOOL playsHapticsOnly;
```

#### Discussion

Setting this property to [`true`](../../Swift/true.md) causes the engine to ignore all audio events, such as [`audioContinuous`](../chhapticevent/eventtype/audiocontinuous.md) and [`audioCustom`](../chhapticevent/eventtype/audiocustom.md). This also reduces latency of starting haptic playback.

> ❗ **Important**:  Changing the value of this property on a running engine has no effect until you stop and restart the engine.

## See Also

### Modifying Playback Properties
- [var playsAudioOnly: Bool](./playsaudioonly.md)
  A Boolean value that indicates whether the engine ignores haptic events and plays audio events only.
- [var isMutedForAudio: Bool](./ismutedforaudio.md)
  A Boolean value that indicates whether the engine mutes audio.
- [var isMutedForHaptics: Bool](./ismutedforhaptics.md)
  A Boolean value that indicates whether the engine mutes haptics.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehaptics/chhapticengine/playshapticsonly)*