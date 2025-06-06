# ComparableComparisonOperator

**Framework**: App Intents  
**Kind**: enum

Operators that indicate the type of comparison check for a conditional statement.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
enum ComparableComparisonOperator
```

## Topics

### Comparable operators
- [ComparableComparisonOperator.greaterThan](comparablecomparisonoperator/greaterthan.md)
  An operator that determines if the parameter is greater than the value.
- [ComparableComparisonOperator.greaterThanOrEqualTo](comparablecomparisonoperator/greaterthanorequalto.md)
  An operator that determines if the parameter is greater than or equal to the value.
- [ComparableComparisonOperator.lessThan](comparablecomparisonoperator/lessthan.md)
  An operator that determines if the parameter is less than the value.
- [ComparableComparisonOperator.lessThanOrEqualTo](comparablecomparisonoperator/lessthanorequalto.md)
  An operator that determines if the parameter is less than or equal to the value.
### Operators
- [static func == (ComparableComparisonOperator, ComparableComparisonOperator) -> Bool](comparablecomparisonoperator/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var hashValue: Int](comparablecomparisonoperator/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](comparablecomparisonoperator/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](comparablecomparisonoperator/equatable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [init<Parameter>(KeyPath<Intent, Parameter>, HasValueComparisonOperator, () -> WhenCondition, otherwise: () -> Otherwise)](parametersummarywhencondition/init(_:_:_:otherwise:).md)
- [enum EquatableComparisonOperator](equatablecomparisonoperator.md)
  Operators that indicate the type of equality check for a conditional statement.
- [enum HasValueComparisonOperator](hasvaluecomparisonoperator.md)
  Operators that indicate the type of value check for a conditional statement.
- [enum OneOfComparisonOperator](oneofcomparisonoperator.md)
  Operators that indicate the type of containment check for a conditional statement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/comparablecomparisonoperator)*