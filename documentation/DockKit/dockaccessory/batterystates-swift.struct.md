# DockAccessory.BatteryStates

**Framework**: DockKit  
**Kind**: struct  
**Role**: Structure

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
- [DockAccessory.BatteryStates.Iterator](./batterystates-swift.struct/iterator.md)
  An object that allows iteration over dock accessory events.
### Instance Methods
- [func makeAsyncIterator() -> DockAccessory.BatteryStates.Iterator](./batterystates-swift.struct/makeasynciterator%28%29.md)
  Creates and returns an iterator that traverses the list of dock accessory events.
### Type Aliases
- [DockAccessory.BatteryStates.Element](./batterystates-swift.struct/element.md)
  A dock accessory event.

## Relationships

### Conforms To
- [AsyncSequence](../../Swift/asyncsequence.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/dockkit/dockaccessory/batterystates-swift.struct)*