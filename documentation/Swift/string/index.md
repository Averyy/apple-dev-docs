# String.Index

**Framework**: Swift  
**Kind**: struct  
**Role**: Structure

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
- [init?(String.Index, within: String.UTF16View)](./index/init%28_,within%29-2txd4.md)
  Creates an index in the given UTF-16 view that corresponds exactly to the specified string position.
- [init?(String.Index, within: String)](./index/init%28_,within%29-2u3iq.md)
  Creates an index in the given string that corresponds exactly to the specified position.
- [init?<S>(AttributedString.Index, within: S)](./index/init%28_,within%29-379kg.md)
- [init?<S>(String.Index, within: S)](./index/init%28_,within%29-3eir6.md)
  Creates an index in the given string that corresponds exactly to the specified position.
- [init?(String.Index, within: String.UTF8View)](./index/init%28_,within%29-5lb6l.md)
  Creates an index in the given UTF-8 view that corresponds exactly to the specified `UTF16View` position.
- [init?(String.Index, within: String.UnicodeScalarView)](./index/init%28_,within%29-7e1rw.md)
  Creates an index in the given Unicode scalars view that corresponds exactly to the specified `UTF16View` position.
- [init(encodedOffset: Int)](./index/init%28encodedoffset%29.md)
  Creates a new index at the specified code unit offset.
- [init<S>(utf16Offset: Int, in: S)](./index/init%28utf16offset,in%29.md)
  Creates a new index at the specified UTF-16 code unit offset
### Instance Properties
- [var encodedOffset: Int](./index/encodedoffset.md)
  The offset into a string’s code units for this index.
### Instance Methods
- [func samePosition(in: String.UTF8View) -> String.UTF8View.Index?](./index/sameposition%28in%29-3mz95.md)
  Returns the position in the given UTF-8 view that corresponds exactly to this index.
- [func samePosition(in: String.UnicodeScalarView) -> String.UnicodeScalarIndex?](./index/sameposition%28in%29-4yeo1.md)
  Returns the position in the given view of Unicode scalars that corresponds exactly to this index.
- [func samePosition(in: String) -> String.Index?](./index/sameposition%28in%29-6oxfv.md)
  Returns the position in the given string that corresponds exactly to this index.
- [func samePosition(in: String.UTF16View) -> String.UTF16View.Index?](./index/sameposition%28in%29-86cct.md)
  Returns the position in the given UTF-16 view that corresponds exactly to this index.
- [func utf16Offset<S>(in: S) -> Int](./index/utf16offset%28in%29.md)
  The UTF-16 code unit offset corresponding to this index.
### Default Implementations
- [Comparable Implementations](./index/comparable-implementations.md)
- [CustomDebugStringConvertible Implementations](./index/customdebugstringconvertible-implementations.md)
- [Equatable Implementations](./index/equatable-implementations.md)
- [Hashable Implementations](./index/hashable-implementations.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../bitwisecopyable.md)
- [Comparable](../comparable.md)
- [Copyable](../copyable.md)
- [CustomDebugStringConvertible](../customdebugstringconvertible.md)
- [Equatable](../equatable.md)
- [Escapable](../escapable.md)
- [Hashable](../hashable.md)
- [Sendable](../sendable.md)
- [SendableMetatype](../sendablemetatype.md)

## See Also

### Related String Types
- [struct Substring](../substring.md)
  A slice of a string.
- [protocol StringProtocol](../stringprotocol.md)
  A type that can represent a string as a collection of characters.
- [String.UnicodeScalarView](./unicodescalarview.md)
  A view of a string’s contents as a collection of Unicode scalar values.
- [String.UTF16View](./utf16view.md)
  A view of a string’s contents as a collection of UTF-16 code units.
- [String.UTF8View](./utf8view.md)
  A view of a string’s contents as a collection of UTF-8 code units.
- [String.Iterator](./iterator.md)
  A type that provides the collection’s iteration interface and encapsulates its iteration state.
- [String.Encoding](./encoding.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/string/index)*