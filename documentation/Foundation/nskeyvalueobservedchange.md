# NSKeyValueObservedChange

**Framework**: Foundation  
**Kind**: struct

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
struct NSKeyValueObservedChange<Value>
```

## Topics

### Instance Properties
- [let indexes: IndexSet?](nskeyvalueobservedchange/indexes.md)
  indexes will be nil unless the observed KeyPath refers to an ordered to-many property
- [let isPrior: Bool](nskeyvalueobservedchange/isprior.md)
  ‘isPrior’ will be true if this change observation is being sent before the change happens, due to .prior being passed to `observe()`
- [let kind: NSKeyValueObservedChange<Value>.Kind](nskeyvalueobservedchange/kind-swift.property.md)
- [let newValue: Value?](nskeyvalueobservedchange/newvalue.md)
  newValue and oldValue will only be non-nil if .new/.old is passed to `observe()`. In general, get the most up to date value by accessing it directly on the observed object instead.
- [let oldValue: Value?](nskeyvalueobservedchange/oldvalue.md)
### Type Aliases
- [NSKeyValueObservedChange.Kind](nskeyvalueobservedchange/kind-swift.typealias.md)

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

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
- [struct NSKeyValueOperator](nskeyvalueoperator.md)
  These constants define the available array operators. See [`Using Collection Operators`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueCoding/CollectionOperators.html) for more information.
- [struct PresentationIntent](presentationintent.md)
  A type that defines presentation intent for blocks of characters like paragraphs, lists, block quotes, and tables.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nskeyvalueobservedchange)*