# init(leftExpressions:rightExpressionAttributeType:modifier:operators:options:)

**Framework**: AppKit  
**Kind**: init

Initializes and returns a “pop-up-pop-up-view”–style row template.

**Availability**:
- macOS 10.5+

## Declaration

```swift
init(leftExpressions: [NSExpression], rightExpressionAttributeType attributeType: NSAttributeType, modifier: NSComparisonPredicate.Modifier, operators: [NSNumber], options: Int)
```

#### Return Value

A row template initialized using the specified arguments.

#### Discussion

The type of `attributeType` dictates the type of view created. For example, [`NSAttributeType.dateAttributeType`](https://developer.apple.com/documentation/CoreData/NSAttributeType/dateAttributeType) creates an [`NSDatePicker`](nsdatepicker.md) object, [`NSAttributeType.integer64AttributeType`](https://developer.apple.com/documentation/CoreData/NSAttributeType/integer64AttributeType) creates a short text field, and [`NSAttributeType.stringAttributeType`](https://developer.apple.com/documentation/CoreData/NSAttributeType/stringAttributeType) produces a longer text field. You can resize the views as you want.

Predicates do not automatically coerce types for you. For example, comparing a number to a string will raise an exception. Therefore, the attribute type is also needed to determine how the control’s object value must be coerced before putting it into a predicate.

## Parameters

- `leftExpressions`: An array of   objects that represent the left side of a predicate.
- `attributeType`: An attribute type for the right side of a predicate. This value dictates the type of view created, and how the control’s object value is coerced before putting it into a predicate.
- `modifier`: A modifier for the predicate (see   for possible values).
- `operators`: An array of   objects specifying the operator type (see   for possible values).
- `options`: Options for the predicate (see   for possible values).

## See Also

- [init(leftExpressions: [NSExpression], rightExpressions: [NSExpression], modifier: NSComparisonPredicate.Modifier, operators: [NSNumber], options: Int)](nspredicateeditorrowtemplate/init(leftexpressions:rightexpressions:modifier:operators:options:).md)
  Initializes and returns a “pop-up-pop-up-pop-up”–style row template.
- [init(compoundTypes: [NSNumber])](nspredicateeditorrowtemplate/init(compoundtypes:).md)
  Initializes and returns a row template suitable for displaying compound predicates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspredicateeditorrowtemplate/init(leftexpressions:rightexpressionattributetype:modifier:operators:options:))*