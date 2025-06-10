# PredicateExpressions.DictionaryKeyDefaultValueSubscript

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
struct DictionaryKeyDefaultValueSubscript<Wrapped, Key, Default> where Wrapped : PredicateExpression, Key : PredicateExpression, Default : PredicateExpression, Wrapped.Output == [Key.Output : Default.Output], Key.Output : Hashable
```

## Topics

### Initializers
- [init(wrapped: Wrapped, key: Key, default: Default)](predicateexpressions/dictionarykeydefaultvaluesubscript/init(wrapped:key:default:).md)
### Instance Properties
- [let `default`: Default](predicateexpressions/dictionarykeydefaultvaluesubscript/default.md)
- [let key: Key](predicateexpressions/dictionarykeydefaultvaluesubscript/key.md)
- [let wrapped: Wrapped](predicateexpressions/dictionarykeydefaultvaluesubscript/wrapped.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/predicateexpressions/dictionarykeydefaultvaluesubscript)*