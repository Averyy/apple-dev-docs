# NSComparisonPredicate.Modifier

**Framework**: Foundation  
**Kind**: enum

Constants that describe the possible types of modifier for a comparison predicate.

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
enum Modifier
```

## Topics

### Constants
- [NSComparisonPredicate.Modifier.direct](nscomparisonpredicate/modifier/direct.md)
  A predicate to compare directly the left and right hand sides.
- [NSComparisonPredicate.Modifier.all](nscomparisonpredicate/modifier/all.md)
  A predicate to compare all entries in the destination of a to-many relationship.
- [NSComparisonPredicate.Modifier.any](nscomparisonpredicate/modifier/any.md)
  A predicate to match with any entry in the destination of a to-many relationship.
### Initializers
- [init?(rawValue: UInt)](nscomparisonpredicate/modifier/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var comparisonPredicateModifier: NSComparisonPredicate.Modifier](nscomparisonpredicate/comparisonpredicatemodifier.md)
  The comparison predicate modifier for the receiver.
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
- [NSComparisonPredicate.Operator](nscomparisonpredicate/operator.md)
  Defines the type of comparison for a comparison predicate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscomparisonpredicate/modifier)*