# NSControl.ControlSize

**Framework**: AppKit  
**Kind**: enum  
**Role**: Enumeration

A constant for specifying a cell’s size.

**Availability**:
- macOS

## Declaration

```swift
enum ControlSize
```

```c
enum NSControlSize : NSUInteger;
```

#### Overview

These constants are used by the [`controlSize`](../nscell/controlsize.md) property.

## Topics

### Sizing Controls
- [NSControl.ControlSize.mini](./controlsize-swift.enum/mini.md)
  The smallest control size.
- [NSControl.ControlSize.small](./controlsize-swift.enum/small.md)
  A size smaller than the default control size.
- [NSControl.ControlSize.regular](./controlsize-swift.enum/regular.md)
  The default control size.
- [NSControl.ControlSize.large](./controlsize-swift.enum/large.md)
  A size larger than the default control size.
### Enumeration Cases
- [NSControl.ControlSize.extraLarge](./controlsize-swift.enum/extralarge.md)
### Initializers
- [init?(ControlSize)](./controlsize-swift.enum/init%28_%29.md)
  Creates a control size from its ControlSize equivalent.
- [init?(rawValue: UInt)](./controlsize-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Constants
- [NSCell.CellType](../nscell/celltype.md)
  Constants for specifying how a cell represents its data (as text or as an image).
- [NSCell.Attribute](../nscell/attribute.md)
  Constants for specifying how a button behaves when pressed and how it displays its state.
- [NSControl.ImagePosition](./imageposition.md)
  A constant for specifying the position of a button’s image relative to its title.
- [enum NSImageScaling](../nsimagescaling.md)
  Constants that specify a cell’s image scaling behavior.
- [NSCell.StyleMask](../nscell/stylemask.md)
  Constants for specifying what happens when a button is pressed or is displaying its alternate state.
- [enum NSControlTint](../nscontroltint.md)
  Constants for specifying a cell’s tint color.
- [NSCell.HitResult](../nscell/hitresult.md)
  Constants used by the [`hitTest(for:in:of:)`](../nscell/hittest%28for,in,of%29.md) method to determine the effect of an event.
- [NSView.BackgroundStyle](../nsview/backgroundstyle.md)
  Background styles to apply to a view’s cell.
- [Deprecated Scaling Constants](../deprecated-scaling-constants.md)
  These are deprecated scaling constants.
- [Data Entry Types](../data-entry-types.md)
  These constants specify how a cell formats numeric data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscontrol/controlsize-swift.enum)*