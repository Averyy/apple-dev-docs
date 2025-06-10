# options

**Framework**: AppKit  
**Kind**: property

Returns the comparison predicate options.

**Availability**:
- macOS 10.5+

## Declaration

```swift
var options: Int { get }
```

#### Return Value

The comparison predicate options for the receiver. See [`NSComparisonPredicate.Options`](https://developer.apple.com/documentation/Foundation/NSComparisonPredicate/Options-swift.struct) for possible values. Returns `0` if this does not apply (for example, for a compound template initialized with [`init(compoundTypes:)`](nspredicateeditorrowtemplate/init(compoundtypes:).md)).

## See Also

- [var leftExpressions: [NSExpression]?](nspredicateeditorrowtemplate/leftexpressions.md)
  Returns the left hand expressions for the receiver.
- [var rightExpressions: [NSExpression]?](nspredicateeditorrowtemplate/rightexpressions.md)
  Returns the right hand expressions for the receiver.
- [var compoundTypes: [NSNumber]?](nspredicateeditorrowtemplate/compoundtypes.md)
  Returns the compound predicate types.
- [var modifier: NSComparisonPredicate.Modifier](nspredicateeditorrowtemplate/modifier.md)
  Returns the comparison predicate modifier for the receiver.
- [var operators: [NSNumber]?](nspredicateeditorrowtemplate/operators.md)
  Returns the array of comparison predicate operators.
- [var rightExpressionAttributeType: NSAttributeType](nspredicateeditorrowtemplate/rightexpressionattributetype.md)
  Returns the attribute type of the receiver’s right expression.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspredicateeditorrowtemplate/options)*