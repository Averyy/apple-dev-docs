# value

**Framework**: Core Haptics  
**Kind**: property

The value of the dynamic parameter.

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

#### Discussion

The range of possible values varies between different parameters. For example, the dynamic parameter for haptic intensity ranges from 0 and 1, indicating a multiplicative envelope, whereas the dynamic parameter for haptic sharpness varies between -1 and 1, indicating that the parameter can additively increase or decrease the sharpness.

## See Also

- [var parameterID: CHHapticDynamicParameter.ID](chhapticdynamicparameter/parameterid.md)
  The dynamic parameter ID defining the type of parameter being modified.
- [var relativeTime: TimeInterval](chhapticdynamicparameter/relativetime.md)
  The time at which this dynamic parameter is applied, relative to the start time of the pattern.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehaptics/chhapticdynamicparameter/value)*