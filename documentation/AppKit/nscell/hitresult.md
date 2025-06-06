# NSCell.HitResult

**Framework**: AppKit  
**Kind**: struct

Constants used by the [`hitTest(for:in:of:)`](nscell/hittest(for:in:of:).md) method to determine the effect of an event.

**Availability**:
- macOS 10.5+

## Declaration

```swift
struct HitResult
```

## Topics

### Constants
- [static var contentArea: NSCell.HitResult](nscell/hitresult/contentarea.md)
  A content area in the cell.
- [static var editableTextArea: NSCell.HitResult](nscell/hitresult/editabletextarea.md)
  An editable text area of the cell.
- [static var trackableArea: NSCell.HitResult](nscell/hitresult/trackablearea.md)
  A trackable area in the cell.
### Initializers
- [init(rawValue: UInt)](nscell/hitresult/init(rawvalue:).md)

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
- [NSCell.StyleMask](nscell/stylemask.md)
  Constants for specifying what happens when a button is pressed or is displaying its alternate state.
- [enum NSControlTint](nscontroltint.md)
  Constants for specifying a cell’s tint color.
- [NSControl.ControlSize](nscontrol/controlsize-swift.enum.md)
  A constant for specifying a cell’s size.
- [NSView.BackgroundStyle](nsview/backgroundstyle.md)
  Background styles to apply to a view’s cell.
- [Deprecated Scaling Constants](deprecated-scaling-constants.md)
  These are deprecated scaling constants.
- [Data Entry Types](data-entry-types.md)
  These constants specify how a cell formats numeric data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscell/hitresult)*