# alignmentGuide(_:computeValue:)

**Framework**: SwiftUI  
**Kind**: method

Sets the view’s horizontal alignment.

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
@preconcurrency
nonisolated func alignmentGuide(_ g: HorizontalAlignment, computeValue: @escaping (ViewDimensions) -> CGFloat) -> some View
```

## Mentions

- [Aligning views within a stack](aligning-views-within-a-stack.md)
- [Aligning views across stacks](aligning-views-across-stacks.md)

#### Return Value

A view modified with respect to its horizontal alignment according to the computation performed in the method’s closure.

#### Discussion

Use `alignmentGuide(_:computeValue:)` to calculate specific offsets to reposition views in relationship to one another. You can return a constant or can use the [`ViewDimensions`](viewdimensions.md) argument to the closure to calculate a return value.

In the example below, the [`HStack`](hstack.md) is offset by a constant of 50 points to the right of center:

```swift
VStack {
    Text("Today's Weather")
        .font(.title)
        .border(.gray)
    HStack {
        Text("🌧")
        Text("Rain & Thunderstorms")
        Text("⛈")
    }
    .alignmentGuide(HorizontalAlignment.center) { _ in  50 }
    .border(.gray)
}
.border(.gray)
```

Changing the alignment of one view may have effects on surrounding views. Here the offset values inside a stack and its contained views is the difference of their absolute offsets.

![A view showing the two emoji offset from a text element using a](https://docs-assets.developer.apple.com/published/d579a7ddd8ed368aada95b05ee12d4af/SwiftUI-View-HAlignmentGuide%402x.png)

## Parameters

- `g`: A   value at which to base the offset.
- `computeValue`: A closure that returns the offset value to apply to   this view.

## See Also

- [Aligning views within a stack](aligning-views-within-a-stack.md)
  Position views inside a stack using alignment guides.
- [Aligning views across stacks](aligning-views-across-stacks.md)
  Create a custom alignment and use it to align views across multiple stacks.
- [struct Alignment](alignment.md)
  An alignment in both axes.
- [struct HorizontalAlignment](horizontalalignment.md)
  An alignment position along the horizontal axis.
- [struct VerticalAlignment](verticalalignment.md)
  An alignment position along the vertical axis.
- [struct DepthAlignment](depthalignment.md)
  An alignment position along the depth axis.
- [protocol AlignmentID](alignmentid.md)
  A type that you use to create custom alignment guides.
- [struct ViewDimensions](viewdimensions.md)
  A view’s size and alignment guides in its own coordinate space.
- [struct ViewDimensions3D](viewdimensions3d.md)
  A view’s 3D size and alignment guides in its own coordinate space.
- [struct SpatialContainer](spatialcontainer.md)
  A layout container that aligns overlapping content in 3D space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/alignmentguide(_:computevalue:))*