# NSCursor

**Framework**: AppKit  
**Kind**: class

A pointer (also called a cursor).

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.0+

## Declaration

```swift
class NSCursor
```

#### Overview

The following table shows and describes the system cursors, and indicates the class method for obtaining them:

| Cursor | Description |
| --- | --- |
| ![arrow cursor](/images/com.apple.appkit/media-2555572@2x.png) | The arrow cursor ([`arrow`](nscursor/arrow.md)) |
| ![I-beam cursor](/images/com.apple.appkit/media-2555577@2x.png) | The I-beam cursor for indicating insertion points ([`iBeam`](nscursor/ibeam.md)) |
| ![cross-hair cursor](/images/com.apple.appkit/media-2555579@2x.png) | The cross-hair cursor ([`crosshair`](nscursor/crosshair.md)) |
| ![closed-hand cursor](/images/com.apple.appkit/media-2555583@2x.png) | The closed-hand cursor ([`closedHand`](nscursor/closedhand.md)) |
| ![open-hand cursor](/images/com.apple.appkit/media-2555589@2x.png) | The open-hand cursor ([`openHand`](nscursor/openhand.md)) |
| ![pointing hand cursor](/images/com.apple.appkit/media-2555596@2x.png) | The pointing-hand cursor ([`pointingHand`](nscursor/pointinghand.md)) |
| ![resize-left cursor](/images/com.apple.appkit/media-2555601@2x.png) | The resize-left cursor ([`resizeLeft`](nscursor/resizeleft.md)) |
| ![resize-right cursor](/images/com.apple.appkit/media-2555605@2x.png) | The resize-right cursor ([`resizeRight`](nscursor/resizeright.md)) |
| ![resize-left-and-right cursor](/images/com.apple.appkit/media-2555610@2x.png) | The resize-left-and-right cursor ([`resizeLeftRight`](nscursor/resizeleftright.md)) |
| ![resize-up cursor](/images/com.apple.appkit/media-2555619@2x.png) | The resize-up cursor ([`resizeUp`](nscursor/resizeup.md)) |
| ![resize-down cursor](/images/com.apple.appkit/media-2555626@2x.png) | The resize-down cursor ([`resizeDown`](nscursor/resizedown.md)) |
| ![resize-up-and-down cursor](/images/com.apple.appkit/media-2555629@2x.png) | The resize-up-and-down cursor ([`resizeUpDown`](nscursor/resizeupdown.md)) |
| ![disappearing item cursor](/images/com.apple.appkit/media-2555632@2x.png) | The disappearing item cursor ([`disappearingItem`](nscursor/disappearingitem.md)) |
| ![disappearing item cursor](/images/com.apple.appkit/media-2555638@2x.png) | The I-Beam text cursor for vertical layout ([`iBeamCursorForVerticalLayout`](nscursor/ibeamcursorforverticallayout.md)). |
| ![operation not allowed cursor](/images/com.apple.appkit/media-2555643@2x.png) | The not allowed cursor ([`operationNotAllowed`](nscursor/operationnotallowed.md)). |
| ![drag link cursor](/images/com.apple.appkit/media-2555647@2x.png) | The drag link cursor ([`dragLink`](nscursor/draglink.md)). |
| ![drag copy cursor](/images/com.apple.appkit/media-2555652@2x.png) | The drag copy cursor ([`dragCopy`](nscursor/dragcopy.md)). |
| ![contextual menu cursor](/images/com.apple.appkit/media-2555658@2x.png) | The contextual menu cursor ([`contextualMenu`](nscursor/contextualmenu.md)). |

In macOS 10.3 and later, cursor size is no longer limited to 16 by 16 pixels.

##### Cursor Rectangles

In Cocoa, you can change the currently displayed cursor based on the position of the mouse over one of your views. You might use this technique to provide visual feedback about what actions the user can take with the mouse. For example, you might display one of the resize cursors whenever the mouse moves over a portion of your view that acts as a custom resizing handle. To set this up, you associate a cursor object with one or more cursor rectangles in the view.

Cursor rectangles are a specialized type of tracking rectangles, which are used to monitor the mouse location in a view. Views implement cursor rectangles using tracking rectangles but provide methods for setting and refreshing cursor rectangles that are distinct from the generic tracking rectangle interface. For information on mouse-tracking and cursor-update events, see [`NSTrackingArea`](nstrackingarea.md).

##### Balancing Cursor Hiding and Unhiding

Each call to [`hide()`](nscursor/hide().md) cursor must have a corresponding [`unhide()`](nscursor/unhide().md) call. For example,

```objc
[NSCursor hide];
[NSCursor hide];
// ...
[NSCursor unhide];
```

Will result in the cursor still being hidden because the `hide` and `unhide` method invocations are not balanced. Instead you must balance the method calls, such as in the following example:

```objc
[NSCursor hide];
[NSCursor hide];
// ...
[NSCursor unhide];
[NSCursor unhide];
```

