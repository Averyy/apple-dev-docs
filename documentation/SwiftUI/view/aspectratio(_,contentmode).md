# aspectRatio(_:contentMode:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Constrains this view’s dimensions to the specified aspect ratio.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
nonisolated
func aspectRatio(_ aspectRatio: CGFloat? = nil, contentMode: ContentMode) -> some View
```

**Other overloads**:

```swift
nonisolated
func aspectRatio(_ aspectRatio: CGSize, contentMode: ContentMode) -> some View
```

## Mentions

- [Fitting images into available space](../fitting-images-into-available-space.md)

## Return Value

A view that constrains this view’s dimensions to the aspect ratio of the given size using `contentMode` as its scaling algorithm.

## Discussion

Use `aspectRatio(_:contentMode:)` to constrain a view’s dimensions to an aspect ratio specified by a [`CGFloat`](../../CoreFoundation/cgfloat-swift.struct.md) using the specified content mode.

If this view is resizable, the resulting view will have `aspectRatio` as its aspect ratio. In this example, the purple ellipse has a 3:4 width-to-height ratio, and scales to fit its frame:

```swift
Ellipse()
    .fill(Color.purple)
    .aspectRatio(0.75, contentMode: .fit)
    .frame(width: 200, height: 200)
    .border(Color(white: 0.75))
```

![A view showing a purple ellipse that has a 3:4 width-to-height ratio,](https://developer.apple.com/tutorials/images/com.apple.SwiftUI/SwiftUI-View-aspectRatio-cgfloat@2x.png)

## Parameters

- `aspectRatio`: The ratio of width to height to use for the resulting view. Use `nil` to maintain the current aspect ratio in the resulting view.
- `contentMode`: A flag that indicates whether this view fits or fills the parent context.

## See Also

### Scaling, rotating, or transforming a view
- [func scaledToFill() -> some View](./scaledtofill%28%29.md)
  Scales this view to fill its parent.
- [func scaledToFit() -> some View](./scaledtofit%28%29.md)
  Scales this view to fit its parent.
- [func scaleEffect(_:anchor:)](./scaleeffect%28_,anchor%29.md)
  Scales this view uniformly by the specified factor, relative to an anchor point.
- [func scaleEffect(x: CGFloat, y: CGFloat, anchor: UnitPoint) -> some View](./scaleeffect%28x,y,anchor%29.md)
  Scales this view’s rendered output by the given horizontal and vertical amounts, relative to an anchor point.
- [func scaleEffect(x: CGFloat, y: CGFloat, z: CGFloat, anchor: UnitPoint3D) -> some View](./scaleeffect%28x,y,z,anchor%29.md)
  Scales this view by the specified horizontal, vertical, and depth factors, relative to an anchor point.
- [func rotationEffect(Angle, anchor: UnitPoint) -> some View](./rotationeffect%28_,anchor%29.md)
  Rotates a view’s rendered output in two dimensions around the specified point.
- [func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat), anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some View](./rotation3deffect%28_,axis,anchor,anchorz,perspective%29.md)
  Renders a view’s content as if it’s rotated in three dimensions around the specified axis.
- [func perspectiveRotationEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat), anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some View](./perspectiverotationeffect%28_,axis,anchor,anchorz,perspective%29.md)
  Renders a view’s content as if it’s rotated in three dimensions around the specified axis.
- [func rotation3DEffect(Rotation3D, anchor: UnitPoint3D) -> some View](./rotation3deffect%28_,anchor%29.md)
  Rotates the view’s content by the specified 3D rotation value.
- [func rotation3DEffect(_:axis:anchor:)](./rotation3deffect%28_,axis,anchor%29.md)
  Rotates the view’s content by an angle about an axis that you specify as a tuple of elements.
- [func transformEffect(CGAffineTransform) -> some View](./transformeffect%28_%29.md)
  Applies an affine transformation to this view’s rendered output.
- [func transform3DEffect(AffineTransform3D) -> some View](./transform3deffect%28_%29.md)
  Applies a 3D transformation to this view’s rendered output.
- [func projectionEffect(ProjectionTransform) -> some View](./projectioneffect%28_%29.md)
  Applies a projection transformation to this view’s rendered output.
- [struct ProjectionTransform](../projectiontransform.md)
  A 3x3 matrix that transforms points in a plane.
- [enum ContentMode](../contentmode.md)
  Constants that define how a view’s content fills the available space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/aspectratio(_:contentmode:))*