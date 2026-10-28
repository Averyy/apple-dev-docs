# TableColumnSelector

**Framework**: AppleNewsFormat  
**Kind**: dictionary  
**Role**: Object

The object for defining conditions that apply a conditional style to a column.

**Availability**:
- Apple News Format 1.7+

## Declaration

```
object TableColumnSelector
```

## Discussion

Use the `TableColumnSelector` object to set the criteria for applying conditional styles to columns. For example, you could set the criteria to select all even columns or to select columns for certain data descriptors.

You can use this object in [`ConditionalTableColumnStyle`](./conditionaltablecolumnstyle.md).

### Example

```json
{
  "components": [
    {
      "role": "datatable",
      "style": "bookTableStyle",
      "showDescriptorLabels": true,
      "sortBy": [
        {
          "descriptor": "id-publication-date",
          "direction": "ascending"
        }
      ],
      "data": {
        "descriptors": [
          {
            "identifier": "id-publication-date",
            "key": "publicationDate",
            "label": "Date",
            "dataType": "string"
          },
          {
            "identifier": "id-title",
            "key": "title",
            "label": "Title",
            "dataType": "string"
          },
          {
            "identifier": "id-publisher",
            "key": "publisher",
            "label": "Publisher",
            "dataType": "string"
          }
        ],
        "records": [
          {
            "title": "Mardi",
            "publicationDate": "1849",
            "publisher": "Harper & Brothers"
          },
          {
            "title": "Typee",
            "publicationDate": "1846",
            "publisher": "Wiley and Putnam"
          },
          {
            "title": "White-Jacket",
            "publicationDate": "1850",
            "publisher": "Harper & Brothers"
          },
          {
            "title": "Omoo",
            "publicationDate": "1847",
            "publisher": "Harper & Brothers"
          },
          {
            "title": "Redburn",
            "publicationDate": "1849",
            "publisher": "Harper & Brothers"
          },
          {
            "title": "Moby-Dick",
            "publicationDate": "1851",
            "publisher": "Harper & Brothers"
          }
        ]
      }
    }
  ],
  "componentStyles": {
    "bookTableStyle": {
      "tableStyle": {
        "columns": {
          "backgroundColor": "#eeeeee",
          "conditional": [
            {
              "selectors": [
                {
                  "columnIndex": 0
                }
              ],
              "backgroundColor": "#dddddd"
            }
          ]
        },
        "headerCells": {
          "padding": 5,
          "textStyle": {
            "fontWeight": "bold"
          }
        },
        "cells": {
          "padding": 2
        }
      }
    }
  }
}
```

## Properties

- `columnIndex` (integer): A number that specifies a column index. The leftmost column of data has an index of `0`. Only the column with the specific index is selected.
- `descriptor` (string): A number that specifies the `identifier` of a specific data descriptor. All columns for this data descriptor are selected. See [`DataDescriptor`](./datadescriptor.md).

  When `dataOrientation` is set to `vertical`, which is the default, each column displays data for one data descriptor. See [`DataTable`](./datatable.md).
- `even` (boolean): A Boolean value when `true`; selects the even columns.
- `odd` (boolean): A Boolean value when `true`; selects the odd columns.

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

*[View on Apple Developer](https://developer.apple.com/documentation/applenewsformat/tablecolumnselector)*