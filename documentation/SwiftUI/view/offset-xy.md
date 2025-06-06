# offset(x:y:)

**Framework**: SwiftUI  
**Kind**: method

Offset this view by the specified horizontal and vertical distances.

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
func offset(x: CGFloat = 0, y: CGFloat = 0) -> some View
```

## Mentions

- [Making fine adjustments to a view’s position](making-fine-adjustments-to-a-view-s-position.md)

#### Return Value

A view that offsets this view by `x` and `y`.

#### Discussion

Use `offset(x:y:)` to shift the displayed contents by the amount specified in the `x` and `y` parameters.

The original dimensions of the view aren’t changed by offsetting the contents; in the example below the gray border drawn by this view surrounds the original position of the text:

```swift
Text("Offset by passing horizontal & vertical distance")
    .border(Color.green)
    .offset(x: 20, y: 50)
    .border(Color.gray)
```

![A screenshot showing a view that offset from its original position](https://docs-assets.developer.apple.com/published/2d9a124308ea31d3006f2d246939c0d1/swiftui-offset-xy%402x.png)

## Parameters

- `x`: The horizontal distance to offset this view.
- `y`: The vertical distance to offset this view.

## See Also

- [Making fine adjustments to a view’s position](making-fine-adjustments-to-a-view-s-position.md)
  Shift the position of a view by applying the offset or position modifier.
- [func position(CGPoint) -> some View](view/position(_:).md)
  Positions the center of this view at the specified point in its parent’s coordinate space.
- [func position(x: CGFloat, y: CGFloat) -> some View](view/position(x:y:).md)
  Positions the center of this view at the specified coordinates in its parent’s coordinate space.
- [func offset(CGSize) -> some View](view/offset(_:).md)
  Offset this view by the horizontal and vertical amount specified in the offset parameter.
- [func offset(z: CGFloat) -> some View](view/offset(z:).md)
  Brings a view forward in Z by the provided distance in points.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/offset(x:y:))*