# PredicateExpressions.SequenceStartsWith

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
struct SequenceStartsWith<Base, Prefix> where Base : PredicateExpression, Prefix : PredicateExpression, Base.Output : Sequence, Prefix.Output : Sequence, Base.Output.Element : Equatable, Base.Output.Element == Prefix.Output.Element
```

## Topics

### Initializers
- [init(base: Base, prefix: Prefix)](./sequencestartswith/init%28base,prefix%29.md)
### Instance Properties
- [let base: Base](./sequencestartswith/base.md)
- [let prefix: Prefix](./sequencestartswith/prefix.md)

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Escapable](../../Swift/escapable.md)
- [PredicateExpression](../predicateexpression.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [StandardPredicateExpression](../standardpredicateexpression.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/predicateexpressions/sequencestartswith)*