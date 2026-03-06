# Curators

**Framework**: Apple Music API  
**Kind**: dictionary

A resource object that represents a curator.

**Availability**:
- Apple Music 1.0+

## Declaration

```swift
object Curators
```

## Topics

### Related Objects
- [object Curators.Attributes](curators/attributes-data.dictionary.md)
  The attributes for a curator resource.
- [object Curators.Relationships](curators/relationships-data.dictionary.md)
  The relationships for a curator resource.

## Properties

- `id` (string) *(required)*: The identifier for the curator.
- `type` (string) *(required)*: This value must always be `curators`.
- `href` (string) *(required)*: The relative location for the curator resource.
- `attributes` (Curators.Attributes): The attributes for the curator.
- `relationships` (Curators.Relationships): The relationships for the curator.

## See Also

- [object AppleCurators](applecurators.md)
  A resource object that represents an Apple curator.
- [object AppleCuratorsResponse](applecuratorsresponse.md)
  The response to a request for Apple curators.
- [object CuratorsResponse](curatorsresponse.md)
  The response to a request for curators.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/curators)*