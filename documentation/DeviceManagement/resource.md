# Resource

**Framework**: Device Management  
**Kind**: dictionary

A resource such as an app or book.

**Availability**:
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object Resource
```

## Topics

### Related Objects
- [object View](view.md)
  A view for the resource.
- [object Resource.Attributes](resource/attributes-data.dictionary.md)
- [object Resource.Meta](resource/meta-data.dictionary.md)
- [object Resource.Relationships](resource/relationships-data.dictionary.md)
- [object Resource.Views](resource/views-data.dictionary.md)

## Properties

- `attributes` (Resource.Attributes): The attribute metadata for the resource.
- `href` (string): The relative location for the resource, if it may be fetched directly.
- `id` (string) *(required)*: The identifier of the resource.
- `meta` (Resource.Meta): Contextual data about the resource.
- `relationships` (Resource.Relationships): The relationships for the resource.
- `type` (string) *(required)*: The type of the resource.
- `views` (Resource.Views): The views for the resource.

## See Also

- [object Relationship](relationship.md)
  A to-one or to-many relationship from one resource object to others.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/resource)*