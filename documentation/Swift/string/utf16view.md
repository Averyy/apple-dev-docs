# String.UTF16View

**Framework**: Swift  
**Kind**: struct

A view of a string’s contents as a collection of UTF-16 code units.

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
struct UTF16View
```

#### Overview

You can access a string’s view of UTF-16 code units by using its `utf16` property. A string’s UTF-16 view encodes the string’s Unicode scalar values as 16-bit integers.

```swift
let flowers = "Flowers 💐"
for v in flowers.utf16 {
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
// 55357
// 56464
```

Unicode scalar values that make up a string’s contents can be up to 21 bits long. The longer scalar values may need two `UInt16` values for storage. Those “pairs” of code units are called .

```swift
let flowermoji = "💐"
for v in flowermoji.unicodeScalars {
    print(v, v.value)
}
// 💐 128144

for v in flowermoji.utf16 {
    print(v)
}
// 55357
// 56464
```

To convert a `String.UTF16View` instance back into a string, use the `String` type’s `init(_:)` initializer.

```swift
let favemoji = "My favorite emoji is 🎉"
if let i = favemoji.utf16.firstIndex(where: { $0 >= 128 }) {
    let asciiPrefix = String(favemoji.utf16[..<i])!
    print(asciiPrefix)
}
// Prints "My favorite emoji is "
```

### Utf16view Elements Match Nsstring Characters

The UTF-16 code units of a string’s `utf16` view match the elements accessed through indexed `NSString` APIs.

```swift
print(flowers.utf16.count)
// Prints "10"

let nsflowers = flowers as NSString
print(nsflowers.length)
// Prints "10"
```

Unlike `NSString`, however, `String.UTF16View` does not use integer indices. If you need to access a specific position in a UTF-16 view, use Swift’s index manipulation methods. The following example accesses the fourth code unit in both the `flowers` and `nsflowers` strings:

```swift
print(nsflowers.character(at: 3))
// Prints "119"

let i = flowers.utf16.index(flowers.utf16.startIndex, offsetBy: 3)
print(flowers.utf16[i])
// Prints "119"
```

Although the Swift overlay updates many Objective-C methods to return native Swift indices and index ranges, some still return instances of `NSRange`. To convert an `NSRange` instance to a range of `String.Index`, use the `Range(_:in:)` initializer, which takes an `NSRange` and a string as arguments.

```swift
let snowy = "❄️ Let it snow! ☃️"
let nsrange = NSRange(location: 3, length: 12)
if let range = Range(nsrange, in: snowy) {
    print(snowy[range])
}
// Prints "Let it snow!"
```

## Topics

### Instance Properties
- [var customPlaygroundQuickLook: _PlaygroundQuickLook](string/utf16view/customplaygroundquicklook.md)
  A custom playground Quick Look for this instance.
### Default Implementations
- [BidirectionalCollection Implementations](string/utf16view/bidirectionalcollection-implementations.md)
- [Collection Implementations](string/utf16view/collection-implementations.md)
- [CustomDebugStringConvertible Implementations](string/utf16view/customdebugstringconvertible-implementations.md)
- [CustomReflectable Implementations](string/utf16view/customreflectable-implementations.md)
- [CustomStringConvertible Implementations](string/utf16view/customstringconvertible-implementations.md)
- [Sequence Implementations](string/utf16view/sequence-implementations.md)

## Relationships

### Conforms To
- [BidirectionalCollection](bidirectionalcollection.md)
- [Collection](collection.md)
- [Copyable](copyable.md)
- [CustomDebugStringConvertible](customdebugstringconvertible.md)
- [CustomReflectable](customreflectable.md)
- [CustomStringConvertible](customstringconvertible.md)
- [Sendable](sendable.md)
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
- [String.UTF8View](string/utf8view.md)
  A view of a string’s contents as a collection of UTF-8 code units.
- [String.Iterator](string/iterator.md)
  A type that provides the collection’s iteration interface and encapsulates its iteration state.
- [String.Encoding](string/encoding.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/string/utf16view)*