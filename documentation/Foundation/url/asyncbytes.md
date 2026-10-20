# URL.AsyncBytes

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

An asynchronous sequence of bytes loaded from the URL.

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

## Topics

### Creating an iterator
- [func makeAsyncIterator() -> URL.AsyncBytes.AsyncIterator](./asyncbytes/makeasynciterator%28%29.md)
  Creates the asynchronous iterator that produces elements of this asynchronous sequence.
- [URL.AsyncBytes.AsyncIterator](./asyncbytes/asynciterator.md)
  The iterator type that produces elements of this asynchronous sequence.
### Adapting Textual Sequences
- [var lines: AsyncLineSequence<URL.AsyncBytes>](./lines.md)
  The URL’s resource data, as an asynchronous sequence of lines of text.
### Supporting Types
- [URL.AsyncBytes.Element](./asyncbytes/element.md)
  The type of element produced by this asynchronous sequence.

## Relationships

### Conforms To
- [AsyncSequence](../../Swift/asyncsequence.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Loading URL contents asynchronously
- [var resourceBytes: URL.AsyncBytes](./resourcebytes.md)
  The URL’s resource data, as an asynchronous sequence of bytes.
- [var lines: AsyncLineSequence<URL.AsyncBytes>](./lines.md)
  The URL’s resource data, as an asynchronous sequence of lines of text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/url/asyncbytes)*