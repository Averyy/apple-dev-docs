# Expression

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 1.0+
- watchOS 11.0+

## Declaration

```swift
struct Expression<each Input, Output>
```

## Topics

### Initializers
- [init((repeat PredicateExpressions.Variable<each Input>) -> any StandardPredicateExpression<Output>)](./expression/init%28_%29.md)
### Instance Properties
- [let expression: any StandardPredicateExpression<Output>](./expression/expression.md)
- [let variable: (repeat PredicateExpressions.Variable<each Input>)](./expression/variable.md)
### Instance Methods
- [func evaluate(repeat each Input) throws -> Output](./expression/evaluate%28_%29.md)

## Relationships

### Conforms To
- [Copyable](../Swift/copyable.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Decodable](../Swift/decodable.md)
- [DecodableWithConfiguration](./decodablewithconfiguration.md)
- [Encodable](../Swift/encodable.md)
- [EncodableWithConfiguration](./encodablewithconfiguration.md)
- [Escapable](../Swift/escapable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Structures
- [struct AsyncCharacterSequence](./asynccharactersequence.md)
  An asynchronous sequence of characters.
- [struct AsyncLineSequence](./asynclinesequence.md)
  An asynchronous sequence of lines of text.
- [struct AsyncUnicodeScalarSequence](./asyncunicodescalarsequence.md)
  An asychronous sequence of Unicode scalar values.
- [struct NSAttributedStringFormattingContextKey](./nsattributedstringformattingcontextkey.md)
  A type that represents a key in the formatting context dictionary.
- [struct NSKeyValueChangeKey](./nskeyvaluechangekey.md)
  The keys that can appear in the change dictionary.
- [struct NSKeyValueObservedChange](./nskeyvalueobservedchange.md)
- [struct NSKeyValueOperator](./nskeyvalueoperator.md)
  These constants define the available array operators. See [Using Collection Operators](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueCoding/CollectionOperators.html) for more information.
- [struct PresentationIntent](./presentationintent.md)
  A type that defines presentation intent for blocks of characters like paragraphs, lists, block quotes, and tables.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/expression)*