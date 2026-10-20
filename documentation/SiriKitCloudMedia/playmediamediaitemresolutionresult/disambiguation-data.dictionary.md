# PlayMediaMediaItemResolutionResult.Disambiguation

**Framework**: SiriKit Cloud Media  
**Kind**: dictionary  
**Role**: Object

A result that requires the user to choose from multiple media items before proceeding.

**Availability**:
- SiriKit Cloud Media 1.0.2+

## Declaration

```
object PlayMediaMediaItemResolutionResult.Disambiguation
```

## Properties

- `mediaItemsToDisambiguate` ([MediaItem]) *(required)*: Media items that might match the user’s intent.

## See Also

### Specifying a Result
- [object PlayMediaMediaItemResolutionResult.Success](./success-data.dictionary.md)
  A media item that successfully matches the intent.
- [object PlayMediaMediaItemResolutionResult.Unsupported](./unsupported-data.dictionary.md)
  The reason your service can’t play the requested media item.
- [object PlayMediaMediaItemResolutionResult.ConfirmationRequired](./confirmationrequired-data.dictionary.md)
  A result that requires the user to confirm the media item before proceeding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirikitcloudmedia/playmediamediaitemresolutionresult/disambiguation-data.dictionary)*