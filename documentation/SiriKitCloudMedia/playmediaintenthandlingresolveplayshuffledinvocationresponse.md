# PlayMediaIntentHandlingResolvePlayShuffledInvocationResponse

**Framework**: SiriKit Cloud Media  
**Kind**: dictionary

Your service’s response to a request to resolve whether a play media intent requests a shuffled queue.

**Availability**:
- SiriKit Cloud Media 1.0.2+

## Declaration

```swift
object PlayMediaIntentHandlingResolvePlayShuffledInvocationResponse
```

## Topics

### Specifying a Result
- [object PlayMediaIntentHandlingResolvePlayShuffledInvocationResponse.Result](playmediaintenthandlingresolveplayshuffledinvocationresponse/result-data.dictionary.md)
  The result of resolving whether a play media intent shuffles the playback queue.

## Properties

- `result` (PlayMediaIntentHandlingResolvePlayShuffledInvocationResponse.Result) *(required)*: The result of processing the intent.
- `method` (string) *(required)*: The action your service takes to process this intent.

## Relationships

### Inherits From
- [InvocationResponse](invocationresponse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirikitcloudmedia/playmediaintenthandlingresolveplayshuffledinvocationresponse)*