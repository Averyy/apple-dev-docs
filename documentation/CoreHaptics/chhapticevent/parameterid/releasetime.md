# releaseTime

**Framework**: Core Haptics  
**Kind**: property

The time at which to begin fading the haptic pattern.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
static let releaseTime: CHHapticEvent.ParameterID
```

#### Discussion

Specify the release time relative to the current time (`t = 0`), in seconds. It indicates when the pattern’s decay process begins. Its value ranges from `0` to `1`, with a default value of `0`.

## See Also

- [static let hapticIntensity: CHHapticEvent.ParameterID](chhapticevent/parameterid/hapticintensity.md)
  The strength of a haptic event.
- [static let hapticSharpness: CHHapticEvent.ParameterID](chhapticevent/parameterid/hapticsharpness.md)
  The feel of a haptic event.
- [static let attackTime: CHHapticEvent.ParameterID](chhapticevent/parameterid/attacktime.md)
  The time at which a haptic pattern’s intensity begins increasing.
- [static let decayTime: CHHapticEvent.ParameterID](chhapticevent/parameterid/decaytime.md)
  The time at which a haptic pattern’s intensity begins decreasing.
- [static let sustained: CHHapticEvent.ParameterID](chhapticevent/parameterid/sustained.md)
  A Boolean value that indicates whether to sustain a haptic event for its specified duration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehaptics/chhapticevent/parameterid/releasetime)*