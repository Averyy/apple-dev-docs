# EquatableComparisonOperator

**Framework**: App Intents  
**Kind**: enum

Operators that indicate the type of equality check for a conditional statement.

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
enum EquatableComparisonOperator
```

## Topics

### Equatable operators
- [EquatableComparisonOperator.equalTo](equatablecomparisonoperator/equalto.md)
  An operator that determines if the parameter and the value are equal.
- [EquatableComparisonOperator.notEqualTo](equatablecomparisonoperator/notequalto.md)
  An operator that determines if the parameter and the value aren’t equal.
### Operators
- [static func == (EquatableComparisonOperator, EquatableComparisonOperator) -> Bool](equatablecomparisonoperator/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var hashValue: Int](equatablecomparisonoperator/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](equatablecomparisonoperator/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](equatablecomparisonoperator/equatable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [init<Parameter>(KeyPath<Intent, Parameter>, HasValueComparisonOperator, () -> WhenCondition, otherwise: () -> Otherwise)](parametersummarywhencondition/init(_:_:_:otherwise:).md)
- [enum ComparableComparisonOperator](comparablecomparisonoperator.md)
  Operators that indicate the type of comparison check for a conditional statement.
- [enum HasValueComparisonOperator](hasvaluecomparisonoperator.md)
  Operators that indicate the type of value check for a conditional statement.
- [enum OneOfComparisonOperator](oneofcomparisonoperator.md)
  Operators that indicate the type of containment check for a conditional statement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/equatablecomparisonoperator)*