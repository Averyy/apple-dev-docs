# DataFormat

**Framework**: AppleNewsFormat  
**Kind**: dictionary  
**Role**: Object

Properties shared by all data format obejct types.

**Availability**:
- Apple News Format 1.7+

## Declaration

```
object DataFormat
```

## Discussion

This object can be used in [`DataDescriptor`](./datadescriptor.md).

## Properties

- `type` (string) *(required)*: The type of format. This must be `float` for a [`FloatDataFormat`](./floatdataformat.md) object or `image` for an [`ImageDataFormat`](./imagedataformat.md) object.

  **Allowed Values**: `float`, `image`

## Relationships

### Inherited By
- [FloatDataFormat](./floatdataformat.md)
- [ImageDataFormat](./imagedataformat.md)

## See Also

### Tables with JSON Data
- [Adding a JSON Table](../AppleNews/adding-a-json-table.md)
  Add a table to your article that displays JSON data in rows and columns.
- [object DataTable](./datatable.md)
  The component for adding a JSON data table.
- [object RecordStore](./recordstore.md)
  The object that contains JSON data for a data table.
- [object DataDescriptor](./datadescriptor.md)
  The object for providing the data type, data formatting, and label for a field in a table.
- [object DataTableSorting](./datatablesorting.md)
  A data category by which to sort the table in descending or ascending order.
- [object FloatDataFormat](./floatdataformat.md)
  The object that allows you to specify the number of digits after the decimal point for numeric values in data table cells.
- [object ImageDataFormat](./imagedataformat.md)
  The object that allows you to specify the minimum and maximum dimensions for images in data table cells.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applenewsformat/dataformat)*