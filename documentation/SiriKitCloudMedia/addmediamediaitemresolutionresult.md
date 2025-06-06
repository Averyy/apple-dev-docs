# AddMediaMediaItemResolutionResult

**Framework**: SiriKit Cloud Media  
**Kind**: dictionary

A media item that matches an add media intent, or information about why your service can’t provide a media item.

**Availability**:
- SiriKit Cloud Media 1.0.2+

## Declaration

```swift
object AddMediaMediaItemResolutionResult
```

#### Discussion

Only provide one of the optional properties. If a client receives a result with more than one outcome, such as `needsValue` and `success`, it arbitrarily chooses one and ignores the rest.

## Topics

### Providing a Media Item
- [object AddMediaMediaItemResolutionResult.Success](addmediamediaitemresolutionresult/success-data.dictionary.md)
  A media item that successfully matches the intent.
### Reporting a Problem
- [object AddMediaMediaItemResolutionResult.Unsupported](addmediamediaitemresolutionresult/unsupported-data.dictionary.md)
  The reason your service can’t add the media item to the user’s library or to a playlist.
- [type AddMediaMediaItemUnsupportedReason](addmediamediaitemunsupportedreason.md)
  Reasons the media service can’t add the media item to the user’s library or to a playlist.
### Clarifying a Possible Match
- [object AddMediaMediaItemResolutionResult.ConfirmationRequired](addmediamediaitemresolutionresult/confirmationrequired-data.dictionary.md)
  A result that requires the user to confirm the media item before you add it to their library or to a playlist.
- [object AddMediaMediaItemResolutionResult.Disambiguation](addmediamediaitemresolutionresult/disambiguation-data.dictionary.md)
  A result that requires the user to choose which media item they want to add to their library or to a playlist.

## Relationships

### Inherits From
- [IntentResolutionResult](intentresolutionresult.md)

## See Also

- [object AddMediaIntentHandlingResolveMediaItemsInvocationResponse](addmediaintenthandlingresolvemediaitemsinvocationresponse.md)
  Your service’s response to a request to resolve media items in an update media affinity intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirikitcloudmedia/addmediamediaitemresolutionresult)*