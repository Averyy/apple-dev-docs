# NSCursor

**Framework**: AppKit  
**Kind**: class  
**Role**: Class

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

```objc
@interface NSCursor : NSObject
```

#### Overview

The following table shows and describes the system cursors, and indicates the class method for obtaining them:

| Cursor | Description |
| --- | --- |
| ![arrow cursor](https://developer.apple.com/tutorials/images/com.apple.appkit/media-2555572@2x.png) | The arrow cursor ([`arrow`](./nscursor/arrow.md)) |
| ![I-beam cursor](https://developer.apple.com/tutorials/images/com.apple.appkit/media-2555577@2x.png) | The I-beam cursor for indicating insertion points ([`iBeam`](./nscursor/ibeam.md)) |
| ![cross-hair cursor](https://developer.apple.com/tutorials/images/com.apple.appkit/media-2555579@2x.png) | The cross-hair cursor ([`crosshair`](./nscursor/crosshair.md)) |
| ![closed-hand cursor](https://developer.apple.com/tutorials/images/com.apple.appkit/media-2555583@2x.png) | The closed-hand cursor ([`closedHand`](./nscursor/closedhand.md)) |
| ![open-hand cursor](https://developer.apple.com/tutorials/images/com.apple.appkit/media-2555589@2x.png) | The open-hand cursor ([`openHand`](./nscursor/openhand.md)) |
| ![pointing hand cursor](https://developer.apple.com/tutorials/images/com.apple.appkit/media-2555596@2x.png) | The pointing-hand cursor ([`pointingHand`](./nscursor/pointinghand.md)) |
| ![resize-left cursor](https://developer.apple.com/tutorials/images/com.apple.appkit/media-2555601@2x.png) | The resize-left cursor ([`resizeLeft`](./nscursor/resizeleft.md)) |
| ![resize-right cursor](https://developer.apple.com/tutorials/images/com.apple.appkit/media-2555605@2x.png) | The resize-right cursor ([`resizeRight`](./nscursor/resizeright.md)) |
| ![resize-left-and-right cursor](https://developer.apple.com/tutorials/images/com.apple.appkit/media-2555610@2x.png) | The resize-left-and-right cursor ([`resizeLeftRight`](./nscursor/resizeleftright.md)) |
| ![resize-up cursor](https://developer.apple.com/tutorials/images/com.apple.appkit/media-2555619@2x.png) | The resize-up cursor ([`resizeUp`](./nscursor/resizeup.md)) |
| ![resize-down cursor](https://developer.apple.com/tutorials/images/com.apple.appkit/media-2555626@2x.png) | The resize-down cursor ([`resizeDown`](./nscursor/resizedown.md)) |
| ![resize-up-and-down cursor](https://developer.apple.com/tutorials/images/com.apple.appkit/media-2555629@2x.png) | The resize-up-and-down cursor ([`resizeUpDown`](./nscursor/resizeupdown.md)) |
| ![disappearing item cursor](https://developer.apple.com/tutorials/images/com.apple.appkit/media-2555632@2x.png) | The disappearing item cursor ([`disappearingItem`](./nscursor/disappearingitem.md)) |
| ![disappearing item cursor](https://developer.apple.com/tutorials/images/com.apple.appkit/media-2555638@2x.png) | The I-Beam text cursor for vertical layout ([`iBeamCursorForVerticalLayout`](./nscursor/ibeamcursorforverticallayout.md)). |
| ![operation not allowed cursor](https://developer.apple.com/tutorials/images/com.apple.appkit/media-2555643@2x.png) | The not allowed cursor ([`operationNotAllowed`](./nscursor/operationnotallowed.md)). |
| ![drag link cursor](https://developer.apple.com/tutorials/images/com.apple.appkit/media-2555647@2x.png) | The drag link cursor ([`dragLink`](./nscursor/draglink.md)). |
| ![drag copy cursor](https://developer.apple.com/tutorials/images/com.apple.appkit/media-2555652@2x.png) | The drag copy cursor ([`dragCopy`](./nscursor/dragcopy.md)). |
| ![contextual menu cursor](https://developer.apple.com/tutorials/images/com.apple.appkit/media-2555658@2x.png) | The contextual menu cursor ([`contextualMenu`](./nscursor/contextualmenu.md)). |

In macOS 10.3 and later, cursor size is no longer limited to 16 by 16 pixels.

##### Cursor rectangles

In Cocoa, you can change the currently displayed cursor based on the position of the mouse over one of your views. You might use this technique to provide visual feedback about what actions the user can take with the mouse. For example, you might display one of the resize cursors whenever the mouse moves over a portion of your view that acts as a custom resizing handle. To set this up, you associate a cursor object with one or more cursor rectangles in the view.

Cursor rectangles are a specialized type of tracking rectangles, which are used to monitor the mouse location in a view. Views implement cursor rectangles using tracking rectangles but provide methods for setting and refreshing cursor rectangles that are distinct from the generic tracking rectangle interface. For information on mouse-tracking and cursor-update events, see [`NSTrackingArea`](./nstrackingarea.md).

##### Balancing cursor hiding and unhiding

Each call to [`hide()`](./nscursor/hide%28%29.md) cursor must have a corresponding [`unhide()`](./nscursor/unhide%28%29.md) call. For example,

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
- [init(image: UIImage, hotSpot: NSPoint)](./nscursor/init%28image,hotspot%29.md)
  Initializes a cursor with the given image and hot spot.
- [init(coder: NSCoder)](./nscursor/init%28coder%29.md)
### Setting cursor attributes
- [var image: UIImage](./nscursor/image.md)
  The cursor’s image.
- [var hotSpot: NSPoint](./nscursor/hotspot.md)
  The position of the click location within the cursor.
- [class func hide()](./nscursor/hide%28%29.md)
  Makes the current cursor invisible.
- [class func unhide()](./nscursor/unhide%28%29.md)
  Negates an earlier call to [`hide()`](./nscursor/hide%28%29.md) by showing the current cursor.
- [class func setHiddenUntilMouseMoves(Bool)](./nscursor/sethiddenuntilmousemoves%28_%29.md)
  Sets whether the cursor is hidden until the mouse moves.
### Controlling which cursor is current
- [class func pop()](./nscursor/pop%28%29-swift.type.method.md)
  Pops the current cursor off the top of the stack.
- [func pop()](./nscursor/pop%28%29-swift.method.md)
  Sends a [`pop()`](./nscursor/pop%28%29-swift.type.method.md) message to the receiver’s class.
- [func push()](./nscursor/push%28%29.md)
  Puts the receiver on top of the cursor stack and makes it the current cursor.
- [func set()](./nscursor/set%28%29.md)
  Makes the receiver the current cursor.
### Retrieving cursor instances
- [class var current: NSCursor](./nscursor/current.md)
  Returns the application’s current cursor.
- [class var arrow: NSCursor](./nscursor/arrow.md)
  Returns the default cursor, the arrow cursor.
- [class var contextualMenu: NSCursor](./nscursor/contextualmenu.md)
  Returns the contextual menu system cursor.
- [class var closedHand: NSCursor](./nscursor/closedhand.md)
  Returns the closed-hand system cursor.
- [class var crosshair: NSCursor](./nscursor/crosshair.md)
  Returns the cross-hair system cursor.
- [class var disappearingItem: NSCursor](./nscursor/disappearingitem.md)
  Returns a cursor indicating that the current operation will result in a disappearing item.
- [class var dragCopy: NSCursor](./nscursor/dragcopy.md)
  Returns a cursor indicating that the current operation will result in a copy action.
- [class var dragLink: NSCursor](./nscursor/draglink.md)
  Returns a cursor indicating that the current operation will result in a link action.
- [class var iBeam: NSCursor](./nscursor/ibeam.md)
  Returns a cursor that looks like a capital I with a tiny crossbeam at its middle.
- [class var iBeamCursorForVerticalLayout: NSCursor](./nscursor/ibeamcursorforverticallayout.md)
  Returns the cursor for editing vertical layout text.
- [class var openHand: NSCursor](./nscursor/openhand.md)
  Returns the open-hand system cursor.
- [class var operationNotAllowed: NSCursor](./nscursor/operationnotallowed.md)
  Returns the operation not allowed cursor.
- [class var pointingHand: NSCursor](./nscursor/pointinghand.md)
  Returns the pointing-hand system cursor.
- [class var zoomIn: NSCursor](./nscursor/zoomin.md)
  Returns the zoom-in cursor.
- [class var zoomOut: NSCursor](./nscursor/zoomout.md)
  Returns the zoom-out cursor.
- [class var columnResize: NSCursor](./nscursor/columnresize.md)
  Returns the cursor for resizing a column (vertical divider) in either direction.
- [class func columnResize(directions: NSHorizontalDirection.Set) -> NSCursor](./nscursor/columnresize%28directions%29.md)
  Returns the cursor for resizing a column (vertical divider) in the specified direction.
- [class var rowResize: NSCursor](./nscursor/rowresize.md)
  Returns the cursor for resizing a row (horizontal divider) in either direction.
- [class func rowResize(directions: NSVerticalDirection.Set) -> NSCursor](./nscursor/rowresize%28directions%29.md)
  Returns the cursor for resizing a row (horizontal divider) in the specified direction.
- [class func frameResize(position: NSCursor.FrameResizePosition, directions: NSCursor.FrameResizeDirection.Set) -> NSCursor](./nscursor/frameresize%28position,directions%29.md)
  Returns the cursor for resizing a rectangular frame from the specified edge or corner.
- [NSCursor.FrameResizeDirection](./nscursor/frameresizedirection.md)
  The direction in which a rectangular frame can be resized.
### Constants
- [AppKit Versions for NSCursor Bug Fixes](./appkit-versions-for-nscursor-bug-fixes.md)
  The version of the AppKit framework containing a specific bug fix.
### Deprecated
- [Deprecated symbols](./nscursor-deprecated-symbols.md)
  Review symbols that are no longer in active development, and their recommended replacements.
### Type Methods
- [+ columnResizeCursorInDirections:](./nscursor/columnresizecursorindirections_.md)
  Returns the cursor for resizing a column (vertical divider) in the specified directions.
- [+ frameResizeCursorFromPosition:inDirections:](./nscursor/frameresizecursorfromposition_indirections_.md)
  Returns the cursor for resizing a rectangular frame from the specified edge or corner.
- [+ rowResizeCursorInDirections:](./nscursor/rowresizecursorindirections_.md)
  Returns the cursor for resizing a row (horizontal divider) in the specified directions.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [Copyable](../Swift/copyable.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Cursors
- [class NSTrackingArea](./nstrackingarea.md)
  A region of a view that generates mouse-tracking and cursor-update events when the pointer is over that region.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscursor)*