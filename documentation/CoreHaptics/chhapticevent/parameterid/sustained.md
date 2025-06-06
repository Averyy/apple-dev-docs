# sustained

**Framework**: Core Haptics  
**Kind**: property

A Boolean value that indicates whether to sustain a haptic event for its specified duration.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
static let sustained: CHHapticEvent.ParameterID
```

#### Discussion

This parameter is an event parameter. It determines whether or not the haptic continues playing at full strength after attack has finished, and before decay begins.

![A graphic showing the effect of sustain: on the left, turning sustain on causes attack and decay to happen outside the haptic pattern, whereas turning sustain off (on the right) causes attan’tand decay to happen within the haptic pattern.](https://docs-assets.developer.apple.com/published/04bc2e5f6d5f61b14f7d15792da853b8/media-3235480%402x.png)

If [`true`](https://developer.apple.com/documentation/swift/true), the engine sustains the haptic pattern throughout its specified duration, increasing only during its [`attackTime`](chhapticevent/parameterid/attacktime.md), and decreasing only after its [`decayTime`](chhapticevent/parameterid/decaytime.md). If [`false`](https://developer.apple.com/documentation/swift/false), the haptic doesn’t stay at full strength between attack and decay, tailing off even before its decay has begun.

## See Also

- [static let hapticIntensity: CHHapticEvent.ParameterID](chhapticevent/parameterid/hapticintensity.md)
  The strength of a haptic event.
- [static let hapticSharpness: CHHapticEvent.ParameterID](chhapticevent/parameterid/hapticsharpness.md)
  The feel of a haptic event.
- [static let attackTime: CHHapticEvent.ParameterID](chhapticevent/parameterid/attacktime.md)
  The time at which a haptic pattern’s intensity begins increasing.
- [static let decayTime: CHHapticEvent.ParameterID](chhapticevent/parameterid/decaytime.md)
  The time at which a haptic pattern’s intensity begins decreasing.
- [static let releaseTime: CHHapticEvent.ParameterID](chhapticevent/parameterid/releasetime.md)
  The time at which to begin fading the haptic pattern.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehaptics/chhapticevent/parameterid/sustained)*