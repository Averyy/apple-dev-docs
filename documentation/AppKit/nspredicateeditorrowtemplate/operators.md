# operators

**Framework**: AppKit  
**Kind**: property

Returns the array of comparison predicate operators.

**Availability**:
- macOS 10.5+

## Declaration

```swift
var operators: [NSNumber]? { get }
```

#### Return Value

The array of [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber) objects specifying the comparison predicate operators. See [`NSComparisonPredicate.Operator`](https://developer.apple.com/documentation/Foundation/NSComparisonPredicate/Operator) for possible values.

## See Also

- [var leftExpressions: [NSExpression]?](nspredicateeditorrowtemplate/leftexpressions.md)
  Returns the left hand expressions for the receiver.
- [var rightExpressions: [NSExpression]?](nspredicateeditorrowtemplate/rightexpressions.md)
  Returns the right hand expressions for the receiver.
- [var compoundTypes: [NSNumber]?](nspredicateeditorrowtemplate/compoundtypes.md)
  Returns the compound predicate types.
- [var modifier: NSComparisonPredicate.Modifier](nspredicateeditorrowtemplate/modifier.md)
  Returns the comparison predicate modifier for the receiver.
- [var options: Int](nspredicateeditorrowtemplate/options.md)
  Returns the comparison predicate options.
- [var rightExpressionAttributeType: NSAttributeType](nspredicateeditorrowtemplate/rightexpressionattributetype.md)
  Returns the attribute type of the receiver’s right expression.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspredicateeditorrowtemplate/operators)*