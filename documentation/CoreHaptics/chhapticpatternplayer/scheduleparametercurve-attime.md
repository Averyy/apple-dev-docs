# scheduleParameterCurve(_:atTime:)

**Framework**: Core Haptics  
**Kind**: method  
**Required**: Yes

Schedules a parameter curve to begin transitioning a parameter at a certain time.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func scheduleParameterCurve(_ parameterCurve: CHHapticParameterCurve, atTime time: TimeInterval) throws
```

#### Discussion

Scheduling a parameter curve tells the haptic pattern player to vary a parameter gradually along the curve. For example, if the intensity of a haptic pattern is `0` at the time of application, then a curve created to set the haptic intensity to `1` will smoothly hit every single continuous value between `0` and `1` during the transition.

![A graph showing how dynamic parameters change instantly, whereas parameter curves vary gradually.](https://docs-assets.developer.apple.com/published/2ff5660c581db9bc320616fbdcfb8964/media-3189138%402x.png)

Scheduling a parameter curve is analogous to sending a dynamic parameter with [`sendParameters(_:atTime:)`](chhapticpatternplayer/sendparameters(_:attime:).md); the only difference is that the curve transitions the parameter gradually, whereas the dynamic parameter changes the parameter immediately at a certain time.

Schedule a parameter curve for one parameter at a time, and specify control points to characterize the curve’s shape. For more information on creating or specifying a parameter curve, see [`CHHapticParameterCurve`](chhapticparametercurve.md).

## Parameters

- `parameterCurve`: The curve along which to vary the parameter.
- `time`: The time at which to begin applying the parameter curve.

## See Also

- [func sendParameters([CHHapticDynamicParameter], atTime: TimeInterval) throws](chhapticpatternplayer/sendparameters(_:attime:).md)
  Sends an array of haptic parameters, starting at the specified time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehaptics/chhapticpatternplayer/scheduleparametercurve(_:attime:))*