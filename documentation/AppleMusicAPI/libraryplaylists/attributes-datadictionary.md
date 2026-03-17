# LibraryPlaylists.Attributes

**Framework**: Apple Music API  
**Kind**: dictionary

The attributes for a library playlist resource.

**Availability**:
- Apple Music 1.0+

## Declaration

```swift
object LibraryPlaylists.Attributes
```

## Properties

- `artwork` (Artwork): The playlist artwork.
- `canEdit` (boolean) *(required)*: Indicates whether the playlist is editable.
- `dateAdded` (string): The date and time the playlist was added to the user’s library. In YYYY-MM-DDThh:mm:ssZ ISO 8601 format.
- `description` (DescriptionAttribute): A description of the playlist.
- `hasCatalog` (boolean) *(required)*: Indicates whether the playlist has a representation in the Apple Music catalog.
- `name` (string) *(required)*: The localized name of the playlist.
- `playParams` (PlayParameters): The value map may be used to initiate playback of available tracks in the playlist.
- `isPublic` (boolean) *(required)*: A flag to indicate whether the library playlist is a public playlist.
- `trackTypes` ([string]): **(Extended)** The resource types that are present in the tracks of the library playlist.
- `inFavorites` (boolean): Whether the catalog resource ID is in the person’s favorites.

## See Also

- [object LibraryPlaylists.Relationships](libraryplaylists/relationships-data.dictionary.md)
  The relationships for a library playlist resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/libraryplaylists/attributes-data.dictionary)*