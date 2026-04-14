# BESelectionTouchPhase

**Framework**: BrowserEngineKit  
**Kind**: enum

The different phases of touch interaction during text selection operations.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- macOS ?+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
enum BESelectionTouchPhase
```

#### Overview

The [`BETextInput`](betextinput.md) protocol provides your app an instance of this structure as an argument to the  [`adjustSelectionBoundary(to:touchPhase:baseIsStart:flags:)`](betextinput/adjustselectionboundary(to:touchphase:baseisstart:flags:).md) callback.

## Topics

### Identifying a selection touch phase
- [BESelectionTouchPhase.ended](beselectiontouchphase/ended.md)
  A phase that indicates when the touch interaction for text selection completes without specifying movement direction.
- [BESelectionTouchPhase.endedMovingBackward](beselectiontouchphase/endedmovingbackward.md)
  A phase that indicates when the touch interaction ends after moving in a backward direction.
- [BESelectionTouchPhase.endedMovingForward](beselectiontouchphase/endedmovingforward.md)
  A phase that indicates when the touch interaction ends after moving in a forward direction.
- [BESelectionTouchPhase.endedNotMoving](beselectiontouchphase/endednotmoving.md)
  A phase that indicates when the touch interaction ends without any movement of the selection boundaries.
- [BESelectionTouchPhase.moved](beselectiontouchphase/moved.md)
  A phase that indicates that a touch actively adjusts the text selection boundaries.
- [BESelectionTouchPhase.started](beselectiontouchphase/started.md)
  A phase that indicates when a new touch interaction for text selection begins.
### Creating a selection touch phase
- [init?(rawValue: Int)](beselectiontouchphase/init(rawvalue:).md)
  Creates a text selection phase with the specified underlying value.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [protocol BETextSelectionDirectionNavigation](betextselectiondirectionnavigation.md)
  A protocol that defines methods for cursor and selection adjustments.
- [struct BESelectionFlags](beselectionflags.md)
  Flags that indicate different states or characteristics of a text selection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/beselectiontouchphase)*