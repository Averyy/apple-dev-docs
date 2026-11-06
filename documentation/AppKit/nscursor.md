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

## Overview

The following table shows and describes the system cursors, and indicates the class method for obtaining them:

| Cursor | Description |
| --- | --- |
| ![arrow cursor](https://developer.apple.com/tutorials/images/com.apple.appkit/nscursor-arrow@2x.png) | The arrow cursor ([`arrow`](./nscursor/arrow.md)) |
| ![I-beam cursor](https://developer.apple.com/tutorials/images/com.apple.appkit/nscursor-horizontal-i-beam@2x.png) | The I-beam cursor for indicating insertion points ([`iBeam`](./nscursor/ibeam.md)) |
| ![cross-hair cursor](https://developer.apple.com/tutorials/images/com.apple.appkit/nscursor-crosshair@2x.png) | The cross-hair cursor ([`crosshair`](./nscursor/crosshair.md)) |
| ![closed-hand cursor](https://developer.apple.com/tutorials/images/com.apple.appkit/nscursor-closed-hand@2x.png) | The closed-hand cursor ([`closedHand`](./nscursor/closedhand.md)) |
| ![open-hand cursor](https://developer.apple.com/tutorials/images/com.apple.appkit/nscursor-open-hand@2x.png) | The open-hand cursor ([`openHand`](./nscursor/openhand.md)) |
| ![pointing hand cursor](https://developer.apple.com/tutorials/images/com.apple.appkit/nscursor-pointing-hand@2x.png) | The pointing-hand cursor ([`pointingHand`](./nscursor/pointinghand.md)) |
| ![disappearing item cursor](https://developer.apple.com/tutorials/images/com.apple.appkit/nscursor-disappearing-item@2x.png) | The disappearing item cursor ([`disappearingItem`](./nscursor/disappearingitem.md)) |
| ![I-beam cursor for vertical layout](https://developer.apple.com/tutorials/images/com.apple.appkit/nscursor-vertical-i-beam@2x.png) | The I-beam text cursor for vertical layout ([`iBeamCursorForVerticalLayout`](./nscursor/ibeamcursorforverticallayout.md)). |
| ![operation not allowed cursor](https://developer.apple.com/tutorials/images/com.apple.appkit/nscursor-operation-not-allowed@2x.png) | The not allowed cursor ([`operationNotAllowed`](./nscursor/operationnotallowed.md)). |
| ![drag link cursor](https://developer.apple.com/tutorials/images/com.apple.appkit/nscursor-drag-link@2x.png) | The drag link cursor ([`dragLink`](./nscursor/draglink.md)). |
| ![drag copy cursor](https://developer.apple.com/tutorials/images/com.apple.appkit/nscursor-drag-copy@2x.png) | The drag copy cursor ([`dragCopy`](./nscursor/dragcopy.md)). |
| ![contextual menu cursor](https://developer.apple.com/tutorials/images/com.apple.appkit/nscursor-contextual-menu@2x.png) | The contextual menu cursor ([`contextualMenu`](./nscursor/contextualmenu.md)). |
| ![zoom-in cursor](https://developer.apple.com/tutorials/images/com.apple.appkit/nscursor-zoom-in@2x.png) | The zoom-in cursor ([`zoomIn`](./nscursor/zoomin.md)). |
| ![zoom-out cursor](https://developer.apple.com/tutorials/images/com.apple.appkit/nscursor-zoom-out@2x.png) | The zoom-out cursor ([`zoomOut`](./nscursor/zoomout.md)). |
| ![column-resize cursor](https://developer.apple.com/tutorials/images/com.apple.appkit/nscursor-resize-left-right@2x.png) | The column-resize cursor, for a vertical divider that can move left or right ([`columnResize`](./nscursor/columnresize.md)). |
| ![column-resize-left cursor](https://developer.apple.com/tutorials/images/com.apple.appkit/nscursor-resize-left@2x.png) | The column-resize cursor, for a divider that can move only left ([`columnResize(directions:)`](./nscursor/columnresize%28directions%29.md) passing [`NSHorizontalDirection.left`](./nshorizontaldirection/left.md)). |
| ![column-resize-right cursor](https://developer.apple.com/tutorials/images/com.apple.appkit/nscursor-resize-right@2x.png) | The column-resize cursor, for a divider that can move only right ([`columnResize(directions:)`](./nscursor/columnresize%28directions%29.md) passing [`NSHorizontalDirection.right`](./nshorizontaldirection/right.md)). |
| ![row-resize cursor](https://developer.apple.com/tutorials/images/com.apple.appkit/nscursor-resize-up-down@2x.png) | The row-resize cursor, for a horizontal divider that can move up or down ([`rowResize`](./nscursor/rowresize.md)). |
| ![row-resize-up cursor](https://developer.apple.com/tutorials/images/com.apple.appkit/nscursor-resize-up@2x.png) | The row-resize cursor, for a divider that can move only up ([`rowResize(directions:)`](./nscursor/rowresize%28directions%29.md) passing [`NSVerticalDirection.up`](./nsverticaldirection/up.md)). |
| ![row-resize-down cursor](https://developer.apple.com/tutorials/images/com.apple.appkit/nscursor-resize-down@2x.png) | The row-resize cursor, for a divider that can move only down ([`rowResize(directions:)`](./nscursor/rowresize%28directions%29.md) passing [`NSVerticalDirection.down`](./nsverticaldirection/down.md)). |

To get a cursor for resizing a rectangular frame, use [`frameResize(position:directions:)`](./nscursor/frameresize%28position,directions%29.md). The `position` parameter selects the edge or corner of the frame, and the `directions` parameter is a set that specifies whether that edge or corner can resize outward, away from the center of the frame, inward, toward the center, or both. The cursor changes to show the allowed directions. The following table shows each variation for the top-left corner:

| Cursor | Description |
| --- | --- |
| ![frame-resize cursor, top-left corner, outward](https://developer.apple.com/tutorials/images/com.apple.appkit/nscursor-northwest@2x.png) | The frame-resize cursor for the top-left corner of a frame that can resize outward, away from its center. For example, `NSCursor.frameResize(position: .topLeft, directions: .outward)` |
| ![frame-resize cursor, top-left corner, inward](https://developer.apple.com/tutorials/images/com.apple.appkit/nscursor-southeast@2x.png) | The frame-resize cursor for the top-left corner of a frame that can resize inward, toward its center. For example, `NSCursor.frameResize(position: .topLeft, directions: .inward)` |
| ![frame-resize cursor, top-left corner, inward and outward](https://developer.apple.com/tutorials/images/com.apple.appkit/nscursor-northwest-southeast@2x.png) | The frame-resize cursor for the top-left corner of a frame that can resize either inward or outward. For example, `NSCursor.frameResize(position: .topLeft, directions: .all)` |

### Cursor rectangles

You can change the currently displayed cursor based on the position of the mouse over one of your views. You might use this technique to provide visual feedback about what actions the user can take with the mouse. For example, you might display one of the resize cursors whenever the mouse moves over a portion of your view that acts as a custom resizing handle. To set this up, you associate a cursor object with one or more cursor rectangles in the view.

Cursor rectangles are a specialized type of tracking rectangles, which monitor the mouse location in a view. Views implement cursor rectangles using tracking rectangles but provide methods for setting and refreshing cursor rectangles that are distinct from the generic tracking rectangle interface. For information on mouse-tracking and cursor-update events, see [`NSTrackingArea`](./nstrackingarea.md).

### Balancing cursor hiding and unhiding

Each call to [`hide()`](./nscursor/hide%28%29.md) must have a corresponding [`unhide()`](./nscursor/unhide%28%29.md) call. For example, the following code leaves the cursor hidden because the `hide` and `unhide` method invocations don’t balance.

**Swift**:

```swift
NSCursor.hide()
NSCursor.hide()
// ...
NSCursor.unhide()
```

**Objective-C**:

```objc
[NSCursor hide];
[NSCursor hide];
// ...
[NSCursor unhide];
```

Instead, balance the method calls, as in the following example:

**Swift**:

```swift
NSCursor.hide()
NSCursor.hide()
// ...
NSCursor.unhide()
NSCursor.unhide()
```

**Objective-C**:

```objc
[NSCursor hide];
[NSCursor hide];
// ...
[NSCursor unhide];
[NSCursor unhide];
```

In the example above, there are corresponding cursor `hide` and `unhide` calls to hide or show the cursor.

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
  Returns the cursor for resizing a column (vertical divider) in the specified directions.
- [class var rowResize: NSCursor](./nscursor/rowresize.md)
  Returns the cursor for resizing a row (horizontal divider) in either direction.
- [class func rowResize(directions: NSVerticalDirection.Set) -> NSCursor](./nscursor/rowresize%28directions%29.md)
  Returns the cursor for resizing a row (horizontal divider) in the specified directions.
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