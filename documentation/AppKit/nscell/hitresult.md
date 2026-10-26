# NSCell.HitResult

**Framework**: AppKit  
**Kind**: struct  
**Role**: Structure

Constants used by the [`hitTest(for:in:of:)`](./hittest%28for,in,of%29.md) method to determine the effect of an event.

**Availability**:
- macOS 10.5+

## Declaration

```swift
struct HitResult
```

```c
enum NSCellHitResult : NSUInteger;
```

## Topics

### Constants
- [static var contentArea: NSCell.HitResult](./hitresult/contentarea.md)
  A content area in the cell.
- [static var editableTextArea: NSCell.HitResult](./hitresult/editabletextarea.md)
  An editable text area of the cell.
- [static var trackableArea: NSCell.HitResult](./hitresult/trackablearea.md)
  A trackable area in the cell.
- [NSCellHitNone](../nscellhitresult/nscellhitnone.md)
  An empty area, or did not hit in the cell.
### Initializers
- [init(rawValue: UInt)](./hitresult/init%28rawvalue%29.md)

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
- [NSCell.StyleMask](./stylemask.md)
  Constants for specifying what happens when a button is pressed or is displaying its alternate state.
- [enum NSControlTint](../nscontroltint.md)
  Constants for specifying a cell’s tint color.
- [NSControl.ControlSize](../nscontrol/controlsize-swift.enum.md)
  A constant for specifying a cell’s size.
- [NSView.BackgroundStyle](../nsview/backgroundstyle.md)
  Background styles to apply to a view’s cell.
- [Deprecated Scaling Constants](../deprecated-scaling-constants.md)
  These are deprecated scaling constants.
- [Data Entry Types](../data-entry-types.md)
  These constants specify how a cell formats numeric data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscell/hitresult)*