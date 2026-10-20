# relativeTime

**Framework**: Core Haptics  
**Kind**: property  
**Role**: Instance Property

The time at which this dynamic parameter is applied, relative to the start time of the pattern.

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

## See Also

### Specifying a Dynamic Parameter’s Value
- [var parameterID: CHHapticDynamicParameter.ID](./parameterid.md)
  The dynamic parameter ID defining the type of parameter being modified.
- [var value: Float](./value.md)
  The value of the dynamic parameter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehaptics/chhapticdynamicparameter/relativetime)*