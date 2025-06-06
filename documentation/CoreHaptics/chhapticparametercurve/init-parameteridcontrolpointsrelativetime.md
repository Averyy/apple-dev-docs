# init(parameterID:controlPoints:relativeTime:)

**Framework**: Core Haptics  
**Kind**: init

Creates a parameter curve from its parameter ID, control points, and start time.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS ?+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
init(parameterID: CHHapticDynamicParameter.ID, controlPoints: [CHHapticParameterCurve.ControlPoint], relativeTime: TimeInterval)
```

## Parameters

- `parameterID`: The ID indicating the type of the dynamic parameter that the parameter curve is modifying.
- `controlPoints`: An array of control points defining how the parameter curve changes over time.
- `relativeTime`: The time at which to start applying the parameter curve.

## See Also

- [CHHapticParameterCurve.ControlPoint](chhapticparametercurve/controlpoint.md)
  A single control point in a parameter curve.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehaptics/chhapticparametercurve/init(parameterid:controlpoints:relativetime:))*