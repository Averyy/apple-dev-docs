# NSTrackingArea.Options

**Framework**: AppKit  
**Kind**: struct  
**Role**: Structure

The data type defined for the constants specified in the `options` parameter of [`init(rect:options:owner:userInfo:)`](./init%28rect,options,owner,userinfo%29.md). These constants are described below; you can specify multiple constants by performing a bitwise-OR operation with them. In particular, you must supply one or more of the tracking-type constants (that is, [`mouseEnteredAndExited`](./options-swift.struct/mouseenteredandexited.md), [`mouseMoved`](./options-swift.struct/mousemoved.md), and [`cursorUpdate`](./options-swift.struct/cursorupdate.md)) and one of the active constants (that is, [`activeWhenFirstResponder`](./options-swift.struct/activewhenfirstresponder.md), [`activeInKeyWindow`](./options-swift.struct/activeinkeywindow.md), [`activeInActiveApp`](./options-swift.struct/activeinactiveapp.md), and [`activeAlways`](./options-swift.struct/activealways.md)). In addition, you may specify any of the behavior constants (that is, [`assumeInside`](./options-swift.struct/assumeinside.md), [`inVisibleRect`](./options-swift.struct/invisiblerect.md), and [`enabledDuringMouseDrag`](./options-swift.struct/enabledduringmousedrag.md)).

**Availability**:
- macOS

## Declaration

```swift
struct Options
```

```c
enum NSTrackingAreaOptions : NSUInteger;
```

## Topics

### Constants
- [static var mouseEnteredAndExited: NSTrackingArea.Options](./options-swift.struct/mouseenteredandexited.md)
  The owner of the tracking area receives [`mouseEntered(with:)`](../nsresponder/mouseentered%28with%29.md) when the mouse cursor enters the area and [`mouseExited(with:)`](../nsresponder/mouseexited%28with%29.md) events when the mouse leaves the area. This value specifies a type of tracking area.
- [static var mouseMoved: NSTrackingArea.Options](./options-swift.struct/mousemoved.md)
  The owner of the tracking area receives [`mouseMoved(with:)`](../nsresponder/mousemoved%28with%29.md) messages while the mouse cursor is within the area. This value specifies a type of tracking area.
- [static var cursorUpdate: NSTrackingArea.Options](./options-swift.struct/cursorupdate.md)
  A tracking option that receives events when the mouse cursor enters and exits the tracking area.
- [static var activeWhenFirstResponder: NSTrackingArea.Options](./options-swift.struct/activewhenfirstresponder.md)
  The owner receives messages when the view is the first responder. This value specifies when the tracking area defined by an [`NSTrackingArea`](../nstrackingarea.md) object is active.
- [static var activeInKeyWindow: NSTrackingArea.Options](./options-swift.struct/activeinkeywindow.md)
  The owner receives messages when the view is in the key window. This value specifies when the tracking area defined by an [`NSTrackingArea`](../nstrackingarea.md) object is active.
- [static var activeInActiveApp: NSTrackingArea.Options](./options-swift.struct/activeinactiveapp.md)
  The owner receives messages when the application is active. This value specifies when the tracking area defined by an [`NSTrackingArea`](../nstrackingarea.md) object is active.
- [static var activeAlways: NSTrackingArea.Options](./options-swift.struct/activealways.md)
  The owner receives messages regardless of first-responder status, window status, or application status. The [`cursorUpdate(with:)`](../nsresponder/cursorupdate%28with%29.md) message is *not* sent when the [`cursorUpdate`](./options-swift.struct/cursorupdate.md) option is specified along with this constant. This value specifies when the tracking area defined by an [`NSTrackingArea`](../nstrackingarea.md) object is active.
- [static var assumeInside: NSTrackingArea.Options](./options-swift.struct/assumeinside.md)
  The first event is generated when the cursor leaves the tracking area, regardless if the cursor is inside the area when the `NSTrackingArea` is added to a view.  If this option is not specified, the first event is generated when the cursor leaves the tracking area if the cursor is initially inside the area, or when the cursor enters the area if the cursor is initially outside it. Generally, you do not want to request this behavior. This value specifies a behavior of the tracking area defined by the [`NSTrackingArea`](../nstrackingarea.md).
- [static var inVisibleRect: NSTrackingArea.Options](./options-swift.struct/invisiblerect.md)
  Mouse tracking occurs only in the visible rectangle of the view—in other words, that region of the tracking rectangle that is unobscured. Otherwise, the entire tracking area is active regardless of overlapping views. The `NSTrackingArea` object is automatically synchronized with changes in the view’s visible area ([`visibleRect`](../nsview/visiblerect.md)) and the value returned from [`rect`](./rect.md) is ignored. This value specifies a behavior of the tracking area defined by the [`NSTrackingArea`](../nstrackingarea.md).
- [static var enabledDuringMouseDrag: NSTrackingArea.Options](./options-swift.struct/enabledduringmousedrag.md)
  The owner receives [`NSMouseEntered`](../nsmouseentered.md) events when the mouse cursor is dragged into the tracking area. If this option is not specified, the owner receives mouse-entered events when the mouse is moved (no buttons pressed) into the tracking area and on [`NSLeftMouseUp`](../nsleftmouseup.md) events after a mouse drag.
### Initializers
- [init(rawValue: UInt)](./options-swift.struct/init%28rawvalue%29.md)

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstrackingarea/options-swift.struct)*