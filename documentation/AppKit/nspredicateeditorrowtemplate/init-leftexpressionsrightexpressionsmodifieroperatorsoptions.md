# init(leftExpressions:rightExpressions:modifier:operators:options:)

**Framework**: AppKit  
**Kind**: init

Initializes and returns a “pop-up-pop-up-pop-up”–style row template.

**Availability**:
- macOS 10.5+

## Declaration

```swift
init(leftExpressions: [NSExpression], rightExpressions: [NSExpression], modifier: NSComparisonPredicate.Modifier, operators: [NSNumber], options: Int)
```

#### Return Value

A row template of the “pop-up-pop-up-pop-up” form, with the left and right pop-ups representing the left and right expression arrays `leftExpressions` and `rightExpressions`, and the center pop-up representing the operators.

## Parameters

- `leftExpressions`: An array of [`NSExpression`](https://developer.apple.com/documentation/Foundation/NSExpression) objects that represent the left side of a predicate.
- `rightExpressions`: An array of [`NSExpression`](https://developer.apple.com/documentation/Foundation/NSExpression) objects that represent the right side of a predicate.
- `modifier`: A modifier for the predicate (see [`NSComparisonPredicate.Modifier`](https://developer.apple.com/documentation/Foundation/NSComparisonPredicate/Modifier) for possible values).
- `operators`: An array of [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber) objects specifying the operator type (see [`NSComparisonPredicate.Operator`](https://developer.apple.com/documentation/Foundation/NSComparisonPredicate/Operator) for possible values).
- `options`: Options for the predicate (see [`NSComparisonPredicate.Options`](https://developer.apple.com/documentation/Foundation/NSComparisonPredicate/Options-swift.struct) for possible values).

## See Also

- [Predicate Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Predicates/AdditionalChapters/Introduction.html#//apple_ref/doc/uid/TP40001789)
- [class NSPredicateEditorRowTemplate](nspredicateeditorrowtemplate.md)
  A template that describes available predicates and how to display them.
- [init(leftExpressions: [NSExpression], rightExpressionAttributeType: NSAttributeType, modifier: NSComparisonPredicate.Modifier, operators: [NSNumber], options: Int)](nspredicateeditorrowtemplate/init(leftexpressions:rightexpressionattributetype:modifier:operators:options:).md)
  Initializes and returns a “pop-up-pop-up-view”–style row template.
- [init(compoundTypes: [NSNumber])](nspredicateeditorrowtemplate/init(compoundtypes:).md)
  Initializes and returns a row template suitable for displaying compound predicates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspredicateeditorrowtemplate/init(leftexpressions:rightexpressions:modifier:operators:options:))*