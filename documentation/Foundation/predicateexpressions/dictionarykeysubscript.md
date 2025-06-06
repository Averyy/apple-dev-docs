# PredicateExpressions.DictionaryKeySubscript

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
struct DictionaryKeySubscript<Wrapped, Key, Value> where Wrapped : PredicateExpression, Key : PredicateExpression, Wrapped.Output == [Key.Output : Value], Key.Output : Hashable
```

## Topics

### Initializers
- [init(wrapped: Wrapped, key: Key)](predicateexpressions/dictionarykeysubscript/init(wrapped:key:).md)
### Instance Properties
- [let key: Key](predicateexpressions/dictionarykeysubscript/key.md)
- [let wrapped: Wrapped](predicateexpressions/dictionarykeysubscript/wrapped.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [PredicateExpression](predicateexpression.md)
- [Sendable](../Swift/Sendable.md)
- [StandardPredicateExpression](standardpredicateexpression.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/predicateexpressions/dictionarykeysubscript)*