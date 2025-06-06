# AsyncThrowingMapSequence.Iterator

**Framework**: Swift  
**Kind**: struct

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

## Topics

### Instance Methods
- [func next() async throws -> Transformed?](asyncthrowingmapsequence/iterator/next.md)
  Produces the next element in the map sequence.
- [func next(isolation: isolated (any Actor)?) async throws -> Transformed?](asyncthrowingmapsequence/iterator/next(isolation:).md)
  Produces the next element in the map sequence.
### Type Aliases
- [AsyncThrowingMapSequence.Iterator.Element](asyncthrowingmapsequence/iterator/element.md)
### Default Implementations
- [AsyncIteratorProtocol Implementations](asyncthrowingmapsequence/iterator/asynciteratorprotocol-implementations.md)

## Relationships

### Conforms To
- [AsyncIteratorProtocol](asynciteratorprotocol.md)
- [Sendable](sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/asyncthrowingmapsequence/iterator)*