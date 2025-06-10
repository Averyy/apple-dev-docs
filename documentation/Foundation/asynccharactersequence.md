# AsyncCharacterSequence

**Framework**: Foundation  
**Kind**: struct

An asynchronous sequence of characters.

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
struct AsyncCharacterSequence<Base> where Base : AsyncSequence, Base.Element == UInt8
```

## Relationships

### Conforms To
- [AsyncSequence](../Swift/AsyncSequence.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

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
- [struct PresentationIntent](presentationintent.md)
  A type that defines presentation intent for blocks of characters like paragraphs, lists, block quotes, and tables.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/asynccharactersequence)*