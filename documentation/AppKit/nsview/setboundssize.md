# setBoundsSize(_:)

**Framework**: AppKit  
**Kind**: method

Sets the size of the view’s bounds rectangle to specified dimensions, inversely scaling its coordinate system relative to its frame rectangle.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func setBoundsSize(_ newSize: NSSize)
```

#### Discussion

For example, a view object with a frame size of (100.0, 100.0) and a bounds size of (200.0, 100.0) draws half as wide along the x axis. This method neither redisplays the view nor marks it as needing display. Set the [`needsDisplay`](nsview/needsdisplay.md) property to [`true`](https://developer.apple.com/documentation/swift/true) when you want the view to be redisplayed.

This method posts an [`boundsDidChangeNotification`](nsview/boundsdidchangenotification.md) to the default notification center if the view is configured to do so.

After calling this method, `NSView` creates an internal transform (or appends these changes to an existing internal transform) to convert from frame coordinates to bounds coordinates in your view. As long as the width-to-height ratio of the two coordinate systems remains the same, your content appears normal. If the ratios differ, your content may appear skewed.

## Parameters

- `newSize`: An   structure specifying the new width and height of the view’s bounds rectangle.

## See Also

- [var bounds: NSRect](nsview/bounds.md)
  The view’s bounds rectangle, which expresses its location and size in its own coordinate system.
- [func setBoundsOrigin(NSPoint)](nsview/setboundsorigin(_:).md)
  Sets the origin of the view’s bounds rectangle to a specified point.
- [var boundsRotation: CGFloat](nsview/boundsrotation.md)
  The angle of rotation, measured in degrees, applied to the view’s bounds rectangle relative to its frame rectangle.
- [class let boundsDidChangeNotification: NSNotification.Name](nsview/boundsdidchangenotification.md)
  Posted whenever the `NSView`‘s bounds rectangle changes to a new value independently of the frame rectangle, but only when the view’s [`postsBoundsChangedNotifications`](nsview/postsboundschangednotifications.md) property is [`true`](https://developer.apple.com/documentation/swift/true).
- [var postsBoundsChangedNotifications: Bool](nsview/postsboundschangednotifications.md)
  A Boolean value indicating whether the view posts notifications when its bounds rectangle changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/setboundssize(_:))*