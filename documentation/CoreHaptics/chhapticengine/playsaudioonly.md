# playsAudioOnly

**Framework**: Core Haptics  
**Kind**: property

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

#### Discussion

If you set a new value on a running engine, you must restart the engine for the change to take effect.

The default value is [`false`](https://developer.apple.com/documentation/swift/false).

## See Also

- [var playsHapticsOnly: Bool](chhapticengine/playshapticsonly.md)
  A Boolean value that indicates whether the engine ignores audio events.
- [var isMutedForAudio: Bool](chhapticengine/ismutedforaudio.md)
  A Boolean value that indicates whether the engine mutes audio.
- [var isMutedForHaptics: Bool](chhapticengine/ismutedforhaptics.md)
  A Boolean value that indicates whether the engine mutes haptics.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehaptics/chhapticengine/playsaudioonly)*