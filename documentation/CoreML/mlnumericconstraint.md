# MLNumericConstraint

**Framework**: Core ML  
**Kind**: class

The value limitations of a number.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
class MLNumericConstraint
```

## Topics

### Numeric Constraints
- [var minNumber: NSNumber](mlnumericconstraint/minnumber.md)
  The smallest numerical value allowed by this constraint.
- [var maxNumber: NSNumber](mlnumericconstraint/maxnumber.md)
  The largest numerical value allowed by this constraint.
- [var enumeratedNumbers: Set<NSNumber>?](mlnumericconstraint/enumeratednumbers.md)
  A set of the numbers allowed in this constraint.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [var numericConstraint: MLNumericConstraint?](mlparameterdescription/numericconstraint.md)
  The constraints of this paramter description value, if and only if the value is numerical.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlnumericconstraint)*