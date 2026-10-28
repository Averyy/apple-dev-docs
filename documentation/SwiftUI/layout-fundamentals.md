# Layout fundamentals

**Framework**: SwiftUI  
**Role**: API Collection

Arrange views inside built-in layout containers like stacks and grids.

## Overview

Use layout containers to arrange the elements of your user interface. Stacks and grids update and adjust the positions of the subviews they contain in response to changes in content or interface dimensions. You can nest layout containers inside other layout containers to any depth to achieve complex layout effects.

![](https://developer.apple.com/tutorials/images/com.apple.SwiftUI/layout-fundamentals-hero@2x.png)

To fine-tune the position, alignment, and other elements of a layout that you build with layout container views, see [Layout adjustments](./layout-adjustments.md). To define custom layout containers, see [Custom layout](./custom-layout.md). For design guidance, see [Layout](https://developer.apple.com/design/human-interface-guidelines/layout) in the Human Interface Guidelines.

## Topics

### Choosing a layout
- [Picking container views for your content](./picking-container-views-for-your-content.md)
  Build flexible user interfaces by using stacks, grids, lists, and forms.
### Statically arranging views in one dimension
- [Building layouts with stack views](./building-layouts-with-stack-views.md)
  Compose complex layouts from primitive container views.
- [struct HStack](./hstack.md)
  A view that arranges its subviews in a horizontal line.
- [struct VStack](./vstack.md)
  A view that arranges its subviews in a vertical line.
### Dynamically arranging views in one dimension
- [Grouping data with lazy stack views](./grouping-data-with-lazy-stack-views.md)
  Split content into logical sections inside lazy stack views.
- [Creating performant scrollable stacks](./creating-performant-scrollable-stacks.md)
  Display large numbers of repeated views efficiently with scroll views, stack views, and lazy stacks.
- [struct LazyHStack](./lazyhstack.md)
  A view that arranges its children in a line that grows horizontally, creating items only as needed.
- [struct LazyVStack](./lazyvstack.md)
  A view that arranges its children in a line that grows vertically, creating items only as needed.
- [struct PinnedScrollableViews](./pinnedscrollableviews.md)
  A set of view types that may be pinned to the bounds of a scroll view.
### Statically arranging views in two dimensions
- [struct Grid](./grid.md)
  A container view that arranges other views in a two dimensional layout.
- [struct GridRow](./gridrow.md)
  A horizontal row in a two dimensional grid container.
- [func gridCellColumns(Int) -> some View](./view/gridcellcolumns%28_%29.md)
  Tells a view that acts as a cell in a grid to span the specified number of columns.
- [func gridCellAnchor(UnitPoint) -> some View](./view/gridcellanchor%28_%29.md)
  Specifies a custom alignment anchor for a view that acts as a grid cell.
- [func gridCellUnsizedAxes(Axis.Set) -> some View](./view/gridcellunsizedaxes%28_%29.md)
  Asks grid layouts not to offer the view extra size in the specified axes.
- [func gridColumnAlignment(HorizontalAlignment) -> some View](./view/gridcolumnalignment%28_%29.md)
  Overrides the default horizontal alignment of the grid column that the view appears in.
### Dynamically arranging views in two dimensions
- [struct LazyHGrid](./lazyhgrid.md)
  A container view that arranges its child views in a grid that grows horizontally, creating items only as needed.
- [struct LazyVGrid](./lazyvgrid.md)
  A container view that arranges its child views in a grid that grows vertically, creating items only as needed.
- [struct GridItem](./griditem.md)
  A description of a row or a column in a lazy grid.
### Dynamically arranging a primary and secondary view
- [struct ArrangementView](./arrangementview.md)
  A view that dynamically lays out a primary and secondary view based on size class, orientation, and reserved regions.
- [func arrangementViewStyle(some ArrangementViewStyle) -> some View](./view/arrangementviewstyle%28_%29.md)
  Sets the style for arrangement views within this view.
- [protocol ArrangementViewStyle](./arrangementviewstyle.md)
  A style that indicates how an arrangement view lays out a primary and secondary view.
- [func overlayArrangementEdge(_:)](./view/overlayarrangementedge%28_%29.md)
  The horizontal edge a view in an overlay arrangement aligns to when the arrangement transitions to a landscape orientation.
- [func splitArrangementFixedLayoutSize(horizontal: Bool, vertical: Bool) -> some View](./view/splitarrangementfixedlayoutsize%28horizontal,vertical%29.md)
  Sets the preferred size constraint for a view in a split arrangement style to the ideal size of the view within its container.
- [func splitArrangementLayoutRatio(CGFloat?) -> some View](./view/splitarrangementlayoutratio%28_%29.md)
  Sets the preferred size ratio for a view in a split style arrangement view.
- [func splitArrangementLayoutRatio(minHorizontal: CGFloat?, idealHorizontal: CGFloat?, maxHorizontal: CGFloat?, minVertical: CGFloat?, idealVertical: CGFloat?, maxVertical: CGFloat?) -> some View](./view/splitarrangementlayoutratio%28minhorizontal,idealhorizontal,maxhorizontal,minvertical,idealvertical,maxvertical%29.md)
  Sets the size ratio for a view in a split style arrangement view.
- [func splitArrangementLayoutSize(minWidth: CGFloat?, idealWidth: CGFloat?, maxWidth: CGFloat?, minHeight: CGFloat?, idealHeight: CGFloat?, maxHeight: CGFloat?) -> some View](./view/splitarrangementlayoutsize%28minwidth,idealwidth,maxwidth,minheight,idealheight,maxheight%29.md)
  Sets the size constraints for a view in a split style arrangement view.
### Layering views
- [Adding a background to your view](./adding-a-background-to-your-view.md)
  Compose a background behind your view and extend it beyond the safe area insets.
- [struct ZStack](./zstack.md)
  A view that overlays its subviews, aligning them in both axes.
- [func zIndex(Double) -> some View](./view/zindex%28_%29.md)
  Controls the display order of overlapping views.
- [func background<V>(alignment: Alignment, content: () -> V) -> some View](./view/background%28alignment,content%29.md)
  Layers the views that you specify behind this view.
- [func background<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View](./view/background%28_,ignoressafeareaedges%29.md)
  Sets the view’s background to a style.
- [func background(ignoresSafeAreaEdges: Edge.Set) -> some View](./view/background%28ignoressafeareaedges%29.md)
  Sets the view’s background to the default background style.
- [func background(_:in:fillStyle:)](./view/background%28_,in,fillstyle%29.md)
  Sets the view’s background to an insettable shape filled with a style.
- [func background(in:fillStyle:)](./view/background%28in,fillstyle%29.md)
  Sets the view’s background to an insettable shape filled with the default background style.
- [func overlay<V>(alignment: Alignment, content: () -> V) -> some View](./view/overlay%28alignment,content%29.md)
  Layers the views that you specify in front of this view.
- [func overlay<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View](./view/overlay%28_,ignoressafeareaedges%29.md)
  Layers the specified style in front of this view.
- [func overlay<S, T>(S, in: T, fillStyle: FillStyle) -> some View](./view/overlay%28_,in,fillstyle%29.md)
  Layers a shape that you specify in front of this view.
- [var backgroundMaterial: Material?](./environmentvalues/backgroundmaterial.md)
  The material underneath the current view.
- [func containerBackground<S>(S, for: ContainerBackgroundPlacement) -> some View](./view/containerbackground%28_,for%29.md)
  Sets the container background of the enclosing container using a view.
- [func containerBackground<V>(for: ContainerBackgroundPlacement, alignment: Alignment, content: () -> V) -> some View](./view/containerbackground%28for,alignment,content%29.md)
  Sets the container background of the enclosing container using a view.
- [struct ContainerBackgroundPlacement](./containerbackgroundplacement.md)
  The placement of a container background.
### Automatically choosing the layout that fits
- [struct ViewThatFits](./viewthatfits.md)
  A view that adapts to the available space by providing the first child view that fits.
### Separators
- [struct Spacer](./spacer.md)
  A flexible space that expands along the major axis of its containing stack layout, or on both axes if not contained in a stack.
- [struct Divider](./divider.md)
  A visual element that can be used to separate other content.

## See Also

### View layout
- [Layout adjustments](./layout-adjustments.md)
  Make fine adjustments to alignment, spacing, padding, and other layout parameters.
- [Custom layout](./custom-layout.md)
  Place views in custom arrangements and create animated transitions between layout types.
- [Lists](./lists.md)
  Display a structured, scrollable column of information.
- [Tables](./tables.md)
  Display selectable, sortable data arranged in rows and columns.
- [View groupings](./view-groupings.md)
  Present views in different kinds of purpose-driven containers, like forms or control groups.
- [Scroll views](./scroll-views.md)
  Enable people to scroll to content that doesn’t fit in the current display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/layout-fundamentals)*