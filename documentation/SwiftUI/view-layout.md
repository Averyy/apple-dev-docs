# Layout modifiers

**Framework**: SwiftUI  
**Role**: API Collection

Tell a view how to arrange itself within a view hierarchy by adjusting its size, position, alignment, padding, and so on.

#### Overview

Use layout modifiers to fine tune the placement of views in a view hierarchy. You can adjust or constrain the size, position, and alignment of a view. You can also add padding around a view, and indicate how the view interacts with system-defined safe areas.

To get started arranging views, see [Layout fundamentals](./layout-fundamentals.md). To make adjustments to a basic layout, see [Layout adjustments](./layout-adjustments.md).

## Topics

### Size
- [func frame(width: CGFloat?, height: CGFloat?, alignment: Alignment) -> some View](./view/frame%28width,height,alignment%29.md)
  Positions this view within an invisible frame with the specified size.
- [func frame(depth: CGFloat?, alignment: DepthAlignment) -> some View](./view/frame%28depth,alignment%29.md)
  Positions this view within an invisible frame with the specified depth.
- [func frame(minWidth: CGFloat?, idealWidth: CGFloat?, maxWidth: CGFloat?, minHeight: CGFloat?, idealHeight: CGFloat?, maxHeight: CGFloat?, alignment: Alignment) -> some View](./view/frame%28minwidth,idealwidth,maxwidth,minheight,idealheight,maxheight,alignment%29.md)
  Positions this view within an invisible frame having the specified size constraints.
- [func frame(minDepth: CGFloat?, idealDepth: CGFloat?, maxDepth: CGFloat?, alignment: DepthAlignment) -> some View](./view/frame%28mindepth,idealdepth,maxdepth,alignment%29.md)
  Positions this view within an invisible frame having the specified depth constraints.
- [func containerRelativeFrame(Axis.Set, alignment: Alignment) -> some View](./view/containerrelativeframe%28_,alignment%29.md)
  Positions this view within an invisible frame with a size relative to the nearest container.
- [func containerRelativeFrame(Axis.Set, alignment: Alignment, (CGFloat, Axis) -> CGFloat) -> some View](./view/containerrelativeframe%28_,alignment,_%29.md)
  Positions this view within an invisible frame with a size relative to the nearest container.
- [func containerRelativeFrame(Axis.Set, count: Int, span: Int, spacing: CGFloat, alignment: Alignment) -> some View](./view/containerrelativeframe%28_,count,span,spacing,alignment%29.md)
  Positions this view within an invisible frame with a size relative to the nearest container.
- [func fixedSize() -> some View](./view/fixedsize%28%29.md)
  Fixes this view at its ideal size.
- [func fixedSize(horizontal: Bool, vertical: Bool) -> some View](./view/fixedsize%28horizontal,vertical%29.md)
  Fixes this view at its ideal size in the specified dimensions.
- [func layoutPriority(Double) -> some View](./view/layoutpriority%28_%29.md)
  Sets the priority by which a parent layout should apportion space to this child.
- [func containerCornerOffset(Edge.Set, sizeToFit: Bool) -> some View](./view/containercorneroffset%28_,sizetofit%29.md)
  Adjusts the view’s layout to avoid the container view’s corner insets for the specified edges.
### Position
- [func position(CGPoint) -> some View](./view/position%28_%29.md)
  Positions the center of this view at the specified point in its parent’s coordinate space.
- [func position(x: CGFloat, y: CGFloat) -> some View](./view/position%28x,y%29.md)
  Positions the center of this view at the specified coordinates in its parent’s coordinate space.
- [func offset(CGSize) -> some View](./view/offset%28_%29.md)
  Offset this view by the horizontal and vertical amount specified in the offset parameter.
- [func offset(x: CGFloat, y: CGFloat) -> some View](./view/offset%28x,y%29.md)
  Offset this view by the specified horizontal and vertical distances.
- [func offset(z: CGFloat) -> some View](./view/offset%28z%29.md)
  Brings a view forward in Z by the provided distance in points.
- [func coordinateSpace(NamedCoordinateSpace) -> some View](./view/coordinatespace%28_%29.md)
  Assigns a name to the view’s coordinate space, so other code can operate on dimensions like points and sizes relative to the named space.
### Alignment
- [func alignmentGuide(_:computeValue:)](./view/alignmentguide%28_,computevalue%29.md)
  Sets the view’s horizontal alignment.
### Padding and spacing
- [func padding(_:)](./view/padding%28_%29.md)
  Adds a different padding amount to each edge of this view.
- [func padding(Edge.Set, CGFloat?) -> some View](./view/padding%28_,_%29.md)
  Adds an equal padding amount to specific edges of this view.
- [func padding3D(_:)](./view/padding3d%28_%29.md)
  Pads this view using the edge insets you specify.
