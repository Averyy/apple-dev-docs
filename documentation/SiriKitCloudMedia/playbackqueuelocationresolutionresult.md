# PlaybackQueueLocationResolutionResult

**Framework**: SiriKit Cloud Media  
**Kind**: dictionary

Information about whether your service can resolve the specified queue location.

**Availability**:
- SiriKit Cloud Media 1.0.2+

## Declaration

```swift
object PlaybackQueueLocationResolutionResult
```

#### Discussion

Only provide one of the optional properties. If a client receives a result with more than one outcome, such as `needsValue` and `success`, it arbitrarily chooses one and ignores the rest.

## Topics

### Specifying a Result
- [object PlaybackQueueLocationResolutionResult.Success](playbackqueuelocationresolutionresult/success-data.dictionary.md)
  A queue location that matches the intent.
- [object PlaybackQueueLocationResolutionResult.ConfirmationRequired](playbackqueuelocationresolutionresult/confirmationrequired-data.dictionary.md)
  A result that requires the user to confirm the playback mode before proceeding.

## Relationships

### Inherits From
- [IntentResolutionResult](intentresolutionresult.md)

## See Also

- [object PlayMediaIntentHandlingResolvePlaybackQueueLocationInvocationResponse](playmediaintenthandlingresolveplaybackqueuelocationinvocationresponse.md)
  Your service’s response to a request to resolve the queue location in a play media intent.
- [type PlaybackQueueLocation](playbackqueuelocation.md)
  Possible locations in a playback queue to insert a media item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirikitcloudmedia/playbackqueuelocationresolutionresult)*