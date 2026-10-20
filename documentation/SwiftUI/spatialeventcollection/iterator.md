# SpatialEventCollection.Iterator

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

An iterator over all events in the collection.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 1.0+
- watchOS 11.0+

## Declaration

```swift
struct Iterator
```

## Topics

### Getting the next event
- [func next() -> SpatialEventCollection.Event?](./iterator/next%28%29.md)
  The next `Event` in the sequence, if one exists.

## Relationships

### Conforms To
- [IteratorProtocol](../../Swift/iteratorprotocol.md)

## See Also

### Iterating over events in the collection
- [func makeIterator() -> SpatialEventCollection.Iterator](./makeiterator%28%29.md)
  Makes an iterator over all events in the collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/spatialeventcollection/iterator)*