# Grid

**Framework**: SwiftUI  
**Kind**: struct

A container view that arranges other views in a two dimensional layout.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
@frozen
struct Grid<Content> where Content : View
```

#### Overview

Create a two dimensional layout by initializing a `Grid` with a collection of [`GridRow`](gridrow.md) structures. The first view in each grid row appears in the grid’s first column, the second view in the second column, and so on. The following example creates a grid with two rows and two columns:

```swift
Grid {
    GridRow {
        Text("Hello")
        Image(systemName: "globe")
    }
    GridRow {
        Image(systemName: "hand.wave")
        Text("World")
    }
}
```

A grid and its rows behave something like a collection of [`HStack`](hstack.md) instances wrapped in a [`VStack`](vstack.md). However, the grid handles row and column creation as a single operation, which applies alignment and spacing to cells, rather than first to rows and then to a column of unrelated rows. The grid produced by the example above demonstrates this:

![A screenshot of items arranged in a grid. The upper-left](https://docs-assets.developer.apple.com/published/6ce3d6ec21845fdf9aab2ca5cbe95f03/Grid-1-iOS%402x.png)

> **Note**: If you need a grid that conforms to the [`Layout`](layout.md) protocol, like when you want to create a conditional layout using [`AnyLayout`](anylayout.md), use [`GridLayout`](gridlayout.md) instead.

##### Multicolumn Cells

If you provide a view rather than a [`GridRow`](gridrow.md) as an element in the grid’s content, the grid uses the view to create a row that spans all of the grid’s columns. For example, you can add a [`Divider`](divider.md) between the rows of the previous example:

```swift
Grid {
    GridRow {
        Text("Hello")
        Image(systemName: "globe")
    }
    Divider()
    GridRow {
        Image(systemName: "hand.wave")
        Text("World")
    }
}
```

Because a divider takes as much horizontal space as its parent offers, the entire grid widens to fill the width offered by its parent view.

![A screenshot of items arranged in a grid. The upper-left](https://docs-assets.developer.apple.com/published/f20954fd2b30390306220984d444d0cf/Grid-2-iOS%402x.png)

To prevent a flexible view from taking more space on a given axis than the other cells in a row or column require, add the [`gridCellUnsizedAxes(_:)`](view/gridcellunsizedaxes(_:).md) view modifier to the view:

```swift
Divider()
    .gridCellUnsizedAxes(.horizontal)
```

This restores the grid to the width that the text and images require:

![A screenshot of items arranged in a grid. The upper-left](https://docs-assets.developer.apple.com/published/f9a8d394b17ecb1bfd61218fb597b5d4/Grid-3-iOS%402x.png)

To make a cell span a specific number of columns rather than the whole grid, use the [`gridCellColumns(_:)`](view/gridcellcolumns(_:).md) modifier on a view that’s contained inside a [`GridRow`](gridrow.md).

##### Column Count

The grid’s column count grows to handle the row with the largest number of columns. If you create rows with different numbers of columns, the grid adds empty cells to the trailing edge of rows that have fewer columns. The example below creates three rows with different column counts:

```swift
Grid {
    GridRow {
        Text("Row 1")
        ForEach(0..<2) { _ in Color.red }
    }
    GridRow {
        Text("Row 2")
        ForEach(0..<5) { _ in Color.green }
    }
    GridRow {
        Text("Row 3")
        ForEach(0..<4) { _ in Color.blue }
    }
}
```

The resulting grid has as many columns as the widest row, adding empty cells to rows that don’t specify enough views:

![A screenshot of a grid with three rows and six columns. The first](https://docs-assets.developer.apple.com/published/dc6a493ef7b4cec08288741d2dfd6c0e/Grid-4-iOS%402x.png)

The grid sets the width of all the cells in a column to match the needs of column’s widest cell. In the example above, the width of the first column depends on the width of the widest [`Text`](text.md) view that the column contains. The other columns, which contain flexible [`Color`](color.md) views, share the remaining horizontal space offered by the grid’s parent view equally.

Similarly, the tallest cell in a row sets the height of the entire row. The cells in the first column of the grid above need only the height required for each string, but the [`Color`](color.md) cells expand to equally share the total height available to the grid. As a result, the color cells determine the row heights.

##### Cell Spacing and Alignment

You can control the spacing between cells in both the horizontal and vertical dimensions and set a default alignment for the content in all the grid cells when you initialize the grid using the [`init(alignment:horizontalSpacing:verticalSpacing:content:)`](grid/init(alignment:horizontalspacing:verticalspacing:content:).md) initializer. Consider a modified version of the previous example:

```swift
Grid(alignment: .bottom, horizontalSpacing: 1, verticalSpacing: 1) {
    // ...
}
```

This configuration causes all of the cells to use [`bottom`](alignment/bottom.md) alignment — which only affects the text cells because the colors fill their cells completely — and it reduces the spacing between cells:

![A screenshot of a grid with three rows and six columns. The first](https://docs-assets.developer.apple.com/published/e5e7c222929c7b2e53711620201fae32/Grid-5-iOS%402x.png)

You can override the alignment of specific cells or groups of cells. For example, you can change the horizontal alignment of the cells in a column by adding the [`gridColumnAlignment(_:)`](view/gridcolumnalignment(_:).md) modifier, or the vertical alignment of the cells in a row by configuring the row’s [`init(alignment:content:)`](gridrow/init(alignment:content:).md) initializer. You can also align a single cell with the [`gridCellAnchor(_:)`](view/gridcellanchor(_:).md) modifier.

##### Performance Considerations

A grid can size its rows and columns correctly because it renders all of its child views immediately. If your app exhibits poor performance when it first displays a large grid that appears inside a [`ScrollView`](scrollview.md), consider switching to a [`LazyVGrid`](lazyvgrid.md) or [`LazyHGrid`](lazyhgrid.md) instead.

Lazy grids render their cells when SwiftUI needs to display them, rather than all at once. This reduces the initial cost of displaying a large scrollable grid that’s never fully visible, but also reduces the grid’s ability to optimally lay out cells. Switch to a lazy grid only if profiling your code shows a worthwhile performance improvement.

## Topics

### Creating a grid
- [init(alignment: Alignment, horizontalSpacing: CGFloat?, verticalSpacing: CGFloat?, content: () -> Content)](grid/init(alignment:horizontalspacing:verticalspacing:content:).md)
  Creates a grid with the specified spacing, alignment, and child views.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [View](view.md)

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/grid)*