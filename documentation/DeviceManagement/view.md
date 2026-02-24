# View

**Framework**: Device Management  
**Kind**: dictionary

A view for the resource.

**Availability**:
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object View
```

## Topics

### Objects
- [object View.Attributes](view/attributes-data.dictionary.md)
  The attribute metadata for the view.
- [object View.Meta](view/meta-data.dictionary.md)
  Contextual data about the view.

## Properties

- `attributes` (View.Attributes): The attribute metadata for the view.
- `data` ([Resource]) *(required)*: A paginated collection of resources in the view.
- `href` (string): A relative location to fetch the view, if it’s directly fetchable.
- `meta` (View.Meta): Contextual data about the view.
- `next` (string): A relative cursor to fetch the next paginated collection of resources in the view if more exist.

## See Also

- [object Resource.Attributes](resource/attributes-data.dictionary.md)
- [object Resource.Meta](resource/meta-data.dictionary.md)
- [object Resource.Relationships](resource/relationships-data.dictionary.md)
- [object Resource.Views](resource/views-data.dictionary.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/view)*