# String.Index

**Framework**: Swift  
**Kind**: struct

A position of a character or code unit in a string.

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
struct Index
```

## Topics

### Initializers
- [init?(String.Index, within: String.UTF16View)](string/index/init(_:within:)-2txd4.md)
  Creates an index in the given UTF-16 view that corresponds exactly to the specified string position.
- [init?(String.Index, within: String)](string/index/init(_:within:)-2u3iq.md)
  Creates an index in the given string that corresponds exactly to the specified position.
- [init?<S>(AttributedString.Index, within: S)](string/index/init(_:within:)-379kg.md)
- [init?<S>(String.Index, within: S)](string/index/init(_:within:)-3eir6.md)
  Creates an index in the given string that corresponds exactly to the specified position.
- [init?(String.Index, within: String.UTF8View)](string/index/init(_:within:)-5lb6l.md)
  Creates an index in the given UTF-8 view that corresponds exactly to the specified `UTF16View` position.
- [init?(String.Index, within: String.UnicodeScalarView)](string/index/init(_:within:)-7e1rw.md)
  Creates an index in the given Unicode scalars view that corresponds exactly to the specified `UTF16View` position.
- [init(encodedOffset: Int)](string/index/init(encodedoffset:).md)
  Creates a new index at the specified code unit offset.
- [init<S>(utf16Offset: Int, in: S)](string/index/init(utf16offset:in:).md)
  Creates a new index at the specified UTF-16 code unit offset
### Instance Properties
- [var encodedOffset: Int](string/index/encodedoffset.md)
  The offset into a string’s code units for this index.
### Instance Methods
- [func samePosition(in: String.UTF8View) -> String.UTF8View.Index?](string/index/sameposition(in:)-3mz95.md)
  Returns the position in the given UTF-8 view that corresponds exactly to this index.
- [func samePosition(in: String.UnicodeScalarView) -> String.UnicodeScalarIndex?](string/index/sameposition(in:)-4yeo1.md)
  Returns the position in the given view of Unicode scalars that corresponds exactly to this index.
- [func samePosition(in: String) -> String.Index?](string/index/sameposition(in:)-6oxfv.md)
  Returns the position in the given string that corresponds exactly to this index.
- [func samePosition(in: String.UTF16View) -> String.UTF16View.Index?](string/index/sameposition(in:)-86cct.md)
  Returns the position in the given UTF-16 view that corresponds exactly to this index.
- [func utf16Offset<S>(in: S) -> Int](string/index/utf16offset(in:).md)
  The UTF-16 code unit offset corresponding to this index.
### Default Implementations
- [Comparable Implementations](string/index/comparable-implementations.md)
- [CustomDebugStringConvertible Implementations](string/index/customdebugstringconvertible-implementations.md)
- [Equatable Implementations](string/index/equatable-implementations.md)
- [Hashable Implementations](string/index/hashable-implementations.md)

## Relationships

### Conforms To
- [BitwiseCopyable](bitwisecopyable.md)
- [Comparable](comparable.md)
- [Copyable](copyable.md)
- [CustomDebugStringConvertible](customdebugstringconvertible.md)
- [Equatable](equatable.md)
- [Hashable](hashable.md)
- [Sendable](sendable.md)
- [SendableMetatype](sendablemetatype.md)

## See Also

- [struct Substring](substring.md)
  A slice of a string.
- [protocol StringProtocol](stringprotocol.md)
  A type that can represent a string as a collection of characters.
- [String.UnicodeScalarView](string/unicodescalarview.md)
  A view of a string’s contents as a collection of Unicode scalar values.
- [String.UTF16View](string/utf16view.md)
  A view of a string’s contents as a collection of UTF-16 code units.
- [String.UTF8View](string/utf8view.md)
  A view of a string’s contents as a collection of UTF-8 code units.
- [String.Iterator](string/iterator.md)
  A type that provides the collection’s iteration interface and encapsulates its iteration state.
- [String.Encoding](string/encoding.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/string/index)*