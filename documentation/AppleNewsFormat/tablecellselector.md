# TableCellSelector

**Framework**: AppleNewsFormat  
**Kind**: dictionary  
**Role**: Object

The object for defining conditions that apply a conditional style to a cell.

**Availability**:
- Apple News Format 1.7+

## Declaration

```
object TableCellSelector
```

#### Discussion

Use the `TableCellSelector` object to set the criteria for applying conditional styles to rows. For example, you could set criteria to select a cell at a specific location or to select cells for a certain data descriptor.

You can use this object in  [`ConditionalTableCellStyle`](./conditionaltablecellstyle.md).

##### Example

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
        "headerCells": {
          "padding": 5,
          "textStyle": {
            "fontWeight": "bold",
            "fontStyle": "normal"
          }
        },
        "cells": {
          "padding": 2,
          "conditional": [
            {
              "selectors": [
                {
                  "oddRows": true
                }
              ],
              "backgroundColor": "#eeeeee"
            }
          ]
        }
      }
    }
  }
}
```

## Properties

- `columnIndex` (integer): Specifies a column index. The leftmost column of data has an index of `0`.
- `descriptor` (string): Specifies the `identifier` of a specific data descriptor. All cells for this data descriptor will be selected. See [`DataDescriptor`](./datadescriptor.md).
- `evenColumns` (boolean): When `true`, selects the cells in even columns.
- `evenRows` (boolean): When `true`, selects the cells in even rows.
- `oddColumns` (boolean): When `true`, selects the cells in odd columns.
- `oddRows` (boolean): When `true`, selects the cells in odd rows.
- `rowIndex` (integer): Specifies a row index. The topmost row of data has an index of `0`.

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
- [object TableBorder](./tableborder.md)
  The object for setting borders for tables.
- [object TableStrokeStyle](./tablestrokestyle.md)
  The object for defining the color, width, and style of a stroke in a table.
- [object Padding](./padding.md)
  The object for defining space around the content in a table cell.
- [object FormattedText](./formattedtext.md)
  The object for specifying formatted text content and styling for captions in table cells.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applenewsformat/tablecellselector)*