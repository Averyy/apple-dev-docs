# NSView.TrackingRectTag

**Framework**: AppKit  
**Kind**: typealias

This type describes the rectangle used to track the mouse.

**Availability**:
- macOS ?+

## Declaration

```swift
typealias TrackingRectTag = Int
```

#### Discussion

If the value of this type is 0, it is invalid. See the methods [`addTrackingRect(_:owner:userData:assumeInside:)`](nsview/addtrackingrect(_:owner:userdata:assumeinside:).md) and [`removeTrackingRect(_:)`](nsview/removetrackingrect(_:).md).

## See Also

- [func addTrackingRect(NSRect, owner: Any, userData: UnsafeMutableRawPointer?, assumeInside: Bool) -> NSView.TrackingRectTag](nsview/addtrackingrect(_:owner:userdata:assumeinside:).md)
  Establishes  an area for tracking mouse-entered and mouse-exited events within the view and returns a tag that identifies the tracking rectangle.
- [func removeTrackingRect(NSView.TrackingRectTag)](nsview/removetrackingrect(_:).md)
  Removes the tracking rectangle identified by a tag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/trackingrecttag)*