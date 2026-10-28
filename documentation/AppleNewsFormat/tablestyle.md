# TableStyle

**Framework**: AppleNewsFormat  
**Kind**: dictionary  
**Role**: Object

The object for defining a style for rows, columns, cells, and headers in a table.

**Availability**:
- Apple News Format 1.7+

## Declaration

```
object TableStyle
```

## Mentions

- [Adding a JSON Table](../AppleNews/adding-a-json-table.md)
- [Adding an HTML Table](../AppleNews/adding-an-html-table.md)
- [Defining and Using Table Styles](../AppleNews/defining-and-using-table-styles.md)
- [Enhancing Your Articles with Styles](../AppleNews/enhancing-your-articles-with-styles.md)

## Discussion

You can style rows, columns, and cells including headers, and also apply conditions to customize your table. For example, you can display a different color for an even row by applying `rows.conditional`.

You can use this object in [`ComponentStyle`](./componentstyle.md).

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

- `cells` (TableCellStyle): Defines the styling for individual cells in a table.
- `columns` (TableColumnStyle): Defines the styling for table columns.
- `headerCells` (TableCellStyle): Defines the styling for individual cells in table headers.
- `headerColumns` (TableColumnStyle): Defines the styling for the table header columns, which are present if `dataOrientation` is  `vertical`, which is the default.
- `headerRows` (TableRowStyle): Defines the styling for table header rows, which are present if `dataOrientation` is  `horizontal`, which is not the default.
- `rows` (TableRowStyle): Defines the styling for table rows.

## See Also

### Table Styles
- [Defining and Using Table Styles](../AppleNews/defining-and-using-table-styles.md)
  Apply table styles, such as borders and backgrounds, to the rows, columns, and cells in your HTML and JSON  tables.
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
- [object Padding](./padding.md)
  The object for defining space around the content in a table cell.
- [object FormattedText](./formattedtext.md)
  The object for specifying formatted text content and styling for captions in table cells.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applenewsformat/tablestyle)*