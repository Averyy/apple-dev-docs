# TableStrokeStyle

**Framework**: AppleNewsFormat  
**Kind**: dictionary  
**Role**: Object

The object for defining the color, width, and style of a stroke in a table.

**Availability**:
- Apple News Format 1.8+

## Declaration

```
object TableStrokeStyle
```

## Discussion

You can specify the `color`, `style` (`solid`), and `width` of a stroke in a table. For example, apply style to divider lines between rows.

### Example

```json
{
  "componentStyles": {
    "exampleStyle": {
      "tableStyle": {
        "rows": {
          "backgroundColor": "#fff",
          "divider": {
            "width": 1,
            "color": "#ddd"
          }
        }
      }
    }
  }
}
```

## Properties

- `color` (Color): The stroke color. The value defaults to `#000` (black).
- `style` (string): The style of the stroke.

  **Allowed Values**: `solid`
- `width` ((SupportedUnits | number)): The width of the stroke line.

  **Default**: `1`; **Allowed Types**: `SupportedUnits`, `number`

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
- [object Padding](./padding.md)
  The object for defining space around the content in a table cell.
- [object FormattedText](./formattedtext.md)
  The object for specifying formatted text content and styling for captions in table cells.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applenewsformat/tablestrokestyle)*