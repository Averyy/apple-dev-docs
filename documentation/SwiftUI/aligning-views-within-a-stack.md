# Aligning views within a stack

**Framework**: SwiftUI

Position views inside a stack using alignment guides.

#### Overview

Stacks place their child views to match their alignment, which defaults to center alignment. When you initialize the stack, you can specify an alignment for the stack to use that also applies to a stack’s child views. If you want to modify the placement of individual child views, use the alignment guide modifier to make adjustments that offset the view from the alignment the stack provides.

To align views across multiple stacks, see [`Aligning views across stacks`](aligning-views-across-stacks.md).

##### Use Defaults for Basic Alignment

For an example of how SwiftUI applies default alignment to the views in an [`HStack`](hstack.md), examine the following code used to provide a status view for a recording app. The `HStack` contains an image view for the icon and two text views with labels that use the [`font(_:)`](view/font(_:).md) modifier to adjust the font size of the text.

```swift
HStack {
    Image("microphone")
    Text("Connecting")
        .font(.caption)
    Text("Bryan")
        .font(.title)
}
.padding()
.border(Color.blue, width: 1)
```

The orange reference line in the following figure shows the default alignment position of the views within the stack. The line functions as a visual reference for the purposes of this article.

![A blue rectangle defines the padded boundary of an HStack, in which a microphone image against the left side, followed the word Connecting styled as a caption, then the name Bryan styled as a title. The child views are spaced evenly across the stack and centered vertically. An orange line runs underneath the view, displaying the location of the default center alignment guide.](https://docs-assets.developer.apple.com/published/e786deee8ebd48ac2caf3af21850ba96/Aligning-Views-Within-a-Stack-1%402x.png)

##### Customize Stack Alignment

You can align content within a stack based on guides provided by the alignments that the stack supports. The various kinds of stacks support the following alignments:

- [`HStack`](hstack.md) uses the guides defined in [`VerticalAlignment`](verticalalignment.md).
- [`VStack`](vstack.md) uses the guides defined in [`HorizontalAlignment`](horizontalalignment.md).
- [`ZStack`](zstack.md) uses the guides defined in [`Alignment`](alignment.md), and a combination of `HorizontalAlignment` and `VerticalAlignment`.

Use the `alignment` parameter when initializing a stack to define the alignment guide for the stack. The following example sets the alignment of the `HStack` to [`firstTextBaseline`](verticalalignment/firsttextbaseline.md), which aligns its child views to the baseline of the first text view (which contains the string “Connecting”):

```swift
HStack(alignment: .firstTextBaseline) {
    Image("microphone")
    Text("Connecting")
        .font(.caption)
    Text("Bryan")
        .font(.title)
}
.padding()
.border(Color.blue, width: 1)
```

![A blue rectangle defines the padded boundary of an HStack, in which a microphone image against the left side, followed the word Connecting styled as a caption, then the name Bryan styled as a title. The child views are spaced evenly across the stack and aligned with the text baselines matching the bottom of the microphone image. An orange line runs underneath the view, displaying the location of the baseline alignment guide.](https://docs-assets.developer.apple.com/published/82076de6ecf9276279d7c9cb905024f2/Aligning-Views-Within-a-Stack-2%402x.png)

##### Adjust the Alignment of Individual Views Within a Stack

Custom images don’t provide a text baseline guide, so the bottom of the image aligns to the text view’s baseline. Adjust the alignment of the image using [`alignmentGuide(_:computeValue:)`](view/alignmentguide(_:computevalue:).md) to get the visual alignment you desire. The alignment guide’s closure provides an instance of [`ViewDimensions`](viewdimensions.md), the parameter `context` in this example — which you can use to return an offset value. The value looked up from `context` with [`bottom`](verticalalignment/bottom.md), provides an offset that aligns the bottom of the image adjusted by an offset to the baseline guide defined on the stack:

```swift
HStack(alignment: .firstTextBaseline) {
    Image("microphone")
        .alignmentGuide(.firstTextBaseline) { context in
            context[.bottom] - 0.12 * context.height
        }
    Text("Connecting")
        .font(.caption)
    Text("Bryan")
        .font(.title)
}
.padding()
.border(Color.blue, width: 1)
```

When you use an alignment guide modifier, make sure to specify an active alignment of the stack. Otherwise, SwiftUI doesn’t invoke the closure to offset the view. In the example above, the [`firstTextBaseline`](verticalalignment/firsttextbaseline.md) input to the alignment guide matches the stack’s alignment, so the adjustment affects the placement of the image:

![A blue rectangle defines the padded boundary of an HStack, in which a microphone image against the left side, followed the word Connecting styled as a caption, then the name Bryan styled as a title. The child views are spaced evenly across the stack and aligned with the text baselines. The microphone image is slightly offset to that the bottom of the microphone aligns with the baseline. An orange line runs underneath the view, displaying the location of the baseline alignment guide.](https://docs-assets.developer.apple.com/published/f51a0a520176a8502cc8628c0fa3f3f9/Aligning-Views-Within-a-Stack-3%402x.png)

##### Use Sf Symbols to Simplify Views When Aligning with Text

You can replace the microphone image with a similar icon from [`SF Symbols`](https://developer.apple.com/design/Human-Interface-Guidelines/sf-symbols) to simplify the view. The icons from SF Symbols use text baseline guides, which means they support whatever font styling you apply to the view.

```swift
HStack(alignment: .firstTextBaseline) {
    Image(systemName: "mic.circle")
        .font(.title)
    Text("Connecting")
        .font(.caption)
    Text("Bryan")
        .font(.title)
}
.padding()
.border(Color.blue, width: 1)
```

![A blue rectangle defines the padded boundary of an HStack, in which a microphone symbol in a circle aligns against the left side, followed the word Connecting styled as a caption, then the name Bryan styled as a title. The child views are spaced evenly across the stack and aligned with the baseline of the name matching the bottom of the microphone within the circle. An orange line runs underneath the view, displaying the location of the baseline alignment guide.](https://docs-assets.developer.apple.com/published/2d597d3b57da46c1172946ac2d5a3c46/Aligning-Views-Within-a-Stack-4%402x.png)

## See Also

- [Aligning views across stacks](aligning-views-across-stacks.md)
  Create a custom alignment and use it to align views across multiple stacks.
- [func alignmentGuide(_:computeValue:)](view/alignmentguide(_:computevalue:).md)
  Sets the view’s horizontal alignment.
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

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/aligning-views-within-a-stack)*