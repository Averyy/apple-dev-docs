# Adding tables to attributed strings in UIKit

**Framework**: UIKit

Create and configure tables in attributed strings and display them in a text view.

#### Overview

[`NSTextTable`](nstexttable.md) and its related classes let you embed tables of rows and columns directly into [`NSAttributedString`](https://developer.apple.com/documentation/Foundation/NSAttributedString) objects on all Apple platforms. [`NSAttributedString`](https://developer.apple.com/documentation/Foundation/NSAttributedString) stores a string together with per-character formatting attributes — such as fonts, colors, and paragraph styles — and is the primary text type for UIKit text views. You build a table from three objects:

- **[`NSTextTable`](nstexttable.md)** represents the table as a whole and defines the column count and layout algorithm.
- **[`NSTextTableBlock`](nstexttableblock.md)** represents a single cell and records the cell’s row, column, and span values. It belongs to a parent table.
- **[`NSTextBlock`](nstextblock.md)** is the base class, and it defines the visual properties (background color, border, padding, margin) that both tables and individual cells share.

You build a table by creating one [`NSTextTable`](nstexttable.md), then creating one [`NSTextTableBlock`](nstexttableblock.md) per cell and assigning each block to a paragraph in the attributed string using [`textBlocks`](nsparagraphstyle/textblocks.md). The text system reads the [`textBlocks`](nsparagraphstyle/textblocks.md) array of adjacent paragraphs to determine the table’s structure.

##### Create the Table and Its Cells

Start by creating the table and configuring its column count. The following code shows how to create a table with three equally sized columns and enable collapsed borders so adjacent cells share a single border line:

```swift
let table = NSTextTable()
table.numberOfColumns = 3
table.collapsesBorders = true
```

Then create a block for each cell, specifying its position and span within the table. The following helper function creates a cell at the specified row and column, sets its width to one-third of the available space, and applies a light gray background, a separator-colored 1-point border, and 4 points of padding on all edges:

```swift
func makeCell(row: Int, column: Int, in table: NSTextTable) -> NSTextTableBlock {
    let cell = NSTextTableBlock(
        table: table,
        startingRow: row, rowSpan: 1,
        startingColumn: column, columnSpan: 1
    )
    cell.setContentWidth(33, type: .percentage)
    cell.backgroundColor = UIColor.secondarySystemBackground
    cell.setBorderColor(.separator)
    cell.setWidth(1, type: .absolute, for: .border)
    cell.setWidth(4, type: .absolute, for: .padding)
    return cell
}
```

##### Apply Cells to Paragraphs

Each cell maps to exactly one paragraph in the attributed string. Assign the cell block to that paragraph using `NSMutableParagraphStyle.textBlocks`. The following code builds a 2×3 table — two rows and three columns — by creating a cell block for each position and appending a styled paragraph for each cell to the attributed string:

```swift
let string = NSMutableAttributedString()

for row in 0..<2 {
    for column in 0..<3 {
        let cell = makeCell(row: row, column: column, in: table)

        let style = NSMutableParagraphStyle()
        style.textBlocks = [cell]

        let cellText = NSAttributedString(
            string: "Row \(row), Col \(column)\n",
            attributes: [.paragraphStyle: style]
        )
        string.append(cellText)
    }
}
```

The [`textBlocks`](nsparagraphstyle/textblocks.md) array is ordered from outermost to innermost block. For a table without nested blocks, each cell paragraph has a single-element array.

##### Configure Per Edge Widths and Colors

You can set widths and border colors independently for each edge using [`setWidth(_:type:for:rectEdge:)`](nstextblock/setwidth(_:type:for:rectedge:).md) and [`setBorderColor(_:rectEdge:)`](nstextblock/setbordercolor(_:rectedge:).md). For example, the following code applies a 2-point blue border to the bottom edge of a cell, leaving the other edges unchanged:

```swift
cell.setWidth(2, type: .absolute, for: .border, rectEdge: .maxYEdge)
cell.setBorderColor(.systemBlue, rectEdge: .maxYEdge)
```

Use the [`CGRectEdge`](https://developer.apple.com/documentation/CoreFoundation/CGRectEdge) values [`CGRectEdge.minXEdge`](https://developer.apple.com/documentation/CoreFoundation/CGRectEdge/minXEdge) (leading), [`CGRectEdge.maxXEdge`](https://developer.apple.com/documentation/CoreFoundation/CGRectEdge/maxXEdge) (trailing), [`CGRectEdge.minYEdge`](https://developer.apple.com/documentation/CoreFoundation/CGRectEdge/minYEdge) (top), and [`CGRectEdge.maxYEdge`](https://developer.apple.com/documentation/CoreFoundation/CGRectEdge/maxYEdge) (bottom).

To support iOS 26 and earlier, use [`setWidth(_:type:for:)`](nstextblock/setwidth(_:type:for:).md) and [`setBorderColor(_:)`](nstextblock/setbordercolor(_:).md) to apply a uniform width or color to all edges.

##### Choose a Layout Algorithm

By default, [`NSTextTable.LayoutAlgorithm.automatic`](nstexttable/layoutalgorithm-swift.enum/automatic.md) distributes width based on content. Use [`NSTextTable.LayoutAlgorithm.automatic`](nstexttable/layoutalgorithm-swift.enum/automatic.md) when you want your column widths to adapt to the content — for example, a label-value table where short labels sit beside values that vary in length.

If you want consistent, predictable column widths regardless of content length, use [`NSTextTable.LayoutAlgorithm.fixed`](nstexttable/layoutalgorithm-swift.enum/fixed.md), which distributes width based on the explicit [`contentWidth`](nstextblock/contentwidth.md) values set on the first row of cells. For example, if your app displays a data grid where each column always occupies one-third of the available width, set each first-row cell to 33 percent and switch to fixed layout:

```swift
table.layoutAlgorithm = .fixed
```

##### Display the Result

Assign the attributed string to a [`UITextView`](uitextview.md) to render the table. The text system reads the paragraph style information embedded in the string to interpret the table structure automatically, so no extra configuration of the view is required:

```swift
textView.attributedText = string
```

## See Also

- [class NSParagraphStyle](nsparagraphstyle.md)
  The paragraph or ruler attributes for an attributed string.
- [class NSMutableParagraphStyle](nsmutableparagraphstyle.md)
  An object for changing the values of the subattributes in a paragraph style attribute.
- [class NSTextTab](nstexttab.md)
  A tab in a paragraph.
- [class NSTextList](nstextlist.md)
  A section of text that forms a single list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/adding-tables-to-attributed-strings)*