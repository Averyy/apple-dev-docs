# options

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

Returns the comparison predicate options.

**Availability**:
- macOS 10.5+

## Declaration

```swift
var options: Int { get }
```

```objc
@property (readonly) NSUInteger options;
```

## Return Value

The comparison predicate options for the receiver. See [`NSComparisonPredicate.Options`](../../Foundation/nscomparisonpredicate/options-swift.struct.md) for possible values. Returns `0` if this does not apply (for example, for a compound template initialized with [`init(compoundTypes:)`](./init%28compoundtypes%29.md)).

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
- [var operators: [NSNumber]?](./operators.md)
  Returns the array of comparison predicate operators.
- [var rightExpressionAttributeType: NSAttributeType](./rightexpressionattributetype.md)
  Returns the attribute type of the receiver’s right expression.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspredicateeditorrowtemplate/options)*