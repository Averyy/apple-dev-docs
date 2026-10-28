# audioPan

**Framework**: Core Haptics  
**Kind**: property  
**Role**: Type Property

The stereo panning of an audio event.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
static let audioPan: CHHapticEvent.ParameterID
```

```c
extern CHHapticEventParameterID CHHapticEventParameterIDAudioPan;
```

## Discussion

This parameter value ranges from -1.0 (panned hard left) to 1.0 (panned hard right). The default value is 0.0 (center panned).

## See Also

### Audio Event Parameter IDs
- [static let audioVolume: CHHapticEvent.ParameterID](./audiovolume.md)
  The volume of an audio event.
- [static let audioPitch: CHHapticEvent.ParameterID](./audiopitch.md)
  The pitch of an audio event.
- [static let audioBrightness: CHHapticEvent.ParameterID](./audiobrightness.md)
  The high-frequency content of an audio event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehaptics/chhapticevent/parameterid/audiopan)*