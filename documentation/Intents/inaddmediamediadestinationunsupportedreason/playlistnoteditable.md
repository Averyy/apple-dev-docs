# INAddMediaMediaDestinationUnsupportedReason.playlistNotEditable

**Framework**: Intents  
**Kind**: case  
**Role**: Case

The user can’t modify the destination playlist.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
case playlistNotEditable
```

```c
INAddMediaMediaDestinationUnsupportedReasonPlaylistNotEditable
```

## Discussion

Provide this error explanation when the user tries to add a media item to a playlist they can’t change, such as another user’s shared playlist or a playlist your service publishes.

## See Also

### Reasons
- [INAddMediaMediaDestinationUnsupportedReason.playlistNameNotFound](./playlistnamenotfound.md)
  The app was unable to find a playlist with that name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inaddmediamediadestinationunsupportedreason/playlistnoteditable)*