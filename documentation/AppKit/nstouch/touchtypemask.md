# NSTouch.TouchTypeMask

**Framework**: AppKit  
**Kind**: struct

A bit mask identifying a direct or indirect touch type.

**Availability**:
- macOS 10.12.2+

## Declaration

```swift
struct TouchTypeMask
```

## Topics

### Creating a Touch Type Mask
- [init(type: NSTouch.TouchType)](nstouch/touchtypemask/init(type:).md)
  Creates a new touch type mask from the touch type.
- [init(rawValue: UInt)](nstouch/touchtypemask/init(rawvalue:).md)
  Creates a new touch type mask from the given raw value.
### Masking the Touch Types
- [static var direct: NSTouch.TouchTypeMask](nstouch/touchtypemask/direct.md)
  A direct touch from a user’s finger on a screen.
- [static var indirect: NSTouch.TouchTypeMask](nstouch/touchtypemask/indirect.md)
  An indirect touch that is not on a screen, like a digitizer touch.

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

- [var type: NSTouch.TouchType](nstouch/type.md)
  A type of touch from a Touch Bar interaction.
- [NSTouch.TouchType](nstouch/touchtype.md)
  A bit mask identifying a direct or indirect touch type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstouch/touchtypemask)*