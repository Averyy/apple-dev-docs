# Adding a JSON Table

**Framework**: Apple News  
**Role**: Article

Add a table to your article that displays JSON data in rows and columns.

#### Overview

To add a table with JSON-formatted data, add a component with the role property set to `datatable`. Set up your table by providing an array of data descriptors that communicate the following:

- Data types
- Unique keys
- Data formats

In the [`DataTable`](../AppleNewsFormat/datatable.md) component, you use `dataRecords` to add your data in key-value pairs that correlate your data with the data descriptors.

You can apply styles to adjust the appearance of your table using the `tableStyle` property of the [`ComponentStyle`](../AppleNewsFormat/componentstyle.md) object the table uses. You can specify styles for individual rows, columns, and cells as well as for the entire table. (See [`TableStyle`](../AppleNewsFormat/tablestyle.md) for more information.)

## See Also

### Tables with JSON Data
- [object DataTable](../AppleNewsFormat/datatable.md)
  The component for adding a JSON data table.
- [object RecordStore](../AppleNewsFormat/recordstore.md)
  The object that contains JSON data for a data table.
- [object DataDescriptor](../AppleNewsFormat/datadescriptor.md)
  The object for providing the data type, data formatting, and label for a field in a table.
- [object DataTableSorting](../AppleNewsFormat/datatablesorting.md)
  A data category by which to sort the table in descending or ascending order.
- [object DataFormat](../AppleNewsFormat/dataformat.md)
  Properties shared by all data format obejct types.
- [object FloatDataFormat](../AppleNewsFormat/floatdataformat.md)
  The object that allows you to specify the number of digits after the decimal point for numeric values in data table cells.
- [object ImageDataFormat](../AppleNewsFormat/imagedataformat.md)
  The object that allows you to specify the minimum and maximum dimensions for images in data table cells.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applenews/adding-a-json-table)*