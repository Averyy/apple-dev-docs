# init(leftExpressions:rightExpressionAttributeType:modifier:operators:options:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Initializes and returns a “pop-up-pop-up-view”–style row template.

**Availability**:
- macOS 10.5+

## Declaration

```swift
init(leftExpressions: [NSExpression], rightExpressionAttributeType attributeType: NSAttributeType, modifier: NSComparisonPredicate.Modifier, operators: [NSNumber], options: Int)
```

```objc
- (instancetype) initWithLeftExpressions:(NSArray<NSExpression *> *) leftExpressions rightExpressionAttributeType:(NSAttributeType) attributeType modifier:(NSComparisonPredicateModifier) modifier operators:(NSArray<NSNumber *> *) operators options:(NSUInteger) options;
```

## Return Value

A row template initialized using the specified arguments.

## Discussion

The type of `attributeType` dictates the type of view created. For example, [`NSAttributeType.dateAttributeType`](../../CoreData/nsattributetype/dateattributetype.md) creates an [`NSDatePicker`](../nsdatepicker.md) object, [`NSAttributeType.integer64AttributeType`](../../CoreData/nsattributetype/integer64attributetype.md) creates a short text field, and [`NSAttributeType.stringAttributeType`](../../CoreData/nsattributetype/stringattributetype.md) produces a longer text field. You can resize the views as you want.

Predicates do not automatically coerce types for you. For example, comparing a number to a string will raise an exception. Therefore, the attribute type is also needed to determine how the control’s object value must be coerced before putting it into a predicate.

## Parameters

- `leftExpressions`: An array of [`NSExpression`](../../Foundation/nsexpression.md) objects that represent the left side of a predicate.
- `attributeType`: An attribute type for the right side of a predicate. This value dictates the type of view created, and how the control’s object value is coerced before putting it into a predicate.
- `modifier`: A modifier for the predicate (see [`NSComparisonPredicate.Modifier`](../../Foundation/nscomparisonpredicate/modifier.md) for possible values).
- `operators`: An array of [`NSNumber`](../../Foundation/nsnumber.md) objects specifying the operator type (see [`NSComparisonPredicate.Operator`](../../Foundation/nscomparisonpredicate/operator.md) for possible values).
- `options`: Options for the predicate (see [`NSComparisonPredicate.Options`](../../Foundation/nscomparisonpredicate/options-swift.struct.md) for possible values).

## See Also

### Initializing a Template
- [init(leftExpressions: [NSExpression], rightExpressions: [NSExpression], modifier: NSComparisonPredicate.Modifier, operators: [NSNumber], options: Int)](./init%28leftexpressions,rightexpressions,modifier,operators,options%29.md)
  Initializes and returns a “pop-up-pop-up-pop-up”–style row template.
- [init(compoundTypes: [NSNumber])](./init%28compoundtypes%29.md)
  Initializes and returns a row template suitable for displaying compound predicates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspredicateeditorrowtemplate/init(leftexpressions:rightexpressionattributetype:modifier:operators:options:))*