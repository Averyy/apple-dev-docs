# ImageDataFormat

**Framework**: AppleNewsFormat  
**Kind**: dictionary  
**Role**: Object

The object that allows you to specify the minimum and maximum dimensions for images in data table cells.

**Availability**:
- Apple News Format 1.7+

## Declaration

```
object ImageDataFormat
```

#### Discussion

When you specify `image` as the data type for an item in [`DataDescriptor`](./datadescriptor.md), you can also indicate a minimum and maximum height and width for the image in the table cell.

This object can be used in [`DataDescriptor`](./datadescriptor.md).

##### Example

```json
"components": [
 {
      "role": "datatable",
      "data": {
        "descriptors": [
          {
            "identifier": "id-image",
            "dataType": "image",
            "format": {
              "type": "image",
              "maximumHeight": "50pt"
            },
            "key": "image",
            "label": "none"
          }
        ],
…]
```

## Properties

- `maximumHeight` ((SupportedUnits | number)): The maximum height of an image in a cell as a number in points or as one of the available units for components.

  If this property is omitted, the maximum height will be determined by the image’s aspect ratio.

  **Allowed Types**: `SupportedUnits`, `number`
- `maximumWidth` ((SupportedUnits | number)): The maximum width of an image in a cell as a number in points or as one of the available units for components. The maximum width cannot be smaller than the minimum width.

  If this property is omitted, the maximum width will be determined by the column width.

  **Allowed Types**: `SupportedUnits`, `number`
- `minimumHeight` ((SupportedUnits | number)): The minimum height of an image in a cell as a number in points or as one of the available units for components.

  If this property is omitted, the height will be determined by the image’s aspect ratio.

  **Allowed Types**: `SupportedUnits`, `number`
- `minimumWidth` ((SupportedUnits | number)): The minimum width of an image in a cell as as a number in points or as one of the available units for components.

  Default value: `20cw`, or `20%` of the component’s width. See  [Specifying Measurements for Components](../AppleNews/specifying-measurements-for-components.md).

  **Default**: `20cw`; **Allowed Types**: `SupportedUnits`, `number`
- `type` (string) *(required)*: The type of data format for this object. This must be `image` for an image format object.

  **Allowed Values**: `image`

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
- [object FloatDataFormat](./floatdataformat.md)
  The object that allows you to specify the number of digits after the decimal point for numeric values in data table cells.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applenewsformat/imagedataformat)*