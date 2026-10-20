# audioPitch

**Framework**: Core Haptics  
**Kind**: property  
**Role**: Type Property

The pitch of an audio event.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
static let audioPitch: CHHapticEvent.ParameterID
```

```c
extern CHHapticEventParameterID CHHapticEventParameterIDAudioPitch;
```

#### Discussion

This parameter value ranges from -1.0 (lowest pitch) to 1.0 (highest pitch).

## See Also

### Audio Event Parameter IDs
- [static let audioVolume: CHHapticEvent.ParameterID](./audiovolume.md)
  The volume of an audio event.
- [static let audioPan: CHHapticEvent.ParameterID](./audiopan.md)
  The stereo panning of an audio event.
- [static let audioBrightness: CHHapticEvent.ParameterID](./audiobrightness.md)
  The high-frequency content of an audio event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehaptics/chhapticevent/parameterid/audiopitch)*