# parameterID

**Framework**: Core Haptics  
**Kind**: property  
**Role**: Instance Property

The parameter ID defining the type of parameter that the curve represents.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var parameterID: CHHapticDynamicParameter.ID { get }
```

```objc
@property (readonly) CHHapticDynamicParameterID parameterID;
```

## See Also

### Describing the Curve
- [var controlPoints: [CHHapticParameterCurve.ControlPoint]](./controlpoints.md)
  An array containing the curve’s control points.
- [var relativeTime: TimeInterval](./relativetime.md)
  The time at which this parameter curve is applied, relative to the start time of the pattern.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehaptics/chhapticparametercurve/parameterid)*