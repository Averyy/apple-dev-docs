# init(leftExpressions:rightExpressions:modifier:operators:options:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Initializes and returns a “pop-up-pop-up-pop-up”–style row template.

**Availability**:
- macOS 10.5+

## Declaration

```swift
init(leftExpressions: [NSExpression], rightExpressions: [NSExpression], modifier: NSComparisonPredicate.Modifier, operators: [NSNumber], options: Int)
```

```objc
- (instancetype) initWithLeftExpressions:(NSArray<NSExpression *> *) leftExpressions rightExpressions:(NSArray<NSExpression *> *) rightExpressions modifier:(NSComparisonPredicateModifier) modifier operators:(NSArray<NSNumber *> *) operators options:(NSUInteger) options;
```

#### Return Value

A row template of the “pop-up-pop-up-pop-up” form, with the left and right pop-ups representing the left and right expression arrays `leftExpressions` and `rightExpressions`, and the center pop-up representing the operators.

## Parameters

- `leftExpressions`: An array of [`NSExpression`](../../Foundation/nsexpression.md) objects that represent the left side of a predicate.
- `rightExpressions`: An array of [`NSExpression`](../../Foundation/nsexpression.md) objects that represent the right side of a predicate.
- `modifier`: A modifier for the predicate (see [`NSComparisonPredicate.Modifier`](../../Foundation/nscomparisonpredicate/modifier.md) for possible values).
- `operators`: An array of [`NSNumber`](../../Foundation/nsnumber.md) objects specifying the operator type (see [`NSComparisonPredicate.Operator`](../../Foundation/nscomparisonpredicate/operator.md) for possible values).
- `options`: Options for the predicate (see [`NSComparisonPredicate.Options`](../../Foundation/nscomparisonpredicate/options-swift.struct.md) for possible values).

## See Also

### Related Documentation
- [class NSPredicateEditorRowTemplate](../nspredicateeditorrowtemplate.md)
  A template that describes available predicates and how to display them.
### Initializing a Template
- [init(leftExpressions: [NSExpression], rightExpressionAttributeType: NSAttributeType, modifier: NSComparisonPredicate.Modifier, operators: [NSNumber], options: Int)](./init%28leftexpressions,rightexpressionattributetype,modifier,operators,options%29.md)
  Initializes and returns a “pop-up-pop-up-view”–style row template.
- [init(compoundTypes: [NSNumber])](./init%28compoundtypes%29.md)
  Initializes and returns a row template suitable for displaying compound predicates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspredicateeditorrowtemplate/init(leftexpressions:rightexpressions:modifier:operators:options:))*