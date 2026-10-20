# URL.AsyncBytes.AsyncIterator

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

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
- [func next() async throws -> UInt8?](./asynciterator/next%28%29.md)
  Asynchronously advances to the next element and returns it, or ends the sequence if there is no next element.
### Supporting types
- [URL.AsyncBytes.Element](./element.md)
  The type of element produced by this asynchronous sequence.

## Relationships

### Conforms To
- [AsyncIteratorProtocol](../../../Swift/asynciteratorprotocol.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Creating an iterator
- [func makeAsyncIterator() -> URL.AsyncBytes.AsyncIterator](./makeasynciterator%28%29.md)
  Creates the asynchronous iterator that produces elements of this asynchronous sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/url/asyncbytes/asynciterator)*