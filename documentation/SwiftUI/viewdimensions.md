# ViewDimensions

**Framework**: SwiftUI  
**Kind**: struct

A view’s size and alignment guides in its own coordinate space.

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
struct ViewDimensions
```

## Mentions

- [Aligning views within a stack](aligning-views-within-a-stack.md)

#### Overview

This structure contains the size and alignment guides of a view. You receive an instance of this structure to use in a variety of layout calculations, like when you:

- Define a default value for a custom alignment guide; see [`defaultValue(in:)`](alignmentid/defaultvalue(in:).md).
- Modify an alignment guide on a view; see [`alignmentGuide(_:computeValue:)`](view/alignmentguide(_:computevalue:).md).
- Ask for the dimensions of a subview of a custom view layout; see [`dimensions(in:)`](layoutsubview/dimensions(in:).md).

##### Custom Alignment Guides

You receive an instance of this structure as the `context` parameter to the [`defaultValue(in:)`](alignmentid/defaultvalue(in:).md) method that you implement to produce the default offset for an alignment guide, or as the first argument to the closure you provide to the [`alignmentGuide(_:computeValue:)`](view/alignmentguide(_:computevalue:).md) view modifier to override the default calculation for an alignment guide. In both cases you can use the instance, if helpful, to calculate the offset for the guide. For example, you could compute a default offset for a custom [`VerticalAlignment`](verticalalignment.md) as a fraction of the view’s [`height`](viewdimensions/height.md):

```swift
private struct FirstThirdAlignment: AlignmentID {
    static func defaultValue(in context: ViewDimensions) -> CGFloat {
        context.height / 3
    }
}

extension VerticalAlignment {
    static let firstThird = VerticalAlignment(FirstThirdAlignment.self)
}
```

As another example, you could use the view dimensions instance to look up the offset of an existing guide and modify it:

```swift
struct ViewDimensionsOffset: View {
    var body: some View {
        VStack(alignment: .leading) {
            Text("Default")
            Text("Indented")
                .alignmentGuide(.leading) { context in
                    context[.leading] - 10
                }
        }
    }
}
```

The example above indents the second text view because the subtraction moves the second text view’s leading guide in the negative x direction, which is to the left in the view’s coordinate space. As a result, SwiftUI moves the second text view to the right, relative to the first text view, to keep their leading guides aligned:

![A screenshot of two strings. The first says Default and the second,](https://docs-assets.developer.apple.com/published/3d9590a457827399824ef411b0a102c0/ViewDimensions-1-iOS%402x.png)

##### Layout Direction

The discussion above describes a left-to-right language environment, but you don’t change your guide calculation to operate in a right-to-left environment. SwiftUI moves the view’s origin from the left to the right side of the view and inverts the positive x direction. As a result, the existing calculation produces the same effect, but in the opposite direction.

You can see this if you use the [`environment(_:_:)`](view/environment(_:_:).md) modifier to set the [`layoutDirection`](environmentvalues/layoutdirection.md) property for the view that you defined above:

```swift
ViewDimensionsOffset()
    .environment(\.layoutDirection, .rightToLeft)
```

With no change in your guide, this produces the desired effect — it indents the second text view’s right side, relative to the first text view’s right side. The leading edge is now on the right, and the direction of the offset is reversed:

![A screenshot of two strings. The first says Default and the second,](https://docs-assets.developer.apple.com/published/914c5c58311529ab9683f501c8dfe50e/ViewDimensions-2-iOS%402x.png)

## Topics

### Getting dimensions
- [var height: CGFloat](viewdimensions/height.md)
  The view’s height.
- [var width: CGFloat](viewdimensions/width.md)
  The view’s width.
### Accessing guide values
- [subscript(_:)](viewdimensions/subscript(_:).md)
  Gets the value of the given horizontal guide.
- [subscript(explicit:)](viewdimensions/subscript(explicit:).md)
  Gets the explicit value of the given horizontal alignment guide.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)

## See Also

- [Aligning views within a stack](aligning-views-within-a-stack.md)
  Position views inside a stack using alignment guides.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/viewdimensions)*