# translateOrigin(to:)

**Framework**: AppKit  
**Kind**: method

Translates the view’s coordinate system so that its origin moves to a new location.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func translateOrigin(to translation: NSPoint)
```

#### Discussion

In the process, the origin of the view’s bounds rectangle is shifted by (`–translation.x`, `–translation.y`). This method neither redisplays the view nor marks it as needing display. You must do this yourself by calling the  [`display()`](nsview/display().md) method or setting the [`needsDisplay`](nsview/needsdisplay.md) property.

Note the difference between this method and setting the bounds origin. Translation effectively moves the image inside the bounds rectangle, while setting the bounds origin effectively moves the rectangle over the image. The two are in a sense inverse, although translation is cumulative, and setting the bounds origin is absolute.

This method posts an [`boundsDidChangeNotification`](nsview/boundsdidchangenotification.md) to the default notification center if the view is configured to do so.

## Parameters

- `translation`: A point that specifies the new origin.

## See Also

- [func setBoundsOrigin(NSPoint)](nsview/setboundsorigin(_:).md)
  Sets the origin of the view’s bounds rectangle to a specified point.
- [var bounds: NSRect](nsview/bounds.md)
  The view’s bounds rectangle, which expresses its location and size in its own coordinate system.
- [func scaleUnitSquare(to: NSSize)](nsview/scaleunitsquare(to:).md)
  Scales the view’s coordinate system so that the unit square scales to the specified dimensions.
- [func rotate(byDegrees: CGFloat)](nsview/rotate(bydegrees:).md)
  Rotates the view’s bounds rectangle by a specified degree value around the origin of the coordinate system, (0.0, 0.0).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/translateorigin(to:))*