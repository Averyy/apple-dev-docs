# init(_:)

**Framework**: Swift  
**Kind**: init  
**Role**: Initializer

Creates a String having the given content.

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
init?(_ codeUnits: Substring.UTF8View)
```

## Discussion

If `codeUnits` is an ill-formed code unit sequence, the result is `nil`.

> **Complexity**: O(N), where N is the length of the resulting `String`’s UTF-8 representation.

## See Also

### Working with String Views
- [var unicodeScalars: String.UnicodeScalarView](./unicodescalars.md)
  The string’s value represented as a collection of Unicode scalar values.
- [init(String.UnicodeScalarView)](./init%28_%29-2t931.md)
  Creates a string corresponding to the given collection of Unicode scalars.
- [init(Substring.UnicodeScalarView)](./init%28_%29-11jx3.md)
  Creates a String having the given content.
- [var utf16: String.UTF16View](./utf16.md)
  A UTF-16 encoding of `self`.
- [init(String.UTF16View)](./init%28_%29-wbcx.md)
  Creates a string corresponding to the given sequence of UTF-16 code units.
- [init?(Substring.UTF16View)](./init%28_%29-expd.md)
  Creates a String having the given content.
- [var utf8: String.UTF8View](./utf8.md)
  A UTF-8 encoding of `self`.
- [init(String.UTF8View)](./init%28_%29-6sprj.md)
  Creates a string corresponding to the given sequence of UTF-8 code units.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/string/init(_:)-83bub)*