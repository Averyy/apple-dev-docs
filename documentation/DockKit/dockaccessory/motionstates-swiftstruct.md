# DockAccessory.MotionStates

**Framework**: DockKit  
**Kind**: struct

An asynchronous sequence of orientation and velocity updates from the device.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+

## Declaration

```swift
struct MotionStates
```

## Topics

### Iterating over motion states
- [DockAccessory.MotionStates.Iterator](dockaccessory/motionstates-swift.struct/iterator.md)
  An object that allows iteration over dock accessory motion states.
- [func makeAsyncIterator() -> DockAccessory.MotionStates.Iterator](dockaccessory/motionstates-swift.struct/makeasynciterator.md)
  Creates and returns an iterator that traverses the list of dock accessory motion states.
- [DockAccessory.MotionStates.Element](dockaccessory/motionstates-swift.struct/element.md)
  A dock accessory motion state.
### Type Aliases
- [DockAccessory.MotionStates.AsyncIterator](dockaccessory/motionstates-swift.struct/asynciterator.md)
  The type of asynchronous iterator that produces elements of this asynchronous sequence.
### Default Implementations
- [AsyncSequence Implementations](dockaccessory/motionstates-swift.struct/asyncsequence-implementations.md)

## Relationships

### Conforms To
- [AsyncSequence](../Swift/AsyncSequence.md)

## See Also

- [var motionStates: DockAccessory.MotionStates](dockaccessory/motionstates-swift.property.md)
  Motion information from the dock accessory that includes current orientation and velocity of all axes.
- [var limits: DockAccessory.Limits](dockaccessory/limits-swift.property.md)
  Current limits for the axes of rotation and maximum angular velocity.
- [DockAccessory.MotionState](dockaccessory/motionstate.md)
  An event that indicates the state of a dock accessory’s current position and speed.
- [DockAccessory.Limits](dockaccessory/limits-swift.struct.md)
  Soft limits on multiple axes of rotation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dockkit/dockaccessory/motionstates-swift.struct)*