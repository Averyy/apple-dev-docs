# AddMediaMediaDestinationResolutionResult

**Framework**: SiriKit Cloud Media  
**Kind**: dictionary

The user’s library or a specified playlist, or information about why your service can’t use the requested destination.

**Availability**:
- SiriKit Cloud Media 1.0.2+

## Declaration

```swift
object AddMediaMediaDestinationResolutionResult
```

#### Discussion

Only provide one of the optional properties. If a client receives a result with more than one outcome, such as `needsValue` and `success`, it arbitrarily chooses one and ignores the rest.

## Topics

### Providing a Destination
- [object AddMediaMediaDestinationResolutionResult.Success](addmediamediadestinationresolutionresult/success-data.dictionary.md)
  A media destination that successfully matches an intent.
- [object MediaDestination](mediadestination.md)
  The user’s library or a playlist.
- [object MediaDestinationLibrary](mediadestinationlibrary.md)
  The user’s library as a destination for an add media intent.
- [object MediaDestinationPlaylist](mediadestinationplaylist.md)
  A playlist as a destination for an add media intent.
### Reporting a Problem
- [object AddMediaMediaDestinationResolutionResult.Unsupported](addmediamediadestinationresolutionresult/unsupported-data.dictionary.md)
  The reason your service can’t add media items to the specified library or playlist.
- [type AddMediaMediaDestinationUnsupportedReason](addmediamediadestinationunsupportedreason.md)
  Reasons the media service can’t add media items to a specified playlist.
### Clarifying a Possible Match
- [object AddMediaMediaDestinationResolutionResult.ConfirmationRequired](addmediamediadestinationresolutionresult/confirmationrequired-data.dictionary.md)
  A result that requires the user to confirm the library or playlist before you add media items to it.
- [object AddMediaMediaDestinationResolutionResult.Disambiguation](addmediamediadestinationresolutionresult/disambiguation-data.dictionary.md)
  A result that requires the user to choose which library or playlist they want to add media items to.

## Relationships

### Inherits From
- [IntentResolutionResult](intentresolutionresult.md)

## See Also

- [object AddMediaIntentHandlingResolveMediaDestinationInvocationResponse](addmediaintenthandlingresolvemediadestinationinvocationresponse.md)
  Your service’s response to a request to resolve media items in an add media intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirikitcloudmedia/addmediamediadestinationresolutionresult)*