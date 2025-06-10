# NSCell.Attribute

**Framework**: AppKit  
**Kind**: enum

Constants for specifying how a button behaves when pressed and how it displays its state.

**Availability**:
- macOS ?+

## Declaration

```swift
enum Attribute
```

#### Overview

These constants are used by the [`NSButton`](nsbutton.md) and [`NSButtonCell`](nsbuttoncell.md) classes.

## Topics

### Constants
- [NSCell.Attribute.cellAllowsMixedState](nscell/attribute/cellallowsmixedstate.md)
  Lets the cell’s state be `NSMixedState`, as well as `NSOffState` and `NSOnState`.
- [NSCell.Attribute.changeBackgroundCell](nscell/attribute/changebackgroundcell.md)
  If the cell’s state is `NSMixedState` or `NSOnState`, changes the cell’s background color from gray to white.
- [NSCell.Attribute.cellChangesContents](nscell/attribute/cellchangescontents.md)
  If the cell’s state is `NSMixedState` or `NSOnState`, displays the cell’s alternate image.
- [NSCell.Attribute.changeGrayCell](nscell/attribute/changegraycell.md)
  If the cell’s state is `NSMixedState` or `NSOnState`, displays the cell’s image as darkened.
- [NSCell.Attribute.cellDisabled](nscell/attribute/celldisabled.md)
  Does not let the user manipulate the cell.
- [NSCell.Attribute.cellEditable](nscell/attribute/celleditable.md)
  Lets the user edit the cell’s contents.
- [NSCell.Attribute.cellHasImageHorizontal](nscell/attribute/cellhasimagehorizontal.md)
  Controls the position of the cell’s image: places the image on the right of any text in the cell.
- [NSCell.Attribute.cellHasImageOnLeftOrBottom](nscell/attribute/cellhasimageonleftorbottom.md)
  Controls the position of the cell’s image: places the image on the left of or below any text in the cell.
- [NSCell.Attribute.cellHasOverlappingImage](nscell/attribute/cellhasoverlappingimage.md)
  Controls the position of the cell’s image: places the image over any text in the cell.
- [NSCell.Attribute.cellHighlighted](nscell/attribute/cellhighlighted.md)
  Draws the cell with a highlighted appearance.
- [NSCell.Attribute.cellIsBordered](nscell/attribute/cellisbordered.md)
  Draws a border around the cell.
- [NSCell.Attribute.cellIsInsetButton](nscell/attribute/cellisinsetbutton.md)
  Insets the cell’s contents from the border.
- [NSCell.Attribute.cellLightsByBackground](nscell/attribute/celllightsbybackground.md)
  If the cell is pushed in, changes the cell’s background color from gray to white.
- [NSCell.Attribute.cellLightsByContents](nscell/attribute/celllightsbycontents.md)
  If the cell is pushed in, displays the cell’s alternate image.
- [NSCell.Attribute.cellLightsByGray](nscell/attribute/celllightsbygray.md)
  If the cell is pushed in, displays the cell’s image as darkened.
- [NSCell.Attribute.pushInCell](nscell/attribute/pushincell.md)
  Determines whether the cell’s image and text appear to be shifted down and to the right.
- [NSCell.Attribute.cellState](nscell/attribute/cellstate.md)
  The cell’s state.
### Initializers
- [init?(rawValue: UInt)](nscell/attribute/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [NSCell.CellType](nscell/celltype.md)
  Constants for specifying how a cell represents its data (as text or as an image).
- [NSControl.ImagePosition](nscontrol/imageposition.md)
  A constant for specifying the position of a button’s image relative to its title.
- [enum NSImageScaling](nsimagescaling.md)
  Constants that specify a cell’s image scaling behavior.
- [typealias StateValue](nscell/statevalue.md)
  Constants for specifying a cell’s state and are used mostly for buttons.
- [NSCell.StyleMask](nscell/stylemask.md)
  Constants for specifying what happens when a button is pressed or is displaying its alternate state.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscell/attribute)*