# NSTouch.TouchTypeMask

**Framework**: AppKit  
**Kind**: struct  
**Role**: Structure

A bit mask identifying a direct or indirect touch type.

**Availability**:
- macOS 10.12.2+

## Declaration

```swift
struct TouchTypeMask
```

```c
enum NSTouchTypeMask : NSUInteger;
```

## Topics

### Creating a Touch Type Mask
- [init(type: NSTouch.TouchType)](./touchtypemask/init%28type%29.md)
  Creates a new touch type mask from the touch type.
- [init(rawValue: UInt)](./touchtypemask/init%28rawvalue%29.md)
  Creates a new touch type mask from the given raw value.
### Masking the Touch Types
- [static var direct: NSTouch.TouchTypeMask](./touchtypemask/direct.md)
  A direct touch from a user’s finger on a screen.
- [static var indirect: NSTouch.TouchTypeMask](./touchtypemask/indirect.md)
  An indirect touch that is not on a screen, like a digitizer touch.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [SetAlgebra](../../Swift/setalgebra.md)

## See Also

### Getting the Touch Type
- [var type: NSTouch.TouchType](./type.md)
  A type of touch from a Touch Bar interaction.
- [NSTouch.TouchType](./touchtype.md)
  A bit mask identifying a direct or indirect touch type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstouch/touchtypemask)*