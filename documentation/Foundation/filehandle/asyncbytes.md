# FileHandle.AsyncBytes

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

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

Use the `for`-`await`-`in` syntax to iterate over the bytes in this sequence. For text files, you can also use its [`characters`](../../Swift/asyncsequence/characters.md), [`unicodeScalars`](../../Swift/asyncsequence/unicodescalars.md), or [`lines`](../../Swift/asyncsequence/lines.md) properties to retrieve the contents in a more convenient format. Since all of these properties conform to [`AsyncSequence`](../../Swift/asyncsequence.md), as does the [`FileHandle`](../filehandle.md) property [`bytes`](./bytes.md), you can use methods defined by [`AsyncSequence`](../../Swift/asyncsequence.md) to perform powerful inline processing. For example, you can skip the first `n` bytes of the file with `myFileHandle.bytes.prefix(n)`.

## Topics

### Adapting Textual Sequences
- [struct AsyncCharacterSequence](../asynccharactersequence.md)
  An asynchronous sequence of characters.
- [struct AsyncUnicodeScalarSequence](../asyncunicodescalarsequence.md)
  An asychronous sequence of Unicode scalar values.
- [struct AsyncLineSequence](../asynclinesequence.md)
  An asynchronous sequence of lines of text.
### Creating an Iterator
- [func makeAsyncIterator() -> FileHandle.AsyncBytes.Iterator](./asyncbytes/makeasynciterator%28%29.md)
  Creates the asynchronous iterator that produces elements of this asynchronous sequence.
### Structures
- [FileHandle.AsyncBytes.Iterator](./asyncbytes/iterator.md)
  An iterator that produces the bytes of a file handle.

## Relationships

### Conforms To
- [AsyncSequence](../../Swift/asyncsequence.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Reading from a file handle asynchronously
- [var bytes: FileHandle.AsyncBytes](./bytes.md)
  The file’s contents, as an asynchronous sequence of bytes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filehandle/asyncbytes)*