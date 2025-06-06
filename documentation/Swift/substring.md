# Substring

**Framework**: Swift  
**Kind**: struct

A slice of a string.

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
struct Substring
```

#### Overview

When you create a slice of a string, a `Substring` instance is the result. Operating on substrings is fast and efficient because a substring shares its storage with the original string. The `Substring` type presents the same interface as `String`, so you can avoid or defer any copying of the string’s contents.

The following example creates a `greeting` string, and then finds the substring of the first sentence:

```swift
let greeting = "Hi there! It's nice to meet you! 👋"
let endOfSentence = greeting.firstIndex(of: "!")!
let firstSentence = greeting[...endOfSentence]
// firstSentence == "Hi there!"
```

You can perform many string operations on a substring. Here, we find the length of the first sentence and create an uppercase version.

```swift
print("'\(firstSentence)' is \(firstSentence.count) characters long.")
// Prints "'Hi there!' is 9 characters long."

let shoutingSentence = firstSentence.uppercased()
// shoutingSentence == "HI THERE!"
```

### Converting a Substring to a String

This example defines a `rawData` string with some unstructured data, and then uses the string’s `prefix(while:)` method to create a substring of the numeric prefix:

```swift
let rawInput = "126 a.b 22219 zzzzzz"
let numericPrefix = rawInput.prefix(while: { "0"..."9" ~= $0 })
// numericPrefix is the substring "126"
```

When you need to store a substring or pass it to a function that requires a `String` instance, you can convert it to a `String` by using the `String(_:)` initializer. Calling this initializer copies the contents of the substring to a new string.

```swift
func parseAndAddOne(_ s: String) -> Int {
    return Int(s, radix: 10)! + 1
}
_ = parseAndAddOne(numericPrefix)
// error: cannot convert value...
let incrementedPrefix = parseAndAddOne(String(numericPrefix))
// incrementedPrefix == 127
```

Alternatively, you can convert the function that takes a `String` to one that is generic over the `StringProtocol` protocol. The following code declares a generic version of the `parseAndAddOne(_:)` function:

```swift
func genericParseAndAddOne<S: StringProtocol>(_ s: S) -> Int {
    return Int(s, radix: 10)! + 1
}
let genericallyIncremented = genericParseAndAddOne(numericPrefix)
// genericallyIncremented == 127
```

You can call this generic function with an instance of either `String` or `Substring`.

> ❗ **Important**: Don’t store substrings longer than you need them to perform a specific operation. A substring holds a reference to the entire storage of the string it comes from, not just to the portion it presents, even when there is no other reference to the original string. Storing substrings may, therefore, prolong the lifetime of string data that is no longer otherwise accessible, which can appear to be memory leakage.

Don’t store substrings longer than you need them to perform a specific operation. A substring holds a reference to the entire storage of the string it comes from, not just to the portion it presents, even when there is no other reference to the original string. Storing substrings may, therefore, prolong the lifetime of string data that is no longer otherwise accessible, which can appear to be memory leakage.

## Topics

### Operators
- [static func ~= (Substring, String) -> Bool](substring/~=(_:_:).md)
### Initializers
- [init()](substring/init.md)
  Creates an empty substring.
- [init(Substring.UTF8View)](substring/init(_:)-4njms.md)
  Creates a Substring having the given content.
- [init(Substring.UTF16View)](substring/init(_:)-61zpv.md)
  Creates a Substring having the given content.
- [init(Substring.UnicodeScalarView)](substring/init(_:)-7k0au.md)
  Creates a Substring having the given content.
### Instance Properties
- [var base: String](substring/base.md)
  Returns the underlying string from which this substring was derived.
- [var characters: Substring](substring/characters.md)
  A view of the string’s contents as a collection of characters.
- [var customPlaygroundQuickLook: _PlaygroundQuickLook](substring/customplaygroundquicklook.md)
  A custom playground Quick Look for this instance.
- [var isContiguousUTF8: Bool](substring/iscontiguousutf8.md)
  Returns whether this string is capable of providing access to validly-encoded UTF-8 contents in contiguous memory in O(1) time.
### Instance Methods
- [func filter((Substring.Element) throws -> Bool) rethrows -> String](substring/filter(_:).md)
- [func makeContiguousUTF8()](substring/makecontiguousutf8.md)
  If this string is not contiguous, make it so. If this mutates the substring, it will invalidate any pre-existing indices.
- [func replaceSubrange(Range<Substring.Index>, with: Substring)](substring/replacesubrange(_:with:)-mfwu.md)
- [func withMutableCharacters<R>((inout Substring) -> R) -> R](substring/withmutablecharacters(_:).md)
  Applies the given closure to a mutable view of the string’s characters.
- [func withUTF8<R>((UnsafeBufferPointer<UInt8>) throws -> R) rethrows -> R](substring/withutf8(_:).md)
  Runs `body` over the content of this substring in contiguous memory. If this substring is not contiguous, this will first make it contiguous, which will also speed up subsequent access. If this mutates the substring, it will invalidate any pre-existing indices.
### Type Aliases
- [Substring.CharacterView](substring/characterview.md)
  A view of a string’s contents as a collection of characters.
- [Substring.Output](substring/output.md)
### Default Implementations
- [BidirectionalCollection Implementations](substring/bidirectionalcollection-implementations.md)
- [Collection Implementations](substring/collection-implementations.md)
- [Comparable Implementations](substring/comparable-implementations.md)
- [CustomDebugStringConvertible Implementations](substring/customdebugstringconvertible-implementations.md)
- [CustomReflectable Implementations](substring/customreflectable-implementations.md)
- [CustomStringConvertible Implementations](substring/customstringconvertible-implementations.md)
- [CustomTestStringConvertible Implementations](substring/customteststringconvertible-implementations.md)
- [Equatable Implementations](substring/equatable-implementations.md)
- [ExpressibleByExtendedGraphemeClusterLiteral Implementations](substring/expressiblebyextendedgraphemeclusterliteral-implementations.md)
- [ExpressibleByStringInterpolation Implementations](substring/expressiblebystringinterpolation-implementations.md)
- [ExpressibleByStringLiteral Implementations](substring/expressiblebystringliteral-implementations.md)
- [ExpressibleByUnicodeScalarLiteral Implementations](substring/expressiblebyunicodescalarliteral-implementations.md)
- [Hashable Implementations](substring/hashable-implementations.md)
- [LosslessStringConvertible Implementations](substring/losslessstringconvertible-implementations.md)
- [RangeReplaceableCollection Implementations](substring/rangereplaceablecollection-implementations.md)
- [RegexComponent Implementations](substring/regexcomponent-implementations.md)
- [Sequence Implementations](substring/sequence-implementations.md)
- [StringProtocol Implementations](substring/stringprotocol-implementations.md)
- [TextOutputStream Implementations](substring/textoutputstream-implementations.md)
- [TextOutputStreamable Implementations](substring/textoutputstreamable-implementations.md)

## Relationships

### Conforms To
- [BidirectionalCollection](bidirectionalcollection.md)
- [Collection](collection.md)
- [Comparable](comparable.md)
- [Copyable](copyable.md)
- [CustomDebugStringConvertible](customdebugstringconvertible.md)
- [CustomReflectable](customreflectable.md)
- [CustomStringConvertible](customstringconvertible.md)
- [CustomTestStringConvertible](../Testing/CustomTestStringConvertible.md)
- [Equatable](equatable.md)
- [ExpressibleByExtendedGraphemeClusterLiteral](expressiblebyextendedgraphemeclusterliteral.md)
- [ExpressibleByStringInterpolation](expressiblebystringinterpolation.md)
- [ExpressibleByStringLiteral](expressiblebystringliteral.md)
- [ExpressibleByUnicodeScalarLiteral](expressiblebyunicodescalarliteral.md)
- [Hashable](hashable.md)
- [LosslessStringConvertible](losslessstringconvertible.md)
- [RangeReplaceableCollection](rangereplaceablecollection.md)
- [RegexComponent](regexcomponent.md)
- [Sendable](sendable.md)
- [Sequence](sequence.md)
- [StringProtocol](stringprotocol.md)
- [TextOutputStream](textoutputstream.md)
- [TextOutputStreamable](textoutputstreamable.md)

## See Also

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
- [String.Iterator](string/iterator.md)
  A type that provides the collection’s iteration interface and encapsulates its iteration state.
- [String.Encoding](string/encoding.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/substring)*