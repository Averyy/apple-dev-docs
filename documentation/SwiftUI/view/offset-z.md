# offset(z:)

**Framework**: SwiftUI  
**Kind**: method

Brings a view forward in Z by the provided distance in points.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
nonisolated
func offset(z: CGFloat) -> some View
```

#### Return Value

A view that is extruded forward in Z by `distance`.

## See Also

- [Making fine adjustments to a view’s position](making-fine-adjustments-to-a-view-s-position.md)
  Shift the position of a view by applying the offset or position modifier.
- [func position(CGPoint) -> some View](view/position(_:).md)
  Positions the center of this view at the specified point in its parent’s coordinate space.
- [func position(x: CGFloat, y: CGFloat) -> some View](view/position(x:y:).md)
  Positions the center of this view at the specified coordinates in its parent’s coordinate space.
- [func offset(CGSize) -> some View](view/offset(_:).md)
  Offset this view by the horizontal and vertical amount specified in the offset parameter.
- [func offset(x: CGFloat, y: CGFloat) -> some View](view/offset(x:y:).md)
  Offset this view by the specified horizontal and vertical distances.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/offset(z:))*