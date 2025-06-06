# removeTrackingRect(_:)

**Framework**: AppKit  
**Kind**: method

Removes the tracking rectangle identified by a tag.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func removeTrackingRect(_ tag: NSView.TrackingRectTag)
```

## Parameters

- `tag`: An integer value identifying a tracking rectangle. It was returned by a previously sent   message.

## See Also

- [func removeTrackingArea(NSTrackingArea)](nsview/removetrackingarea(_:).md)
  Removes a given tracking area from the view.
- [func addTrackingRect(NSRect, owner: Any, userData: UnsafeMutableRawPointer?, assumeInside: Bool) -> NSView.TrackingRectTag](nsview/addtrackingrect(_:owner:userdata:assumeinside:).md)
  Establishes  an area for tracking mouse-entered and mouse-exited events within the view and returns a tag that identifies the tracking rectangle.
- [typealias TrackingRectTag](nsview/trackingrecttag.md)
  This type describes the rectangle used to track the mouse.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/removetrackingrect(_:))*