# translateOrigin(to:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Translates the view’s coordinate system so that its origin moves to a new location.

**Availability**:
- macOS

## Declaration

```swift
func translateOrigin(to translation: NSPoint)
```

```objc
- (void) translateOriginToPoint:(NSPoint) translation;
```

#### Discussion

In the process, the origin of the view’s bounds rectangle is shifted by (`–translation.x`, `–translation.y`). This method neither redisplays the view nor marks it as needing display. You must do this yourself by calling the  [`display()`](./display%28%29.md) method or setting the [`needsDisplay`](./needsdisplay.md) property.

Note the difference between this method and setting the bounds origin. Translation effectively moves the image inside the bounds rectangle, while setting the bounds origin effectively moves the rectangle over the image. The two are in a sense inverse, although translation is cumulative, and setting the bounds origin is absolute.

This method posts an [`boundsDidChangeNotification`](./boundsdidchangenotification.md) to the default notification center if the view is configured to do so.

## Parameters

- `translation`: A point that specifies the new origin.

## See Also

### Related Documentation
- [func setBoundsOrigin(NSPoint)](./setboundsorigin%28_%29.md)
  Sets the origin of the view’s bounds rectangle to a specified point.
- [var bounds: NSRect](./bounds.md)
  The view’s bounds rectangle, which expresses its location and size in its own coordinate system.
### Modifying the Coordinate System
- [func scaleUnitSquare(to: NSSize)](./scaleunitsquare%28to%29.md)
  Scales the view’s coordinate system so that the unit square scales to the specified dimensions.
- [func rotate(byDegrees: CGFloat)](./rotate%28bydegrees%29.md)
  Rotates the view’s bounds rectangle by a specified degree value around the origin of the coordinate system, (0.0, 0.0).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/translateorigin(to:))*