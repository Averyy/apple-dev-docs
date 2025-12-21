# DockAccessory.StateChanges

**Framework**: DockKit  
**Kind**: struct

An asynchronous sequence of dock accessory state changes.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+

## Declaration

```swift
struct StateChanges
```

## Topics

### Iterating over state changes
- [DockAccessory.StateChanges.Iterator](dockaccessory/statechanges/iterator.md)
  An object that allows iteration over dock accessory state changes.
- [func makeAsyncIterator() -> DockAccessory.StateChanges.Iterator](dockaccessory/statechanges/makeasynciterator.md)
  Creates and returns an iterator that traverses the list of dock accessory state changes.
- [DockAccessory.StateChanges.Element](dockaccessory/statechanges/element.md)
  A dock accessory state change.

## Relationships

### Conforms To
- [AsyncSequence](../Swift/AsyncSequence.md)

## See Also

- [var firmwareVersion: String?](dockaccessory/firmwareversion.md)
  The firmware version of the dock accessory.
- [var hardwareModel: String?](dockaccessory/hardwaremodel.md)
  The model of the dock accessory.
- [let identifier: DockAccessory.Identifier](dockaccessory/identifier-swift.property.md)
  The name and unique identifer of the dock accessory.
- [DockAccessory.Identifier](dockaccessory/identifier-swift.struct.md)
  Information that uniquely identifies the dock accessory.
- [DockAccessory.Category](dockaccessory/category.md)
  Types of supported dock accesories.
- [DockAccessory.State](dockaccessory/state.md)
  The state of a dock accessory.
- [DockAccessory.StateChange](dockaccessory/statechange.md)
  An event that indicates a change in the state of a dock accessory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dockkit/dockaccessory/statechanges)*