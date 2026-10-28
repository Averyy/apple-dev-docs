# relativeTime

**Framework**: Core Haptics  
**Kind**: property  
**Role**: Instance Property

The time at which the associated parameter reaches this value, relative to the start time of the parameter curve.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var relativeTime: TimeInterval { get set }
```

```objc
@property (readwrite) NSTimeInterval relativeTime;
```

## Discussion

Think of the time as the control point’s x-coordinate.

## See Also

### Specifying Control Point Coordinates
- [var value: Float](./value.md)
  The parameter value of the point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehaptics/chhapticparametercurve/controlpoint/relativetime)*