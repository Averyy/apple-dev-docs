# PresentationIntent

**Framework**: Foundation  
**Kind**: struct

A type that defines presentation intent for blocks of characters like paragraphs, lists, block quotes, and tables.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
struct PresentationIntent
```

## Topics

### Structures
- [PresentationIntent.IntentType](presentationintent/intenttype.md)
- [PresentationIntent.TableColumn](presentationintent/tablecolumn.md)
### Initializers
- [init(PresentationIntent.Kind, identity: Int, parent: PresentationIntent?)](presentationintent/init(_:identity:parent:).md)
- [init(types: [PresentationIntent.IntentType])](presentationintent/init(types:).md)
### Instance Properties
- [var components: [PresentationIntent.IntentType]](presentationintent/components.md)
- [var count: Int](presentationintent/count.md)
- [var indentationLevel: Int](presentationintent/indentationlevel.md)
- [var isValid: Bool](presentationintent/isvalid.md)
### Enumerations
- [PresentationIntent.Kind](presentationintent/kind.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct AsyncCharacterSequence](asynccharactersequence.md)
  An asynchronous sequence of characters.
- [struct AsyncLineSequence](asynclinesequence.md)
  An asynchronous sequence of lines of text.
- [struct AsyncUnicodeScalarSequence](asyncunicodescalarsequence.md)
  An asychronous sequence of Unicode scalar values.
- [struct Expression](expression.md)
- [struct NSAttributedStringFormattingContextKey](nsattributedstringformattingcontextkey.md)
- [struct NSKeyValueChangeKey](nskeyvaluechangekey.md)
  The keys that can appear in the change dictionary.
- [struct NSKeyValueObservedChange](nskeyvalueobservedchange.md)
- [struct NSKeyValueOperator](nskeyvalueoperator.md)
  These constants define the available array operators. See [`Using Collection Operators`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueCoding/CollectionOperators.html) for more information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/presentationintent)*