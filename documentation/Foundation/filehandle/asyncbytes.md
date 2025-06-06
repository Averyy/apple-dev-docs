# FileHandle.AsyncBytes

**Framework**: Foundation  
**Kind**: struct

An asynchronous sequence of bytes.

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
struct AsyncBytes
```

#### Overview

Use the `for`-`await`-`in` syntax to iterate over the bytes in this sequence. For text files, you can also use its [`characters`](https://developer.apple.com/documentation/Swift/AsyncSequence/characters), [`unicodeScalars`](https://developer.apple.com/documentation/Swift/AsyncSequence/unicodeScalars), or [`lines`](https://developer.apple.com/documentation/Swift/AsyncSequence/lines) properties to retrieve the contents in a more convenient format. Since all of these properties conform to [`AsyncSequence`](https://developer.apple.com/documentation/Swift/AsyncSequence), as does the [`FileHandle`](filehandle.md) property [`bytes`](filehandle/bytes.md), you can use methods defined by [`AsyncSequence`](https://developer.apple.com/documentation/Swift/AsyncSequence) to perform powerful inline processing. For example, you can skip the first `n` bytes of the file with `myFileHandle.bytes.prefix(n)`.

## Topics

### Adapting Textual Sequences
- [struct AsyncCharacterSequence](asynccharactersequence.md)
  An asynchronous sequence of characters.
- [struct AsyncUnicodeScalarSequence](asyncunicodescalarsequence.md)
  An asychronous sequence of Unicode scalar values.
- [struct AsyncLineSequence](asynclinesequence.md)
  An asynchronous sequence of lines of text.
### Structures
- [FileHandle.AsyncBytes.Iterator](filehandle/asyncbytes/iterator.md)

## Relationships

### Conforms To
- [AsyncSequence](../Swift/AsyncSequence.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var bytes: FileHandle.AsyncBytes](filehandle/bytes.md)
  The file’s contents, as an asynchronous sequence of bytes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filehandle/asyncbytes)*