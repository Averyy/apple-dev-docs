# value

**Framework**: Core Haptics  
**Kind**: property  
**Role**: Instance Property

The parameter value of the point.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var value: Float { get set }
```

```objc
@property (readwrite) float value;
```

## Discussion

Think of the value as the control point’s y-coordinate.

> **Note**:  The range of possible values varies between different parameters.

## See Also

### Specifying Control Point Coordinates
- [var relativeTime: TimeInterval](./relativetime.md)
  The time at which the associated parameter reaches this value, relative to the start time of the parameter curve.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehaptics/chhapticparametercurve/controlpoint/value)*