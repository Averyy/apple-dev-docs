# comparisonPredicateModifier

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The comparison predicate modifier for the receiver.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var comparisonPredicateModifier: NSComparisonPredicate.Modifier { get }
```

```objc
@property (readonly) NSComparisonPredicateModifier comparisonPredicateModifier;
```

#### Discussion

The default value is [`NSComparisonPredicate.Modifier.direct`](./modifier/direct.md).

## See Also

### Getting Information About a Comparison Predicate
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
- [NSComparisonPredicate.Operator](./operator.md)
  Defines the type of comparison for a comparison predicate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscomparisonpredicate/comparisonpredicatemodifier)*