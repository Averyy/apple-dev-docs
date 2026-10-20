# Playlists.Attributes

**Framework**: Apple Music API  
**Kind**: dictionary  
**Role**: Object

The attributes for a playlist resource.

**Availability**:
- Apple Music 1.0+

## Declaration

```
object Playlists.Attributes
```

## Properties

- `artwork` (Artwork): The playlist artwork.
- `curatorName` (string) *(required)*: The display name of the curator.
- `description` (DescriptionAttribute): A description of the playlist.
- `isChart` (boolean) *(required)*: Indicates whether the playlist represents a popularity chart.
- `lastModifiedDate` (string): The date the playlist was last modified.
- `name` (string) *(required)*: The localized name of the playlist.
- `playlistType` (string) *(required)*: The type of playlist. Possible values are:

  Editorial: A playlist created by an Apple Music curator.

  External: A playlist created by a non-Apple curator or brand.

  Personal-mix: A personalized playlist for an Apple Music user.

  Replay: A personalized Apple Music Replay playlist for an Apple Music user.

  User-shared: A playlist created and shared by an Apple Music user.

  **Allowed Values**: `editorial`, `external`, `personal-mix`, `replay`, `user-shared`
- `playParams` (PlayParameters): The value map may be used to initiate playback of available tracks in the playlist.
- `url` (string) *(required)*: The URL for sharing the playlist in Apple Music.
- `trackTypes` ([string]): **(Extended)** The resource types that are present in the tracks of the playlists.

  **Allowed Values**: `music-videos`, `songs`
- `inFavorites` (boolean)

## See Also

### Related Objects
- [object Playlists.Relationships](./relationships-data.dictionary.md)
  The relationships for a playlist resource.
- [object Playlists.Views](./views-data.dictionary.md)
  The views for a music video resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/playlists/attributes-data.dictionary)*