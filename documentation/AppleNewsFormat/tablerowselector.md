# TableRowSelector

**Framework**: AppleNewsFormat  
**Kind**: dictionary  
**Role**: Object

The object for defining conditions that apply a conditional style to a row.

**Availability**:
- Apple News Format 1.7+

## Declaration

```
object TableRowSelector
```

#### Discussion

Use the `TableRowSelector` object to set the criteria for applying conditional styles to rows. For example, you could set criteria to select all odd rows, all even rows, or a single row.

You can use this object in [`ConditionalTableRowStyle`](./conditionaltablerowstyle.md).

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

- `descriptor` (string): A string that specifies the identifier of a specific data descriptor. All rows for this data descriptor are selected. See [`DataDescriptor`](./datadescriptor.md).

  When `dataOrientation` is `horizontal`, which is not the default each row displays data for one data descriptor. See [`DataTable`](./datatable.md).
- `even` (boolean): A Boolean value when `true`; selects the even rows.
- `odd` (boolean): A Boolean value when `true`; selects the odd rows.
- `rowIndex` (integer): A number that specifies a row index. The topmost row of data has an index of `0`. The specified column is selected.

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

*[View on Apple Developer](https://developer.apple.com/documentation/applenewsformat/tablerowselector)*