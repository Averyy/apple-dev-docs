# value

**Framework**: Core Haptics  
**Kind**: property

The value of the parameter.

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

The range of possible values varies between different parameters. For example, haptic intensity and haptic sharpness vary between `0` and `1`, with `0` indicating minimal intensity or sharpness, and `1` indicating the maximum intensity or sharpness value allowed. See the individual parameter pages for the ranges and default values of each parameter.

## See Also

- [var parameterID: CHHapticEvent.ParameterID](chhapticeventparameter/parameterid.md)
  The haptic parameter ID indicating what type of parameter the current event represents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehaptics/chhapticeventparameter/value)*