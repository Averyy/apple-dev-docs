# PlayMediaMediaItemResolutionResult

**Framework**: SiriKit Cloud Media  
**Kind**: dictionary

A media item that matches a play media intent, or information about why your service can’t provide a media item.

**Availability**:
- SiriKit Cloud Media 1.0.2+

## Declaration

```swift
object PlayMediaMediaItemResolutionResult
```

#### Discussion

Only provide one of the optional properties. If a client receives a result with more than one outcome, such as `unsupported` and `success`, it arbitrarily chooses one and ignores the rest.

## Topics

### Specifying a Result
- [object PlayMediaMediaItemResolutionResult.Success](playmediamediaitemresolutionresult/success-data.dictionary.md)
  A media item that successfully matches the intent.
- [object PlayMediaMediaItemResolutionResult.Unsupported](playmediamediaitemresolutionresult/unsupported-data.dictionary.md)
  The reason your service can’t play the requested media item.
- [object PlayMediaMediaItemResolutionResult.Disambiguation](playmediamediaitemresolutionresult/disambiguation-data.dictionary.md)
  A result that requires the user to choose from multiple media items before proceeding.
- [object PlayMediaMediaItemResolutionResult.ConfirmationRequired](playmediamediaitemresolutionresult/confirmationrequired-data.dictionary.md)
  A result that requires the user to confirm the media item before proceeding.

## Relationships

### Inherits From
- [IntentResolutionResult](intentresolutionresult.md)

## See Also

- [object PlayMediaIntentHandlingResolveMediaItemsInvocationResponse](playmediaintenthandlingresolvemediaitemsinvocationresponse.md)
  Your service’s response to a request to resolve media items in a play media intent.
- [type PlayMediaMediaItemUnsupportedReason](playmediamediaitemunsupportedreason.md)
  Reasons the media service can’t play the media item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirikitcloudmedia/playmediamediaitemresolutionresult)*