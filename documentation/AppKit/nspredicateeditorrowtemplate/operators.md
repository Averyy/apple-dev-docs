# operators

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

Returns the array of comparison predicate operators.

**Availability**:
- macOS 10.5+

## Declaration

```swift
var operators: [NSNumber]? { get }
```

```objc
@property (copy, readonly, nullable) NSArray<NSNumber *> * operators;
```

#### Return Value

The array of [`NSNumber`](../../Foundation/nsnumber.md) objects specifying the comparison predicate operators. See [`NSComparisonPredicate.Operator`](../../Foundation/nscomparisonpredicate/operator.md) for possible values.

## See Also

### Information About a Row Template
- [var leftExpressions: [NSExpression]?](./leftexpressions.md)
  Returns the left hand expressions for the receiver.
- [var rightExpressions: [NSExpression]?](./rightexpressions.md)
  Returns the right hand expressions for the receiver.
- [var compoundTypes: [NSNumber]?](./compoundtypes.md)
  Returns the compound predicate types.
- [var modifier: NSComparisonPredicate.Modifier](./modifier.md)
  Returns the comparison predicate modifier for the receiver.
- [var options: Int](./options.md)
  Returns the comparison predicate options.
- [var rightExpressionAttributeType: NSAttributeType](./rightexpressionattributetype.md)
  Returns the attribute type of the receiver’s right expression.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspredicateeditorrowtemplate/operators)*