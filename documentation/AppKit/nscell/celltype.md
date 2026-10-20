# NSCell.CellType

**Framework**: AppKit  
**Kind**: enum  
**Role**: Enumeration

Constants for specifying how a cell represents its data (as text or as an image).

**Availability**:
- macOS

## Declaration

```swift
enum CellType
```

```c
enum NSCellType : NSUInteger;
```

## Topics

### Constants
- [NSCell.CellType.nullCellType](./celltype/nullcelltype.md)
  Cell displays nothing.
- [NSCell.CellType.textCellType](./celltype/textcelltype.md)
  Cell displays text.
- [NSCell.CellType.imageCellType](./celltype/imagecelltype.md)
  Cell displays images.
### Initializers
- [init?(rawValue: UInt)](./celltype/init%28rawvalue%29.md)

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
- [NSCell.HitResult](./hitresult.md)
  Constants used by the [`hitTest(for:in:of:)`](./hittest%28for,in,of%29.md) method to determine the effect of an event.
- [NSView.BackgroundStyle](../nsview/backgroundstyle.md)
  Background styles to apply to a view’s cell.
- [Deprecated Scaling Constants](../deprecated-scaling-constants.md)
  These are deprecated scaling constants.
- [Data Entry Types](../data-entry-types.md)
  These constants specify how a cell formats numeric data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscell/celltype)*