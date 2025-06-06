# hapticSharpness

**Framework**: Core Haptics  
**Kind**: property

The feel of a haptic event.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
static let hapticSharpness: CHHapticEvent.ParameterID
```

#### Discussion

Specify a pattern’s sharpness by setting this value from 0.0 to 1.0. Haptic patterns with low sharpness have a round and organic feel, whereas haptic patterns with high sharpness feel more crisp and precise. The diagram below depicts sharpness of haptic events as a single line to indicate the sensation of persistent feedback against the user’s hand:

![A diagram showing sharpness of three transient haptic events on the left, and sharpness of three continuous haptic events on the right.](https://docs-assets.developer.apple.com/published/3f9b18cbf32aef4988e7731251dfaf54/media-3242668%402x.png)

To change the sharpness dynamically, use [`hapticSharpnessControl`](chhapticdynamicparameter/id/hapticsharpnesscontrol.md).

## See Also

- [static let hapticIntensity: CHHapticEvent.ParameterID](chhapticevent/parameterid/hapticintensity.md)
  The strength of a haptic event.
- [static let attackTime: CHHapticEvent.ParameterID](chhapticevent/parameterid/attacktime.md)
  The time at which a haptic pattern’s intensity begins increasing.
- [static let decayTime: CHHapticEvent.ParameterID](chhapticevent/parameterid/decaytime.md)
  The time at which a haptic pattern’s intensity begins decreasing.
- [static let releaseTime: CHHapticEvent.ParameterID](chhapticevent/parameterid/releasetime.md)
  The time at which to begin fading the haptic pattern.
- [static let sustained: CHHapticEvent.ParameterID](chhapticevent/parameterid/sustained.md)
  A Boolean value that indicates whether to sustain a haptic event for its specified duration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehaptics/chhapticevent/parameterid/hapticsharpness)*