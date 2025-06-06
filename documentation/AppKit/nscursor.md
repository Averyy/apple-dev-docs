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
| ![arrow cursor](https://docs-assets.developer.apple.com/published/f5571bd2498dc6e9eff8f3279ff44d17/media-2555572%402x.png) | The arrow cursor ([`arrow`](nscursor/arrow.md)) |
| ![I-beam cursor](https://docs-assets.developer.apple.com/published/f4788c1bd99f401c0418cd180815c699/media-2555577%402x.png) | The I-beam cursor for indicating insertion points ([`iBeam`](nscursor/ibeam.md)) |
| ![cross-hair cursor](https://docs-assets.developer.apple.com/published/431226755082dd535f4f58efd8ea3b84/media-2555579%402x.png) | The cross-hair cursor ([`crosshair`](nscursor/crosshair.md)) |
| ![closed-hand cursor](https://docs-assets.developer.apple.com/published/c7130b0e393dbd35279cba83b5691030/media-2555583%402x.png) | The closed-hand cursor ([`closedHand`](nscursor/closedhand.md)) |
| ![open-hand cursor](https://docs-assets.developer.apple.com/published/0ce031acfefb1716cb08f75f937c3356/media-2555589%402x.png) | The open-hand cursor ([`openHand`](nscursor/openhand.md)) |
| ![pointing hand cursor](https://docs-assets.developer.apple.com/published/9925dce0ba11e526114196b82d29b3fb/media-2555596%402x.png) | The pointing-hand cursor ([`pointingHand`](nscursor/pointinghand.md)) |
| ![resize-left cursor](https://docs-assets.developer.apple.com/published/b3a4afd6c54285fe09e84c1512410595/media-2555601%402x.png) | The resize-left cursor ([`resizeLeft`](nscursor/resizeleft.md)) |
| ![resize-right cursor](https://docs-assets.developer.apple.com/published/c58a0e9fc1f26da597f22f22bb9bcedd/media-2555605%402x.png) | The resize-right cursor ([`resizeRight`](nscursor/resizeright.md)) |
| ![resize-left-and-right cursor](https://docs-assets.developer.apple.com/published/8c3cce19c90056e4cacadb9ab8eb68a0/media-2555610%402x.png) | The resize-left-and-right cursor ([`resizeLeftRight`](nscursor/resizeleftright.md)) |
| ![resize-up cursor](https://docs-assets.developer.apple.com/published/4be1d56a99fc6a8db1290e4572015d31/media-2555619%402x.png) | The resize-up cursor ([`resizeUp`](nscursor/resizeup.md)) |
| ![resize-down cursor](https://docs-assets.developer.apple.com/published/190389a3c980efc8995d8a147e1d9c96/media-2555626%402x.png) | The resize-down cursor ([`resizeDown`](nscursor/resizedown.md)) |
| ![resize-up-and-down cursor](https://docs-assets.developer.apple.com/published/0fb307eaa6ee6a028d3b31c4ceed9ee9/media-2555629%402x.png) | The resize-up-and-down cursor ([`resizeUpDown`](nscursor/resizeupdown.md)) |
| ![disappearing item cursor](https://docs-assets.developer.apple.com/published/f42a29763b234d05b677eb7b0650e463/media-2555632%402x.png) | The disappearing item cursor ([`disappearingItem`](nscursor/disappearingitem.md)) |
| ![disappearing item cursor](https://docs-assets.developer.apple.com/published/d5d3477930b200b78572b916906d9fdc/media-2555638%402x.png) | The I-Beam text cursor for vertical layout ([`iBeamCursorForVerticalLayout`](nscursor/ibeamcursorforverticallayout.md)). |
| ![None](https://docs-assets.developer.apple.com/published/4a3179b5bcb997a39c6c7f665e3efc06/media-2555643%402x.png) | The not allowed cursor ([`operationNotAllowed`](nscursor/operationnotallowed.md)). |
| ![None](https://docs-assets.developer.apple.com/published/e8b26cc0d5f1ac1ee3fff76364451816/media-2555647%402x.png) | The drag link cursor ([`dragLink`](nscursor/draglink.md)). |
| ![None](https://docs-assets.developer.apple.com/published/257116379198465aa14194a6301dc130/media-2555652%402x.png) | The drag copy cursor ([`dragCopy`](nscursor/dragcopy.md)). |
| ![None](https://docs-assets.developer.apple.com/published/2a1dff1bf1637a6868e2ba322f2726f2/media-2555658%402x.png) | The contextual menu cursor ([`contextualMenu`](nscursor/contextualmenu.md)). |

In macOS 10.3 and later, cursor size is no longer limited to 16 by 16 pixels.

##### Cursor Rectangles

In Cocoa, you can change the currently displayed cursor based on the position of the mouse over one of your views. You might use this technique to provide visual feedback about what actions the user can take with the mouse. For example, you might display one of the resize cursors whenever the mouse moves over a portion of your view that acts as a custom resizing handle. To set this up, you associate a cursor object with one or more cursor rectangles in the view.

Cursor rectangles are a specialized type of tracking rectangles, which are used to monitor the mouse location in a view. Views implement cursor rectangles using tracking rectangles but provide methods for setting and refreshing cursor rectangles that are distinct from the generic tracking rectangle interface. For information on how to set up cursor rectangles, see [`Mouse-Tracking and Cursor-Update Events`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/EventOverview/MouseTrackingEvents/MouseTrackingEvents.html#//apple_ref/doc/uid/10000060i-CH11).

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

### Initializing a New Cursor
- [init(image: UIImage, hotSpot: NSPoint)](nscursor/init(image:hotspot:).md)
  Initializes a cursor with the given image and hot spot.
- [convenience init(image: NSImage, foregroundColorHint: NSColor?, backgroundColorHint: NSColor?, hotSpot: NSPoint)](nscursor/init(image:foregroundcolorhint:backgroundcolorhint:hotspot:).md)
  Initializes the cursor with the specified image and hot spot.
### Setting Cursor Attributes
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
### Controlling Which Cursor Is Current
- [class func pop()](nscursor/pop-swift.type.method.md)
  Pops the current cursor off the top of the stack.
- [func pop()](nscursor/pop-swift.method.md)
  Sends a [`pop()`](nscursor/pop()-swift.type.method.md) message to the receiver’s class.
- [func push()](nscursor/push.md)
  Puts the receiver on top of the cursor stack and makes it the current cursor.
- [func set()](nscursor/set.md)
  Makes the receiver the current cursor.
- [func mouseEntered(with: NSEvent)](nscursor/mouseentered(with:).md)
  Automatically sent to the receiver when the cursor enters a cursor rectangle owned by the receiver.
- [func setOnMouseEntered(Bool)](nscursor/setonmouseentered(_:).md)
  Specifies whether the receiver accepts [`mouseEntered(with:)`](nscursor/mouseentered(with:).md) events.
- [var isSetOnMouseEntered: Bool](nscursor/issetonmouseentered.md)
  A Boolean value indicating whether the receiver becomes current on receiving a [`mouseEntered(with:)`](nscursor/mouseentered(with:).md) message.
- [func mouseExited(with: NSEvent)](nscursor/mouseexited(with:).md)
  Automatically sent to the receiver when the cursor exits a cursor rectangle owned by the receiver.
- [func setOnMouseExited(Bool)](nscursor/setonmouseexited(_:).md)
  Sets whether the receiver accepts [`mouseExited(with:)`](nscursor/mouseexited(with:).md) events.
- [var isSetOnMouseExited: Bool](nscursor/issetonmouseexited.md)
  A Boolean value indicating whether the receiver becomes current when it receives a [`mouseExited(with:)`](nscursor/mouseexited(with:).md) message.
### Retrieving Cursor Instances
- [class var current: NSCursor](nscursor/current.md)
  Returns the application’s current cursor.
- [class var currentSystem: NSCursor?](nscursor/currentsystem.md)
  Returns the current system cursor.
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
- [class var openHand: NSCursor](nscursor/openhand.md)
  Returns the open-hand system cursor.
- [class var operationNotAllowed: NSCursor](nscursor/operationnotallowed.md)
  Returns the operation not allowed cursor.
- [class var pointingHand: NSCursor](nscursor/pointinghand.md)
  Returns the pointing-hand system cursor.
- [class var resizeDown: NSCursor](nscursor/resizedown.md)
  Returns the resize-down system cursor.
- [class var resizeLeft: NSCursor](nscursor/resizeleft.md)
  Returns the resize-left system cursor.
- [class var resizeLeftRight: NSCursor](nscursor/resizeleftright.md)
  Returns the resize-left-and-right system cursor.
- [class var resizeRight: NSCursor](nscursor/resizeright.md)
  Returns the resize-right system cursor.
- [class var resizeUp: NSCursor](nscursor/resizeup.md)
  Returns the resize-up system cursor.
- [class var resizeUpDown: NSCursor](nscursor/resizeupdown.md)
  Returns the resize-up-and-down system cursor.
- [class var iBeamCursorForVerticalLayout: NSCursor](nscursor/ibeamcursorforverticallayout.md)
  Returns the cursor for editing vertical layout text.
### Constants
- [AppKit Versions for NSCursor Bug Fixes](appkit-versions-for-nscursor-bug-fixes.md)
  The version of the AppKit framework containing a specific bug fix.
### Initializers
- [init(coder: NSCoder)](nscursor/init(coder:).md)
### Type Properties
- [class var columnResize: NSCursor](nscursor/columnresize.md)
  Returns the cursor for resizing a column (vertical divider) in either direction.
- [class var rowResize: NSCursor](nscursor/rowresize.md)
  Returns the cursor for resizing a row (horizontal divider) in either direction.
- [class var zoomIn: NSCursor](nscursor/zoomin.md)
  Returns the zoom-in cursor.
- [class var zoomOut: NSCursor](nscursor/zoomout.md)
  Returns the zoom-out cursor.
### Type Methods
- [class func columnResize(directions: NSHorizontalDirection.Set) -> NSCursor](nscursor/columnresize(directions:).md)
  Returns the cursor for resizing a column (vertical divider) in the specified direction.
- [class func frameResize(position: NSCursor.FrameResizePosition, directions: NSCursor.FrameResizeDirection.Set) -> NSCursor](nscursor/frameresize(position:directions:).md)
  Returns the cursor for resizing a rectangular frame from the specified edge or corner.
- [class func javaBusyButClickable() -> NSCursor!](nscursor/javabusybutclickable.md)
- [class func javaMove() -> NSCursor!](nscursor/javamove.md)
- [class func javaResizeNE() -> NSCursor!](nscursor/javaresizene.md)
- [class func javaResizeNW() -> NSCursor!](nscursor/javaresizenw.md)
- [class func javaResizeSE() -> NSCursor!](nscursor/javaresizese.md)
- [class func javaResizeSW() -> NSCursor!](nscursor/javaresizesw.md)
- [class func javaSetAllowsCursorSet(inBackground: Bool)](nscursor/javasetallowscursorset(inbackground:).md)
- [class func rowResize(directions: NSVerticalDirection.Set) -> NSCursor](nscursor/rowresize(directions:).md)
  Returns the cursor for resizing a row (horizontal divider) in the specified direction.
### Enumerations
- [NSCursor.FrameResizeDirection](nscursor/frameresizedirection.md)
  The direction in which a rectangular frame can be resized.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [class NSTrackingArea](nstrackingarea.md)
  A region of a view that generates mouse-tracking and cursor-update events when the pointer is over that region.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscursor)*