# Layout adjustments

**Framework**: SwiftUI

Make fine adjustments to alignment, spacing, padding, and other layout parameters.

#### Overview

Layout containers like stacks and grids provide a great starting point for arranging views in your app’s user interface. When you need to make fine adjustments, use layout view modifiers. You can adjust or constrain the size, position, and alignment of a view. You can also add padding around a view, and indicate how the view interacts with system-defined safe areas.

![None](https://docs-assets.developer.apple.com/published/44eb8b59b2583dbb9feab193d65420ee/layout-adjustments-hero%402x.png)

To get started with a basic layout, see [`Layout fundamentals`](layout-fundamentals.md). For design guidance, see [`Layout`](https://developer.apple.com/design/Human-Interface-Guidelines/layout) in the Human Interface Guidelines.

## Topics

### Finetuning a layout
- [Laying out a simple view](laying-out-a-simple-view.md)
  Create a view layout by adjusting the size of views.
- [Inspecting view layout](inspecting-view-layout.md)
  Determine the position and extent of a view using Xcode previews or by adding temporary borders.
### Adding padding around a view
- [func padding(_:)](view/padding(_:).md)
  Adds a different padding amount to each edge of this view.
- [func padding(Edge.Set, CGFloat?) -> some View](view/padding(_:_:).md)
  Adds an equal padding amount to specific edges of this view.
- [func padding3D(_:)](view/padding3d(_:).md)
  Pads this view using the edge insets you specify.
- [func padding3D(Edge3D.Set, CGFloat?) -> some View](view/padding3d(_:_:).md)
  Pads this view using the edge insets you specify.
- [func scenePadding(Edge.Set) -> some View](view/scenepadding(_:).md)
  Adds padding to the specified edges of this view using an amount that’s appropriate for the current scene.
- [func scenePadding(ScenePadding, edges: Edge.Set) -> some View](view/scenepadding(_:edges:).md)
  Adds a specified kind of padding to the specified edges of this view using an amount that’s appropriate for the current scene.
- [struct ScenePadding](scenepadding.md)
  The padding used to space a view from its containing scene.
### Influencing a view’s size
- [func frame(width: CGFloat?, height: CGFloat?, alignment: Alignment) -> some View](view/frame(width:height:alignment:).md)
  Positions this view within an invisible frame with the specified size.
- [func frame(depth: CGFloat?, alignment: DepthAlignment) -> some View](view/frame(depth:alignment:).md)
  Positions this view within an invisible frame with the specified depth.
- [func frame(minWidth: CGFloat?, idealWidth: CGFloat?, maxWidth: CGFloat?, minHeight: CGFloat?, idealHeight: CGFloat?, maxHeight: CGFloat?, alignment: Alignment) -> some View](view/frame(minwidth:idealwidth:maxwidth:minheight:idealheight:maxheight:alignment:).md)
  Positions this view within an invisible frame having the specified size constraints.
- [func frame(minDepth: CGFloat?, idealDepth: CGFloat?, maxDepth: CGFloat?, alignment: DepthAlignment) -> some View](view/frame(mindepth:idealdepth:maxdepth:alignment:).md)
  Positions this view within an invisible frame having the specified depth constraints.
- [func containerRelativeFrame(Axis.Set, alignment: Alignment) -> some View](view/containerrelativeframe(_:alignment:).md)
  Positions this view within an invisible frame with a size relative to the nearest container.
- [func containerRelativeFrame(Axis.Set, alignment: Alignment, (CGFloat, Axis) -> CGFloat) -> some View](view/containerrelativeframe(_:alignment:_:).md)
  Positions this view within an invisible frame with a size relative to the nearest container.
- [func containerRelativeFrame(Axis.Set, count: Int, span: Int, spacing: CGFloat, alignment: Alignment) -> some View](view/containerrelativeframe(_:count:span:spacing:alignment:).md)
  Positions this view within an invisible frame with a size relative to the nearest container.
- [func fixedSize() -> some View](view/fixedsize.md)
  Fixes this view at its ideal size.
- [func fixedSize(horizontal: Bool, vertical: Bool) -> some View](view/fixedsize(horizontal:vertical:).md)
  Fixes this view at its ideal size in the specified dimensions.
- [func layoutPriority(Double) -> some View](view/layoutpriority(_:).md)
  Sets the priority by which a parent layout should apportion space to this child.
### Adjusting a view’s position
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
- [func offset(z: CGFloat) -> some View](view/offset(z:).md)
  Brings a view forward in Z by the provided distance in points.
### Aligning views
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
- [struct ViewDimensions](viewdimensions.md)
  A view’s size and alignment guides in its own coordinate space.
### Setting margins
- [func contentMargins(CGFloat, for: ContentMarginPlacement) -> some View](view/contentmargins(_:for:).md)
  Configures the content margin for a provided placement.
- [func contentMargins(_:_:for:)](view/contentmargins(_:_:for:).md)
  Configures the content margin for a provided placement.
- [struct ContentMarginPlacement](contentmarginplacement.md)
  The placement of margins.
### Staying in the safe areas
- [func ignoresSafeArea(SafeAreaRegions, edges: Edge.Set) -> some View](view/ignoressafearea(_:edges:).md)
  Expands the safe area of a view.
- [func safeAreaInset(edge:alignment:spacing:content:)](view/safeareainset(edge:alignment:spacing:content:).md)
  Shows the specified content beside the modified view.
- [func safeAreaPadding(_:)](view/safeareapadding(_:).md)
  Adds the provided insets into the safe area of this view.
- [func safeAreaPadding(Edge.Set, CGFloat?) -> some View](view/safeareapadding(_:_:).md)
  Adds the provided insets into the safe area of this view.
- [struct SafeAreaRegions](safearearegions.md)
  A set of symbolic safe area regions.
### Setting a layout direction
- [func layoutDirectionBehavior(LayoutDirectionBehavior) -> some View](view/layoutdirectionbehavior(_:).md)
  Sets the behavior of this view for different layout directions.
- [enum LayoutDirectionBehavior](layoutdirectionbehavior.md)
  A description of what should happen when the layout direction changes.
- [var layoutDirection: LayoutDirection](environmentvalues/layoutdirection.md)
  The layout direction associated with the current environment.
- [enum LayoutDirection](layoutdirection.md)
  A direction in which SwiftUI can lay out content.
### Reacting to interface characteristics
- [var isLuminanceReduced: Bool](environmentvalues/isluminancereduced.md)
  A Boolean value that indicates whether the display or environment currently requires reduced luminance.
- [var displayScale: CGFloat](environmentvalues/displayscale.md)
  The display scale of this environment.
- [var pixelLength: CGFloat](environmentvalues/pixellength.md)
  The size of a pixel on the screen.
- [var horizontalSizeClass: UserInterfaceSizeClass?](environmentvalues/horizontalsizeclass.md)
  The horizontal size class of this environment.
- [var verticalSizeClass: UserInterfaceSizeClass?](environmentvalues/verticalsizeclass.md)
  The vertical size class of this environment.
- [enum UserInterfaceSizeClass](userinterfacesizeclass.md)
  A set of values that indicate the visual size available to the view.
### Accessing edges and regions
- [enum Edge](edge.md)
  An enumeration to indicate one edge of a rectangle.
- [enum Edge3D](edge3d.md)
  An edge or face of a 3D volume.
- [enum HorizontalEdge](horizontaledge.md)
  An edge on the horizontal axis.
- [enum VerticalEdge](verticaledge.md)
  An edge on the vertical axis.
- [struct EdgeInsets](edgeinsets.md)
  The inset distances for the sides of a rectangle.
- [struct EdgeInsets3D](edgeinsets3d.md)
  The inset distances for the faces of a 3D volume.

## See Also

- [Layout fundamentals](layout-fundamentals.md)
  Arrange views inside built-in layout containers like stacks and grids.
- [Custom layout](custom-layout.md)
  Place views in custom arrangements and create animated transitions between layout types.
- [Lists](lists.md)
  Display a structured, scrollable column of information.
- [Tables](tables.md)
  Display selectable, sortable data arranged in rows and columns.
- [View groupings](view-groupings.md)
  Present views in different kinds of purpose-driven containers, like forms or control groups.
- [Scroll views](scroll-views.md)
  Enable people to scroll to content that doesn’t fit in the current display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/layout-adjustments)*