- [func padding3D(Edge3D.Set, CGFloat?) -> some View](./view/padding3d%28_,_%29.md)
  Pads this view using the edge insets you specify.
- [func listRowInsets(EdgeInsets?) -> some View](./view/listrowinsets%28_%29.md)
  Applies an inset to the rows in a list.
- [func listRowInsets(Edge.Set, CGFloat?) -> some View](./view/listrowinsets%28_,_%29.md)
  Sets the insets of rows in a list on the specified edges.
- [func scenePadding(Edge.Set) -> some View](./view/scenepadding%28_%29.md)
  Adds padding to the specified edges of this view using an amount that’s appropriate for the current scene.
- [func scenePadding(ScenePadding, edges: Edge.Set) -> some View](./view/scenepadding%28_,edges%29.md)
  Adds a specified kind of padding to the specified edges of this view using an amount that’s appropriate for the current scene.
- [func listRowSpacing(CGFloat?) -> some View](./view/listrowspacing%28_%29.md)
  Sets the vertical spacing between two adjacent rows in a List.
- [func listSectionSpacing(_:)](./view/listsectionspacing%28_%29.md)
  Sets the spacing between adjacent sections in a [`List`](./list.md) to a custom value.
- [func listSectionMargins(Edge.Set, CGFloat?) -> some View](./view/listsectionmargins%28_,_%29.md)
  Set the section margins for the specific edges.
### Grid configuration
- [func gridCellColumns(Int) -> some View](./view/gridcellcolumns%28_%29.md)
  Tells a view that acts as a cell in a grid to span the specified number of columns.
- [func gridCellAnchor(UnitPoint) -> some View](./view/gridcellanchor%28_%29.md)
  Specifies a custom alignment anchor for a view that acts as a grid cell.
- [func gridCellUnsizedAxes(Axis.Set) -> some View](./view/gridcellunsizedaxes%28_%29.md)
  Asks grid layouts not to offer the view extra size in the specified axes.
- [func gridColumnAlignment(HorizontalAlignment) -> some View](./view/gridcolumnalignment%28_%29.md)
  Overrides the default horizontal alignment of the grid column that the view appears in.
### Safe area and margins
- [func ignoresSafeArea(SafeAreaRegions, edges: Edge.Set) -> some View](./view/ignoressafearea%28_,edges%29.md)
  Expands the safe area of a view.
- [func ignoresSafeArea(SafeAreaRegions, edges: Edge.Set, alignment: Alignment?) -> some View](./view/ignoressafearea%28_,edges,alignment%29.md)
  Expands the safe area of a view aligning content within the new bounds using the provided alignment.
- [func safeAreaInset(edge:alignment:spacing:content:)](./view/safeareainset%28edge,alignment,spacing,content%29.md)
  Shows the specified content beside the modified view.
- [func safeAreaBar(edge:alignment:spacing:content:)](./view/safeareabar%28edge,alignment,spacing,content%29.md)
  Shows the specified content as a custom bar beside the modified view.
- [func safeAreaPadding(_:)](./view/safeareapadding%28_%29.md)
  Adds the provided insets into the safe area of this view.
- [func safeAreaPadding(Edge.Set, CGFloat?) -> some View](./view/safeareapadding%28_,_%29.md)
  Adds the provided insets into the safe area of this view.
- [func contentMargins(CGFloat, for: ContentMarginPlacement) -> some View](./view/contentmargins%28_,for%29.md)
  Configures the content margin for a provided placement.
- [func contentMargins(_:_:for:)](./view/contentmargins%28_,_,for%29.md)
  Configures the content margin for a provided placement.
### Arrangement views
- [func arrangementViewStyle(some ArrangementViewStyle) -> some View](./view/arrangementviewstyle%28_%29.md)
  Sets the style for arrangement views within this view.
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
### Layer order
- [func zIndex(Double) -> some View](./view/zindex%28_%29.md)
  Controls the display order of overlapping views.
### Layout direction
- [func layoutDirectionBehavior(LayoutDirectionBehavior) -> some View](./view/layoutdirectionbehavior%28_%29.md)
  Sets the behavior of this view for different layout directions.
### Custom layout characteristics
- [func layoutValue<K>(key: K.Type, value: K.Value) -> some View](./view/layoutvalue%28key,value%29.md)
  Associates a value with a custom layout property.
- [func containerValue<V>(WritableKeyPath<ContainerValues, V>, V) -> some View](./view/containervalue%28_,_%29.md)
  Sets a particular container value of a view.

## See Also

### Drawing views
- [Style modifiers](./view-style-modifiers.md)
  Apply built-in styles to different types of views.
- [Graphics and rendering modifiers](./view-graphics-and-rendering.md)
  Affect the way the system draws a view, for example by scaling or masking a view, or by applying graphical effects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view-layout)*