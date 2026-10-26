# RecordStore

**Framework**: AppleNewsFormat  
**Kind**: dictionary  
**Role**: Object

The object that contains JSON data for a data table.

**Availability**:
- Apple News Format 1.7+

## Declaration

```
object RecordStore
```

## Mentions

- [Defining and Using Table Styles](../AppleNews/defining-and-using-table-styles.md)

#### Discussion

The `RecordStore` object uses two required properties to provide the `data` for a table and to specify how that data will be used in the table.

- Data `descriptors` define how the data is interpreted and how it will be displayed in the table. For each set of data, data descriptors communicate the data type, unique keys, data formats, and header labels for the table.
- Data `records` provide the actual data as a set of key-value pairs that relate to the descriptors.

For example, your data `descriptors` might describe a table that contains stock symbols and prices; each data record could provide the symbol and price for a particular stock.

This object can be used in [`DataTable`](./datatable.md).

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
            "name": "Amelia Earhart",
            "occupation": "Pilot"
          },
          {
            "name": "Grace Hopper",
            "occupation": "Computer Scientist"
          }
        ]
      }
    }
  ]
}
```

## Topics

### Objects
- [object RecordStore.records](./recordstore/records-data.dictionary.md)
  Define and provide data records that fit within the structure defined by descriptors for a data table.

## Properties

- `descriptors` ([DataDescriptor]) *(required)*: Provides information about the data that can be in each data record.

  The order of the descriptors determines the order of the columns (or the rows if the table’s `dataOrientation` is set to horizontal.)

  Version 1.5
- `records` ([RecordStore.records]) *(required)*: Provides data records that fit within the structure defined by `descriptors`. Each descriptor can be used only once per record.

  You can choose not to include all values from a given record in a data table. Only data that corresponds to a data descriptor will be included in your data table.

## See Also

### Tables with JSON Data
- [Adding a JSON Table](../AppleNews/adding-a-json-table.md)
  Add a table to your article that displays JSON data in rows and columns.
- [object DataTable](./datatable.md)
  The component for adding a JSON data table.
- [object DataDescriptor](./datadescriptor.md)
  The object for providing the data type, data formatting, and label for a field in a table.
- [object DataTableSorting](./datatablesorting.md)
  A data category by which to sort the table in descending or ascending order.
- [object DataFormat](./dataformat.md)
  Properties shared by all data format obejct types.
- [object FloatDataFormat](./floatdataformat.md)
  The object that allows you to specify the number of digits after the decimal point for numeric values in data table cells.
- [object ImageDataFormat](./imagedataformat.md)
  The object that allows you to specify the minimum and maximum dimensions for images in data table cells.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applenewsformat/recordstore)*