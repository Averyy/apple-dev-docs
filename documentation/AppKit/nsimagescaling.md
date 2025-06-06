# NSImageScaling

**Framework**: AppKit  
**Kind**: enum

Constants that specify a cell’s image scaling behavior.

**Availability**:
- macOS 10.5+

## Declaration

```swift
enum NSImageScaling
```

## Topics

### Constants
- [NSImageScaling.scaleProportionallyDown](nsimagescaling/scaleproportionallydown.md)
  If it is too large for the destination, scale the image down while preserving the aspect ratio.
- [NSImageScaling.scaleAxesIndependently](nsimagescaling/scaleaxesindependently.md)
  Scale each dimension to exactly fit destination.
- [NSImageScaling.scaleNone](nsimagescaling/scalenone.md)
  Do not scale the image.
- [NSImageScaling.scaleProportionallyUpOrDown](nsimagescaling/scaleproportionallyupordown.md)
  Scale the image to its maximum possible dimensions while both staying within the destination area and preserving its aspect ratio.
### Type Properties
- [static var NSScaleNone: NSImageScaling](nsimagescaling/nsscalenone.md)
- [static var NSScaleProportionally: NSImageScaling](nsimagescaling/nsscaleproportionally.md)
- [static var NSScaleToFit: NSImageScaling](nsimagescaling/nsscaletofit.md)
### Initializers
- [init?(rawValue: UInt)](nsimagescaling/init(rawvalue:).md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimagescaling)*