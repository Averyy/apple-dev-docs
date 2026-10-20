# characters

**Framework**: Swift  
**Kind**: property  
**Role**: Instance Property

A non-blocking sequence of `Characters` created by decoding the elements of `self` as UTF8.

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
var characters: AsyncCharacterSequence<Self> { get }
```

Available when `Element` is `UInt8`.

## See Also

### Adapting Textual Sequences
- [struct AsyncCharacterSequence](../../Foundation/asynccharactersequence.md)
  An asynchronous sequence of characters.
- [var unicodeScalars: AsyncUnicodeScalarSequence<Self>](./unicodescalars.md)
  A non-blocking sequence of `UnicodeScalars` created by decoding the elements of `self` as UTF8.
- [struct AsyncUnicodeScalarSequence](../../Foundation/asyncunicodescalarsequence.md)
  An asychronous sequence of Unicode scalar values.
- [var lines: AsyncLineSequence<Self>](./lines.md)
  A non-blocking sequence of newline-separated `Strings` created by decoding the elements of `self` as UTF8.
- [struct AsyncLineSequence](../../Foundation/asynclinesequence.md)
  An asynchronous sequence of lines of text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/asyncsequence/characters)*