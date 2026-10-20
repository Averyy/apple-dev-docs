# NSComparisonPredicate.Modifier

**Framework**: Foundation  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum NSComparisonPredicateModifier : NSUInteger;
```

## Topics

### Constants
- [NSComparisonPredicate.Modifier.direct](./modifier/direct.md)
  A predicate to compare directly the left and right hand sides.
- [NSComparisonPredicate.Modifier.all](./modifier/all.md)
  A predicate to compare all entries in the destination of a to-many relationship.
- [NSComparisonPredicate.Modifier.any](./modifier/any.md)
  A predicate to match with any entry in the destination of a to-many relationship.
### Initializers
- [init?(rawValue: UInt)](./modifier/init%28rawvalue%29.md)

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
- [NSComparisonPredicate.Operator](./operator.md)
  Defines the type of comparison for a comparison predicate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscomparisonpredicate/modifier)*