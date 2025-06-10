# String.UnicodeScalarView

**Framework**: Swift  
**Kind**: struct

A view of a string’s contents as a collection of Unicode scalar values.

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
struct UnicodeScalarView
```

#### Overview

You can access a string’s view of Unicode scalar values by using its `unicodeScalars` property. Unicode scalar values are the 21-bit codes that are the basic unit of Unicode. Each scalar value is represented by a `Unicode.Scalar` instance and is equivalent to a UTF-32 code unit.

```swift
let flowers = "Flowers 💐"
for v in flowers.unicodeScalars {
    print(v.value)
}
// 70
// 108
// 111
// 119
// 101
// 114
// 115
// 32
// 128144
```

Some characters that are visible in a string are made up of more than one Unicode scalar value. In that case, a string’s `unicodeScalars` view contains more elements than the string itself.

```swift
let flag = "🇵🇷"
for c in flag {
    print(c)
}
// 🇵🇷

for v in flag.unicodeScalars {
    print(v.value)
}
// 127477
// 127479
```

You can convert a `String.UnicodeScalarView` instance back into a string using the `String` type’s `init(_:)` initializer.

```swift
let favemoji = "My favorite emoji is 🎉"
if let i = favemoji.unicodeScalars.firstIndex(where: { $0.value >= 128 }) {
    let asciiPrefix = String(favemoji.unicodeScalars[..<i])
    print(asciiPrefix)
}
// Prints "My favorite emoji is "
```

## Topics

### Instance Properties
- [var customPlaygroundQuickLook: _PlaygroundQuickLook](string/unicodescalarview/customplaygroundquicklook.md)
  A custom playground Quick Look for this instance.
### Default Implementations
- [BidirectionalCollection Implementations](string/unicodescalarview/bidirectionalcollection-implementations.md)
- [Collection Implementations](string/unicodescalarview/collection-implementations.md)
- [CustomDebugStringConvertible Implementations](string/unicodescalarview/customdebugstringconvertible-implementations.md)
- [CustomReflectable Implementations](string/unicodescalarview/customreflectable-implementations.md)
- [CustomStringConvertible Implementations](string/unicodescalarview/customstringconvertible-implementations.md)
- [RangeReplaceableCollection Implementations](string/unicodescalarview/rangereplaceablecollection-implementations.md)
- [Sequence Implementations](string/unicodescalarview/sequence-implementations.md)

## Relationships

### Conforms To
- [BidirectionalCollection](bidirectionalcollection.md)
- [Collection](collection.md)
- [Copyable](copyable.md)
- [CustomDebugStringConvertible](customdebugstringconvertible.md)
- [CustomReflectable](customreflectable.md)
- [CustomStringConvertible](customstringconvertible.md)
- [RangeReplaceableCollection](rangereplaceablecollection.md)
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
- [String.UTF16View](string/utf16view.md)
  A view of a string’s contents as a collection of UTF-16 code units.
- [String.UTF8View](string/utf8view.md)
  A view of a string’s contents as a collection of UTF-8 code units.
- [String.Iterator](string/iterator.md)
  A type that provides the collection’s iteration interface and encapsulates its iteration state.
- [String.Encoding](string/encoding.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/string/unicodescalarview)*