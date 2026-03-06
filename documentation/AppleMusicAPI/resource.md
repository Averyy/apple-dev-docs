# Resource

**Framework**: Apple Music API  
**Kind**: dictionary

A resource—such as an album, song, or playlist.

**Availability**:
- Apple Music 1.0+

## Declaration

```swift
object Resource
```

#### Discussion

A Resource object may contain just these identifier members: `id`, `type`, `href`, and `meta`.

## Topics

### Related Objects
- [object Resource.Attributes](resource/attributes-data.dictionary.md)
  Attributes representing the metadata of the resource.
- [object Resource.Relationships](resource/relationships-data.dictionary.md)
  Relationships belonging to the resource.
### Dictionaries
- [object Resource.Meta](resource/meta-data.dictionary.md)
  Information about the request or response.
- [object Resource.Views](resource/views-data.dictionary.md)
  Views belonging to the resource.

## Properties

- `id` (string) *(required)*: Persistent identifier of the resource.
- `type` (string) *(required)*: The type of resource.
- `href` (string): A URL subpath that fetches the resource as the primary object. This member is only present in responses.
- `attributes` (Resource.Attributes): Attributes belonging to the resource (can be a subset of the attributes). The members are the names of the attributes defined in the object model.
- `relationships` (Resource.Relationships): Relationships belonging to the resource (can be a subset of the relationships). The members are the names of the relationships defined in the object model. See [`Relationship`](relationship.md) object for the values of the members.
- `meta` (Resource.Meta): Information about the request or response. The members may be any of the endpoint parameters.
- `views` (Resource.Views): The relationship views for the resource.

## See Also

- [object Relationship](relationship.md)
  A to-one or to-many relationship from one resource object to others.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/resource)*