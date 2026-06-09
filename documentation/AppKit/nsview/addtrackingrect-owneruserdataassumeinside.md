# addTrackingRect(_:owner:userData:assumeInside:)

**Framework**: AppKit  
**Kind**: method

Establishes an area for tracking mouse-entered and mouse-exited events within the view and returns a tag that identifies the tracking rectangle.

**Availability**:
- macOS ?+

## Declaration

```swift
func addTrackingRect(_ rect: NSRect, owner: Any, userData data: UnsafeMutableRawPointer?, assumeInside flag: Bool) -> NSView.TrackingRectTag
```

#### Return Value

A tag that identifies the tracking rectangle. It is stored in the associated [`NSEvent`](nsevent.md) objects and can be used to remove the tracking rectangle.

#### Discussion

Tracking rectangles provide a general mechanism that can be used to trigger actions based on the cursor location (for example, a status bar or hint field that provides information on the item the cursor lies over). To simply change the cursor over a particular area, use [`addCursorRect(_:cursor:)`](nsview/addcursorrect(_:cursor:).md). If you must use tracking rectangles to change the cursor, the [`NSCursor`](nscursor.md) class specification describes the additional methods that must be invoked to change cursors by using tracking rectangles.

In macOS 10.5 and later, tracking areas provide a greater range of functionality (see [`addTrackingArea(_:)`](nsview/addtrackingarea(_:).md)).

## Parameters

- `rect`: A rectangle that defines a region of the view for tracking mouse-entered and mouse-exited events.
- `owner`: The object that gets sent the event messages. It can be the view itself or some other object (such as an NSCursor or a custom drawing tool object), as long as it responds to both [`mouseEntered(with:)`](nsresponder/mouseentered(with:).md) and [`mouseExited(with:)`](nsresponder/mouseexited(with:).md).
- `data`: Data stored in the [`NSEvent`](nsevent.md) object for each tracking event.
- `flag`: If [`true`](https://developer.apple.com/documentation/Swift/true), the first event will be generated when the cursor leaves `aRect`, regardless if the cursor is inside `aRect` when the tracking rectangle is added. If [`false`](https://developer.apple.com/documentation/Swift/false) the first event will be generated when the cursor leaves `aRect` if the cursor is initially inside `aRect`, or when the cursor enters `aRect` if the cursor is initially outside `aRect`.  You usually want to set this flag to [`false`](https://developer.apple.com/documentation/Swift/false).

## See Also

- [func addTrackingArea(NSTrackingArea)](nsview/addtrackingarea(_:).md)
  Adds a given tracking area to the view.
- [var userData: UnsafeMutableRawPointer?](nsevent/userdata.md)
  The data associated with a mouse-tracking event.
- [func removeTrackingRect(NSView.TrackingRectTag)](nsview/removetrackingrect(_:).md)
  Removes the tracking rectangle identified by a tag.
- [typealias TrackingRectTag](nsview/trackingrecttag.md)
  This type describes the rectangle used to track the mouse.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/addtrackingrect(_:owner:userdata:assumeinside:))*