# AddMediaMediaDestinationUnsupportedReason

**Framework**: SiriKit Cloud Media  
**Kind**: typealias  
**Role**: Type

Reasons the media service can’t add media items to a specified playlist.

**Availability**:
- SiriKit Cloud Media 1.0.2+

## Declaration

```
string AddMediaMediaDestinationUnsupportedReason
```

## Possible Values

- `playlistNameNotFound`: Your service can’t find the playlist.
- `playlistNotEditable`: The user doesn’t have permission to edit the playlist.

## See Also

### Reporting a Problem
- [object AddMediaMediaDestinationResolutionResult.Unsupported](./addmediamediadestinationresolutionresult/unsupported-data.dictionary.md)
  The reason your service can’t add media items to the specified library or playlist.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirikitcloudmedia/addmediamediadestinationunsupportedreason)*