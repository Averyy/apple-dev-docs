# UpdateMediaAffinityMediaItemResolutionResult.Success

**Framework**: SiriKit Cloud Media  
**Kind**: dictionary  
**Role**: Object

A media item that successfully matches the intent.

**Availability**:
- SiriKit Cloud Media 1.0.2+

## Declaration

```
object UpdateMediaAffinityMediaItemResolutionResult.Success
```

## Properties

- `resolvedMediaItem` (MediaItem) *(required)*: The song, album, podcast, or other media item that the user expresses a preference for.

## See Also

### Specifying the Result
- [object UpdateMediaAffinityMediaItemResolutionResult.Unsupported](./unsupported-data.dictionary.md)
  The reason your service can’t update information about the requested media item.
- [object UpdateMediaAffinityMediaItemResolutionResult.Disambiguation](./disambiguation-data.dictionary.md)
  A result that requires the user to choose from multiple media items before proceeding.
- [object UpdateMediaAffinityMediaItemResolutionResult.ConfirmationRequired](./confirmationrequired-data.dictionary.md)
  A result that requires the user to confirm the media item before proceeding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirikitcloudmedia/updatemediaaffinitymediaitemresolutionresult/success-data.dictionary)*