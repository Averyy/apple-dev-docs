# FormattedText

**Framework**: AppleNewsFormat  
**Kind**: dictionary  
**Role**: Object

The object for specifying formatted text content and styling for captions in table cells.

**Availability**:
- Apple News Format 1.7+

## Declaration

```
object FormattedText
```

## Mentions

- [Defining and Using Table Styles](../AppleNews/defining-and-using-table-styles.md)
- [Using HTML with Apple News Format](../AppleNews/using-html-with-apple-news-format.md)
- [Using Markdown with Apple News Format](../AppleNews/using-markdown-with-apple-news-format.md)

#### Discussion

Use a `FormattedText` object to provide the content and style for text strings you use in data tables and as caption descriptors. You can use a `FormattedText` object for:

- Row and column headers (the value of the `label` property in [`DataDescriptor`](./datadescriptor.md))
- Data in JSON tables (the value of a key-value pair in a record in [`RecordStore`](./recordstore.md))

To apply a style to a `FormattedText` object, you can use a [`ComponentTextStyle`](./componenttextstyle.md). You can also use either HTML or [`InlineTextStyle`](./inlinetextstyle.md) objects to further customize ranges of text. See [Using HTML with Apple News Format](../AppleNews/using-html-with-apple-news-format.md).

> **Note**:  `FormattedText` objects don’t support Markdown syntax.

You can use this object in [`DataDescriptor`](./datadescriptor.md), [`RecordStore`](./recordstore.md), and [`CaptionDescriptor`](./captiondescriptor.md).

##### Example

```json
{
  "components": [
    {
      "role": "datatable",
      "data": {
        "descriptors": [
          {
            "identifier": "id-title",
            "key": "title",
            "dataType": "text",
            "label": "Title"
          }
        ],
        "records": [
          {
            "title": {
              "type": "formatted_text",
              "text": "<strong>Name</strong>",
              "format": "html"
            }
          }
        ]
      }
    }
  ]
}
```

## Properties

- `type` (string) *(required)*: The `type` must be `formatted_text`.

  **Allowed Values**: `formatted_text`
- `additions` ([Addition]): An array of addition objects that supply additional information for ranges of text in the `text` property.

  Apple News ignores this property when you set `format` to `html`.
- `format` (string): The formatting or markup method applied to the text. If you set `format` to `html`, neither `additions` nor `inlineTextStyles` is supported.

  **Default**: `none`; **Allowed Values**: `html`, `none`
- `inlineTextStyles` ([InlineTextStyle]): An array specifying ranges of characters and a [`TextStyle`](./textstyle.md) object to apply to each range.

  Apple News ignores this property when you set `format` to `html`.
- `text` (string) *(required)*: The text, including any HTML tags.
- `textStyle` ((ComponentTextStyle | string)): Either a component text style object, or the name string of one of your styles in the [`ArticleDocument.componentTextStyles`](./articledocument/componenttextstyles-data.dictionary.md) object.

  **Allowed Types**: `ComponentTextStyle`, `string`

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
- [object Padding](./padding.md)
  The object for defining space around the content in a table cell.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applenewsformat/formattedtext)*