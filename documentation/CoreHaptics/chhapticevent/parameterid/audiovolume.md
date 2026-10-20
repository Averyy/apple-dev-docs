# audioVolume

**Framework**: Core Haptics  
**Kind**: property  
**Role**: Type Property

The volume of an audio event.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
static let audioVolume: CHHapticEvent.ParameterID
```

```c
extern CHHapticEventParameterID CHHapticEventParameterIDAudioVolume;
```

#### Discussion

This parameter value ranges from 0.0 (silent) to 1.0 (maximum volume).

## See Also

### Audio Event Parameter IDs
- [static let audioPan: CHHapticEvent.ParameterID](./audiopan.md)
  The stereo panning of an audio event.
- [static let audioPitch: CHHapticEvent.ParameterID](./audiopitch.md)
  The pitch of an audio event.
- [static let audioBrightness: CHHapticEvent.ParameterID](./audiobrightness.md)
  The high-frequency content of an audio event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehaptics/chhapticevent/parameterid/audiovolume)*