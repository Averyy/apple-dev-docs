# NSComparisonPredicate.Operator

**Framework**: Foundation  
**Kind**: enum

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

## Topics

### Constants
- [NSComparisonPredicate.Operator.lessThan](nscomparisonpredicate/operator/lessthan.md)
  A less-than predicate.
- [NSComparisonPredicate.Operator.lessThanOrEqualTo](nscomparisonpredicate/operator/lessthanorequalto.md)
  A less-than-or-equal-to predicate.
- [NSComparisonPredicate.Operator.greaterThan](nscomparisonpredicate/operator/greaterthan.md)
  A greater-than predicate.
- [NSComparisonPredicate.Operator.greaterThanOrEqualTo](nscomparisonpredicate/operator/greaterthanorequalto.md)
  A greater-than-or-equal-to predicate.
- [NSComparisonPredicate.Operator.equalTo](nscomparisonpredicate/operator/equalto.md)
  An equal-to predicate.
- [NSComparisonPredicate.Operator.notEqualTo](nscomparisonpredicate/operator/notequalto.md)
  A not-equal-to predicate.
- [NSComparisonPredicate.Operator.matches](nscomparisonpredicate/operator/matches.md)
  A full regular expression matching predicate.
- [NSComparisonPredicate.Operator.like](nscomparisonpredicate/operator/like.md)
  A simple subset of the MATCHES predicate, similar in behavior to SQL `LIKE`.
- [NSComparisonPredicate.Operator.beginsWith](nscomparisonpredicate/operator/beginswith.md)
  A begins-with predicate.
- [NSComparisonPredicate.Operator.endsWith](nscomparisonpredicate/operator/endswith.md)
  An ends-with predicate.
- [NSComparisonPredicate.Operator.in](nscomparisonpredicate/operator/in.md)
  A predicate to determine if the left hand side is in the right hand side.
- [NSComparisonPredicate.Operator.customSelector](nscomparisonpredicate/operator/customselector.md)
  A predicate that uses a custom selector that takes a single argument and returns a `BOOL` value.
- [NSComparisonPredicate.Operator.contains](nscomparisonpredicate/operator/contains.md)
  A predicate to determine if the left hand side contains the right hand side.
- [NSComparisonPredicate.Operator.between](nscomparisonpredicate/operator/between.md)
  A predicate to determine if the left hand side lies at or between bounds specified by the right hand side.
- [NSComparisonPredicate.Operator.lessThan](nscomparisonpredicate/operator/lessthan.md)
  A less-than predicate.
- [NSComparisonPredicate.Operator.lessThanOrEqualTo](nscomparisonpredicate/operator/lessthanorequalto.md)
  A less-than-or-equal-to predicate.
- [NSComparisonPredicate.Operator.greaterThan](nscomparisonpredicate/operator/greaterthan.md)
  A greater-than predicate.
- [NSComparisonPredicate.Operator.greaterThanOrEqualTo](nscomparisonpredicate/operator/greaterthanorequalto.md)
  A greater-than-or-equal-to predicate.
- [NSComparisonPredicate.Operator.equalTo](nscomparisonpredicate/operator/equalto.md)
  An equal-to predicate.
- [NSComparisonPredicate.Operator.notEqualTo](nscomparisonpredicate/operator/notequalto.md)
  A not-equal-to predicate.
- [NSComparisonPredicate.Operator.matches](nscomparisonpredicate/operator/matches.md)
  A full regular expression matching predicate.
- [NSComparisonPredicate.Operator.like](nscomparisonpredicate/operator/like.md)
  A simple subset of the MATCHES predicate, similar in behavior to SQL `LIKE`.
- [NSComparisonPredicate.Operator.beginsWith](nscomparisonpredicate/operator/beginswith.md)
  A begins-with predicate.
- [NSComparisonPredicate.Operator.endsWith](nscomparisonpredicate/operator/endswith.md)
  An ends-with predicate.
- [NSComparisonPredicate.Operator.in](nscomparisonpredicate/operator/in.md)
  A predicate to determine if the left hand side is in the right hand side.
- [NSComparisonPredicate.Operator.customSelector](nscomparisonpredicate/operator/customselector.md)
  A predicate that uses a custom selector that takes a single argument and returns a `BOOL` value.
- [NSComparisonPredicate.Operator.contains](nscomparisonpredicate/operator/contains.md)
  A predicate to determine if the left hand side contains the right hand side.
- [NSComparisonPredicate.Operator.between](nscomparisonpredicate/operator/between.md)
  A predicate to determine if the left hand side lies at or between bounds specified by the right hand side.
### Initializers
- [init?(rawValue: UInt)](nscomparisonpredicate/operator/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var comparisonPredicateModifier: NSComparisonPredicate.Modifier](nscomparisonpredicate/comparisonpredicatemodifier.md)
  The comparison predicate modifier for the receiver.
- [NSComparisonPredicate.Modifier](nscomparisonpredicate/modifier.md)
  Constants that describe the possible types of modifier for a comparison predicate.
- [var customSelector: Selector?](nscomparisonpredicate/customselector.md)
  The selector for the receiver.
- [var rightExpression: NSExpression](nscomparisonpredicate/rightexpression.md)
  The right expression for the receiver.
- [var leftExpression: NSExpression](nscomparisonpredicate/leftexpression.md)
  The left expression for the receiver.
- [var options: NSComparisonPredicate.Options](nscomparisonpredicate/options-swift.property.md)
  The options to use for the receiver.
- [NSComparisonPredicate.Options](nscomparisonpredicate/options-swift.struct.md)
  Constants that describe the possible types of string comparison for comparison predicates.
- [var predicateOperatorType: NSComparisonPredicate.Operator](nscomparisonpredicate/predicateoperatortype.md)
  The predicate type for the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscomparisonpredicate/operator)*