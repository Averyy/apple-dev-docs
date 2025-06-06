# URL.AsyncBytes

**Framework**: Foundation  
**Kind**: struct

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

### Adapting Textual Sequences
- [var lines: AsyncLineSequence<URL.AsyncBytes>](url/lines.md)
  The URL’s resource data, as an asynchronous sequence of lines of text.

## Relationships

### Conforms To
- [AsyncSequence](../Swift/AsyncSequence.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var resourceBytes: URL.AsyncBytes](url/resourcebytes.md)
  The URL’s resource data, as an asynchronous sequence of bytes.
- [var lines: AsyncLineSequence<URL.AsyncBytes>](url/lines.md)
  The URL’s resource data, as an asynchronous sequence of lines of text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/url/asyncbytes)*