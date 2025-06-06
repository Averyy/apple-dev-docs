# hapticIntensity

**Framework**: Core Haptics  
**Kind**: property

The strength of a haptic event.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
static let hapticIntensity: CHHapticEvent.ParameterID
```

#### Discussion

This parameter maps to the haptic pattern’s amplitude or strength. Its value ranges from 0.0 (weak) to 1.0 (strong). Think of intensity as the volume of a haptic pattern, indicating how impactful it feels in the user’s hand. The higher the haptic intensity, the stronger the resulting haptic.

![Short blue bars show the intensity of a transient haptic event on the left, and long orange bars show a continuous haptic event on the right.](https://docs-assets.developer.apple.com/published/231267e4c61ce4a0cf7f2dcf45e0f9f7/media-3242667%402x.png)

To change the intensity dynamically, use [`hapticIntensityControl`](chhapticdynamicparameter/id/hapticintensitycontrol.md).

## See Also

- [static let hapticSharpness: CHHapticEvent.ParameterID](chhapticevent/parameterid/hapticsharpness.md)
  The feel of a haptic event.
- [static let attackTime: CHHapticEvent.ParameterID](chhapticevent/parameterid/attacktime.md)
  The time at which a haptic pattern’s intensity begins increasing.
- [static let decayTime: CHHapticEvent.ParameterID](chhapticevent/parameterid/decaytime.md)
  The time at which a haptic pattern’s intensity begins decreasing.
- [static let releaseTime: CHHapticEvent.ParameterID](chhapticevent/parameterid/releasetime.md)
  The time at which to begin fading the haptic pattern.
- [static let sustained: CHHapticEvent.ParameterID](chhapticevent/parameterid/sustained.md)
  A Boolean value that indicates whether to sustain a haptic event for its specified duration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehaptics/chhapticevent/parameterid/hapticintensity)*