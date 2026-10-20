# CHHapticParameterCurve.ControlPoint

**Framework**: Core Haptics  
**Kind**: class  
**Role**: Class

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

```objc
@interface CHHapticParameterCurveControlPoint : NSObject
```

## Topics

### Creating a Control Point
- [init(relativeTime: TimeInterval, value: Float)](./controlpoint/init%28relativetime,value%29.md)
  Creates a control point from its time and value.
### Specifying Control Point Coordinates
- [var relativeTime: TimeInterval](./controlpoint/relativetime.md)
  The time at which the associated parameter reaches this value, relative to the start time of the parameter curve.
- [var value: Float](./controlpoint/value.md)
  The parameter value of the point.

## Relationships

### Inherits From
- [NSObject](../../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../../Swift/cvararg.md)
- [CustomDebugStringConvertible](../../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [NSObjectProtocol](../../ObjectiveC/nsobjectprotocol.md)

## See Also

### Creating a Curve
- [init(parameterID: CHHapticDynamicParameter.ID, controlPoints: [CHHapticParameterCurve.ControlPoint], relativeTime: TimeInterval)](./init%28parameterid,controlpoints,relativetime%29.md)
  Creates a parameter curve from its parameter ID, control points, and start time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehaptics/chhapticparametercurve/controlpoint)*