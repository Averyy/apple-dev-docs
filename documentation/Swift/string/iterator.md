# String.Iterator

**Framework**: Swift  
**Kind**: struct

A type that provides the collection’s iteration interface and encapsulates its iteration state.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
@frozen
struct Iterator
```

#### Overview

By default, a collection conforms to the `Sequence` protocol by supplying `IndexingIterator` as its associated `Iterator` type.

## Topics

### Instance Methods
- [func next() -> Character?](string/iterator/next.md)
  Advances to the next element and returns it, or `nil` if no next element exists.
### Type Aliases
- [String.Iterator.Element](string/iterator/element.md)
  The type of element traversed by the iterator.

## Relationships

### Conforms To
- [IteratorProtocol](iteratorprotocol.md)
- [Sendable](sendable.md)
- [SendableMetatype](sendablemetatype.md)

## See Also

- [struct Substring](substring.md)
  A slice of a string.
- [protocol StringProtocol](stringprotocol.md)
  A type that can represent a string as a collection of characters.
- [String.Index](string/index.md)
  A position of a character or code unit in a string.
- [String.UnicodeScalarView](string/unicodescalarview.md)
  A view of a string’s contents as a collection of Unicode scalar values.
- [String.UTF16View](string/utf16view.md)
  A view of a string’s contents as a collection of UTF-16 code units.
- [String.UTF8View](string/utf8view.md)
  A view of a string’s contents as a collection of UTF-8 code units.
- [String.Encoding](string/encoding.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/string/iterator)*