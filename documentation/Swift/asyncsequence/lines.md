# lines

**Framework**: Swift  
**Kind**: property

A non-blocking sequence of newline-separated `Strings` created by decoding the elements of `self` as UTF8.

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
var lines: AsyncLineSequence<Self> { get }
```

## See Also

- [var characters: AsyncCharacterSequence<Self>](asyncsequence/characters.md)
  A non-blocking sequence of `Characters` created by decoding the elements of `self` as UTF8.
- [struct AsyncCharacterSequence](../foundation/asynccharactersequence.md)
  An asynchronous sequence of characters.
- [var unicodeScalars: AsyncUnicodeScalarSequence<Self>](asyncsequence/unicodescalars.md)
  A non-blocking sequence of `UnicodeScalars` created by decoding the elements of `self` as UTF8.
- [struct AsyncUnicodeScalarSequence](../foundation/asyncunicodescalarsequence.md)
  An asychronous sequence of Unicode scalar values.
- [struct AsyncLineSequence](../foundation/asynclinesequence.md)
  An asynchronous sequence of lines of text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/asyncsequence/lines)*