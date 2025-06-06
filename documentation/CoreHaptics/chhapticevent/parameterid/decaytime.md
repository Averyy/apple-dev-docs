# decayTime

**Framework**: Core Haptics  
**Kind**: property

The time at which a haptic pattern’s intensity begins decreasing.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
static let decayTime: CHHapticEvent.ParameterID
```

#### Discussion

This parameter can be an event parameter or a dynamic parameter. A fixed value indicates that the haptic begins decreasing in intensity at the set time, where time `0` indicates now, or the current time.

A dynamic value indicates that the start time of the decrease can change. For example, a value of `0` indicates that the decay time is at its default value. Positive values up to `1.0` increase the decay time exponentially, while negative values down to `-1.0` decrease the decay time exponentially.

Haptic intensity responds to this parameter. For example, the following graphic shows the intensity of a haptic pattern in gray. At the beginning, the haptic pattern’s intensity increases from zero to its final value over a certain amount of time; this duration is called the . As the haptic pattern reaches its end, the intensity gradually transitions to zero over a certain amount of time; this duration is called the .

![A series of lines showing how a haptic pattern ramps down in intensity for various values of decay.](https://docs-assets.developer.apple.com/published/772b8a678caa044cf704d0316bcfde5f/media-3199008%402x.png)

## See Also

- [static let hapticIntensity: CHHapticEvent.ParameterID](chhapticevent/parameterid/hapticintensity.md)
  The strength of a haptic event.
- [static let hapticSharpness: CHHapticEvent.ParameterID](chhapticevent/parameterid/hapticsharpness.md)
  The feel of a haptic event.
- [static let attackTime: CHHapticEvent.ParameterID](chhapticevent/parameterid/attacktime.md)
  The time at which a haptic pattern’s intensity begins increasing.
- [static let releaseTime: CHHapticEvent.ParameterID](chhapticevent/parameterid/releasetime.md)
  The time at which to begin fading the haptic pattern.
- [static let sustained: CHHapticEvent.ParameterID](chhapticevent/parameterid/sustained.md)
  A Boolean value that indicates whether to sustain a haptic event for its specified duration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehaptics/chhapticevent/parameterid/decaytime)*