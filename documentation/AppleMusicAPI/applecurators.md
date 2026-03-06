# AppleCurators

**Framework**: Apple Music API  
**Kind**: dictionary

A resource object that represents an Apple curator.

**Availability**:
- Apple Music 1.0+

## Declaration

```swift
object AppleCurators
```

## Topics

### Related Objects
- [object AppleCurators.Attributes](applecurators/attributes-data.dictionary.md)
  The attributes for an Apple curator resource.
- [object AppleCurators.Relationships](applecurators/relationships-data.dictionary.md)
  The relationships for an Apple curator resource.

## Properties

- `id` (string) *(required)*: The identifier for the Apple curator.
- `type` (string) *(required)*: This value must always be `apple-curators`.
- `href` (string) *(required)*: The relative location for the Apple curator resource.
- `attributes` (AppleCurators.Attributes): The attributes for the Apple curator.
- `relationships` (AppleCurators.Relationships): The relationships for the Apple curator.

## See Also

- [object AppleCuratorsResponse](applecuratorsresponse.md)
  The response to a request for Apple curators.
- [object Curators](curators.md)
  A resource object that represents a curator.
- [object CuratorsResponse](curatorsresponse.md)
  The response to a request for curators.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/applecurators)*