# Defining and Using Table Styles

**Framework**: Apple News  
**Role**: Article

Apply table styles, such as borders and backgrounds, to the rows, columns, and cells in your HTML and JSON  tables.

#### Overview

Apple News Format lets you apply styles to individual rows, columns, and cells in your HTML and JSON data tables. In addition, you can apply text styles to text in table cells. In an HTML table, you format the text using HTML. In a JSON table, you use [`FormattedText`](https://developer.apple.com/documentation/applenewsformat/formattedtext) as the value of a key-value pair in a record in [`RecordStore`](https://developer.apple.com/documentation/applenewsformat/recordstore). The [`DataDescriptor`](https://developer.apple.com/documentation/applenewsformat/datadescriptor) for that record must have a `dataType` of `text`.

To set the style for the rows, columns, and cells in a table, you use the [`TableStyle`](https://developer.apple.com/documentation/applenewsformat/tablestyle) object in the [`ComponentStyle`](https://developer.apple.com/documentation/applenewsformat/componentstyle) the table uses.

The following table lists the styles that you can apply to the rows, columns, and cells in tables. All can be conditional styles that Apple News Format applies to parts of the table that meet certain criteria, such as odd-numbered rows or a cell in a specific location.

| **Parts of the table** | **Style options** |
| --- | --- |
| Rows and row headers | Background color or fill, divider lines, row height |
| Columns and column headers | Background color or fill, divider lines, minimum column width, column width |
| Cells and cell headers | Background color or fill, border, cell height, horizontal alignment, minimum width, cell padding, vertical alignment, cell width |

## See Also

### Table Styles
- [object TableStyle](https://developer.apple.com/documentation/applenewsformat/tablestyle)
  The object for defining a style for rows, columns, cells, and headers in a table.
- [object TableRowStyle](https://developer.apple.com/documentation/applenewsformat/tablerowstyle)
  The object for applying styles to rows in a table.
- [object ConditionalTableRowStyle](https://developer.apple.com/documentation/applenewsformat/conditionaltablerowstyle)
  The object for applying styles to table rows that meet certain conditions.
- [object TableRowSelector](https://developer.apple.com/documentation/applenewsformat/tablerowselector)
  The object for defining conditions that apply a conditional style to a row.
- [object TableColumnStyle](https://developer.apple.com/documentation/applenewsformat/tablecolumnstyle)
  The object for applying styles to columns in a table.
- [object ConditionalTableColumnStyle](https://developer.apple.com/documentation/applenewsformat/conditionaltablecolumnstyle)
  The object for applying styles to table columns that meet certain conditions.
- [object TableColumnSelector](https://developer.apple.com/documentation/applenewsformat/tablecolumnselector)
  The object for defining conditions that apply a conditional style to a column.
- [object TableCellStyle](https://developer.apple.com/documentation/applenewsformat/tablecellstyle)
  The object for applying styles to cells in a table.
- [object ConditionalTableCellStyle](https://developer.apple.com/documentation/applenewsformat/conditionaltablecellstyle)
  The object for applying a style to table cells that meet certain conditions.
- [object TableCellSelector](https://developer.apple.com/documentation/applenewsformat/tablecellselector)
  The object for defining conditions that apply a conditional style to a cell.
- [object TableBorder](https://developer.apple.com/documentation/applenewsformat/tableborder)
  The object for setting borders for tables.
- [object TableStrokeStyle](https://developer.apple.com/documentation/applenewsformat/tablestrokestyle)
  The object for defining the color, width, and style of a stroke in a table.
- [object Padding](https://developer.apple.com/documentation/applenewsformat/padding)
  The object for defining space around the content in a table cell.
- [object FormattedText](https://developer.apple.com/documentation/applenewsformat/formattedtext)
  The object for specifying formatted text content and styling for captions in table cells.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applenews/defining-and-using-table-styles)*