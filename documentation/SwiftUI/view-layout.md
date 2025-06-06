# Layout modifiers

**Framework**: SwiftUI

Tell a view how to arrange itself within a view hierarchy by adjusting its size, position, alignment, padding, and so on.

#### Overview

Use layout modifiers to fine tune the placement of views in a view hierarchy. You can adjust or constrain the size, position, and alignment of a view. You can also add padding around a view, and indicate how the view interacts with system-defined safe areas.

To get started arranging views, see [`Layout fundamentals`](layout-fundamentals.md). To make adjustments to a basic layout, see [`Layout adjustments`](layout-adjustments.md).

## Topics

### Size
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
### Position
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
- [func coordinateSpace(NamedCoordinateSpace) -> some View](view/coordinatespace(_:).md)
  Assigns a name to the view’s coordinate space, so other code can operate on dimensions like points and sizes relative to the named space.
### Alignment
- [func alignmentGuide(_:computeValue:)](view/alignmentguide(_:computevalue:).md)
  Sets the view’s horizontal alignment.
### Padding and spacing
- [func padding(_:)](view/padding(_:).md)
  Adds a different padding amount to each edge of this view.
- [func padding(Edge.Set, CGFloat?) -> some View](view/padding(_:_:).md)
  Adds an equal padding amount to specific edges of this view.
- [func padding3D(_:)](view/padding3d(_:).md)
  Pads this view using the edge insets you specify.
- [func padding3D(Edge3D.Set, CGFloat?) -> some View](view/padding3d(_:_:).md)
  Pads this view using the edge insets you specify.
- [func listRowInsets(EdgeInsets?) -> some View](view/listrowinsets(_:).md)
  Applies an inset to the rows in a list.
- [func scenePadding(Edge.Set) -> some View](view/scenepadding(_:).md)
  Adds padding to the specified edges of this view using an amount that’s appropriate for the current scene.
- [func scenePadding(ScenePadding, edges: Edge.Set) -> some View](view/scenepadding(_:edges:).md)
  Adds a specified kind of padding to the specified edges of this view using an amount that’s appropriate for the current scene.
- [func listRowSpacing(CGFloat?) -> some View](view/listrowspacing(_:).md)
  Sets the vertical spacing between two adjacent rows in a List.
- [func listSectionSpacing(_:)](view/listsectionspacing(_:).md)
  Sets the spacing between adjacent sections in a [`List`](list.md) to a custom value.
### Grid configuration
- [func gridCellColumns(Int) -> some View](view/gridcellcolumns(_:).md)
  Tells a view that acts as a cell in a grid to span the specified number of columns.
- [func gridCellAnchor(UnitPoint) -> some View](view/gridcellanchor(_:).md)
  Specifies a custom alignment anchor for a view that acts as a grid cell.
- [func gridCellUnsizedAxes(Axis.Set) -> some View](view/gridcellunsizedaxes(_:).md)
  Asks grid layouts not to offer the view extra size in the specified axes.
- [func gridColumnAlignment(HorizontalAlignment) -> some View](view/gridcolumnalignment(_:).md)
  Overrides the default horizontal alignment of the grid column that the view appears in.
### Safe area and margins
- [func ignoresSafeArea(SafeAreaRegions, edges: Edge.Set) -> some View](view/ignoressafearea(_:edges:).md)
  Expands the safe area of a view.
- [func safeAreaInset(edge:alignment:spacing:content:)](view/safeareainset(edge:alignment:spacing:content:).md)
  Shows the specified content beside the modified view.
- [func safeAreaPadding(_:)](view/safeareapadding(_:).md)
  Adds the provided insets into the safe area of this view.
- [func safeAreaPadding(Edge.Set, CGFloat?) -> some View](view/safeareapadding(_:_:).md)
  Adds the provided insets into the safe area of this view.
- [func contentMargins(CGFloat, for: ContentMarginPlacement) -> some View](view/contentmargins(_:for:).md)
  Configures the content margin for a provided placement.
- [func contentMargins(_:_:for:)](view/contentmargins(_:_:for:).md)
  Configures the content margin for a provided placement.
### Layer order
- [func zIndex(Double) -> some View](view/zindex(_:).md)
  Controls the display order of overlapping views.
### Layout direction
- [func layoutDirectionBehavior(LayoutDirectionBehavior) -> some View](view/layoutdirectionbehavior(_:).md)
  Sets the behavior of this view for different layout directions.
### Custom layout characteristics
- [func layoutValue<K>(key: K.Type, value: K.Value) -> some View](view/layoutvalue(key:value:).md)
  Associates a value with a custom layout property.

## See Also

- [Style modifiers](view-style-modifiers.md)
  Apply built-in styles to different types of views.
- [Graphics and rendering modifiers](view-graphics-and-rendering.md)
  Affect the way the system draws a view, for example by scaling or masking a view, or by applying graphical effects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view-layout)*