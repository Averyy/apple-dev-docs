# CHHapticParameterCurve.ControlPoint

**Framework**: Core Haptics  
**Kind**: class

A single control point in a parameter curve.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
class ControlPoint
```

## Topics

### Creating a Control Point
- [init(relativeTime: TimeInterval, value: Float)](chhapticparametercurve/controlpoint/init(relativetime:value:).md)
  Creates a control point from its time and value.
### Specifying Control Point Coordinates
- [var relativeTime: TimeInterval](chhapticparametercurve/controlpoint/relativetime.md)
  The time at which the associated parameter reaches this value, relative to the start time of the parameter curve.
- [var value: Float](chhapticparametercurve/controlpoint/value.md)
  The parameter value of the point.

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

- [init(parameterID: CHHapticDynamicParameter.ID, controlPoints: [CHHapticParameterCurve.ControlPoint], relativeTime: TimeInterval)](chhapticparametercurve/init(parameterid:controlpoints:relativetime:).md)
  Creates a parameter curve from its parameter ID, control points, and start time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehaptics/chhapticparametercurve/controlpoint)*