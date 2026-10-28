# init(compoundTypes:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Initializes and returns a row template suitable for displaying compound predicates.

**Availability**:
- macOS 10.5+

## Declaration

```swift
init(compoundTypes: [NSNumber])
```

```objc
- (instancetype) initWithCompoundTypes:(NSArray<NSNumber *> *) compoundTypes;
```

## Return Value

A row template initialized for displaying compound predicates of the types specified by `compoundTypes`.

## Discussion

[`NSPredicateEditor`](../nspredicateeditor.md) contains such a template by default.

## Parameters

- `compoundTypes`: An array of [`NSNumber`](../../Foundation/nsnumber.md) objects specifying compound predicate types. See [`NSCompoundPredicate.LogicalType`](../../Foundation/nscompoundpredicate/logicaltype.md) for possible values.

## See Also

### Initializing a Template
- [init(leftExpressions: [NSExpression], rightExpressions: [NSExpression], modifier: NSComparisonPredicate.Modifier, operators: [NSNumber], options: Int)](./init%28leftexpressions,rightexpressions,modifier,operators,options%29.md)
  Initializes and returns a “pop-up-pop-up-pop-up”–style row template.
- [init(leftExpressions: [NSExpression], rightExpressionAttributeType: NSAttributeType, modifier: NSComparisonPredicate.Modifier, operators: [NSNumber], options: Int)](./init%28leftexpressions,rightexpressionattributetype,modifier,operators,options%29.md)
  Initializes and returns a “pop-up-pop-up-view”–style row template.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspredicateeditorrowtemplate/init(compoundtypes:))*