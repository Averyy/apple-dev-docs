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
### Initializers
- [init?(coder: NSCoder)](mlnumericconstraint/init(coder:).md)

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)

## See Also

- [var numericConstraint: MLNumericConstraint?](mlparameterdescription/numericconstraint.md)
  The constraints of this paramter description value, if and only if the value is numerical.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlnumericconstraint)*