# controlPoints

**Framework**: Core Haptics  
**Kind**: property  
**Role**: Instance Property

An array containing the curve’s control points.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var controlPoints: [CHHapticParameterCurve.ControlPoint] { get }
```

```objc
@property (readonly) NSArray<CHHapticParameterCurveControlPoint *> * controlPoints;
```

## See Also

### Describing the Curve
- [var parameterID: CHHapticDynamicParameter.ID](./parameterid.md)
  The parameter ID defining the type of parameter that the curve represents.
- [var relativeTime: TimeInterval](./relativetime.md)
  The time at which this parameter curve is applied, relative to the start time of the pattern.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehaptics/chhapticparametercurve/controlpoints)*