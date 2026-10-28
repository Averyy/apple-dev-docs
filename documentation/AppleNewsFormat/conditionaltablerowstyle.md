# ConditionalTableRowStyle

**Framework**: AppleNewsFormat  
**Kind**: dictionary  
**Role**: Object

The object for applying styles to table rows that meet certain conditions.

**Availability**:
- Apple News Format 1.7+

## Declaration

```
object ConditionalTableRowStyle
```

## Discussion

Table rows can have conditional styles — styles applied only to rows that meet certain conditions. You can use any table row style as a conditional style.

For example, you might define a conditional table row style that changes the background color for all even-numbered rows.

You can use this object in [`TableRowStyle`](./tablerowstyle.md).

### Example

```json
{
  "components": [
    {
      "role": "datatable",
      "style": "exampleTableStyle",
      "showDescriptorLabels": true,
      "sortBy": [
        {
          "descriptor": "id-name",
          "direction": "descending"
        }
      ],
      "data": {
        "descriptors": [
          {
            "identifier": "id-name",
            "key": "name",
            "label": {
              "type": "formatted_text",
              "text": "Name",
              "textStyle": {
                "textColor": "black"
              }
            },
            "dataType": "string"
          },
          {
            "identifier": "id-occupation",
            "key": "occupation",
            "label": "Occupation",
            "dataType": "string"
          }
        ],
        "records": [
          {
            "name": "Amelia Earhart",
            "occupation": "Pilot"
          },
          {
            "name": "Grace Hopper",
            "occupation": "Computer Scientist"
          }
        ]
      }
    }
  ],
  "componentStyles": {
    "exampleTableStyle": {
      "tableStyle": {
        "rows": {
          "backgroundColor": "#fff",
          "divider": {
            "width": 1,
            "color": "#ddd"
          },
          "conditional": [
            {
              "selectors": [
                {
                  "even": true
                }
              ],
              "backgroundColor": "#eeeeee"
            }
          ]
        },
        "headerRows": {
          "backgroundColor": "#ccc",
          "divider": {
            "width": 2,
            "color": "#999"
          }
        },
        "cells": {
          "padding": 6,
          "verticalAlignment": "top"
        }
      }
    }
  }
}
```

## Properties

- `backgroundColor` (Color): The background color for the row.

  If you omit this property, the background is transparent.

  The cell’s background color is highest priority, followed by column, and finally row. Apple News applies all three colors, meaning that non-opaque values can cause combined colors. For example, using a red row together with a blue column, both with 50% opacity, creates a purple cell.
- `divider` (TableStrokeStyle): The stroke style for the divider line below the row.
- `height` ((SupportedUnits | number)): The height of the row, as a number in points, or using one of the available units of measure for components. See [Specifying Measurements for Components](../AppleNews/specifying-measurements-for-components.md).

  By default, the height of each row is determined by the height of the content in that row.

  **Allowed Types**: `SupportedUnits`, `number`
- `selectors` ([TableRowSelector]) *(required)*: An array of one or more selectors, each of which specifies one or more conditions.

  Apple News applies this conditional table row style to rows that meet all of the conditions of at least one of these selectors.

## Relationships

### Inherits From
- [TableRowStyle](./tablerowstyle.md)

## See Also

### Table Styles
- [Defining and Using Table Styles](../AppleNews/defining-and-using-table-styles.md)
  Apply table styles, such as borders and backgrounds, to the rows, columns, and cells in your HTML and JSON  tables.
- [object TableStyle](./tablestyle.md)
  The object for defining a style for rows, columns, cells, and headers in a table.
- [object TableRowStyle](./tablerowstyle.md)
  The object for applying styles to rows in a table.
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
- [object Padding](./padding.md)
  The object for defining space around the content in a table cell.
- [object FormattedText](./formattedtext.md)
  The object for specifying formatted text content and styling for captions in table cells.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applenewsformat/conditionaltablerowstyle)*