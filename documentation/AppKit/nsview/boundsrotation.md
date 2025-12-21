# boundsRotation

**Framework**: AppKit  
**Kind**: property

The angle of rotation, measured in degrees, applied to the view’s bounds rectangle relative to its frame rectangle.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var boundsRotation: CGFloat { get set }
```

#### Discussion

Positive values indicate counterclockwise rotation. Negative values indicate clockwise rotation. Rotation is performed around the coordinate system origin, (0.0, 0.0), which need not coincide with that of the frame rectangle or the bounds rectangle. Changing the value of this property neither redisplays the view nor marks it as needing display. Set the [`needsDisplay`](nsview/needsdisplay.md) property to [`true`](https://developer.apple.com/documentation/Swift/true) when you want the view to be redisplayed.

Bounds rotation affects the orientation of the drawing within the view object’s frame rectangle, but not the orientation of the frame rectangle itself. Also, for a rotated bounds rectangle to enclose all the visible areas of its view object—that is, to guarantee coverage over the frame rectangle—it must also contain some areas that aren’t visible. This can cause unnecessary drawing to be requested, which may affect performance. It may be better in many cases to rotate the coordinate system in the [`draw(_:)`](nsview/draw(_:).md) method rather than use this method.

After changing the value of this property, the view creates an internal transform (or appends these changes to an existing internal transform) to convert from frame coordinates to bounds coordinates in your view. As long as the width-to-height ratio of the two coordinate systems remains the same, your content appears normal. If the ratios differ, your content may appear skewed.

Changing the value of this property results in the posting of an [`boundsDidChangeNotification`](nsview/boundsdidchangenotification.md) to the default notification center if the view is configured to do so.

## See Also

- [func rotate(byDegrees: CGFloat)](nsview/rotate(bydegrees:).md)
  Rotates the view’s bounds rectangle by a specified degree value around the origin of the coordinate system, (0.0, 0.0).
- [var bounds: NSRect](nsview/bounds.md)
  The view’s bounds rectangle, which expresses its location and size in its own coordinate system.
- [func setBoundsOrigin(NSPoint)](nsview/setboundsorigin(_:).md)
  Sets the origin of the view’s bounds rectangle to a specified point.
- [func setBoundsSize(NSSize)](nsview/setboundssize(_:).md)
  Sets the size of the view’s bounds rectangle to specified dimensions, inversely scaling its coordinate system relative to its frame rectangle.
- [class let boundsDidChangeNotification: NSNotification.Name](nsview/boundsdidchangenotification.md)
  A notification that posts when the view’s bounds rectangle changes to a new value independently of the frame rectangle.
- [var postsBoundsChangedNotifications: Bool](nsview/postsboundschangednotifications.md)
  A Boolean value indicating whether the view posts notifications when its bounds rectangle changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/boundsrotation)*