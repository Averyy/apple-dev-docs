# NSTouch

**Framework**: AppKit  
**Kind**: class

A snapshot of a particular touch at an instant in time.

**Availability**:
- macOS 10.6+

## Declaration

```swift
class NSTouch
```

#### Overview

A touch event is not persistent throughout the touch. A touch creates new instances as it progresses. Use the identity property to follow a specific touch across its lifetime.

Touches do not have a corresponding screen location. The first touch of a touch collection latches to the view underlying the cursor using the same hit detection as mouse events. Additional touches on the same device latch to the same view. Latches remain on views until the user ends a touch or an event cancels it.

## Topics

### Getting the Touch Type
- [var type: NSTouch.TouchType](nstouch/type.md)
  A type of touch from a Touch Bar interaction.
- [NSTouch.TouchType](nstouch/touchtype.md)
  A bit mask identifying a direct or indirect touch type.
- [NSTouch.TouchTypeMask](nstouch/touchtypemask.md)
  A bit mask identifying a direct or indirect touch type.
### Using Touch Properties
- [var identity: any NSCopying & NSObjectProtocol](nstouch/identity.md)
  The changes to a particular touch during its lifetime.
- [var phase: NSTouch.Phase](nstouch/phase-swift.property.md)
  The current phase of the touch.
- [NSTouch.Phase](nstouch/phase-swift.struct.md)
  The possible phases of a touch.
- [var normalizedPosition: NSPoint](nstouch/normalizedposition.md)
  The normalized position of the touch.
- [var isResting: Bool](nstouch/isresting.md)
  The indicator for a resting touch.
### Using Touch Device Properties
- [var device: Any?](nstouch/device.md)
  The digitizer that generates the touch. Useful to distinguish touches emanating from multiple-device scenarios.
- [var deviceSize: NSSize](nstouch/devicesize.md)
  The range of the touch device in points, such as 72 ppi.
### Getting the Touch Location
- [func location(in: NSView?) -> NSPoint](nstouch/location(in:).md)
  Indicates the location of the touch in the view’s coordinates.
- [func previousLocation(in: NSView?) -> NSPoint](nstouch/previouslocation(in:).md)
  Indicates the previous location of the touch in the view’s coordinates.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class NSEvent](nsevent.md)
  An object that contains information about an input action, such as a mouse click or a key press.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstouch)*