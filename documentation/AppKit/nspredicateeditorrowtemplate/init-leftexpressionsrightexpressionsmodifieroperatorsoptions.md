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

- `leftExpressions`: An array of   objects that represent the left side of a predicate.
- `rightExpressions`: An array of   objects that represent the right side of a predicate.
- `modifier`: A modifier for the predicate (see   for possible values).
- `operators`: An array of   objects specifying the operator type (see   for possible values).
- `options`: Options for the predicate (see   for possible values).

## See Also

- [Predicate Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Predicates/AdditionalChapters/Introduction.html#//apple_ref/doc/uid/TP40001789)
- [Control and Cell Programming Topics](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ControlCell/ControlCell.html#//apple_ref/doc/uid/10000015i)
- [init(leftExpressions: [NSExpression], rightExpressionAttributeType: NSAttributeType, modifier: NSComparisonPredicate.Modifier, operators: [NSNumber], options: Int)](nspredicateeditorrowtemplate/init(leftexpressions:rightexpressionattributetype:modifier:operators:options:).md)
  Initializes and returns a “pop-up-pop-up-view”–style row template.
- [init(compoundTypes: [NSNumber])](nspredicateeditorrowtemplate/init(compoundtypes:).md)
  Initializes and returns a row template suitable for displaying compound predicates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspredicateeditorrowtemplate/init(leftexpressions:rightexpressions:modifier:operators:options:))*