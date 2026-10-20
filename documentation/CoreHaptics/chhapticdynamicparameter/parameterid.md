# parameterID

**Framework**: Core Haptics  
**Kind**: property  
**Role**: Instance Property

The dynamic parameter ID defining the type of parameter being modified.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
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

### Specifying a Dynamic Parameter’s Value
- [var relativeTime: TimeInterval](./relativetime.md)
  The time at which this dynamic parameter is applied, relative to the start time of the pattern.
- [var value: Float](./value.md)
  The value of the dynamic parameter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehaptics/chhapticdynamicparameter/parameterid)*