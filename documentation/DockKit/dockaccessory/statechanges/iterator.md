# DockAccessory.StateChanges.Iterator

**Framework**: DockKit  
**Kind**: struct  
**Role**: Structure

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
- [func next() async -> DockAccessory.StateChange?](./iterator/next%28%29.md)
  Provide the next dock accessory state change in the list.

## Relationships

### Conforms To
- [AsyncIteratorProtocol](../../../Swift/asynciteratorprotocol.md)

## See Also

### Iterating over state changes
- [func makeAsyncIterator() -> DockAccessory.StateChanges.Iterator](./makeasynciterator%28%29.md)
  Creates and returns an iterator that traverses the list of dock accessory state changes.
- [DockAccessory.StateChanges.Element](./element.md)
  A dock accessory state change.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dockkit/dockaccessory/statechanges/iterator)*