# NSControlTint

**Framework**: AppKit  
**Kind**: enum

Constants for specifying a cell’s tint color.

**Availability**:
- macOS ?+

## Declaration

```swift
enum NSControlTint
```

#### Overview

These constants are used by the [`controlTint`](nscell/controltint.md) property.

## Topics

### System Tints
- [NSControlTint.defaultControlTint](nscontroltint/defaultcontroltint.md)
  The current default tint setting.
- [NSControlTint.blueControlTint](nscontroltint/bluecontroltint.md)
  Aqua control tint.
- [NSControlTint.graphiteControlTint](nscontroltint/graphitecontroltint.md)
  Graphite control tint.
- [NSControlTint.clearControlTint](nscontroltint/clearcontroltint.md)
  Clear control tint.
### Initializers
- [init?(rawValue: UInt)](nscontroltint/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [NSCell.CellType](nscell/celltype.md)
  Constants for specifying how a cell represents its data (as text or as an image).
- [NSCell.Attribute](nscell/attribute.md)
  Constants for specifying how a button behaves when pressed and how it displays its state.
- [NSControl.ImagePosition](nscontrol/imageposition.md)
  A constant for specifying the position of a button’s image relative to its title.
- [enum NSImageScaling](nsimagescaling.md)
  Constants that specify a cell’s image scaling behavior.
- [typealias StateValue](nscell/statevalue.md)
  Constants for specifying a cell’s state and are used mostly for buttons.
- [NSCell.StyleMask](nscell/stylemask.md)
  Constants for specifying what happens when a button is pressed or is displaying its alternate state.
- [NSControl.ControlSize](nscontrol/controlsize-swift.enum.md)
  A constant for specifying a cell’s size.
- [NSCell.HitResult](nscell/hitresult.md)
  Constants used by the [`hitTest(for:in:of:)`](nscell/hittest(for:in:of:).md) method to determine the effect of an event.
- [NSView.BackgroundStyle](nsview/backgroundstyle.md)
  Background styles to apply to a view’s cell.
- [Deprecated Scaling Constants](deprecated-scaling-constants.md)
  These are deprecated scaling constants.
- [Data Entry Types](data-entry-types.md)
  These constants specify how a cell formats numeric data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscontroltint)*