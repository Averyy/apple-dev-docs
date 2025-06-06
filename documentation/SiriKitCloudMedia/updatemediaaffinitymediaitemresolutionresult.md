# UpdateMediaAffinityMediaItemResolutionResult

**Framework**: SiriKit Cloud Media  
**Kind**: dictionary

A media item that matches an update media affinity intent, or information about why your service can’t provide a media item.

**Availability**:
- SiriKit Cloud Media 1.0.2+

## Declaration

```swift
object UpdateMediaAffinityMediaItemResolutionResult
```

## Topics

### Specifying the Result
- [object UpdateMediaAffinityMediaItemResolutionResult.Success](updatemediaaffinitymediaitemresolutionresult/success-data.dictionary.md)
  A media item that successfully matches the intent.
- [object UpdateMediaAffinityMediaItemResolutionResult.Unsupported](updatemediaaffinitymediaitemresolutionresult/unsupported-data.dictionary.md)
  The reason your service can’t update information about the requested media item.
- [object UpdateMediaAffinityMediaItemResolutionResult.Disambiguation](updatemediaaffinitymediaitemresolutionresult/disambiguation-data.dictionary.md)
  A result that requires the user to choose from multiple media items before proceeding.
- [object UpdateMediaAffinityMediaItemResolutionResult.ConfirmationRequired](updatemediaaffinitymediaitemresolutionresult/confirmationrequired-data.dictionary.md)
  A result that requires the user to confirm the media item before proceeding.

## Relationships

### Inherits From
- [IntentResolutionResult](intentresolutionresult.md)

## See Also

- [object UpdateMediaAffinityIntentHandlingResolveMediaItemsInvocationResponse](updatemediaaffinityintenthandlingresolvemediaitemsinvocationresponse.md)
  Your service’s response to a request to resolve media items in an update media affinity intent.
- [type UpdateMediaAffinityMediaItemUnsupportedReason](updatemediaaffinitymediaitemunsupportedreason.md)
  Reasons the media service can’t update information about the media item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirikitcloudmedia/updatemediaaffinitymediaitemresolutionresult)*