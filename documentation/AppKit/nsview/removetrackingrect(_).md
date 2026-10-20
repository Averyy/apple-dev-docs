# removeTrackingRect(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Removes the tracking rectangle identified by a tag.

**Availability**:
- macOS

## Declaration

```swift
func removeTrackingRect(_ tag: NSView.TrackingRectTag)
```

```objc
- (void) removeTrackingRect:(NSTrackingRectTag) tag;
```

## Parameters

- `tag`: An integer value identifying a tracking rectangle. It was returned by a previously sent [`addTrackingRect(_:owner:userData:assumeInside:)`](./addtrackingrect%28_,owner,userdata,assumeinside%29.md) message.

## See Also

### Related Documentation
- [func removeTrackingArea(NSTrackingArea)](./removetrackingarea%28_%29.md)
  Removes a given tracking area from the view.
### Managing Tracking Rectangles
- [func addTrackingRect(NSRect, owner: Any, userData: UnsafeMutableRawPointer?, assumeInside: Bool) -> NSView.TrackingRectTag](./addtrackingrect%28_,owner,userdata,assumeinside%29.md)
  Establishes an area for tracking mouse-entered and mouse-exited events within the view and returns a tag that identifies the tracking rectangle.
- [typealias TrackingRectTag](./trackingrecttag.md)
  This type describes the rectangle used to track the mouse.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/removetrackingrect(_:))*