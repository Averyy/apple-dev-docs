# rightExpression

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The right expression for the receiver.

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
var rightExpression: NSExpression { get }
```

```objc
@property (retain, readonly) NSExpression * rightExpression;
```

#### Discussion

`nil` if there is none.

## See Also

### Getting Information About a Comparison Predicate
- [var comparisonPredicateModifier: NSComparisonPredicate.Modifier](./comparisonpredicatemodifier.md)
  The comparison predicate modifier for the receiver.
- [NSComparisonPredicate.Modifier](./modifier.md)
  Constants that describe the possible types of modifier for a comparison predicate.
- [var customSelector: Selector?](./customselector.md)
  The selector for the receiver.
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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscomparisonpredicate/rightexpression)*