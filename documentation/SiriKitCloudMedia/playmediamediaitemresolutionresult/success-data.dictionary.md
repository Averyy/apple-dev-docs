# PlayMediaMediaItemResolutionResult.Success

**Framework**: SiriKit Cloud Media  
**Kind**: dictionary  
**Role**: Object

A media item that successfully matches the intent.

**Availability**:
- SiriKit Cloud Media 1.0.2+

## Declaration

```
object PlayMediaMediaItemResolutionResult.Success
```

## Properties

- `resolvedMediaItem` (MediaItem) *(required)*: The song, album, podcast, or other media item that the user wants to play.

## See Also

### Specifying a Result
- [object PlayMediaMediaItemResolutionResult.Unsupported](./unsupported-data.dictionary.md)
  The reason your service can’t play the requested media item.
- [object PlayMediaMediaItemResolutionResult.Disambiguation](./disambiguation-data.dictionary.md)
  A result that requires the user to choose from multiple media items before proceeding.
- [object PlayMediaMediaItemResolutionResult.ConfirmationRequired](./confirmationrequired-data.dictionary.md)
  A result that requires the user to confirm the media item before proceeding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirikitcloudmedia/playmediamediaitemresolutionresult/success-data.dictionary)*