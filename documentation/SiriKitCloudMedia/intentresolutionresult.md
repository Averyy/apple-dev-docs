# IntentResolutionResult

**Framework**: SiriKit Cloud Media  
**Kind**: dictionary

An object that matches a parameter of an intent, or information about why your service can’t determine a value for the parameter.

**Availability**:
- SiriKit Cloud Media 1.0.2+

## Declaration

```swift
object IntentResolutionResult
```

## Topics

### Providing a Generic Result
- [object IntentResolutionResult.NeedsValue](intentresolutionresult/needsvalue-data.dictionary.md)
  An empty object that indicates the service must have a value for this parameter, but the intent doesn’t include one.
- [object IntentResolutionResult.NotRequired](intentresolutionresult/notrequired-data.dictionary.md)
  An empty object that indicates the intent doesn’t include a value for this parameter, but the server can proceed without one.
- [object IntentResolutionResult.Unsupported](intentresolutionresult/unsupported-data.dictionary.md)
  An empty object that indicates the server doesn’t support this parameter.

## Relationships

### Inherited By
- [AddMediaMediaDestinationResolutionResult](addmediamediadestinationresolutionresult.md)
- [AddMediaMediaItemResolutionResult](addmediamediaitemresolutionresult.md)
- [BooleanResolutionResult](booleanresolutionresult.md)
- [MediaAffinityTypeResolutionResult](mediaaffinitytyperesolutionresult.md)
- [PlayMediaMediaItemResolutionResult](playmediamediaitemresolutionresult.md)
- [PlaybackQueueLocationResolutionResult](playbackqueuelocationresolutionresult.md)
- [PlaybackRepeatModeResolutionResult](playbackrepeatmoderesolutionresult.md)
- [UpdateMediaAffinityMediaItemResolutionResult](updatemediaaffinitymediaitemresolutionresult.md)

## See Also

- [object Intent](intent.md)
  A user request for your service to fulfill.
- [object IntentResponse](intentresponse.md)
  Your service’s response to an intent.
- [object UserActivity](useractivity.md)
  The context for playing a media queue.
- [object BooleanResolutionResult](booleanresolutionresult.md)
  A Boolean value that matches an intent parameter, or information about why your service can’t determine the value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirikitcloudmedia/intentresolutionresult)*