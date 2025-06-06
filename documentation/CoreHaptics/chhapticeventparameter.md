# CHHapticEventParameter

**Framework**: Core Haptics  
**Kind**: class

A static parameter value that represents a single property of the haptic pattern.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
class CHHapticEventParameter
```

#### Overview

Event parameters specify values for haptics associated with the event. For example, an intensity event parameter determines how intense the haptic feels when it fires. Event parameters are static; they don’t change over the course of the pattern. To change a parameter value after a haptic has started playing, use a [`CHHapticDynamicParameter`](chhapticdynamicparameter.md) to make an immediate change, or a [`CHHapticParameterCurve`](chhapticparametercurve.md) to transition smoothly.

![A rising blue line represents how a parameter curve changes the parameter’s value gradually over time, while an orange line shows how dynamic parameters change the parameter’s value immediately.](https://docs-assets.developer.apple.com/published/d1d479278871beef7f6678c56ea8743b/media-3197279%402x.png)

When you send a dynamic parameter to the haptic pattern, its value changes immediately, at the specified time. When you send a parameter curve instead, the value changes gradually according to the type of curve you specified.

## Topics

### Creating an Event Parameter
- [init(parameterID: CHHapticEvent.ParameterID, value: Float)](chhapticeventparameter/init(parameterid:value:).md)
  Creates a haptic event parameter from its ID and value.
- [CHHapticEvent.ParameterID](chhapticevent/parameterid.md)
  An identifier for an event parameter.
### Specifying an Event Parameter’s Value
- [var parameterID: CHHapticEvent.ParameterID](chhapticeventparameter/parameterid.md)
  The haptic parameter ID indicating what type of parameter the current event represents.
- [var value: Float](chhapticeventparameter/value.md)
  The value of the parameter.

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
- [class CHHapticDynamicParameter](chhapticdynamicparameter.md)
  A value that you send to a haptic pattern player to alter a property value during playback.
- [class CHHapticParameterCurve](chhapticparametercurve.md)
  A curve that you send to a haptic pattern player to alter a property value gradually during playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehaptics/chhapticeventparameter)*