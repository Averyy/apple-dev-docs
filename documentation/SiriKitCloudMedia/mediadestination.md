# MediaDestination

**Framework**: SiriKit Cloud Media  
**Kind**: dictionary

The user’s library or a playlist.

**Availability**:
- SiriKit Cloud Media 1.0.2+

## Declaration

```swift
object MediaDestination
```

#### Discussion

A playlist can be either a [`MediaItem`](mediaitem.md) or a [`MediaDestination`](mediadestination.md). When the user adds a song to a playlist, the playlist is the [`MediaDestination`](mediadestination.md). When the user adds a playlist to their library, the playlist is a [`MediaItem`](mediaitem.md), and the user’s library is the [`MediaDestination`](mediadestination.md).

## Relationships

### Inherited By
- [MediaDestinationLibrary](mediadestinationlibrary.md)
- [MediaDestinationPlaylist](mediadestinationplaylist.md)

## See Also

- [object AddMediaMediaDestinationResolutionResult.Success](addmediamediadestinationresolutionresult/success-data.dictionary.md)
  A media destination that successfully matches an intent.
- [object MediaDestinationLibrary](mediadestinationlibrary.md)
  The user’s library as a destination for an add media intent.
- [object MediaDestinationPlaylist](mediadestinationplaylist.md)
  A playlist as a destination for an add media intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirikitcloudmedia/mediadestination)*