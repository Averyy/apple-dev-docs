# AppleCurators.Attributes

**Framework**: Apple Music API  
**Kind**: dictionary

The attributes for an Apple curator resource.

**Availability**:
- Apple Music 1.0+

## Declaration

```swift
object AppleCurators.Attributes
```

## Properties

- `artwork` (Artwork) *(required)*: The curator artwork.
- `editorialNotes` (EditorialNotes): The notes about the curator that appear in the Apple Music catalog.
- `kind` (string) *(required)*: The type of curator. Possible values are: `Curator`: An individual curator entity. `Genre`: A curator that represents a cohesive music genre. `Show`: A curator associated with a particular Apple Music show.
- `name` (string) *(required)*: The localized name of the curator.
- `shortName` (string): The localized shortened name of the curator.
- `showHostName` (string): The name of the host if `kind` is `Show`.
- `url` (string) *(required)*: The URL for sharing the curator in Apple Music.

## See Also

- [object AppleCurators.Relationships](applecurators/relationships-data.dictionary.md)
  The relationships for an Apple curator resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/applecurators/attributes-data.dictionary)*