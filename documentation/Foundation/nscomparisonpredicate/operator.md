# NSComparisonPredicate.Operator

**Framework**: Foundation  
**Kind**: enum  
**Role**: Enumeration

Defines the type of comparison for a comparison predicate.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
enum Operator
```

```c
enum NSPredicateOperatorType : NSUInteger;
```

## Topics

### Constants
- [NSComparisonPredicate.Operator.lessThan](./operator/lessthan.md)
  A less-than predicate.
- [NSComparisonPredicate.Operator.lessThanOrEqualTo](./operator/lessthanorequalto.md)
  A less-than-or-equal-to predicate.
- [NSComparisonPredicate.Operator.greaterThan](./operator/greaterthan.md)
  A greater-than predicate.
- [NSComparisonPredicate.Operator.greaterThanOrEqualTo](./operator/greaterthanorequalto.md)
  A greater-than-or-equal-to predicate.
- [NSComparisonPredicate.Operator.equalTo](./operator/equalto.md)
  An equal-to predicate.
- [NSComparisonPredicate.Operator.notEqualTo](./operator/notequalto.md)
  A not-equal-to predicate.
- [NSComparisonPredicate.Operator.matches](./operator/matches.md)
  A full regular expression matching predicate.
- [NSComparisonPredicate.Operator.like](./operator/like.md)
  A simple subset of the MATCHES predicate, similar in behavior to SQL `LIKE`.
- [NSComparisonPredicate.Operator.beginsWith](./operator/beginswith.md)
  A begins-with predicate.
- [NSComparisonPredicate.Operator.endsWith](./operator/endswith.md)
  An ends-with predicate.
- [NSComparisonPredicate.Operator.in](./operator/in.md)
  A predicate to determine if the left hand side is in the right hand side.
- [NSComparisonPredicate.Operator.customSelector](./operator/customselector.md)
  A predicate that uses a custom selector that takes a single argument and returns a `BOOL` value.
- [NSComparisonPredicate.Operator.contains](./operator/contains.md)
  A predicate to determine if the left hand side contains the right hand side.
- [NSComparisonPredicate.Operator.between](./operator/between.md)
  A predicate to determine if the left hand side lies at or between bounds specified by the right hand side.
### Initializers
- [init?(rawValue: UInt)](./operator/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Getting Information About a Comparison Predicate
- [var comparisonPredicateModifier: NSComparisonPredicate.Modifier](./comparisonpredicatemodifier.md)
  The comparison predicate modifier for the receiver.
- [NSComparisonPredicate.Modifier](./modifier.md)
  Constants that describe the possible types of modifier for a comparison predicate.
- [var customSelector: Selector?](./customselector.md)
  The selector for the receiver.
- [var rightExpression: NSExpression](./rightexpression.md)
  The right expression for the receiver.
- [var leftExpression: NSExpression](./leftexpression.md)
  The left expression for the receiver.
- [var options: NSComparisonPredicate.Options](./options-swift.property.md)
  The options to use for the receiver.
- [NSComparisonPredicate.Options](./options-swift.struct.md)
  Constants that describe the possible types of string comparison for comparison predicates.
- [var predicateOperatorType: NSComparisonPredicate.Operator](./predicateoperatortype.md)
  The predicate type for the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscomparisonpredicate/operator)*