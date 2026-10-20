# DockAccessory.StateChanges

**Framework**: DockKit  
**Kind**: struct  
**Role**: Structure

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
- [DockAccessory.StateChanges.Iterator](./statechanges/iterator.md)
  An object that allows iteration over dock accessory state changes.
- [func makeAsyncIterator() -> DockAccessory.StateChanges.Iterator](./statechanges/makeasynciterator%28%29.md)
  Creates and returns an iterator that traverses the list of dock accessory state changes.
- [DockAccessory.StateChanges.Element](./statechanges/element.md)
  A dock accessory state change.

## Relationships

### Conforms To
- [AsyncSequence](../../Swift/asyncsequence.md)

## See Also

### Getting accessory information
- [var firmwareVersion: String?](./firmwareversion.md)
  The firmware version of the dock accessory.
- [var hardwareModel: String?](./hardwaremodel.md)
  The model of the dock accessory.
- [let identifier: DockAccessory.Identifier](./identifier-swift.property.md)
  The name and unique identifer of the dock accessory.
- [DockAccessory.Identifier](./identifier-swift.struct.md)
  Information that uniquely identifies the dock accessory.
- [DockAccessory.Category](./category.md)
  Types of supported dock accesories.
- [DockAccessory.State](./state.md)
  The state of a dock accessory.
- [DockAccessory.StateChange](./statechange.md)
  An event that indicates a change in the state of a dock accessory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dockkit/dockaccessory/statechanges)*