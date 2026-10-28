# ConditionalTableColumnStyle

**Framework**: AppleNewsFormat  
**Kind**: dictionary  
**Role**: Object

The object for applying styles to table columns that meet certain conditions.

**Availability**:
- Apple News Format 1.7+

## Declaration

```
object ConditionalTableColumnStyle
```

## Discussion

Table columns can have conditional styles — styles applied to columns that meet certain conditions. You can use any table column style as a conditional style.

For example, you might define a conditional table column style that changes the background color for all odd-numbered columns.

You can use this object in [`TableColumnStyle`](./tablecolumnstyle.md).

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

- `backgroundColor` (Color): The background color for the column.

  If you omit this property, the background is transparent.

  The cell’s background color is highest priority, followed by column, and finally row. Apple News applies all three colors, meaning that non-opaque values can cause combined colors. For example, using a red row together with a blue column, both with 50% opacity, creates a purple cell.
- `divider` (TableStrokeStyle): The stroke style for the divider line to the right of the column.
- `minimumWidth` ((SupportedUnits | number)): The minimum width of the column as a number in points, or in one of the available units of measure for components. See [Specifying Measurements for Components](../AppleNews/specifying-measurements-for-components.md).

  **Allowed Types**: `SupportedUnits`, `number`
- `selectors` ([TableColumnSelector]) *(required)*: An array of one or more selectors, each of which specifies one or more conditions.

  Apple News applies this conditional table column style to columns that meet all of the conditions of at least one of the selectors.
- `width` (integer): The relative column width. This value influences the distribution of column width but doesn’t dictate any exact values. To set an exact minimum width, use `minimumWidth` instead.

  It might be useful to think of the value of `width` as a percentage of the component’s width. For example, if you want one column’s width to be about half that of the whole component, and another to be about a quarter of the component width, use values of `50` and `25`.

## Relationships

### Inherits From
- [TableColumnStyle](./tablecolumnstyle.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/applenewsformat/conditionaltablecolumnstyle)*