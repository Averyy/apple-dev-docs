# QueryResult.Iterator

**Framework**: RealityKit  
**Kind**: struct

The type of iterator used for entity query results.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+ (Beta)
- visionOS ?+

## Declaration

```swift
struct Iterator
```

## Topics

### Advancing the iterator
- [func next() -> Element?](queryresult/iterator/next.md)
  Advances to the next entity and returns it.

## Relationships

### Conforms To
- [IteratorProtocol](../Swift/IteratorProtocol.md)

## See Also

- [func makeIterator() -> QueryResult<Element>.Iterator](queryresult/makeiterator.md)
  Returns an iterator for the contained entities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/queryresult/iterator)*