# Layout fundamentals

**Framework**: SwiftUI

Arrange views inside built-in layout containers like stacks and grids.

#### Overview

Use layout containers to arrange the elements of your user interface. Stacks and grids update and adjust the positions of the subviews they contain in response to changes in content or interface dimensions. You can nest layout containers inside other layout containers to any depth to achieve complex layout effects.

![None](https://docs-assets.developer.apple.com/published/9fd862b8214f1de236f13a51187c257f/layout-fundamentals-hero%402x.png)

To finetune the position, alignment, and other elements of a layout that you build with layout container views, see [`Layout adjustments`](layout-adjustments.md). To define custom layout containers, see [`Custom layout`](custom-layout.md). For design guidance, see [`Layout`](https://developer.apple.com/design/Human-Interface-Guidelines/layout) in the Human Interface Guidelines.

## Topics

### Choosing a layout
- [Picking container views for your content](picking-container-views-for-your-content.md)
  Build flexible user interfaces by using stacks, grids, lists, and forms.
### Statically arranging views in one dimension
- [Building layouts with stack views](building-layouts-with-stack-views.md)
  Compose complex layouts from primitive container views.
- [struct HStack](hstack.md)
  A view that arranges its subviews in a horizontal line.
- [struct VStack](vstack.md)
  A view that arranges its subviews in a vertical line.
### Dynamically arranging views in one dimension
- [Grouping data with lazy stack views](grouping-data-with-lazy-stack-views.md)
  Split content into logical sections inside lazy stack views.
- [Creating performant scrollable stacks](creating-performant-scrollable-stacks.md)
  Display large numbers of repeated views efficiently with scroll views, stack views, and lazy stacks.
- [struct LazyHStack](lazyhstack.md)
  A view that arranges its children in a line that grows horizontally, creating items only as needed.
- [struct LazyVStack](lazyvstack.md)
  A view that arranges its children in a line that grows vertically, creating items only as needed.
- [struct PinnedScrollableViews](pinnedscrollableviews.md)
  A set of view types that may be pinned to the bounds of a scroll view.
### Statically arranging views in two dimensions
- [struct Grid](grid.md)
  A container view that arranges other views in a two dimensional layout.
- [struct GridRow](gridrow.md)
  A horizontal row in a two dimensional grid container.
- [func gridCellColumns(Int) -> some View](view/gridcellcolumns(_:).md)
  Tells a view that acts as a cell in a grid to span the specified number of columns.
- [func gridCellAnchor(UnitPoint) -> some View](view/gridcellanchor(_:).md)
  Specifies a custom alignment anchor for a view that acts as a grid cell.
- [func gridCellUnsizedAxes(Axis.Set) -> some View](view/gridcellunsizedaxes(_:).md)
  Asks grid layouts not to offer the view extra size in the specified axes.
- [func gridColumnAlignment(HorizontalAlignment) -> some View](view/gridcolumnalignment(_:).md)
  Overrides the default horizontal alignment of the grid column that the view appears in.
### Dynamically arranging views in two dimensions
- [struct LazyHGrid](lazyhgrid.md)
  A container view that arranges its child views in a grid that grows horizontally, creating items only as needed.
- [struct LazyVGrid](lazyvgrid.md)
  A container view that arranges its child views in a grid that grows vertically, creating items only as needed.
- [struct GridItem](griditem.md)
  A description of a row or a column in a lazy grid.
### Layering views
- [Adding a background to your view](adding-a-background-to-your-view.md)
  Compose a background behind your view and extend it beyond the safe area insets.
- [struct ZStack](zstack.md)
  A view that overlays its subviews, aligning them in both axes.
- [func zIndex(Double) -> some View](view/zindex(_:).md)
  Controls the display order of overlapping views.
- [func background<V>(alignment: Alignment, content: () -> V) -> some View](view/background(alignment:content:).md)
  Layers the views that you specify behind this view.
- [func background<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View](view/background(_:ignoressafeareaedges:).md)
  Sets the view’s background to a style.
- [func background(ignoresSafeAreaEdges: Edge.Set) -> some View](view/background(ignoressafeareaedges:).md)
  Sets the view’s background to the default background style.
- [func background(_:in:fillStyle:)](view/background(_:in:fillstyle:).md)
  Sets the view’s background to an insettable shape filled with a style.
- [func background(in:fillStyle:)](view/background(in:fillstyle:).md)
  Sets the view’s background to an insettable shape filled with the default background style.
- [func overlay<V>(alignment: Alignment, content: () -> V) -> some View](view/overlay(alignment:content:).md)
  Layers the views that you specify in front of this view.
- [func overlay<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View](view/overlay(_:ignoressafeareaedges:).md)
  Layers the specified style in front of this view.
- [func overlay<S, T>(S, in: T, fillStyle: FillStyle) -> some View](view/overlay(_:in:fillstyle:).md)
  Layers a shape that you specify in front of this view.
- [var backgroundMaterial: Material?](environmentvalues/backgroundmaterial.md)
  The material underneath the current view.
- [func containerBackground<S>(S, for: ContainerBackgroundPlacement) -> some View](view/containerbackground(_:for:).md)
  Sets the container background of the enclosing container using a view.
- [func containerBackground<V>(for: ContainerBackgroundPlacement, alignment: Alignment, content: () -> V) -> some View](view/containerbackground(for:alignment:content:).md)
  Sets the container background of the enclosing container using a view.
- [struct ContainerBackgroundPlacement](containerbackgroundplacement.md)
  The placement of a container background.
### Automatically choosing the layout that fits
- [struct ViewThatFits](viewthatfits.md)
  A view that adapts to the available space by providing the first child view that fits.
### Separators
- [struct Spacer](spacer.md)
  A flexible space that expands along the major axis of its containing stack layout, or on both axes if not contained in a stack.
- [struct Divider](divider.md)
  A visual element that can be used to separate other content.

## See Also

- [Layout adjustments](layout-adjustments.md)
  Make fine adjustments to alignment, spacing, padding, and other layout parameters.
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

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/layout-fundamentals)*