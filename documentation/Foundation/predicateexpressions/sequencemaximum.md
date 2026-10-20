# PredicateExpressions.SequenceMaximum

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

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
struct SequenceMaximum<Elements> where Elements : PredicateExpression, Elements.Output : Sequence, Elements.Output.Element : Comparable
```

## Topics

### Initializers
- [init(elements: Elements)](./sequencemaximum/init%28elements%29.md)
### Instance Properties
- [let elements: Elements](./sequencemaximum/elements.md)

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Escapable](../../Swift/escapable.md)
- [PredicateExpression](../predicateexpression.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [StandardPredicateExpression](../standardpredicateexpression.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/predicateexpressions/sequencemaximum)*