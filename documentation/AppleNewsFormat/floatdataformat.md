# FloatDataFormat

**Framework**: AppleNewsFormat  
**Kind**: dictionary  
**Role**: Object

The object that allows you to specify the number of digits after the decimal point for numeric values in data table cells.

**Availability**:
- Apple News Format 1.7+

## Declaration

```
object FloatDataFormat
```

#### Discussion

When you specify `float` as the data type for an item in [`DataDescriptor`](./datadescriptor.md), you can indicate the number of places after the decimal point that you want to display.

This object can be used in [`DataDescriptor`](./datadescriptor.md).

##### Example

```json
{
  "components": [
    {
      "role": "datatable",
      "data": {
        "descriptors": [
          {
            "identifier": "id-float",
            "dataType": "float",
            "format": {
              "type": "float",
              "decimals": 3
            },
            "key": "image",
            "label": "none"
          }
        ],
        …
      }
    }
  ]
}
```

## Properties

- `decimals` (integer): The number of digits that can appear after the decimal point. The number will be rounded to this number of digits after the decimal.

  **Default**: `2`; **Minimum**: `0`
- `type` (string) *(required)*: The type of data format for this object. This must be float for a `float` data format object.

  **Allowed Values**: `float`

## Relationships

### Inherits From
- [DataFormat](./dataformat.md)

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
- [object DataFormat](./dataformat.md)
  Properties shared by all data format obejct types.
- [object ImageDataFormat](./imagedataformat.md)
  The object that allows you to specify the minimum and maximum dimensions for images in data table cells.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applenewsformat/floatdataformat)*