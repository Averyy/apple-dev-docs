# AnimationLibraryComponent.AnimationCollection.Iterator

**Framework**: RealityKit  
**Kind**: struct

An object to iterate over all animations in the collection.

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

## Topics

### Instance Methods
- [func next() -> AnimationLibraryComponent.AnimationCollection.Element?](animationlibrarycomponent/animationcollection/iterator/next.md)
  Advances to the next element and returns it, or `nil` if no next element exists.
### Type Aliases
- [AnimationLibraryComponent.AnimationCollection.Iterator.Element](animationlibrarycomponent/animationcollection/iterator/element.md)
  The type of element traversed by the iterator.

## Relationships

### Conforms To
- [IteratorProtocol](../Swift/IteratorProtocol.md)

## See Also

- [func makeIterator() -> AnimationLibraryComponent.AnimationCollection.Iterator](animationlibrarycomponent/animationcollection/makeiterator.md)
  Returns an iterator over the animations in the collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/animationlibrarycomponent/animationcollection/iterator)*