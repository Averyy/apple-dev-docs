# attackTime

**Framework**: Core Haptics  
**Kind**: property  
**Role**: Type Property

The time at which a haptic pattern’s intensity begins increasing.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
static let attackTime: CHHapticEvent.ParameterID
```

```c
extern CHHapticEventParameterID CHHapticEventParameterIDAttackTime;
```

#### Discussion

This parameter can be an event parameter or a dynamic parameter. An event parameter indicates that the haptic begins increasing in intensity at the set time, where time `0` indicates now, or the current time.

A dynamic value indicates that the time at which ramp-up begins can change. For example, a value of `0` indicates that the attack time is at its default value. Positive values up to `1.0` increase the attack time exponentially, while negative values down to `-1.0` decrease the attack time exponentially. Haptic intensity responds to this parameter.

![A series of lines showing how a haptic pattern ramps up in intensity for various values of attack.](https://developer.apple.com/tutorials/images/com.apple.corehaptics/media-3235478@2x.png)

## See Also

### Haptic Event Parameter IDs
- [static let hapticIntensity: CHHapticEvent.ParameterID](./hapticintensity.md)
  The strength of a haptic event.
- [static let hapticSharpness: CHHapticEvent.ParameterID](./hapticsharpness.md)
  The feel of a haptic event.
- [static let decayTime: CHHapticEvent.ParameterID](./decaytime.md)
  The time at which a haptic pattern’s intensity begins decreasing.
- [static let releaseTime: CHHapticEvent.ParameterID](./releasetime.md)
  The time at which to begin fading the haptic pattern.
- [static let sustained: CHHapticEvent.ParameterID](./sustained.md)
  A Boolean value that indicates whether to sustain a haptic event for its specified duration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehaptics/chhapticevent/parameterid/attacktime)*