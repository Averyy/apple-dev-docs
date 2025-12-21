# DockAccessory.MotionStates.Iterator

**Framework**: DockKit  
**Kind**: struct

An object that allows iteration over dock accessory motion states.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+

## Declaration

```swift
struct Iterator
```

## Topics

### Instance Methods
- [func next() async -> DockAccessory.MotionState?](dockaccessory/motionstates-swift.struct/iterator/next.md)
  Provide the next dock accessory motion state in the list.

## Relationships

### Conforms To
- [AsyncIteratorProtocol](../Swift/AsyncIteratorProtocol.md)

## See Also

- [func makeAsyncIterator() -> DockAccessory.MotionStates.Iterator](dockaccessory/motionstates-swift.struct/makeasynciterator.md)
  Creates and returns an iterator that traverses the list of dock accessory motion states.
- [DockAccessory.MotionStates.Element](dockaccessory/motionstates-swift.struct/element.md)
  A dock accessory motion state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dockkit/dockaccessory/motionstates-swift.struct/iterator)*