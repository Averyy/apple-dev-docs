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
- [Copyable](../swift/copyable.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Decodable](../swift/decodable.md)
- [Encodable](../swift/encodable.md)
- [Escapable](../swift/escapable.md)
- [PredicateExpression](predicateexpression.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [StandardPredicateExpression](standardpredicateexpression.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/predicateexpressions/dictionarykeysubscript)*