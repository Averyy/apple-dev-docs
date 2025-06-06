# NSCell.StyleMask

**Framework**: AppKit  
**Kind**: struct

Constants for specifying what happens when a button is pressed or is displaying its alternate state.

**Availability**:
- macOS ?+

## Declaration

```swift
struct StyleMask
```

#### Overview

These contents are used by the [`highlightsBy`](nsbuttoncell/highlightsby.md) and [`showsStateBy`](nsbuttoncell/showsstateby.md) methods of [`NSButtonCell`](nsbuttoncell.md).

## Topics

### Constants
- [static var pushInCellMask: NSCell.StyleMask](nscell/stylemask/pushincellmask.md)
  The button cell “pushes in” if it has a border.
- [static var contentsCellMask: NSCell.StyleMask](nscell/stylemask/contentscellmask.md)
  The button cell displays its alternate icon and/or title.
- [static var changeGrayCellMask: NSCell.StyleMask](nscell/stylemask/changegraycellmask.md)
  The button cell swaps the “control color” (the [`controlColor`](nscolor/controlcolor.md) method of `NSColor`) and white pixels on its background and icon.
- [static var changeBackgroundCellMask: NSCell.StyleMask](nscell/stylemask/changebackgroundcellmask.md)
  Same as `NSChangeGrayCellMask`, but only background pixels are changed.
### Initializers
- [init(rawValue: UInt)](nscell/stylemask/init(rawvalue:).md)

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
- [enum NSControlTint](nscontroltint.md)
  Constants for specifying a cell’s tint color.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscell/stylemask)*