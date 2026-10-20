# isMutedForHaptics

**Framework**: Core Haptics  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the engine mutes haptics.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var isMutedForHaptics: Bool { get set }
```

```objc
@property (nonatomic, readwrite) BOOL isMutedForHaptics;
```

## See Also

### Modifying Playback Properties
- [var playsAudioOnly: Bool](./playsaudioonly.md)
  A Boolean value that indicates whether the engine ignores haptic events and plays audio events only.
- [var playsHapticsOnly: Bool](./playshapticsonly.md)
  A Boolean value that indicates whether the engine ignores audio events.
- [var isMutedForAudio: Bool](./ismutedforaudio.md)
  A Boolean value that indicates whether the engine mutes audio.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehaptics/chhapticengine/ismutedforhaptics)*