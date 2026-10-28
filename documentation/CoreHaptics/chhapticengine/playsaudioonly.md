# playsAudioOnly

**Framework**: Core Haptics  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the engine ignores haptic events and plays audio events only.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var playsAudioOnly: Bool { get set }
```

```objc
@property (nonatomic, readwrite) BOOL playsAudioOnly;
```

## Discussion

If you set a new value on a running engine, you must restart the engine for the change to take effect.

The default value is [`false`](../../Swift/false.md).

## See Also

### Modifying Playback Properties
- [var playsHapticsOnly: Bool](./playshapticsonly.md)
  A Boolean value that indicates whether the engine ignores audio events.
- [var isMutedForAudio: Bool](./ismutedforaudio.md)
  A Boolean value that indicates whether the engine mutes audio.
- [var isMutedForHaptics: Bool](./ismutedforhaptics.md)
  A Boolean value that indicates whether the engine mutes haptics.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehaptics/chhapticengine/playsaudioonly)*