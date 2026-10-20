# AddMediaMediaItemResolutionResult.Disambiguation

**Framework**: SiriKit Cloud Media  
**Kind**: dictionary  
**Role**: Object

A result that requires the user to choose which media item they want to add to their library or to a playlist.

**Availability**:
- SiriKit Cloud Media 1.0.2+

## Declaration

```
object AddMediaMediaItemResolutionResult.Disambiguation
```

## Properties

- `mediaItemsToDisambiguate` ([MediaItem]) *(required)*: Media items that might match the user’s intent.

## See Also

### Clarifying a Possible Match
- [object AddMediaMediaItemResolutionResult.ConfirmationRequired](./confirmationrequired-data.dictionary.md)
  A result that requires the user to confirm the media item before you add it to their library or to a playlist.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirikitcloudmedia/addmediamediaitemresolutionresult/disambiguation-data.dictionary)*