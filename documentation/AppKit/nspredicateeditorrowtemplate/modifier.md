# modifier

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

Returns the comparison predicate modifier for the receiver.

**Availability**:
- macOS 10.5+

## Declaration

```swift
var modifier: NSComparisonPredicate.Modifier { get }
```

```objc
@property (readonly) NSComparisonPredicateModifier modifier;
```

#### Return Value

The comparison predicate modifier for the receiver.

## See Also

### Information About a Row Template
- [var leftExpressions: [NSExpression]?](./leftexpressions.md)
  Returns the left hand expressions for the receiver.
- [var rightExpressions: [NSExpression]?](./rightexpressions.md)
  Returns the right hand expressions for the receiver.
- [var compoundTypes: [NSNumber]?](./compoundtypes.md)
  Returns the compound predicate types.
- [var operators: [NSNumber]?](./operators.md)
  Returns the array of comparison predicate operators.
- [var options: Int](./options.md)
  Returns the comparison predicate options.
- [var rightExpressionAttributeType: NSAttributeType](./rightexpressionattributetype.md)
  Returns the attribute type of the receiver’s right expression.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspredicateeditorrowtemplate/modifier)*