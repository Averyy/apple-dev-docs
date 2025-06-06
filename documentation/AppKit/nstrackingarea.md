# NSTrackingArea

**Framework**: AppKit  
**Kind**: class

A region of a view that generates mouse-tracking and cursor-update events when the pointer is over that region.

**Availability**:
- macOS 10.5+

## Declaration

```swift
class NSTrackingArea
```

#### Overview

When creating a tracking-area object, you specify a rectangle (in the view’s coordinate system), an owning object, and one or more options, along with (optionally) a dictionary of data. After it’s created, you add the tracking-area object to a view using the [`addTrackingArea(_:)`](nsview/addtrackingarea(_:).md) method. Depending on the options specified, the owner of the tracking area receives [`mouseEntered(with:)`](nsresponder/mouseentered(with:).md), [`mouseExited(with:)`](nsresponder/mouseexited(with:).md), [`mouseMoved(with:)`](nsresponder/mousemoved(with:).md), and [`cursorUpdate(with:)`](nsresponder/cursorupdate(with:).md) messages when the mouse cursor enters, moves within, and leaves the tracking area. Currently the tracking area is restricted to rectangles.

An [`NSTrackingArea`](nstrackingarea.md) object belongs to its view rather than to its window. Consequently, you can add and remove tracking rectangles without needing to worry if the view has been added to a window. In addition, this design makes it possible for the AppKit to compute the geometry of tracking areas automatically when a view moves and, in some cases, when a view changes size.

Using [`NSTrackingArea`](nstrackingarea.md), you can configure the scope of activity for mouse tracking. There are four options:

- The tracking area is active only when the view is first responder.
- The tracking area is active when the view is in the key window.
- The tracking area is active when the application is active.
- The tracking area is active always (even when the application is inactive).

Other options for [`NSTrackingArea`](nstrackingarea.md) objects include specifying that the tracking area should be synchronized with the visible rectangle of the view ([`visibleRect`](nsview/visiblerect.md)) and for generating `mouseEntered:` and `mouseExited`: events when the mouse is dragged.

Other [`NSView`](nsview.md) methods related to [`NSTrackingArea`](nstrackingarea.md) objects (in addition to [`addTrackingArea(_:)`](nsview/addtrackingarea(_:).md)) include [`removeTrackingArea(_:)`](nsview/removetrackingarea(_:).md) and [`updateTrackingAreas()`](nsview/updatetrackingareas().md). Views can override the latter method to recompute and replace their [`NSTrackingArea`](nstrackingarea.md) objects in certain situations, such as a change in the size of the `visibleRect`.

## Topics

### Initializing the Tracking-Area Object
- [init(rect: NSRect, options: NSTrackingArea.Options, owner: Any?, userInfo: [AnyHashable : Any]?)](nstrackingarea/init(rect:options:owner:userinfo:).md)
  Initializes and returns an object defining a region of a view to receive mouse-tracking events, mouse-moved events, cursor-update events, or possibly all these events.
### Getting Object Attributes
- [var options: NSTrackingArea.Options](nstrackingarea/options-swift.property.md)
  The options specified for the receiver.
- [var owner: AnyObject?](nstrackingarea/owner.md)
  The object owning the receiver, which is the recipient of mouse-tracking, mouse-movement, and cursor-update messages.
- [var rect: NSRect](nstrackingarea/rect.md)
  The rectangle defining the area encompassed by the receiver.
- [var userInfo: [AnyHashable : Any]?](nstrackingarea/userinfo.md)
  The dictionary containing the data associated with the receiver when it was created.
### Constants
- [NSTrackingArea.Options](nstrackingarea/options-swift.struct.md)
  The data type defined for the constants specified in the `options` parameter of [`init(rect:options:owner:userInfo:)`](nstrackingarea/init(rect:options:owner:userinfo:).md). These constants are described below; you can specify multiple constants by performing a bitwise-OR operation with them. In particular, you must supply one or more of the tracking-type constants (that is, [`mouseEnteredAndExited`](nstrackingarea/options-swift.struct/mouseenteredandexited.md), [`mouseMoved`](nstrackingarea/options-swift.struct/mousemoved.md), and [`cursorUpdate`](nstrackingarea/options-swift.struct/cursorupdate.md)) and one of the active constants (that is, [`activeWhenFirstResponder`](nstrackingarea/options-swift.struct/activewhenfirstresponder.md), [`activeInKeyWindow`](nstrackingarea/options-swift.struct/activeinkeywindow.md), [`activeInActiveApp`](nstrackingarea/options-swift.struct/activeinactiveapp.md), and [`activeAlways`](nstrackingarea/options-swift.struct/activealways.md)). In addition, you may specify any of the behavior constants (that is, [`assumeInside`](nstrackingarea/options-swift.struct/assumeinside.md), [`inVisibleRect`](nstrackingarea/options-swift.struct/invisiblerect.md), and [`enabledDuringMouseDrag`](nstrackingarea/options-swift.struct/enabledduringmousedrag.md)).

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class NSCursor](nscursor.md)
  A pointer (also called a cursor).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstrackingarea)*