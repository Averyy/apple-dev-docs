# scaledToFit3D()

**Framework**: SwiftUI  
**Kind**: method

Scales this view to fit its parent.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
nonisolated
func scaledToFit3D() -> some View
```

#### Return Value

A view that scales this view to fit its parent, maintaining this view’s aspect ratio.

#### Discussion

This view’s 3D aspect ratio is maintained as the view scales. This method is equivalent to calling `aspectRatio3D(nil, contentMode: .fit)`.

```swift
Model3D(named: "Plane") { resolved in
    resolved
        .resizable()
        .scaledToFit3D()
} placeholder: {
    ProgressView()
}
.frame(width: 400, height: 400)
.frame(depth: 200)
.border(Color(white: 0.75))
```

## See Also

- [func scaledToFill() -> some View](view/scaledtofill.md)
  Scales this view to fill its parent.
- [func scaledToFill3D() -> some View](view/scaledtofill3d.md)
  Scales this view to fill its parent.
- [func scaledToFit() -> some View](view/scaledtofit.md)
  Scales this view to fit its parent.
- [func scaleEffect(_:anchor:)](view/scaleeffect(_:anchor:).md)
  Scales this view’s rendered output by the given amount in both the horizontal and vertical directions, relative to an anchor point.
- [func scaleEffect(x: CGFloat, y: CGFloat, anchor: UnitPoint) -> some View](view/scaleeffect(x:y:anchor:).md)
  Scales this view’s rendered output by the given horizontal and vertical amounts, relative to an anchor point.
- [func scaleEffect(x: CGFloat, y: CGFloat, z: CGFloat, anchor: UnitPoint3D) -> some View](view/scaleeffect(x:y:z:anchor:).md)
  Scales this view by the specified horizontal, vertical, and depth factors, relative to an anchor point.
- [func imageScale(Image.Scale) -> some View](view/imagescale(_:).md)
  Scales images within the view according to one of the relative sizes available including small, medium, and large images sizes.
- [func aspectRatio(_:contentMode:)](view/aspectratio(_:contentmode:).md)
  Constrains this view’s dimensions to the specified aspect ratio.
- [func aspectRatio3D(Size3D?, contentMode: ContentMode) -> some View](view/aspectratio3d(_:contentmode:).md)
  Constrains this view’s dimensions to the specified 3D aspect ratio.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/scaledtofit3d())*