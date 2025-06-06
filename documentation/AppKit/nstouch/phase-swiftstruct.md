# NSTouch.Phase

**Framework**: AppKit  
**Kind**: struct

The possible phases of a touch.

**Availability**:
- macOS 10.7+

## Declaration

```swift
struct Phase
```

#### Overview

These constants are used by [`phase`](nstouch/phase-swift.property.md).

## Topics

### Creating a Touch Phase
- [init(rawValue: UInt)](nstouch/phase-swift.struct/init(rawvalue:).md)
  Creates a new touch phase from the given raw value.
### Constants
- [static var began: NSTouch.Phase](nstouch/phase-swift.struct/began.md)
  A finger touched the device. Or, a resting touch transitioned to an active touch and resting touches are not wanted by the view hierarchy.
- [static var moved: NSTouch.Phase](nstouch/phase-swift.struct/moved.md)
  A finger moved on the device.
- [static var stationary: NSTouch.Phase](nstouch/phase-swift.struct/stationary.md)
  A finger is touching the device, but hasn’t moved since the previous event.
- [static var ended: NSTouch.Phase](nstouch/phase-swift.struct/ended.md)
  A finger was lifted from the screen. Or, an active touch transitioned to a resting touch and resting touches are not wanted by the view hierarchy.
- [static var cancelled: NSTouch.Phase](nstouch/phase-swift.struct/cancelled.md)
  The system cancelled tracking for the touch, as when (for example) the window associated with the touch resigns key or is deactivated.
- [static var touching: NSTouch.Phase](nstouch/phase-swift.struct/touching.md)
  Matches the [`began`](nstouch/phase-swift.struct/began.md), [`moved`](nstouch/phase-swift.struct/moved.md), or [`stationary`](nstouch/phase-swift.struct/stationary.md) phases of a touch.
- [static var any: NSTouch.Phase](nstouch/phase-swift.struct/any.md)
  Matches any phase of a touch.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [var identity: any NSCopying & NSObjectProtocol](nstouch/identity.md)
  The changes to a particular touch during its lifetime.
- [var phase: NSTouch.Phase](nstouch/phase-swift.property.md)
  The current phase of the touch.
- [var normalizedPosition: NSPoint](nstouch/normalizedposition.md)
  The normalized position of the touch.
- [var isResting: Bool](nstouch/isresting.md)
  The indicator for a resting touch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstouch/phase-swift.struct)*