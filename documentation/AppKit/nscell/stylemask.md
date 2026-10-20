# NSCell.StyleMask

**Framework**: AppKit  
**Kind**: struct  
**Role**: Structure

Constants for specifying what happens when a button is pressed or is displaying its alternate state.

**Availability**:
- macOS

## Declaration

```swift
struct StyleMask
```

```c
enum NSCellStyleMask : NSUInteger;
```

#### Overview

These contents are used by the [`highlightsBy`](../nsbuttoncell/highlightsby.md) and [`showsStateBy`](../nsbuttoncell/showsstateby.md) methods of [`NSButtonCell`](../nsbuttoncell.md).

## Topics

### Constants
- [static var pushInCellMask: NSCell.StyleMask](./stylemask/pushincellmask.md)
  The button cell “pushes in” if it has a border.
- [static var contentsCellMask: NSCell.StyleMask](./stylemask/contentscellmask.md)
  The button cell displays its alternate icon and/or title.
- [static var changeGrayCellMask: NSCell.StyleMask](./stylemask/changegraycellmask.md)
  The button cell swaps the “control color” (the [`controlColor`](../nscolor/controlcolor.md) method of `NSColor`) and white pixels on its background and icon.
- [static var changeBackgroundCellMask: NSCell.StyleMask](./stylemask/changebackgroundcellmask.md)
  Same as `NSChangeGrayCellMask`, but only background pixels are changed.
### Initializers
- [init(rawValue: UInt)](./stylemask/init%28rawvalue%29.md)

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

### Constants
- [NSCell.CellType](./celltype.md)
  Constants for specifying how a cell represents its data (as text or as an image).
- [NSCell.Attribute](./attribute.md)
  Constants for specifying how a button behaves when pressed and how it displays its state.
- [NSControl.ImagePosition](../nscontrol/imageposition.md)
  A constant for specifying the position of a button’s image relative to its title.
- [enum NSImageScaling](../nsimagescaling.md)
  Constants that specify a cell’s image scaling behavior.
- [enum NSControlTint](../nscontroltint.md)
  Constants for specifying a cell’s tint color.
- [NSControl.ControlSize](../nscontrol/controlsize-swift.enum.md)
  A constant for specifying a cell’s size.
- [NSCell.HitResult](./hitresult.md)
  Constants used by the [`hitTest(for:in:of:)`](./hittest%28for,in,of%29.md) method to determine the effect of an event.
- [NSView.BackgroundStyle](../nsview/backgroundstyle.md)
  Background styles to apply to a view’s cell.
- [Deprecated Scaling Constants](../deprecated-scaling-constants.md)
  These are deprecated scaling constants.
- [Data Entry Types](../data-entry-types.md)
  These constants specify how a cell formats numeric data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscell/stylemask)*