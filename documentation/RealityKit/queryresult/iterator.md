# QueryResult.Iterator

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

The type of iterator used for entity query results.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+
- visionOS

## Declaration

```swift
struct Iterator
```

## Topics

### Advancing the iterator
- [func next() -> Element?](./iterator/next%28%29.md)
  Advances to the next entity and returns it.

## Relationships

### Conforms To
- [IteratorProtocol](../../Swift/iteratorprotocol.md)

## See Also

### Creating an iterator
- [func makeIterator() -> QueryResult<Element>.Iterator](./makeiterator%28%29.md)
  Returns an iterator for the contained entities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/queryresult/iterator)*