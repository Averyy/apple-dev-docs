# Building layouts with stack views

**Framework**: SwiftUI

Compose complex layouts from primitive container views.

#### Overview

Individually, [`HStack`](hstack.md), [`VStack`](vstack.md), and [`ZStack`](zstack.md) are simple views. [`HStack`](hstack.md) positions views in a horizontal line, [`VStack`](vstack.md) positions them in a vertical line, and [`ZStack`](zstack.md) overlays views on top of one another.

![A diagram showing the three different stack views; Horizontal, vertical, and depth. Each stack contains a square and a circle shape stacked together either side-by-side horizontally or vertically, or layered one on top of the other.](https://docs-assets.developer.apple.com/published/ce0ca452c3bcccf11149a8728f1c489f/Building-Layouts-with-Stack-Views-1%402x.png)

When you initialize them with default parameters, stack views center align their content and insert a small amount of spacing between each contained view. But, when you combine and customize stacks with view modifiers, [`Spacer`](spacer.md), and [`Divider`](divider.md) views, you can create highly flexible and complex layouts.

##### Plan Your Layout Hierarchy

Think about a layout in terms of how you might create it using the various types of stack views as you start to translate your design into code. Break down complex designs into smaller, simpler pieces you can build with stack views.

For example, you might build this profile view using three stack views:

![A diagram showing how a generic user profile layout might utilize stack views. The diagram shows the rendered layout next to an exploded, 3D illustration of the view hierarchy showing four layers of views stacked on top of each other. The lowest level of the hierarchy is a ZStack; above that is an Image view, then an HStack, and finally a VStack and Spacer view at the highest level.](https://docs-assets.developer.apple.com/published/a5b7b41f3a40302214f2f18543eaaadf/Building-Layouts-with-Stack-Views-2%402x.png)

A [`ZStack`](zstack.md) contains an [`Image`](image.md) view that displays a profile picture with a semi-transparent [`HStack`](hstack.md) overlaid on top. The [`HStack`](hstack.md) contains a [`VStack`](vstack.md) with a pair of [`Text`](text.md) views inside it, and a [`Spacer`](spacer.md) view pushes the [`VStack`](vstack.md) to the leading side.

To create this stack view:

```swift
struct ProfileView: View {
    var body: some View {
        ZStack(alignment: .bottom) {
            Image("ProfilePicture")
                .resizable()
                .aspectRatio(contentMode: .fit)
            HStack {
                VStack(alignment: .leading) {
                    Text("Rachael Chiseck")
                        .font(.headline)
                    Text("Chief Executive Officer")
                        .font(.subheadline)
                }
                Spacer()
            }
            .padding()
            .foregroundColor(.primary)
            .background(Color.primary
                            .colorInvert()
                            .opacity(0.75))
        }
    }
}
```

##### Position Views with Alignment and Spacer Views

Align any contained views inside a stack view by using a combination of the `alignment` property, [`Spacer`](spacer.md), and [`Divider`](divider.md) views.

In the previous example layout, the [`VStack`](vstack.md) that contains the two [`Text`](text.md) views uses the [`leading`](horizontalalignment/leading.md) alignment:

![A diagram showing two views being aligned in three different ways in a vertical stack view. Leading, where both views are aligned to the leading edge of the stack. Centered, where both views are centered in the stack. Finally trailing, where both views are aligned with the trailing edge](https://docs-assets.developer.apple.com/published/d3ad16aec1948970076cc098e438be1f/Building-Layouts-with-Stack-Views-3%402x.png)

The `alignment` property doesn’t position the [`VStack`](vstack.md) inside its container; instead, it positions the views inside the [`VStack`](vstack.md).

The `alignment` property of a [`VStack`](vstack.md) only applies to the horizontal alignment of the contained controls using [`HorizontalAlignment`](horizontalalignment.md). Similarly, the `alignment` property for an [`HStack`](hstack.md) only controls the vertical alignment using [`VerticalAlignment`](verticalalignment.md). Finally, you can align views inside a [`ZStack`](zstack.md) along both axes with [`Alignment`](alignment.md).

Use [`Spacer`](spacer.md) views to align views along the primary axis of an [`HStack`](hstack.md) or [`VStack`](vstack.md). Spacers expand to fill any available space and push content apart from other views or the edges of the stack.

![A diagram showing the use of spacer views in three vertical stack views. The first stack shows a spacer view pushing another view to the top of its container. The second stack shows a spacer view pushing two views apart, ending with the views aligned to the top and bottom of their container. a spacer view pushing another view to the bottom of its container.](https://docs-assets.developer.apple.com/published/189fa436f07ed0011bd0c1abeb167723/Building-Layouts-with-Stack-Views-4%402x.png)

[`Divider`](divider.md) views also add space in between a stack’s subviews, but only insert enough space to draw a line across the stack’s minor axis. They don’t expand to fill available space.

##### Create Adaptive Layouts Instead of Explicit Layouts

Wherever possible, define structure and hierarchy rather than explicitly positioning view frames. Instead of using explicit heights and widths for views, let them expand to fill available space. Adaptive layouts that you build adapt more easily to different device sizes and platforms.

It is possible to create this article’s example layout with two stack views rather than three, by manipulating the [`Text`](text.md) view frames explicitly. While the output might look the same, the code to implement it is more brittle, and might not scale as well across devices of different size classes.

You may need to make adjustments to a layout that uses explicit adjustments by using view modifiers such as [`frame(width:height:alignment:)`](view/frame(width:height:alignment:).md) or [`position(x:y:)`](view/position(x:y:).md), but only consider this when you can’t achieve your desired layout in an adaptive, flexible way. For more information on making fine adjustments to view layout, see [`Making fine adjustments to a view’s position`](making-fine-adjustments-to-a-view-s-position.md).

##### Add Depth in Alternative Ways

In some situations it may make sense to add depth to your layout by using the [`overlay(_:alignment:)`](view/overlay(_:alignment:).md) and [`background(_:alignment:)`](view/background(_:alignment:).md) view modifiers instead of a [`ZStack`](zstack.md). The background view modifier places another view behind the view you’re modifying, and overlay places a view on top of it.

Choose between a stack-based approach and the view modifier approach based on how you want to determine the size of the final layout. If your layout has one dominant view that defines the size of the layout, use the [`overlay(_:alignment:)`](view/overlay(_:alignment:).md) or [`background(_:alignment:)`](view/background(_:alignment:).md) view modifier on that view. If you want the final view size to come from an aggregation of all the contained views, use a [`ZStack`](zstack.md).

For example, this code overlays a `ProfileDetail` view on top of the [`Image`](image.md) view:

```swift
struct ProfileViewWithOverlay: View {
    var body: some View {
        VStack {
            Image("ProfilePicture")
                .resizable()
                .aspectRatio(contentMode: .fit)
                .overlay(ProfileDetail(), alignment: .bottom)
        }
    }
}

struct ProfileDetail: View {
    var body: some View {
        HStack {
            VStack(alignment: .leading) {
                Text("Rachael Chiseck")
                    .font(.headline)
                Text("Chief Executive Officer")
                    .font(.subheadline)
            }
            Spacer()
        }
        .padding()
        .foregroundColor(.primary)
        .background(Color.primary
                        .colorInvert()
                        .opacity(0.75))
    }
}
```

## See Also

- [struct HStack](hstack.md)
  A view that arranges its subviews in a horizontal line.
- [struct VStack](vstack.md)
  A view that arranges its subviews in a vertical line.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/building-layouts-with-stack-views)*