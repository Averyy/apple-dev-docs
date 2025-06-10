# PredicateExpressions.RangeExpressionContains

**Framework**: Foundation  
**Kind**: struct

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
struct RangeExpressionContains<RangeExpression, Element> where RangeExpression : PredicateExpression, Element : PredicateExpression, RangeExpression.Output : RangeExpression, Element.Output == RangeExpression.Output.Bound
```

## Topics

### Initializers
- [init(range: RangeExpression, element: Element)](predicateexpressions/rangeexpressioncontains/init(range:element:).md)
### Instance Properties
- [let element: Element](predicateexpressions/rangeexpressioncontains/element.md)
- [let range: RangeExpression](predicateexpressions/rangeexpressioncontains/range.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [PredicateExpression](predicateexpression.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [StandardPredicateExpression](standardpredicateexpression.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/predicateexpressions/rangeexpressioncontains)*