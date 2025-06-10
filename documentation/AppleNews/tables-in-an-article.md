# Tables in an Article

**Framework**: Apple News

Add a JSON or HTML data table, and understand  the options for changing the look of your table.

#### Overview

Apple News Format lets you add both JSON and HTML tables as components in your article.

- In JSON tables, you create the table structure and add data using JSON objects and properties. You can also sort your data in the table.
- In HTML tables, you use HTML tags to set up a table with your data already formatted as HTML rows.

For both the JSON and HTML table components, you can adjust the look of the rows, columns, and cells in the table using the Component Style object used by the component.

Once you add a table, you can apply styles (backgrounds, borders, and so on) and add row and column labels. You can also use conditions to apply styles only to those rows, columns, and cells that meet a specific criteria. See [`Enhancing Your Articles with Styles`](enhancing-your-articles-with-styles.md).

> **Note**: When you view your published article with its table, notice that the News app positions and sizes the table to make use of the available space. If data in the table is wider than the component, News scrolls the data horizontally within the component.

## Topics

### Tables with JSON Data
- [Adding a JSON Table](adding-a-json-table.md)
  Add a table to your article that displays JSON data in rows and columns.
- [object DataTable](../applenewsformat/datatable.md)
  The component for adding a JSON data table.
- [object RecordStore](../applenewsformat/recordstore.md)
  The object that contains JSON data for a data table.
- [object DataDescriptor](../applenewsformat/datadescriptor.md)
  The object for providing the data type, data formatting, and label for a field in a table.
- [object DataTableSorting](../applenewsformat/datatablesorting.md)
  A data category by which to sort the table in descending or ascending order.
- [object DataFormat](../applenewsformat/dataformat.md)
  Properties shared by all data format obejct types.
- [object FloatDataFormat](../applenewsformat/floatdataformat.md)
  The object that allows you to specify the number of digits after the decimal point for numeric values in data table cells.
- [object ImageDataFormat](../applenewsformat/imagedataformat.md)
  The object that allows you to specify the minimum and maximum dimensions for images in data table cells.
### Tables with HTML Data
- [Adding an HTML Table](adding-an-html-table.md)
  Add a table formatted in HTML to your article.
- [object HTMLTable](../applenewsformat/htmltable.md)
  The component for adding tables with HTML data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applenews/tables-in-an-article)*