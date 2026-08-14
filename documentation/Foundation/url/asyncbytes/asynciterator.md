# URL.AsyncBytes.AsyncIterator

**Framework**: Foundation  
**Kind**: struct

The iterator type that produces elements of this asynchronous sequence.

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
@frozen
struct AsyncIterator
```

## Topics

### Producing iterator values
- [func next() async throws -> UInt8?](url/asyncbytes/asynciterator/next.md)
  Asynchronously advances to the next element and returns it, or ends the sequence if there is no next element.
### Supporting types
- [URL.AsyncBytes.Element](url/asyncbytes/element.md)
  The type of element produced by this asynchronous sequence.

## Relationships

### Conforms To
- [AsyncIteratorProtocol](../swift/asynciteratorprotocol.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [func makeAsyncIterator() -> URL.AsyncBytes.AsyncIterator](url/asyncbytes/makeasynciterator.md)
  Creates the asynchronous iterator that produces elements of this asynchronous sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/url/asyncbytes/asynciterator)*