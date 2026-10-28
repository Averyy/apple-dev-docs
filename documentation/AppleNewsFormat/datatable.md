# DataTable

**Framework**: AppleNewsFormat  
**Kind**: dictionary  
**Role**: Object

The component for adding a JSON data table.

**Availability**:
- Apple News Format 1.7+

## Declaration

```
object DataTable
```

## Mentions

- [Adding a JSON Table](../AppleNews/adding-a-json-table.md)
- [Preparing Image, Video, Audio, Music, and ARKit Assets](../AppleNews/preparing-image-video-audio-music-and-arkit-assets.md)

## Discussion

Add a `DataTable` component that uses table data provided in a JSON format. Information about the table, including the data itself, is provided by the `data` property, whose value is a [`RecordStore`](./recordstore.md) object that contains both the table data and information about the data, such as data types and header labels.

You can apply styles to table rows, columns, and cells using a [`ComponentStyle`](./componentstyle.md) object that has a [`TableStyle`](./tablestyle.md) defined.

### Example

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
              "text": "Name",
              "textStyle": {
                "textColor": "black"
              }
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
      },
      "style": {
        "tableStyle": {
          "rows": {
            "backgroundColor": "#fff",
            "divider": {
              "width": 1,
              "color": "#ddd"
            }
          },
          "headerRows": {
            "backgroundColor": "#ccc",
            "divider": {
              "width": 2,
              "color": "#999"
            }
          },
          "cells": {
            "padding": 6,
            "verticalAlignment": "top"
          }
        }
      },
      "layout": {
        "columnStart": 0,
        "columnSpan": 7,
        "margin": 20
      }
    }
  ]
}
```

## Properties

- `data` (RecordStore) *(required)*: An object that provides data for the table. This property also provides information about the data, such as data types and header labels, in the form of the data descriptor.
- `role` (string) *(required)*: Always `datatable` for this component.

  **Allowed Values**: `datatable`
- `anchor` (Anchor): An object that defines vertical alignment with another component.
- `animation` ((ComponentAnimation | string("none"))): An object that defines an animation to be applied to the component.

  The `none` value is used for conditional design elements. Adding it here has no effect.

  **Allowed Types**: `ComponentAnimation`, `string("none")`
- `behavior` ((Behavior | string("none"))): An object that defines behavior for a component, like [`Parallax`](./parallax.md) or [`Springy`](./springy.md).

  The `none` value is used for conditional design elements. Adding it here has no effect.

  **Allowed Types**: `Behavior`, `string("none")`
- `conditional` ((ConditionalComponent | [ConditionalComponent])): An instance or array of component properties that can be applied conditionally, and the conditions that cause them to be applied.

  **Allowed Types**: `ConditionalComponent`, `[ConditionalComponent]`
- `dataOrientation` (string): A string value that determines the table orientation.

  Valid values:

  - `vertical`. The headers are a row at the top of the table, and each data record is a column.
  - `horizontal`. The headers are a column at the left of the table, and each data record is a row.

  **Default**: `horizontal`; **Allowed Values**: `horizontal`, `vertical`
- `hidden` (boolean): A Boolean value that determines whether the component is hidden.

  **Default**: `false`
- `identifier` (string): An optional unique identifier for this component. If used, this `identifier` must be unique across the entire document. You will need an `identifier` for your component if you want to anchor other components to it.
- `layout` ((ComponentLayout | string)): An inline `ComponentLayout` object that contains layout information, or a string reference to a `ComponentLayout` object that is defined at the top level of the document.

  If `layout` is not defined, size and position will be based on various factors, such as the device type, the length of the content, and the `role` of this component.

  **Allowed Types**: `ComponentLayout`, `string`
- `showDescriptorLabels` (boolean): A Boolean value that determines whether the headers are shown. If `true`, the headers are visible, with the labels defined in the [`RecordStore`](./recordstore.md). If `false`, the headers are not visible.

  **Default**: `true`
- `sortBy` ([DataTableSorting]): An array that determines how table data is sorted. Rules are applied in the order in which they are provided in the array.

  If this property is not defined, data records are displayed in the order in which they are provided in the data [`RecordStore`](./recordstore.md).
- `style` ((ComponentStyle | string | string("none"))): An inline `ComponentStyle` object that defines the appearance of this component or a string reference to a `ComponentStyle` object that is defined at the top level of the document.

  If this property is omitted, the table is styled according to a component style called `default-datatable`. If `default-datatable` doesn’t exist or doesn’t define table styling, the table is styled according to a component style called `default`. If no table styling is defined in any of these places, Apple News uses its built-in default table styling.

  The `none` value is used for conditional design elements. Adding it here has no effect.

  **Allowed Types**: `ComponentStyle`, `string`, `string("none")`

## Relationships

### Inherits From
- [Component](./component.md)

## See Also

### Tables with JSON Data
- [Adding a JSON Table](../AppleNews/adding-a-json-table.md)
  Add a table to your article that displays JSON data in rows and columns.
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
- [object ImageDataFormat](./imagedataformat.md)
  The object that allows you to specify the minimum and maximum dimensions for images in data table cells.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applenewsformat/datatable)*