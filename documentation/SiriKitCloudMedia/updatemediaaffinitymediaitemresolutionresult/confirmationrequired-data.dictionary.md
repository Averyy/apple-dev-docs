# UpdateMediaAffinityMediaItemResolutionResult.ConfirmationRequired

**Framework**: SiriKit Cloud Media  
**Kind**: dictionary  
**Role**: Object

A result that requires the user to confirm the media item before proceeding.

**Availability**:
- SiriKit Cloud Media 1.0.2+

## Declaration

```
object UpdateMediaAffinityMediaItemResolutionResult.ConfirmationRequired
```

## Properties

- `mediaItemToConfirm` (MediaItem) *(required)*: A media item for the user to confirm or reject.

## See Also

### Specifying the Result
- [object UpdateMediaAffinityMediaItemResolutionResult.Success](./success-data.dictionary.md)
  A media item that successfully matches the intent.
- [object UpdateMediaAffinityMediaItemResolutionResult.Unsupported](./unsupported-data.dictionary.md)
  The reason your service can’t update information about the requested media item.
- [object UpdateMediaAffinityMediaItemResolutionResult.Disambiguation](./disambiguation-data.dictionary.md)
  A result that requires the user to choose from multiple media items before proceeding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirikitcloudmedia/updatemediaaffinitymediaitemresolutionresult/confirmationrequired-data.dictionary)*