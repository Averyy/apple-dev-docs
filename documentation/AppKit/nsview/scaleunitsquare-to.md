# scaleUnitSquare(to:)

**Framework**: AppKit  
**Kind**: method

Scales the view’s coordinate system so that the unit square scales to the specified dimensions.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func scaleUnitSquare(to newUnitSize: NSSize)
```

#### Discussion

For example, a `newUnitSize` of (0.5, 1.0) causes the view’s horizontal coordinates to be halved, in turn doubling the width of its bounds rectangle. Note that scaling is performed from the origin of the coordinate system, (0.0, 0.0), not the origin of the bounds rectangle; as a result, both the origin and size of the bounds rectangle are changed. The frame rectangle remains unchanged.

This method does not redisplay the view or mark it as needing display. You must do this yourself by calling the  [`display()`](nsview/display().md) method or setting the [`needsDisplay`](nsview/needsdisplay.md) property.

This method posts an [`boundsDidChangeNotification`](nsview/boundsdidchangenotification.md) to the default notification center if the view is configured to do so.

## Parameters

- `newUnitSize`: An   structure specifying the new unit size.

## See Also

- [func setBoundsSize(NSSize)](nsview/setboundssize(_:).md)
  Sets the size of the view’s bounds rectangle to specified dimensions, inversely scaling its coordinate system relative to its frame rectangle.
- [func translateOrigin(to: NSPoint)](nsview/translateorigin(to:).md)
  Translates the view’s coordinate system so that its origin moves to a new location.
- [func rotate(byDegrees: CGFloat)](nsview/rotate(bydegrees:).md)
  Rotates the view’s bounds rectangle by a specified degree value around the origin of the coordinate system, (0.0, 0.0).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/scaleunitsquare(to:))*