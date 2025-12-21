# unicodeScalars

**Framework**: Swift  
**Kind**: property

A non-blocking sequence of `UnicodeScalars` created by decoding the elements of `self` as UTF8.

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
var unicodeScalars: AsyncUnicodeScalarSequence<Self> { get }
```

## See Also

- [var characters: AsyncCharacterSequence<Self>](asyncsequence/characters.md)
  A non-blocking sequence of `Characters` created by decoding the elements of `self` as UTF8.
- [struct AsyncCharacterSequence](../Foundation/AsyncCharacterSequence.md)
  An asynchronous sequence of characters.
- [struct AsyncUnicodeScalarSequence](../Foundation/AsyncUnicodeScalarSequence.md)
  An asychronous sequence of Unicode scalar values.
- [var lines: AsyncLineSequence<Self>](asyncsequence/lines.md)
  A non-blocking sequence of newline-separated `Strings` created by decoding the elements of `self` as UTF8.
- [struct AsyncLineSequence](../Foundation/AsyncLineSequence.md)
  An asynchronous sequence of lines of text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/asyncsequence/unicodescalars)*