There are corresponding cursor `hide` and `unhide` calls, thus the cursor will become visible.

## Topics

### Initializing a new cursor
- [init(image: UIImage, hotSpot: NSPoint)](nscursor/init(image:hotspot:).md)
  Initializes a cursor with the given image and hot spot.
- [init(coder: NSCoder)](nscursor/init(coder:).md)
### Setting cursor attributes
- [var image: UIImage](nscursor/image.md)
  The cursor’s image.
- [var hotSpot: NSPoint](nscursor/hotspot.md)
  The position of the click location within the cursor.
- [class func hide()](nscursor/hide.md)
  Makes the current cursor invisible.
- [class func unhide()](nscursor/unhide.md)
  Negates an earlier call to [`hide()`](nscursor/hide().md) by showing the current cursor.
- [class func setHiddenUntilMouseMoves(Bool)](nscursor/sethiddenuntilmousemoves(_:).md)
  Sets whether the cursor is hidden until the mouse moves.
### Controlling which cursor is current
- [class func pop()](nscursor/pop-swift.type.method.md)
  Pops the current cursor off the top of the stack.
- [func pop()](nscursor/pop-swift.method.md)
  Sends a [`pop()`](nscursor/pop()-swift.type.method.md) message to the receiver’s class.
- [func push()](nscursor/push.md)
  Puts the receiver on top of the cursor stack and makes it the current cursor.
- [func set()](nscursor/set.md)
  Makes the receiver the current cursor.
### Retrieving cursor instances
- [class var current: NSCursor](nscursor/current.md)
  Returns the application’s current cursor.
- [class var arrow: NSCursor](nscursor/arrow.md)
  Returns the default cursor, the arrow cursor.
- [class var contextualMenu: NSCursor](nscursor/contextualmenu.md)
  Returns the contextual menu system cursor.
- [class var closedHand: NSCursor](nscursor/closedhand.md)
  Returns the closed-hand system cursor.
- [class var crosshair: NSCursor](nscursor/crosshair.md)
  Returns the cross-hair system cursor.
- [class var disappearingItem: NSCursor](nscursor/disappearingitem.md)
  Returns a cursor indicating that the current operation will result in a disappearing item.
- [class var dragCopy: NSCursor](nscursor/dragcopy.md)
  Returns a cursor indicating that the current operation will result in a copy action.
- [class var dragLink: NSCursor](nscursor/draglink.md)
  Returns a cursor indicating that the current operation will result in a link action.
- [class var iBeam: NSCursor](nscursor/ibeam.md)
  Returns a cursor that looks like a capital I with a tiny crossbeam at its middle.
- [class var iBeamCursorForVerticalLayout: NSCursor](nscursor/ibeamcursorforverticallayout.md)
  Returns the cursor for editing vertical layout text.
- [class var openHand: NSCursor](nscursor/openhand.md)
  Returns the open-hand system cursor.
- [class var operationNotAllowed: NSCursor](nscursor/operationnotallowed.md)
  Returns the operation not allowed cursor.
- [class var pointingHand: NSCursor](nscursor/pointinghand.md)
  Returns the pointing-hand system cursor.
- [class var zoomIn: NSCursor](nscursor/zoomin.md)
  Returns the zoom-in cursor.
- [class var zoomOut: NSCursor](nscursor/zoomout.md)
  Returns the zoom-out cursor.
- [class var columnResize: NSCursor](nscursor/columnresize.md)
  Returns the cursor for resizing a column (vertical divider) in either direction.
- [class func columnResize(directions: NSHorizontalDirection.Set) -> NSCursor](nscursor/columnresize(directions:).md)
  Returns the cursor for resizing a column (vertical divider) in the specified direction.
- [class var rowResize: NSCursor](nscursor/rowresize.md)
  Returns the cursor for resizing a row (horizontal divider) in either direction.
- [class func rowResize(directions: NSVerticalDirection.Set) -> NSCursor](nscursor/rowresize(directions:).md)
  Returns the cursor for resizing a row (horizontal divider) in the specified direction.
- [class func frameResize(position: NSCursor.FrameResizePosition, directions: NSCursor.FrameResizeDirection.Set) -> NSCursor](nscursor/frameresize(position:directions:).md)
  Returns the cursor for resizing a rectangular frame from the specified edge or corner.
- [NSCursor.FrameResizeDirection](nscursor/frameresizedirection.md)
  The direction in which a rectangular frame can be resized.
### Constants
- [AppKit Versions for NSCursor Bug Fixes](appkit-versions-for-nscursor-bug-fixes.md)
  The version of the AppKit framework containing a specific bug fix.
### Deprecated
- [Deprecated symbols](nscursor-deprecated-symbols.md)
  Review symbols that are no longer in active development, and their recommended replacements.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [Copyable](../swift/copyable.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Escapable](../swift/escapable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)

## See Also

- [class NSTrackingArea](nstrackingarea.md)
  A region of a view that generates mouse-tracking and cursor-update events when the pointer is over that region.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscursor)*