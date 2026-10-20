# PredicateExpressions.DictionaryKeyDefaultValueSubscript

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
struct DictionaryKeyDefaultValueSubscript<Wrapped, Key, Default> where Wrapped : PredicateExpression, Key : PredicateExpression, Default : PredicateExpression, Wrapped.Output == [Key.Output : Default.Output], Key.Output : Hashable
```

## Topics

### Initializers
- [init(wrapped: Wrapped, key: Key, default: Default)](./dictionarykeydefaultvaluesubscript/init%28wrapped,key,default%29.md)
### Instance Properties
- [let `default`: Default](./dictionarykeydefaultvaluesubscript/default.md)
- [let key: Key](./dictionarykeydefaultvaluesubscript/key.md)
- [let wrapped: Wrapped](./dictionarykeydefaultvaluesubscript/wrapped.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/predicateexpressions/dictionarykeydefaultvaluesubscript)*