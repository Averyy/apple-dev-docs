# setBoundsOrigin(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Sets the origin of the view’s bounds rectangle to a specified point.

**Availability**:
- macOS

## Declaration

```swift
func setBoundsOrigin(_ newOrigin: NSPoint)
```

```objc
- (void) setBoundsOrigin:(NSPoint) newOrigin;
```

#### Discussion

In setting the new bounds origin, this method effectively shifts the view’s coordinate system so `newOrigin` lies at the origin of the view’s frame rectangle. It neither redisplays the view nor marks it as needing display. Set the [`needsDisplay`](./needsdisplay.md) property to [`true`](../../Swift/true.md) when you want the view to be redisplayed.

This method posts an [`boundsDidChangeNotification`](./boundsdidchangenotification.md) to the default notification center if the view is configured to do so.

After calling this method, `NSView` creates an internal transform (or appends these changes to an existing internal transform) to convert from frame coordinates to bounds coordinates in your view. As long as the width-to-height ratio of the two coordinate systems remains the same, your content appears normal. If the ratios differ, your content may appear skewed.

## Parameters

- `newOrigin`: A point specifying the new bounds origin of the view.

## See Also

### Related Documentation
- [func translateOrigin(to: NSPoint)](./translateorigin%28to%29.md)
  Translates the view’s coordinate system so that its origin moves to a new location.
### Modifying the bounds rectangle
- [var bounds: NSRect](./bounds.md)
  The view’s bounds rectangle, which expresses its location and size in its own coordinate system.
- [func setBoundsSize(NSSize)](./setboundssize%28_%29.md)
  Sets the size of the view’s bounds rectangle to specified dimensions, inversely scaling its coordinate system relative to its frame rectangle.
- [var boundsRotation: CGFloat](./boundsrotation.md)
  The angle of rotation, measured in degrees, applied to the view’s bounds rectangle relative to its frame rectangle.
- [class let boundsDidChangeNotification: NSNotification.Name](./boundsdidchangenotification.md)
  A notification that posts when the view’s bounds rectangle changes to a new value independently of the frame rectangle.
- [NSView.BoundsDidChangeMessage](./boundsdidchangemessage.md)
- [var postsBoundsChangedNotifications: Bool](./postsboundschangednotifications.md)
  A Boolean value indicating whether the view posts notifications when its bounds rectangle changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/setboundsorigin(_:))*