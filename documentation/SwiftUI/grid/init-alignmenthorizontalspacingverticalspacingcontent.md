# init(alignment:horizontalSpacing:verticalSpacing:content:)

**Framework**: SwiftUI  
**Kind**: init

Creates a grid with the specified spacing, alignment, and child views.

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
init(alignment: Alignment = .center, horizontalSpacing: CGFloat? = nil, verticalSpacing: CGFloat? = nil, @ViewBuilder content: () -> Content)
```

#### Discussion

Use this initializer to create a [`Grid`](grid.md). Provide a content closure that defines the rows of the grid, and optionally customize the spacing between cells and the alignment of content within each cell. The following example customizes the spacing between cells:

```swift
Grid(horizontalSpacing: 30, verticalSpacing: 30) {
    ForEach(0..<5) { row in
        GridRow {
            ForEach(0..<5) { column in
                Text("(\(column), \(row))")
            }
        }
    }
}
```

You can list rows and the cells within rows directly, or you can use a [`ForEach`](foreach.md) structure to generate either, as the example above does:

![A screenshot of a grid that contains five rows and five columns.](https://docs-assets.developer.apple.com/published/ce1054ab05e5584be7d38afca7b369b3/Grid-init-1-iOS%402x.png)

By default, the grid’s alignment value applies to all of the cells in the grid. However, you can also change the alignment for particular cells or groups of cells:

- Override the vertical alignment for the cells in a row by specifying a [`VerticalAlignment`](verticalalignment.md) parameter to the corresponding row’s [`init(alignment:content:)`](gridrow/init(alignment:content:).md) initializer.
- Override the horizontal alignment for the cells in a column by adding a [`gridColumnAlignment(_:)`](view/gridcolumnalignment(_:).md) view modifier to exactly one of the cells in the column, and specifying a [`HorizontalAlignment`](horizontalalignment.md) parameter.
- Specify a custom alignment anchor for a particular cell by using the [`gridCellAnchor(_:)`](view/gridcellanchor(_:).md) modifier on the cell’s view.

## Parameters

- `alignment`: The guide for aligning the child views within the   space allocated for a given cell. The default is   .
- `horizontalSpacing`: The horizontal distance between each cell, given   in points. The value is   by default, which results in a   default distance between cells that’s appropriate for the platform.
- `verticalSpacing`: The vertical distance between each cell, given   in points. The value is   by default, which results in a   default distance between cells that’s appropriate for the platform.
- `content`: A closure that creates the grid’s rows.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/grid/init(alignment:horizontalspacing:verticalspacing:content:))*