# bytes

**Framework**: Foundation  
**Kind**: property

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

#### Discussion

Use the `for`-`await`-`in` syntax to iterate over the bytes in this sequence. For text files, you can also use its [`characters`](https://developer.apple.com/documentation/Swift/AsyncSequence/characters), [`unicodeScalars`](https://developer.apple.com/documentation/Swift/AsyncSequence/unicodeScalars), or [`lines`](https://developer.apple.com/documentation/Swift/AsyncSequence/lines) properties to retrieve the contents in a more convenient format. Since all of these properties conform to [`AsyncSequence`](https://developer.apple.com/documentation/Swift/AsyncSequence), as does [`bytes`](filehandle/bytes.md) itself, you can use methods defined by [`AsyncSequence`](https://developer.apple.com/documentation/Swift/AsyncSequence) to perform powerful inline processing. For example, you can skip the first `n` bytes of the file with `myFileHandle.bytes.prefix(n)`.

> 💡 **Tip**:  Rather than creating a [`FileHandle`](filehandle.md) to read a file asynchronously, you can instead use a `file://` URL in combination with the [`resourceBytes`](url/resourcebytes.md) property in [`URL`](url.md).

 Rather than creating a [`FileHandle`](filehandle.md) to read a file asynchronously, you can instead use a `file://` URL in combination with the [`resourceBytes`](url/resourcebytes.md) property in [`URL`](url.md).

## See Also

- [FileHandle.AsyncBytes](filehandle/asyncbytes.md)
  An asynchronous sequence of bytes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filehandle/bytes)*