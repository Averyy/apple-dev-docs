# DockAccessory.StateChanges.Iterator

**Framework**: DockKit  
**Kind**: struct

An object that allows iteration over dock accessory state changes.

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

### Iterating over state changes
- [func next() async -> DockAccessory.StateChange?](dockaccessory/statechanges/iterator/next.md)
  Provide the next dock accessory state change in the list.
### Type Aliases
- [DockAccessory.StateChanges.Iterator.Element](dockaccessory/statechanges/iterator/element.md)
### Default Implementations
- [AsyncIteratorProtocol Implementations](dockaccessory/statechanges/iterator/asynciteratorprotocol-implementations.md)

## Relationships

### Conforms To
- [AsyncIteratorProtocol](../Swift/AsyncIteratorProtocol.md)

## See Also

- [func makeAsyncIterator() -> DockAccessory.StateChanges.Iterator](dockaccessory/statechanges/makeasynciterator.md)
  Creates and returns an iterator that traverses the list of dock accessory state changes.
- [DockAccessory.StateChanges.Element](dockaccessory/statechanges/element.md)
  A dock accessory state change.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dockkit/dockaccessory/statechanges/iterator)*