# compoundTypes

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

Returns the compound predicate types.

**Availability**:
- macOS 10.5+

## Declaration

```swift
var compoundTypes: [NSNumber]? { get }
```

```objc
@property (copy, readonly, nullable) NSArray<NSNumber *> * compoundTypes;
```

#### Return Value

An array of [`NSNumber`](../../Foundation/nsnumber.md) objects specifying compound predicate types. See [`NSCompoundPredicate.LogicalType`](../../Foundation/nscompoundpredicate/logicaltype.md) for possible values.

## See Also

### Information About a Row Template
- [var leftExpressions: [NSExpression]?](./leftexpressions.md)
  Returns the left hand expressions for the receiver.
- [var rightExpressions: [NSExpression]?](./rightexpressions.md)
  Returns the right hand expressions for the receiver.
- [var modifier: NSComparisonPredicate.Modifier](./modifier.md)
  Returns the comparison predicate modifier for the receiver.
- [var operators: [NSNumber]?](./operators.md)
  Returns the array of comparison predicate operators.
- [var options: Int](./options.md)
  Returns the comparison predicate options.
- [var rightExpressionAttributeType: NSAttributeType](./rightexpressionattributetype.md)
  Returns the attribute type of the receiver’s right expression.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspredicateeditorrowtemplate/compoundtypes)*