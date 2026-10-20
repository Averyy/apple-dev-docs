# AsyncFlatMapSequence.Iterator

**Framework**: Swift  
**Kind**: struct  
**Role**: Structure

The iterator that produces elements of the flat map sequence.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
struct Iterator
```

Available when `Base` conforms to `AsyncSequence` and `SegmentOfResult` conforms to `AsyncSequence`.

## Topics

### Instance Methods
- [func next() async rethrows -> SegmentOfResult.Element?](./iterator/next%28%29.md)
  Produces the next element in the flat map sequence.
- [func next(isolation: isolated (any Actor)?) async throws(AsyncFlatMapSequence<Base, SegmentOfResult>.Failure) -> SegmentOfResult.Element?](./iterator/next%28isolation%29.md)
  Produces the next element in the flat map sequence.
### Type Aliases
- [AsyncFlatMapSequence.Iterator.Element](./iterator/element.md)
### Default Implementations
- [AsyncIteratorProtocol Implementations](./iterator/asynciteratorprotocol-implementations.md)

## Relationships

### Conforms To
- [AsyncIteratorProtocol](../asynciteratorprotocol.md)
- [Sendable](../sendable.md)
- [SendableMetatype](../sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/asyncflatmapsequence/iterator)*