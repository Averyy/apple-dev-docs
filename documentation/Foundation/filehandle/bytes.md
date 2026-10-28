# bytes

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The file’s contents, as an asynchronous sequence of bytes.

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
var bytes: FileHandle.AsyncBytes { get }
```

## Discussion

Use the `for`-`await`-`in` syntax to iterate over the bytes in this sequence. For text files, you can also use its [`characters`](../../Swift/asyncsequence/characters.md), [`unicodeScalars`](../../Swift/asyncsequence/unicodescalars.md), or [`lines`](../../Swift/asyncsequence/lines.md) properties to retrieve the contents in a more convenient format. Since all of these properties conform to [`AsyncSequence`](../../Swift/asyncsequence.md), as does [`bytes`](./bytes.md) itself, you can use methods defined by [`AsyncSequence`](../../Swift/asyncsequence.md) to perform powerful inline processing. For example, you can skip the first `n` bytes of the file with `myFileHandle.bytes.prefix(n)`.

> 💡 **Tip**:  Rather than creating a [`FileHandle`](../filehandle.md) to read a file asynchronously, you can instead use a `file://` URL in combination with the [`resourceBytes`](../url/resourcebytes.md) property in [`URL`](../url.md).

## See Also

### Reading from a file handle asynchronously
- [FileHandle.AsyncBytes](./asyncbytes.md)
  An asynchronous sequence of bytes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filehandle/bytes)*