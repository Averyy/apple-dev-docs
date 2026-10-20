# MLNumericConstraint

**Framework**: Core ML  
**Kind**: class  
**Role**: Class

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

```objc
@interface MLNumericConstraint : NSObject
```

## Topics

### Numeric Constraints
- [var minNumber: NSNumber](./mlnumericconstraint/minnumber.md)
  The smallest numerical value allowed by this constraint.
- [var maxNumber: NSNumber](./mlnumericconstraint/maxnumber.md)
  The largest numerical value allowed by this constraint.
- [var enumeratedNumbers: Set<NSNumber>?](./mlnumericconstraint/enumeratednumbers.md)
  A set of the numbers allowed in this constraint.
### Initializers
- [init?(coder: NSCoder)](./mlnumericconstraint/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Constraining numeric values
- [var numericConstraint: MLNumericConstraint?](./mlparameterdescription/numericconstraint.md)
  The constraints of this paramter description value, if and only if the value is numerical.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlnumericconstraint)*