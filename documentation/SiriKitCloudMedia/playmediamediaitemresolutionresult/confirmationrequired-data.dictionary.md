# PlayMediaMediaItemResolutionResult.ConfirmationRequired

**Framework**: SiriKit Cloud Media  
**Kind**: dictionary  
**Role**: Object

A result that requires the user to confirm the media item before proceeding.

**Availability**:
- SiriKit Cloud Media 1.0.2+

## Declaration

```
object PlayMediaMediaItemResolutionResult.ConfirmationRequired
```

#### Discussion

Prefer to provide a successful result, even if you aren’t sure that you’re identifying the media item accurately. The user can cancel playback and try asking again.

## Properties

- `mediaItemToConfirm` (MediaItem) *(required)*: A media item for the user to confirm or reject.

## See Also

### Specifying a Result
- [object PlayMediaMediaItemResolutionResult.Success](./success-data.dictionary.md)
  A media item that successfully matches the intent.
- [object PlayMediaMediaItemResolutionResult.Unsupported](./unsupported-data.dictionary.md)
  The reason your service can’t play the requested media item.
- [object PlayMediaMediaItemResolutionResult.Disambiguation](./disambiguation-data.dictionary.md)
  A result that requires the user to choose from multiple media items before proceeding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirikitcloudmedia/playmediamediaitemresolutionresult/confirmationrequired-data.dictionary)*