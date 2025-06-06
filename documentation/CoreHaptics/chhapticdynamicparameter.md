# CHHapticDynamicParameter

**Framework**: Core Haptics  
**Kind**: class

A value that you send to a haptic pattern player to alter a property value during playback.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
class CHHapticDynamicParameter
```

#### Overview

Dynamic parameters change their associated event parameters at specific times. When you send a dynamic parameter to a haptic pattern player, the value associated with the parameter changes abruptly at the specified time, across all events in the pattern. To precipitate a gradual change, use a [`CHHapticParameterCurve`](chhapticparametercurve.md) object.

For haptic intensity and audio volume, the final property value is equal to the original event parameter value multiplied by the dynamic parameter value. For all other parameters, the final property value is equal to the dynamic parameter value added to the original event parameter value. In both cases, the resulting value is limited to the range with minimum and maximum values corresponding to the specified event parameter.

## Topics

### Creating a Dynamic Parameter
- [init(parameterID: CHHapticDynamicParameter.ID, value: Float, relativeTime: TimeInterval)](chhapticdynamicparameter/init(parameterid:value:relativetime:).md)
  Creates a dynamic parameter from its ID, value, and start time.
- [CHHapticDynamicParameter.ID](chhapticdynamicparameter/id.md)
  The identifier that reveals the type of property associated with a dynamic parameter.
### Specifying a Dynamic Parameter’s Value
- [var parameterID: CHHapticDynamicParameter.ID](chhapticdynamicparameter/parameterid.md)
  The dynamic parameter ID defining the type of parameter being modified.
- [var relativeTime: TimeInterval](chhapticdynamicparameter/relativetime.md)
  The time at which this dynamic parameter is applied, relative to the start time of the pattern.
- [var value: Float](chhapticdynamicparameter/value.md)
  The value of the dynamic parameter.

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
- [class CHHapticParameterCurve](chhapticparametercurve.md)
  A curve that you send to a haptic pattern player to alter a property value gradually during playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehaptics/chhapticdynamicparameter)*