# DataDescriptor

**Framework**: AppleNewsFormat  
**Kind**: dictionary  
**Role**: Object

The object for providing the data type, data formatting, and label for a field in a table.

**Availability**:
- Apple News Format 1.7+

## Declaration

```
object DataDescriptor
```

## Mentions

- [Defining and Using Table Styles](../AppleNews/defining-and-using-table-styles.md)

#### Discussion

A `DataDescriptor` object defines the data in a table by including basic information such as data type, data format, and a name for this set of data that identifies the kind of information it is. For example, the name could be “product number” or “release year”. An array of all the data descriptors for a table is located in the table’s [`RecordStore`](./recordstore.md).

##### Example

```json
{
  "components": [
    {
      "role": "datatable",
      "showDescriptorLabels": true,
      "sortBy": [
        {
          "descriptor": "id-name",
          "direction": "descending"
        }
      ],
      "data": {
        "descriptors": [
          {
            "identifier": "id-image",
            "key": "image",
            "label": {
              "type": "formatted_text",
              "text": "Image"
            },
            "format": {
              "type": "image",
              "maximumWidth": "50pt"
            },
            "dataType": "image"
          },
          {
            "identifier": "id-name",
            "key": "name",
            "label": {
              "type": "formatted_text",
              "text": "Name"
            },
            "dataType": "string"
          },
          {
            "identifier": "id-occupation",
            "key": "occupation",
            "label": "Occupation",
            "dataType": "string"
          }
        ],
        "records": [
          {
            "image": "bundle://image-1.jpg",
            "name": "Amelia Earhart",
            "occupation": "Pilot"
          },
          {
            "image": "bundle://image-2.jpg",
            "name": "Grace Hopper",
            "occupation": "Computer Scientist"
          }
        ]
      }
    }
  ]
}
```

## Properties

- `dataType` (string) *(required)*: The data type.

  Valid values:

  - `string`. Short text values, shorter than a typical sentence. Column widths are calculated differently for `string` and `text` data. `string` supports data values that are provided as strings or as [`FormattedText`](./formattedtext.md).
  - `text`. Long text values, as long as a typical sentence or longer. Column widths are calculated differently for `string` and `text` data. `text` supports data values that are provided as strings or as [`FormattedText`](./formattedtext.md).
  - `image`. Image URLs, starting with `bundle://` for an image provided in the same location as `article.json`, or starting with `http://` or `https://` for remote images. The images are displayed in the table. See [Preparing Image, Video, Audio, Music, and ARKit Assets](../AppleNews/preparing-image-video-audio-music-and-arkit-assets.md). To control image size, use a [`ImageDataFormat`](./imagedataformat.md) object as the value of the `format` property.
  - `number`. Numerical values where the more specific data type is not known.
  - `integer`. Integer values.
  - `float`. Floating-point values. To format the value, use a [`FloatDataFormat`](./floatdataformat.md) in the `format` property.

  **Allowed Values**: `string`, `text`, `image`, `number`, `integer`, `float`
- `key` (string) *(required)*: The name of this data descriptor. In a data record, you use this name as the key in a key-value pair, where the value is the data itself. This key must be unique across data descriptors in this data record store. See [`RecordStore`](./recordstore.md).
- `label` ((FormattedText | string)) *(required)*: The text to appear in the table header for this data category. This text can be provided as a string or a [`FormattedText`](./formattedtext.md) object.

  **Allowed Types**: `FormattedText`, `string`
- `format` (DataFormat): The object that sets some additional formatting preferences if you are using the `float` or `image` data type. For example, use a [`FloatDataFormat`](./floatdataformat.md) object in this property to control rounding, or use an [`ImageDataFormat`](./imagedataformat.md) to control image size.
- `identifier` (string): A unique identifier for this data descriptor. If used, identifiers must be unique across descriptors in this data record store. An identifier is required if you want to sort your table by any order other than the order in which the records are provided.

## See Also

### Tables with JSON Data
- [Adding a JSON Table](../AppleNews/adding-a-json-table.md)
  Add a table to your article that displays JSON data in rows and columns.
- [object DataTable](./datatable.md)
  The component for adding a JSON data table.
- [object RecordStore](./recordstore.md)
  The object that contains JSON data for a data table.
- [object DataTableSorting](./datatablesorting.md)
  A data category by which to sort the table in descending or ascending order.
- [object DataFormat](./dataformat.md)
  Properties shared by all data format obejct types.
- [object FloatDataFormat](./floatdataformat.md)
  The object that allows you to specify the number of digits after the decimal point for numeric values in data table cells.
- [object ImageDataFormat](./imagedataformat.md)
  The object that allows you to specify the minimum and maximum dimensions for images in data table cells.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applenewsformat/datadescriptor)*