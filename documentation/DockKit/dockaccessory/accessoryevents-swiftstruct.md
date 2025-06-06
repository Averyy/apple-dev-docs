# DockAccessory.AccessoryEvents

**Framework**: DockKit  
**Kind**: struct

An asynchronous sequence of dock accessory events.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- macOS 14.4+

## Declaration

```swift
struct AccessoryEvents
```

## Topics

### Structures
- [DockAccessory.AccessoryEvents.Iterator](dockaccessory/accessoryevents-swift.struct/iterator.md)
  An object that allows iteration over dock accessory events.
### Instance Methods
- [func makeAsyncIterator() -> DockAccessory.AccessoryEvents.Iterator](dockaccessory/accessoryevents-swift.struct/makeasynciterator.md)
  Creates and returns an iterator that traverses the list of dock accessory events.
### Type Aliases
- [DockAccessory.AccessoryEvents.AsyncIterator](dockaccessory/accessoryevents-swift.struct/asynciterator.md)
  The type of asynchronous iterator that produces elements of this asynchronous sequence.
- [DockAccessory.AccessoryEvents.Element](dockaccessory/accessoryevents-swift.struct/element.md)
  A dock accessory event.
### Default Implementations
- [AsyncSequence Implementations](dockaccessory/accessoryevents-swift.struct/asyncsequence-implementations.md)

## Relationships

### Conforms To
- [AsyncSequence](../Swift/AsyncSequence.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/dockkit/dockaccessory/accessoryevents-swift.struct)*