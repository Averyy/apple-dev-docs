# String.UTF8View

**Framework**: Swift  
**Kind**: struct

A view of a string’s contents as a collection of UTF-8 code units.

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
struct UTF8View
```

#### Overview

You can access a string’s view of UTF-8 code units by using its `utf8` property. A string’s UTF-8 view encodes the string’s Unicode scalar values as 8-bit integers.

```swift
let flowers = "Flowers 💐"
for v in flowers.utf8 {
    print(v)
}
// 70
// 108
// 111
// 119
// 101
// 114
// 115
// 32
// 240
// 159
// 146
// 144
```

A string’s Unicode scalar values can be up to 21 bits in length. To represent those scalar values using 8-bit integers, more than one UTF-8 code unit is often required.

```swift
let flowermoji = "💐"
for v in flowermoji.unicodeScalars {
    print(v, v.value)
}
// 💐 128144

for v in flowermoji.utf8 {
    print(v)
}
// 240
// 159
// 146
// 144
```

In the encoded representation of a Unicode scalar value, each UTF-8 code unit after the first is called a .

### Utf8view Elements Match Encoded C Strings

Swift streamlines interoperation with C string APIs by letting you pass a `String` instance to a function as an `Int8` or `UInt8` pointer. When you call a C function using a `String`, Swift automatically creates a buffer of UTF-8 code units and passes a pointer to that buffer. The code units of that buffer match the code units in the string’s `utf8` view.

The following example uses the C `strncmp` function to compare the beginning of two Swift strings. The `strncmp` function takes two `const char*` pointers and an integer specifying the number of characters to compare. Because the strings are identical up to the 14th character, comparing only those characters results in a return value of `0`.

```swift
let s1 = "They call me 'Bell'"
let s2 = "They call me 'Stacey'"

print(strncmp(s1, s2, 14))
// Prints "0"
print(String(s1.utf8.prefix(14))!)
// Prints "They call me '"
```

Extending the compared character count to 15 includes the differing characters, so a nonzero result is returned.

```swift
print(strncmp(s1, s2, 15))
// Prints "-17"
print(String(s1.utf8.prefix(15))!)
// Prints "They call me 'B"
```

## Topics

### Instance Properties
- [var customPlaygroundQuickLook: _PlaygroundQuickLook](string/utf8view/customplaygroundquicklook.md)
  A custom playground Quick Look for this instance.
- [var span: Span<UTF8.CodeUnit>](string/utf8view/span.md)
  A span over the UTF8 code units that make up this string.
### Default Implementations
- [BidirectionalCollection Implementations](string/utf8view/bidirectionalcollection-implementations.md)
- [Collection Implementations](string/utf8view/collection-implementations.md)
- [CustomDebugStringConvertible Implementations](string/utf8view/customdebugstringconvertible-implementations.md)
- [CustomReflectable Implementations](string/utf8view/customreflectable-implementations.md)
- [CustomStringConvertible Implementations](string/utf8view/customstringconvertible-implementations.md)
- [Sequence Implementations](string/utf8view/sequence-implementations.md)

## Relationships

### Conforms To
- [BidirectionalCollection](bidirectionalcollection.md)
- [Collection](collection.md)
- [Copyable](copyable.md)
- [CustomDebugStringConvertible](customdebugstringconvertible.md)
- [CustomReflectable](customreflectable.md)
- [CustomStringConvertible](customstringconvertible.md)
- [Sendable](sendable.md)
- [SendableMetatype](sendablemetatype.md)
- [Sequence](sequence.md)

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
- [String.Iterator](string/iterator.md)
  A type that provides the collection’s iteration interface and encapsulates its iteration state.
- [String.Encoding](string/encoding.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/string/utf8view)*