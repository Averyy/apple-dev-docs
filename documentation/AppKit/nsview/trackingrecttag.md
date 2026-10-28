# NSView.TrackingRectTag

**Framework**: AppKit  
**Kind**: typealias  
**Role**: Type Alias

This type describes the rectangle used to track the mouse.

**Availability**:
- macOS

## Declaration

```swift
typealias TrackingRectTag = Int
```

```c
typedef NSInteger NSTrackingRectTag;
```

## Discussion

If the value of this type is 0, it is invalid. See the methods [`addTrackingRect(_:owner:userData:assumeInside:)`](./addtrackingrect%28_,owner,userdata,assumeinside%29.md) and [`removeTrackingRect(_:)`](./removetrackingrect%28_%29.md).

## See Also

### Managing Tracking Rectangles
- [func addTrackingRect(NSRect, owner: Any, userData: UnsafeMutableRawPointer?, assumeInside: Bool) -> NSView.TrackingRectTag](./addtrackingrect%28_,owner,userdata,assumeinside%29.md)
  Establishes an area for tracking mouse-entered and mouse-exited events within the view and returns a tag that identifies the tracking rectangle.
- [func removeTrackingRect(NSView.TrackingRectTag)](./removetrackingrect%28_%29.md)
  Removes the tracking rectangle identified by a tag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/trackingrecttag)*