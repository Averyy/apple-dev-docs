# TableRowStyle

**Framework**: AppleNewsFormat  
**Kind**: dictionary  
**Role**: Object

The object for applying styles to rows in a table.

**Availability**:
- Apple News Format 1.7+

## Declaration

```
object TableRowStyle
```

#### Discussion

You can apply styles that affect the look of the table rows, including the row background color, the color of the divider lines between rows, and the height of a row. For example, you could add a blue background color and apply a medium-gray divider to each row in your table.

You can also set up conditional row styles — styles applied only to rows that meet certain criteria. For example, you could apply a background shading to all odd-numbered rows. See [`ConditionalTableRowStyle`](./conditionaltablerowstyle.md).

You can use this object in [`TableStyle`](./tablestyle.md).

##### Example

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

- `backgroundColor` (Color): The background color for the table row.

  If you omit this property, the background is transparent.

  The cell background color is highest priority, followed by the column, and finally the row. Apple News applies all three colors, meaning that non-opaque values can cause combined colors. For example, using a red row together with a blue column, both with 50% opacity, creates a purple cell.
- `conditional` ([ConditionalTableRowStyle]): An array of styles you apply to rows that meet specified conditions. You can use this to create a table with alternating row background colors.
- `divider` (TableStrokeStyle): The stroke style for the divider lines between rows.
- `height` ((SupportedUnits | number)): The height of the table row, as a number in points, or using the available units for components.

  By default, the height of each row is determined by the height of the content in that row. See [Specifying Measurements for Components](../AppleNews/specifying-measurements-for-components.md)

  **Allowed Types**: `SupportedUnits`, `number`

## Relationships

### Inherited By
- [ConditionalTableRowStyle](./conditionaltablerowstyle.md)

## See Also

### Table Styles
- [Defining and Using Table Styles](../AppleNews/defining-and-using-table-styles.md)
  Apply table styles, such as borders and backgrounds, to the rows, columns, and cells in your HTML and JSON  tables.
- [object TableStyle](./tablestyle.md)
  The object for defining a style for rows, columns, cells, and headers in a table.
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
- [object Padding](./padding.md)
  The object for defining space around the content in a table cell.
- [object FormattedText](./formattedtext.md)
  The object for specifying formatted text content and styling for captions in table cells.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applenewsformat/tablerowstyle)*