# MediaDestinationPlaylist

**Framework**: SiriKit Cloud Media  
**Kind**: dictionary  
**Role**: Object

A playlist as a destination for an add media intent.

**Availability**:
- SiriKit Cloud Media 1.0.2+

## Declaration

```
object MediaDestinationPlaylist
```

## Properties

- `mediaDestinationType` (string) *(required)*: The type of collection the user wants to store their media items in.

  **Allowed Values**: `playlist`
- `playlistName` (string) *(required)*: The name of the playlist.

  **Minimum Length**: `1`; **Maximum Length**: `1000`

## Relationships

### Inherits From
- [MediaDestination](./mediadestination.md)

## See Also

### Providing a Destination
- [object AddMediaMediaDestinationResolutionResult.Success](./addmediamediadestinationresolutionresult/success-data.dictionary.md)
  A media destination that successfully matches an intent.
- [object MediaDestination](./mediadestination.md)
  The user’s library or a playlist.
- [object MediaDestinationLibrary](./mediadestinationlibrary.md)
  The user’s library as a destination for an add media intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirikitcloudmedia/mediadestinationplaylist)*