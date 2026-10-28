# predicateWithLeftExpression:rightExpression:modifier:type:options:

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Creates and returns a predicate of a given type formed by combining given left and right expressions using a given modifier and options.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```objc
+ (NSComparisonPredicate *) predicateWithLeftExpression:(NSExpression *) lhs rightExpression:(NSExpression *) rhs modifier:(NSComparisonPredicateModifier) modifier type:(NSPredicateOperatorType) type options:(NSComparisonPredicateOptions) options;
```

## Return Value

A new predicate of type `type` formed by combining the given left and right expressions using the `modifier` and `options`.

## Parameters

- `lhs`: The left hand expression.
- `rhs`: The right hand expression.
- `modifier`: The modifier to apply.
- `type`: The predicate operator type.
- `options`: The options to apply (see [`NSComparisonPredicate.Options`](./options-swift.struct.md)). For no options, pass `0`.

## See Also

### Creating Comparison Predicates
- [Displaying searchable content by using a search controller](../../UIKit/displaying-searchable-content-by-using-a-search-controller.md)
  Create a user interface with searchable content in a table view.
- [+ predicateWithLeftExpression:rightExpression:customSelector:](./predicatewithleftexpression_rightexpression_customselector_.md)
  Returns a new predicate formed by combining the left and right expressions using a given selector.
- [init(leftExpression: NSExpression, rightExpression: NSExpression, customSelector: Selector)](./init%28leftexpression,rightexpression,customselector%29.md)
  Creates a predicate that you form by combining specified left and right expressions using a specified selector.
- [init(leftExpression: NSExpression, rightExpression: NSExpression, modifier: NSComparisonPredicate.Modifier, type: NSComparisonPredicate.Operator, options: NSComparisonPredicate.Options)](./init%28leftexpression,rightexpression,modifier,type,options%29.md)
  Creates a predicate to a specified type that you form by combining specified left and right expressions using a specified modifier and options.
- [init?(coder: NSCoder)](./init%28coder%29.md)
  Creates a predicate by decoding from the coder you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscomparisonpredicate/predicatewithleftexpression:rightexpression:modifier:type:options:)*