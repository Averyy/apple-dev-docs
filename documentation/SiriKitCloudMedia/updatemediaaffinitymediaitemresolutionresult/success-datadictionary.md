# UpdateMediaAffinityMediaItemResolutionResult.Success

**Framework**: SiriKit Cloud Media  
**Kind**: dictionary

A media item that successfully matches the intent.

**Availability**:
- SiriKit Cloud Media 1.0.2+

## Declaration

```swift
object UpdateMediaAffinityMediaItemResolutionResult.Success
```

## Properties

- `resolvedMediaItem` (MediaItem) *(required)*: The song, album, podcast, or other media item that the user expresses a preference for.

## See Also

- [object UpdateMediaAffinityMediaItemResolutionResult.Unsupported](updatemediaaffinitymediaitemresolutionresult/unsupported-data.dictionary.md)
  The reason your service can’t update information about the requested media item.
- [object UpdateMediaAffinityMediaItemResolutionResult.Disambiguation](updatemediaaffinitymediaitemresolutionresult/disambiguation-data.dictionary.md)
  A result that requires the user to choose from multiple media items before proceeding.
- [object UpdateMediaAffinityMediaItemResolutionResult.ConfirmationRequired](updatemediaaffinitymediaitemresolutionresult/confirmationrequired-data.dictionary.md)
  A result that requires the user to confirm the media item before proceeding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirikitcloudmedia/updatemediaaffinitymediaitemresolutionresult/success-data.dictionary)*