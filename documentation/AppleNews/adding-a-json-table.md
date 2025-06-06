# Adding a JSON Table

**Framework**: Apple News

Add a table to your article that displays JSON data in rows and columns.

#### Overview

To add a table with JSON-formatted data, add a component with the role property set to `datatable`. Set up your table by providing an array of data descriptors that communicate the following:

- Data types
- Unique keys
- Data formats

In the [`DataTable`](https://developer.apple.com/documentation/applenewsformat/datatable) component, you use `dataRecords` to add your data in key-value pairs that correlate your data with the data descriptors.

You can apply styles to adjust the appearance of your table using the `tableStyle` property of the [`ComponentStyle`](https://developer.apple.com/documentation/applenewsformat/componentstyle) object the table uses. You can specify styles for individual rows, columns, and cells as well as for the entire table. (See [`TableStyle`](https://developer.apple.com/documentation/applenewsformat/tablestyle) for more information.)

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/applenews/adding-a-json-table)*