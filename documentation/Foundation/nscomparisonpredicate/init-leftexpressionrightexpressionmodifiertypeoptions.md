# init(leftExpression:rightExpression:modifier:type:options:)

**Framework**: Foundation  
**Kind**: init

Creates a predicate to a specified type that you form by combining specified left and right expressions using a specified modifier and options.

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
init(leftExpression lhs: NSExpression, rightExpression rhs: NSExpression, modifier: NSComparisonPredicate.Modifier, type: NSComparisonPredicate.Operator, options: NSComparisonPredicate.Options = [])
```

#### Return Value

The receiver, initialized to a predicate of type `type` formed by combining the left and right expressions using the `modifier` and `options`.

## Parameters

- `lhs`: The left hand expression.
- `rhs`: The right hand expression.
- `modifier`: The modifier to apply.
- `type`: The predicate operator type.
- `options`: The options to apply (see  ). For no options, pass  .

## See Also

- [Displaying searchable content by using a search controller](../UIKit/displaying-searchable-content-by-using-a-search-controller.md)
  Create a user interface with searchable content in a table view.
- [init(leftExpression: NSExpression, rightExpression: NSExpression, customSelector: Selector)](nscomparisonpredicate/init(leftexpression:rightexpression:customselector:).md)
  Creates a predicate that you form by combining specified left and right expressions using a specified selector.
- [init?(coder: NSCoder)](nscomparisonpredicate/init(coder:).md)
  Creates a predicate by decoding from the coder you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscomparisonpredicate/init(leftexpression:rightexpression:modifier:type:options:))*