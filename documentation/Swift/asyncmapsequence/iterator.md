# AsyncMapSequence.Iterator

**Framework**: Swift  
**Kind**: struct  
**Role**: Structure

The iterator that produces elements of the map sequence.

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

Available when `Base` conforms to `AsyncSequence`.

## Topics

### Instance Methods
- [func next() async rethrows -> Transformed?](./iterator/next%28%29.md)
  Produces the next element in the map sequence.
- [func next(isolation: isolated (any Actor)?) async throws(AsyncMapSequence<Base, Transformed>.Failure) -> Transformed?](./iterator/next%28isolation%29.md)
  Produces the next element in the map sequence.
### Type Aliases
- [AsyncMapSequence.Iterator.Element](./iterator/element.md)
### Default Implementations
- [AsyncIteratorProtocol Implementations](./iterator/asynciteratorprotocol-implementations.md)

## Relationships

### Conforms To
- [AsyncIteratorProtocol](../asynciteratorprotocol.md)
- [Sendable](../sendable.md)
- [SendableMetatype](../sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/asyncmapsequence/iterator)*