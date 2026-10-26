# Padding

**Framework**: AppleNewsFormat  
**Kind**: dictionary  
**Role**: Object

The object for defining space around the content in a table cell.

**Availability**:
- Apple News Format 1.7+

## Declaration

```
object Padding
```

#### Discussion

Use cell padding to add space around the content in the cell. For example, you can set the amount of padding between the right side of the cell and the content, or the left side of the cell and the content.

You can use this object in [`TableCellStyle`](./tablecellstyle.md) and [`ConditionalTableCellStyle`](./conditionaltablecellstyle.md).

##### Example

```json
{
  "componentStyles": {
    "exampleForTables": {
      "tableStyle": {
        "cells": {
          "verticalAlignment": "top",
          "padding": {
            "left": 6,
            "right": 6,
            "bottom": 4,
            "top": 2
          }
        }
      }
    }
  }
}
```

## Properties

- `bottom` ((SupportedUnits | number)): The amount of padding between the bottom of the cell and the content, as a number in points or using the available units for components. See [Specifying Measurements for Components](../AppleNews/specifying-measurements-for-components.md).

  **Allowed Types**: `SupportedUnits`, `number`
- `left` ((SupportedUnits | number)): The amount of padding between the left side of the cell and the content, as a number in points or using the available units for components.

  **Allowed Types**: `SupportedUnits`, `number`
- `right` ((SupportedUnits | number)): The amount of padding between the right side of the cell and the content, as as a number in points or using the available units for components.

  **Allowed Types**: `SupportedUnits`, `number`
- `top` ((SupportedUnits | number)): The amount of padding between the top of the cell and the content, as a number in points or using the available units for components.

  **Allowed Types**: `SupportedUnits`, `number`

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
- [object TableBorder](./tableborder.md)
  The object for setting borders for tables.
- [object TableStrokeStyle](./tablestrokestyle.md)
  The object for defining the color, width, and style of a stroke in a table.
- [object FormattedText](./formattedtext.md)
  The object for specifying formatted text content and styling for captions in table cells.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applenewsformat/padding)*