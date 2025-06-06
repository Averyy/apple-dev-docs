# compoundTypes

**Framework**: AppKit  
**Kind**: property

Returns the compound predicate types.

**Availability**:
- macOS 10.5+

## Declaration

```swift
var compoundTypes: [NSNumber]? { get }
```

#### Return Value

An array of [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber) objects specifying compound predicate types. See [`NSCompoundPredicate.LogicalType`](https://developer.apple.com/documentation/Foundation/NSCompoundPredicate/LogicalType) for possible values.

## See Also

- [var leftExpressions: [NSExpression]?](nspredicateeditorrowtemplate/leftexpressions.md)
  Returns the left hand expressions for the receiver.
- [var rightExpressions: [NSExpression]?](nspredicateeditorrowtemplate/rightexpressions.md)
  Returns the right hand expressions for the receiver.
- [var modifier: NSComparisonPredicate.Modifier](nspredicateeditorrowtemplate/modifier.md)
  Returns the comparison predicate modifier for the receiver.
- [var operators: [NSNumber]?](nspredicateeditorrowtemplate/operators.md)
  Returns the array of comparison predicate operators.
- [var options: Int](nspredicateeditorrowtemplate/options.md)
  Returns the comparison predicate options.
- [var rightExpressionAttributeType: NSAttributeType](nspredicateeditorrowtemplate/rightexpressionattributetype.md)
  Returns the attribute type of the receiver’s right expression.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspredicateeditorrowtemplate/compoundtypes)*