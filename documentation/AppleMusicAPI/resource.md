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

## See Also

- [object Relationship](relationship.md)
  A to-one or to-many relationship from one resource object to others.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/resource)*