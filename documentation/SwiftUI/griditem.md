# GridItem

**Framework**: SwiftUI  
**Kind**: struct

A description of a row or a column in a lazy grid.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
struct GridItem
```

#### Overview

Use an array of `GridItem` instances to configure the layout of items in a lazy grid. Each grid item in the array specifies layout properties like size and spacing for the rows of a [`LazyHGrid`](lazyhgrid.md) or the columns of a [`LazyVGrid`](lazyvgrid.md). The following example defines four rows for a horizontal grid, each with different characteristics:

```swift
struct GridItemDemo: View {
    let rows = [
        GridItem(.fixed(30), spacing: 1),
        GridItem(.fixed(60), spacing: 10),
        GridItem(.fixed(90), spacing: 20),
        GridItem(.fixed(10), spacing: 50)
    ]

    var body: some View {
        ScrollView(.horizontal) {
            LazyHGrid(rows: rows, spacing: 5) {
                ForEach(0...300, id: \.self) { _ in
                    Color.red.frame(width: 30)
                    Color.green.frame(width: 30)
                    Color.blue.frame(width: 30)
                    Color.yellow.frame(width: 30)
                }
            }
        }
    }
}
```

A lazy horizontal grid sets the width of each column based on the widest cell in the column. It can do this because it has access to all of the views in a given column at once. In the example above, the [`Color`](color.md) views always have the same fixed width, resulting in a uniform column width across the whole grid.

However, a lazy horizontal grid doesn’t generally have access to all the views in a row, because it generates new cells as people scroll through information in your app. Instead, it relies on a grid item for information about each row. The example above indicates a different fixed height for each row, and sets a different amount of spacing to appear after each row:

![A screenshot of a grid of rectangles arranged in four rows and a large](https://docs-assets.developer.apple.com/published/ff94e7d6f74fa48a46bcef0b7636b5f4/GridItem-1-iOS%402x.png)

## Topics

### Creating a grid item
- [init(GridItem.Size, spacing: CGFloat?, alignment: Alignment?)](griditem/init(_:spacing:alignment:).md)
  Creates a grid item with the specified size, spacing, and alignment.
### Inspecting grid item properties
- [var alignment: Alignment?](griditem/alignment.md)
  The alignment to use when placing each view.
- [var spacing: CGFloat?](griditem/spacing.md)
  The spacing to the next item.
- [var size: GridItem.Size](griditem/size-swift.property.md)
  The size of the item, which is the width of a column item or the height of a row item.
- [GridItem.Size](griditem/size-swift.enum.md)
  The size in the minor axis of one or more rows or columns in a grid layout.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct LazyHGrid](lazyhgrid.md)
  A container view that arranges its child views in a grid that grows horizontally, creating items only as needed.
- [struct LazyVGrid](lazyvgrid.md)
  A container view that arranges its child views in a grid that grows vertically, creating items only as needed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/griditem)*