# init(rect:options:owner:userInfo:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Initializes and returns an object defining a region of a view to receive mouse-tracking events, mouse-moved events, cursor-update events, or possibly all these events.

**Availability**:
- macOS 10.5+

## Declaration

```swift
init(rect: NSRect, options: NSTrackingArea.Options = [], owner: Any?, userInfo: [AnyHashable : Any]? = nil)
```

```objc
- (instancetype) initWithRect:(NSRect) rect options:(NSTrackingAreaOptions) options owner:(id) owner userInfo:(NSDictionary<id,id> *) userInfo;
```

## Return Value

The newly-initialized tracking area object.

## Discussion

After creating and initializing an `NSTrackingArea` object with this method, you must add it to a target view using the [`addTrackingArea(_:)`](../nsview/addtrackingarea%28_%29.md) method. When changes in the view require changes in the geometry of its tracking areas, the Application Kit invokes [`updateTrackingAreas()`](../nsview/updatetrackingareas%28%29.md). The view should implement this method to replace the current `NSTrackingArea` object with one with a recomputed area.

### Special Considerations

Beginning with OS X v10.5, the [`init(rect:options:owner:userInfo:)`](./init%28rect,options,owner,userinfo%29.md), along with the [`addTrackingArea(_:)`](../nsview/addtrackingarea%28_%29.md) method of `NSView`, replace the `NSView` method [`addTrackingRect(_:owner:userData:assumeInside:)`](../nsview/addtrackingrect%28_,owner,userdata,assumeinside%29.md).

## Parameters

- `rect`: A rectangle that defines a region of a target view, in the view’s coordinate system, for tracking events related to mouse tracking and cursor updating. The specified rectangle should not exceed the view’s bounds rectangle.
- `options`: One or more constants that specify the type of tracking area, the situations when the area is active, and special behaviors of the tracking area. See the description of [`NSTrackingArea.Options`](./options-swift.struct.md) and related constants for details. You must specify one or more options for the initialized object for the type of tracking area and for when the tracking area is active; zero is not a valid value.
- `owner`: The object to receive the requested mouse-tracking, mouse-moved, or cursor-update messages. It does not necessarily have to be the view associated with the created `NSTrackingArea` object, but should be an object capable of responding to the `NSResponder` methods [`mouseEntered(with:)`](../nsresponder/mouseentered%28with%29.md), [`mouseExited(with:)`](../nsresponder/mouseexited%28with%29.md), [`mouseMoved(with:)`](../nsresponder/mousemoved%28with%29.md), and [`cursorUpdate(with:)`](../nsresponder/cursorupdate%28with%29.md).
- `userInfo`: A dictionary containing arbitrary data for each mouse-entered, mouse-exited, and cursor-update event. When handling such an event you can obtain the dictionary by sending [`userData`](../nsevent/userdata.md) to the `NSEvent` object. (The dictionary is not available for mouse-moved events.) This parameter may be `nil`.

## See Also

### Related Documentation
- [var userInfo: [AnyHashable : Any]?](./userinfo.md)
  The dictionary containing the data associated with the receiver when it was created.
- [var rect: NSRect](./rect.md)
  The rectangle defining the area encompassed by the receiver.
- [var owner: AnyObject?](./owner.md)
  The object owning the receiver, which is the recipient of mouse-tracking, mouse-movement, and cursor-update messages.
- [var options: NSTrackingArea.Options](./options-swift.property.md)
  The options specified for the receiver.
- [class NSTrackingArea](../nstrackingarea.md)
  A region of a view that generates mouse-tracking and cursor-update events when the pointer is over that region.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstrackingarea/init(rect:options:owner:userinfo:))*