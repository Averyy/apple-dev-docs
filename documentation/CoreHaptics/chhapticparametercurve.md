# CHHapticParameterCurve

**Framework**: Core Haptics  
**Kind**: class

A curve that you send to a haptic pattern player to alter a property value gradually during playback.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS ?+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
class CHHapticParameterCurve
```

## Mentions

- [Representing haptic patterns in AHAP files](representing-haptic-patterns-in-ahap-files.md)

#### Overview

Parameter curves serve the same purpose as dynamic parameters in that they alter a property value during playback. Unlike dynamic parameters, which change a property value instantaneously, parameter curves interpolate linearly between parameter values to ensure a smooth transition.

![A rising blue line represents how a parameter curve changes the parameter’s value gradually over time, while an orange line shows how dynamic parameters change the parameter’s value immediately.](https://docs-assets.developer.apple.com/published/d3baad051047d3e1a340b1dbd49ed56c/media-3197275%402x.png)

For example, a parameter curven’tr haptic intensity modulates the intensity over time, ensuring a smooth transition between the current intensity and the upcoming one. Parameter curves apply to all events in a pattern; it isn’t possible to apply one to only a single event.

## Topics

### Creating a Curve
- [init(parameterID: CHHapticDynamicParameter.ID, controlPoints: [CHHapticParameterCurve.ControlPoint], relativeTime: TimeInterval)](chhapticparametercurve/init(parameterid:controlpoints:relativetime:).md)
  Creates a parameter curve from its parameter ID, control points, and start time.
- [CHHapticParameterCurve.ControlPoint](chhapticparametercurve/controlpoint.md)
  A single control point in a parameter curve.
### Describing the Curve
- [var controlPoints: [CHHapticParameterCurve.ControlPoint]](chhapticparametercurve/controlpoints.md)
  An array containing the curve’s control points.
- [var parameterID: CHHapticDynamicParameter.ID](chhapticparametercurve/parameterid.md)
  The parameter ID defining the type of parameter that the curve represents.
- [var relativeTime: TimeInterval](chhapticparametercurve/relativetime.md)
  The time at which this parameter curve is applied, relative to the start time of the pattern.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Delivering Rich App Experiences with Haptics](delivering-rich-app-experiences-with-haptics.md)
  Enhance your app’s experience by incorporating haptic and sound feedback into key interactive moments.
- [Playing Collision-Based Haptic Patterns](playing-collision-based-haptic-patterns.md)
  Play a custom haptic pattern whose strength depends on an object’s collision speed.
- [Updating Continuous and Transient Haptic Parameters in Real Time](updating-continuous-and-transient-haptic-parameters-in-real-time.md)
  Generate continuous and transient haptic patterns in response to user touch.
- [class CHHapticEvent](chhapticevent.md)
  An object that describes a single haptic or audio event.
- [class CHHapticEventParameter](chhapticeventparameter.md)
  A static parameter value that represents a single property of the haptic pattern.
- [class CHHapticDynamicParameter](chhapticdynamicparameter.md)
  A value that you send to a haptic pattern player to alter a property value during playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehaptics/chhapticparametercurve)*