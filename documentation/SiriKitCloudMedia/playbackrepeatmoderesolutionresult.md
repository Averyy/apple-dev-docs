# PlaybackRepeatModeResolutionResult

**Framework**: SiriKit Cloud Media  
**Kind**: dictionary

Information about whether your service can identify the specified repeat mode.

**Availability**:
- SiriKit Cloud Media 1.0.2+

## Declaration

```swift
object PlaybackRepeatModeResolutionResult
```

#### Discussion

Only provide one of the optional properties. If a client receives a result with more than one outcome, such as `needsValue` and `success`, it arbitrarily chooses one and ignores the rest.

## Topics

### Specifying a Result
- [object PlaybackRepeatModeResolutionResult.Success](playbackrepeatmoderesolutionresult/success-data.dictionary.md)
  A playback mode that successfully matches the intent.
- [object PlaybackRepeatModeResolutionResult.ConfirmationRequired](playbackrepeatmoderesolutionresult/confirmationrequired-data.dictionary.md)
  A result that requires the user to confirm the playback mode before proceeding.

## Relationships

### Inherits From
- [IntentResolutionResult](intentresolutionresult.md)

## See Also

- [object PlayMediaIntentHandlingResolvePlaybackRepeatModeInvocationResponse](playmediaintenthandlingresolveplaybackrepeatmodeinvocationresponse.md)
  Your service’s response to a request to resolve the repeat mode in a play media intent.
- [object PlayMediaIntentHandlingResolvePlaybackRepeatModeInvocationResponse.Result](playmediaintenthandlingresolveplaybackrepeatmodeinvocationresponse/result-data.dictionary.md)
  The result of resolving the repeat mode for a play media intent.
- [type PlaybackRepeatMode](playbackrepeatmode.md)
  The possible repeat modes for a media queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirikitcloudmedia/playbackrepeatmoderesolutionresult)*