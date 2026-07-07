# aspectRatio3D(_:contentMode:)

**Framework**: SwiftUI  
**Kind**: method

Constrains this view’s dimensions to the specified 3D aspect ratio.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
@export(implementation)
nonisolated func aspectRatio3D(_ aspectRatio: Size3D? = nil, contentMode: ContentMode) -> some View
```

#### Return Value

A view that constrains this view’s dimensions to `aspectRatio`, using `contentMode` as its scaling algorithm.

#### Discussion

If this view is resizable, the resulting view will have `aspectRatio` as its aspect ratio. In this example, the Model3D has a 2 : 3 : 1 width to height to depth ratio, and scales to fit its frame:

```swift
Model3D(named: "Sphere") { resolved in
    let ratio3D = Size3D(width: 2, height: 3, depth: 1)
    resolved
        .resizable()
        .aspectRatio3D(ratio3D, contentMode: .fit)
} placeholder: {
    ProgressView()
}
.frame(width: 200, height: 200)
.frame(depth: 200)
.border(Color(white: 0.75))
```

## Parameters

- `aspectRatio`: The ratio of width to height to depth to use for the resulting view. If `aspectRatio` is `nil`, the resulting view maintains this view’s aspect ratio.
- `contentMode`: A flag indicating whether this view should fit or fill the parent context.

## See Also

- [func scaledToFill() -> some View](view/scaledtofill.md)
  Scales this view to fill its parent.
- [func scaledToFill3D() -> some View](view/scaledtofill3d.md)
  Scales this view to fill its parent.
- [func scaledToFit() -> some View](view/scaledtofit.md)
  Scales this view to fit its parent.
- [func scaledToFit3D() -> some View](view/scaledtofit3d.md)
  Scales this view to fit its parent.
- [func scaleEffect(_:anchor:)](view/scaleeffect(_:anchor:).md)
  Scales this view uniformly by the specified factor, relative to an anchor point.
- [func scaleEffect(x: CGFloat, y: CGFloat, anchor: UnitPoint) -> some View](view/scaleeffect(x:y:anchor:).md)
  Scales this view’s rendered output by the given horizontal and vertical amounts, relative to an anchor point.
- [func scaleEffect(x: CGFloat, y: CGFloat, z: CGFloat, anchor: UnitPoint3D) -> some View](view/scaleeffect(x:y:z:anchor:).md)
  Scales this view by the specified horizontal, vertical, and depth factors, relative to an anchor point.
- [func imageScale(Image.Scale) -> some View](view/imagescale(_:).md)
  Scales images within the view according to one of the relative sizes available including small, medium, and large images sizes.
- [func aspectRatio(_:contentMode:)](view/aspectratio(_:contentmode:).md)
  Constrains this view’s dimensions to the specified aspect ratio.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/aspectratio3d(_:contentmode:))*