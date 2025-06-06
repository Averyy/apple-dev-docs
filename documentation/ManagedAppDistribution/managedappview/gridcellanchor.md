# gridCellAnchor(_:)

**Framework**: ManagedAppDistribution  
**Kind**: method

Specifies a custom alignment anchor for a view that acts as a grid cell.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- macOS 13.0+
- tvOS 16.0+
- watchOS 9.0+

## Declaration

```swift
nonisolated
func gridCellAnchor(_ anchor: UnitPoint) -> some View
```

#### Return Value

A view that uses the specified anchor point to align its content.

#### Discussion

Grids, like stacks and other layout containers, perform most alignment operations using alignment guides. The grid moves the contents of each cell in a row in the y direction until the specified `VerticalAlignment` guide of each view in the row aligns with the same guide of all the other views in the row. Similarly, the grid aligns the `HorizontalAlignment` guides of views in a column by adjusting views in the x direction. See the guide types for more information about typical SwiftUI alignment operations.

When you use the `gridCellAnchor(_:)` modifier on a view in a grid, the grid changes to an anchor-based alignment strategy for the associated cell. With anchor alignment, the grid projects a `UnitPoint` that you specify onto both the view and the cell, and aligns the two projections. For example, consider the following grid:

```None
Grid(horizontalSpacing: 1, verticalSpacing: 1) {
    GridRow {
        Color.red.frame(width: 60, height: 60)
        Color.red.frame(width: 60, height: 60)
    }
    GridRow {
        Color.red.frame(width: 60, height: 60)
        Color.blue.frame(width: 10, height: 10)
            .gridCellAnchor(UnitPoint(x: 0.25, y: 0.75))
    }
}
```

The grid creates red reference squares in the first row and column to establish row and column sizes. Without the anchor modifier, the blue marker in the remaining cell would appear at the center of its cell, because of the grid’s default `Alignment/center` alignment. With the anchor modifier shown in the code above, the grid aligns the one quarter point of the marker with the one quarter point of its cell in the x direction, as measured from the origin at the top left of the cell. The grid also aligns the three quarters point of the marker with the three quarters point of the cell in the y direction:

`UnitPoint` defines many convenience points that correspond to the typical alignment guides, which you can use as well. For example, you can use `UnitPoint/topTrailing` to align the top and trailing edges of a view in a cell with the top and trailing edges of the cell:

```None
Color.blue.frame(width: 10, height: 10)
    .gridCellAnchor(.topTrailing)
```

Applying the anchor-based alignment strategy to a single cell doesn’t affect the alignment strategy that the grid uses on other cells.

##### Anchor Alignment for Merged Cells

If you use the `View/gridCellColumns(_:)` modifier to cause a cell to span more than one column, or if you place a view in a grid outside of a row so that the view spans the entire grid, the grid automatically converts its vertical and horizontal alignment guides to the unit point equivalent for the merged cell, and uses an anchor-based approach for that cell. For example, the following grid places the marker at the center of the merged cell by converting the grid’s default `Alignment/center` alignment guide to a `UnitPoint/center` anchor for the blue marker in the merged cell:

```None
Grid(alignment: .center, horizontalSpacing: 1, verticalSpacing: 1) {
    GridRow {
        Color.red.frame(width: 60, height: 60)
        Color.red.frame(width: 60, height: 60)
        Color.red.frame(width: 60, height: 60)
    }
    GridRow {
        Color.red.frame(width: 60, height: 60)
        Color.blue.frame(width: 10, height: 10)
            .gridCellColumns(2)
    }
}
```

The grid makes this conversion in part to avoid ambiguity. Each column has its own horizontal guide, and it isn’t clear which of these a cell that spans multiple columns should align with. Further, in the example above, neither of the center alignment guides for the second or third column would provide the expected behavior, which is to center the marker in the merged cell. Anchor alignment provides this behavior:

## Parameters

- `anchor`: The unit point that defines how to align the view   within the bounds of its grid cell.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedappdistribution/managedappview/gridcellanchor(_:))*