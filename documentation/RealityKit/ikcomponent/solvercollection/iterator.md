# IKComponent.SolverCollection.Iterator

**Framework**: RealityKit  
**Kind**: struct

A type that provides the collection’s iteration interface and encapsulates its iteration state.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
struct Iterator
```

#### Overview

By default, a collection conforms to the `Sequence` protocol by supplying `IndexingIterator` as its associated `Iterator` type.

## Topics

### Instance Methods
- [func next() -> IKComponent.SolverCollection.Element?](ikcomponent/solvercollection/iterator/next.md)
  Advances to the next element and returns it, or `nil` if no next element exists.
### Type Aliases
- [IKComponent.SolverCollection.Iterator.Element](ikcomponent/solvercollection/iterator/element.md)
  The type of element traversed by the iterator.

## Relationships

### Conforms To
- [IteratorProtocol](../Swift/IteratorProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/ikcomponent/solvercollection/iterator)*