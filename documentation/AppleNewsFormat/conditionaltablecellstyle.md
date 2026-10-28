# ConditionalTableCellStyle

**Framework**: AppleNewsFormat  
**Kind**: dictionary  
**Role**: Object

The object for applying a style to table cells that meet certain conditions.

**Availability**:
- Apple News Format 1.7+

## Declaration

```
object ConditionalTableCellStyle
```

## Discussion

Cells in Data Table components and HTML Table components can have conditional styles — styles applied only to cells that meet certain conditions. You can use any table cell style as a conditional style.

For example, you might define a conditional table cell style that changes the background color for a cell at a specific location.

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
                  "columnIndex": 1
                }
              ],
              "textStyle": {
                "fontStyle": "italic"
              }
            }
          ]
        }
      }
    }
  }
}
```

## Properties

- `backgroundColor` (Color): The background color for the cell.

  If you omit this property, the background is transparent.

  The cell background color is highest priority, followed by the column, and finally the row. Apple News applies all three colors, meaning that non-opaque values can cause combined colors. For example, using a red row together with a blue column, both with 50% opacity, creates a purple cell.
- `border` (TableBorder): The border for the cell. Because the border is inside the cell, it affects the size of the content within the cell. The bigger the border, the less available space for content.
- `height` ((SupportedUnits | number)): The height of the cell and its row, as a number in points, or using one of the available units of measure for components.

  By default, the height of each row is determined by the height of the content in that row. See [Specifying Measurements for Components](../AppleNews/specifying-measurements-for-components.md).

  **Allowed Types**: `SupportedUnits`, `number`
- `horizontalAlignment` (string): The horizontal alignment of content inside cells.

  **Default**: `left`; **Allowed Values**: `left`, `center`, `right`
- `minimumWidth` ((SupportedUnits | number)): The minimum width of the cell and its column, as a number in points or using one of the available units of measure for components.

  **Allowed Types**: `SupportedUnits`, `number`
- `padding` ((SupportedUnits | Padding | number)): The space around the content in a table cell in points, supported units, or a [`Padding`](./padding.md) object that specifies padding for each side separately.

  **Allowed Types**: `SupportedUnits`, `Padding`, `number`
- `selectors` ([TableCellSelector]) *(required)*: An array of one or more selectors, each of which specifies one or more conditions.

  Apple News applies this conditional table cell style to cells that meet all of the conditions of at least one of the selectors.
- `textStyle` ((ComponentTextStyle | string)): The name string of one of your styles in the Article [`ArticleDocument.componentTextStyles`](./articledocument/componenttextstyles-data.dictionary.md) object.

  **Allowed Types**: `ComponentTextStyle`, `string`
- `verticalAlignment` (string): Defines the vertical alignment of content inside cells.

  **Default**: `center`; **Allowed Values**: `top`, `center`, `bottom`
- `width` (integer): The column width, as a percentage only. This property only indicates proportionate width; you can’t use it to control exact width. See `minimumWidth`.

## Relationships

### Inherits From
- [TableCellStyle](./tablecellstyle.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/applenewsformat/conditionaltablecellstyle)*