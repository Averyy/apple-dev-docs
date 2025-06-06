# MediaAffinityTypeResolutionResult

**Framework**: SiriKit Cloud Media  
**Kind**: dictionary

A media affinity that matches an update media affinity intent, or information about why your service can’t determine the media affinity.

**Availability**:
- SiriKit Cloud Media 1.0.2+

## Declaration

```swift
object MediaAffinityTypeResolutionResult
```

#### Discussion

Only provide one of the optional properties. If a client receives a result with more than one outcome, such as `needsValue` and `success`, it arbitrarily chooses one and ignores the rest.

## Topics

### Specifying the Result
- [object MediaAffinityTypeResolutionResult.ConfirmationRequired](mediaaffinitytyperesolutionresult/confirmationrequired-data.dictionary.md)
  A result that requires the user to confirm the media affinity before proceeding.
- [object MediaAffinityTypeResolutionResult.Success](mediaaffinitytyperesolutionresult/success-data.dictionary.md)
  A media affinity that successfully matches the intent.

## Relationships

### Inherits From
- [IntentResolutionResult](intentresolutionresult.md)

## See Also

- [type MediaAffinityType](mediaaffinitytype.md)
  A preference or dislike for a media item.
- [object UpdateMediaAffinityIntentHandlingResolveAffinityTypeInvocationResponse](updatemediaaffinityintenthandlingresolveaffinitytypeinvocationresponse.md)
  Your service’s response to a request that expresses a preference or dislike for a media item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirikitcloudmedia/mediaaffinitytyperesolutionresult)*