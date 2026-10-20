# scaleUnitSquare(to:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Scales the view’s coordinate system so that the unit square scales to the specified dimensions.

**Availability**:
- macOS

## Declaration

```swift
func scaleUnitSquare(to newUnitSize: NSSize)
```

```objc
- (void) scaleUnitSquareToSize:(NSSize) newUnitSize;
```

#### Discussion

For example, a `newUnitSize` of (0.5, 1.0) causes the view’s horizontal coordinates to be halved, in turn doubling the width of its bounds rectangle. Note that scaling is performed from the origin of the coordinate system, (0.0, 0.0), not the origin of the bounds rectangle; as a result, both the origin and size of the bounds rectangle are changed. The frame rectangle remains unchanged.

This method does not redisplay the view or mark it as needing display. You must do this yourself by calling the  [`display()`](./display%28%29.md) method or setting the [`needsDisplay`](./needsdisplay.md) property.

This method posts an [`boundsDidChangeNotification`](./boundsdidchangenotification.md) to the default notification center if the view is configured to do so.

## Parameters

- `newUnitSize`: An `NSSize` structure specifying the new unit size.

## See Also

### Related Documentation
- [func setBoundsSize(NSSize)](./setboundssize%28_%29.md)
  Sets the size of the view’s bounds rectangle to specified dimensions, inversely scaling its coordinate system relative to its frame rectangle.
### Modifying the Coordinate System
- [func translateOrigin(to: NSPoint)](./translateorigin%28to%29.md)
  Translates the view’s coordinate system so that its origin moves to a new location.
- [func rotate(byDegrees: CGFloat)](./rotate%28bydegrees%29.md)
  Rotates the view’s bounds rectangle by a specified degree value around the origin of the coordinate system, (0.0, 0.0).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/scaleunitsquare(to:))*