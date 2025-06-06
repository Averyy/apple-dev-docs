# DockAccessory.BatteryStates

**Framework**: DockKit  
**Kind**: struct

An asynchronous sequence of dock accessory battery states.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+

## Declaration

```swift
struct BatteryStates
```

## Topics

### Structures
- [DockAccessory.BatteryStates.Iterator](dockaccessory/batterystates-swift.struct/iterator.md)
  An object that allows iteration over dock accessory events.
### Instance Methods
- [func makeAsyncIterator() -> DockAccessory.BatteryStates.Iterator](dockaccessory/batterystates-swift.struct/makeasynciterator.md)
  Creates and returns an iterator that traverses the list of dock accessory events.
### Type Aliases
- [DockAccessory.BatteryStates.AsyncIterator](dockaccessory/batterystates-swift.struct/asynciterator.md)
  The type of asynchronous iterator that produces elements of this asynchronous sequence.
- [DockAccessory.BatteryStates.Element](dockaccessory/batterystates-swift.struct/element.md)
  A dock accessory event.
### Default Implementations
- [AsyncSequence Implementations](dockaccessory/batterystates-swift.struct/asyncsequence-implementations.md)

## Relationships

### Conforms To
- [AsyncSequence](../Swift/AsyncSequence.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/dockkit/dockaccessory/batterystates-swift.struct)*