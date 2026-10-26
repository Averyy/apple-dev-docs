# init(coder:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Creates a predicate by decoding from the coder you specify.

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
init?(coder: NSCoder)
```

```objc
- (instancetype) initWithCoder:(NSCoder *) coder;
```

## Parameters

- `coder`: The coder to read data from.

## See Also

### Creating Comparison Predicates
- [Displaying searchable content by using a search controller](../../UIKit/displaying-searchable-content-by-using-a-search-controller.md)
  Create a user interface with searchable content in a table view.
- [init(leftExpression: NSExpression, rightExpression: NSExpression, customSelector: Selector)](./init%28leftexpression,rightexpression,customselector%29.md)
  Creates a predicate that you form by combining specified left and right expressions using a specified selector.
- [init(leftExpression: NSExpression, rightExpression: NSExpression, modifier: NSComparisonPredicate.Modifier, type: NSComparisonPredicate.Operator, options: NSComparisonPredicate.Options)](./init%28leftexpression,rightexpression,modifier,type,options%29.md)
  Creates a predicate to a specified type that you form by combining specified left and right expressions using a specified modifier and options.
- [+ predicateWithLeftExpression:rightExpression:customSelector:](./predicatewithleftexpression_rightexpression_customselector_.md)
  Returns a new predicate formed by combining the left and right expressions using a given selector.
- [+ predicateWithLeftExpression:rightExpression:modifier:type:options:](./predicatewithleftexpression_rightexpression_modifier_type_options_.md)
  Creates and returns a predicate of a given type formed by combining given left and right expressions using a given modifier and options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscomparisonpredicate/init(coder:))*