# NSView.AutoresizingMask

**Framework**: AppKit  
**Kind**: struct  
**Role**: Structure

Constants that specify the autoresizing behaviors for views.

**Availability**:
- macOS

## Declaration

```swift
struct AutoresizingMask
```

```c
enum NSAutoresizingMaskOptions : NSUInteger;
```

## Topics

### Getting the Autoresizing mask
- [static var none: NSView.AutoresizingMask](./autoresizingmask-swift.struct/none.md)
  The view cannot be resized.
- [static var minXMargin: NSView.AutoresizingMask](./autoresizingmask-swift.struct/minxmargin.md)
  The left margin between the view and its superview is flexible.
- [static var width: NSView.AutoresizingMask](./autoresizingmask-swift.struct/width.md)
  The view’s width is flexible.
- [static var maxXMargin: NSView.AutoresizingMask](./autoresizingmask-swift.struct/maxxmargin.md)
  The right margin between the view and its superview is flexible.
- [static var minYMargin: NSView.AutoresizingMask](./autoresizingmask-swift.struct/minymargin.md)
  The bottom margin between the view and its superview is flexible.
- [static var height: NSView.AutoresizingMask](./autoresizingmask-swift.struct/height.md)
  The view’s height is flexible.
- [static var maxYMargin: NSView.AutoresizingMask](./autoresizingmask-swift.struct/maxymargin.md)
  The top margin between the view and its superview is flexible.
### Creating an Autoresizing Mask
- [init(rawValue: UInt)](./autoresizingmask-swift.struct/init%28rawvalue%29.md)

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

### Resizing Subviews
- [var autoresizesSubviews: Bool](./autoresizessubviews.md)
  A Boolean value indicating whether the view applies the autoresizing behavior to its subviews when its frame size changes.
- [var autoresizingMask: NSView.AutoresizingMask](./autoresizingmask-swift.property.md)
  The options that determine how the view is resized relative to its superview.
- [func resizeSubviews(withOldSize: NSSize)](./resizesubviews%28witholdsize%29.md)
  Informs the view’s subviews that the view’s bounds rectangle size has changed.
- [func resize(withOldSuperviewSize: NSSize)](./resize%28witholdsuperviewsize%29.md)
  Informs the view that the bounds size of its superview has changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/autoresizingmask-swift.struct)*