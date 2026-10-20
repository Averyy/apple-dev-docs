# sustained

**Framework**: Core Haptics  
**Kind**: property  
**Role**: Type Property

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

```c
extern CHHapticEventParameterID CHHapticEventParameterIDSustained;
```

#### Discussion

This parameter is an event parameter. It determines whether or not the haptic continues playing at full strength after attack has finished, and before decay begins.

![A graphic showing the effect of sustain: on the left, turning sustain on causes attack and decay to happen outside the haptic pattern, whereas turning sustain off (on the right) causes attan’tand decay to happen within the haptic pattern.](https://developer.apple.com/tutorials/images/com.apple.corehaptics/media-3235480@2x.png)

If [`true`](../../../Swift/true.md), the engine sustains the haptic pattern throughout its specified duration, increasing only during its [`attackTime`](./attacktime.md), and decreasing only after its [`decayTime`](./decaytime.md). If [`false`](../../../Swift/false.md), the haptic doesn’t stay at full strength between attack and decay, tailing off even before its decay has begun.

## See Also

### Haptic Event Parameter IDs
- [static let hapticIntensity: CHHapticEvent.ParameterID](./hapticintensity.md)
  The strength of a haptic event.
- [static let hapticSharpness: CHHapticEvent.ParameterID](./hapticsharpness.md)
  The feel of a haptic event.
- [static let attackTime: CHHapticEvent.ParameterID](./attacktime.md)
  The time at which a haptic pattern’s intensity begins increasing.
- [static let decayTime: CHHapticEvent.ParameterID](./decaytime.md)
  The time at which a haptic pattern’s intensity begins decreasing.
- [static let releaseTime: CHHapticEvent.ParameterID](./releasetime.md)
  The time at which to begin fading the haptic pattern.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehaptics/chhapticevent/parameterid/sustained)*