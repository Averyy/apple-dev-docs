# TableBorder

**Framework**: AppleNewsFormat  
**Kind**: dictionary  
**Role**: Object

The object for setting borders for tables.

**Availability**:
- Apple News Format 1.8+

## Declaration

```
object TableBorder
```

#### Discussion

The `TableBorder` object defines a table cell border. The border style is the same for all sides of the table cell. Use a value of `false` for any side of a border that you don’t want to show.

##### Example

```json
{
  "componentStyles": {
    "exampleStyle": {
      "tableStyle": {
        "cells": {
          "border": {
            "all": {
              "width": 2,
              "color": "#ddd",
              "style": "solid"
            },
            "left": false,
            "right": false
          }
        }
      }
    }
  }
}
```

## Properties

- `all` (TableStrokeStyle): Defines the stroke properties of the border. You can’t set stroke properties for each side; you can only disable or enable the border for each side.
- `bottom` (boolean): Indicates whether Apple News applies the border to the bottom.

  **Default**: `true`
- `left` (boolean): Indicates whether Apple News applies the border to the left side.

  **Default**: `true`
- `right` (boolean): Indicates whether Apple News applies the border to the right side.

  **Default**: `true`
- `top` (boolean): Indicates whether Apple News applies the border to the top.

  **Default**: `true`

## See Also

### Table Styles
- [Defining and Using Table Styles](../AppleNews/defining-and-using-table-styles.md)
  Apply table styles, such as borders and backgrounds, to the rows, columns, and cells in your HTML and JSON  tables.
- [object TableStyle](./tablestyle.md)
  The object for defining a style for rows, columns, cells, and headers in a table.
- [object TableRowStyle](./tablerowstyle.md)
  The object for applying styles to rows in a table.
- [object ConditionalTableRowStyle](./conditionaltablerowstyle.md)
  The object for applying styles to table rows that meet certain conditions.
- [object TableRowSelector](./tablerowselector.md)
  The object for defining conditions that apply a conditional style to a row.
- [object TableColumnStyle](./tablecolumnstyle.md)
  The object for applying styles to columns in a table.
- [object ConditionalTableColumnStyle](./conditionaltablecolumnstyle.md)
  The object for applying styles to table columns that meet certain conditions.
- [object TableColumnSelector](./tablecolumnselector.md)
  The object for defining conditions that apply a conditional style to a column.
- [object TableCellStyle](./tablecellstyle.md)
  The object for applying styles to cells in a table.
- [object ConditionalTableCellStyle](./conditionaltablecellstyle.md)
  The object for applying a style to table cells that meet certain conditions.
- [object TableCellSelector](./tablecellselector.md)
  The object for defining conditions that apply a conditional style to a cell.
- [object TableStrokeStyle](./tablestrokestyle.md)
  The object for defining the color, width, and style of a stroke in a table.
- [object Padding](./padding.md)
  The object for defining space around the content in a table cell.
- [object FormattedText](./formattedtext.md)
  The object for specifying formatted text content and styling for captions in table cells.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applenewsformat/tableborder)*