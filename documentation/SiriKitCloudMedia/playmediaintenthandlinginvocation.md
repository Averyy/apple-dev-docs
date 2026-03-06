# PlayMediaIntentHandlingInvocation

**Framework**: SiriKit Cloud Media  
**Kind**: dictionary

A request to process a play media intent.

**Availability**:
- SiriKit Cloud Media 1.0.2+

## Declaration

```swift
object PlayMediaIntentHandlingInvocation
```

## Topics

### Accessing the Intent
- [object PlayMediaIntentHandlingInvocation.Params](playmediaintenthandlinginvocation/params-data.dictionary.md)
  The parameters of a play media intent request.

## Properties

- `params` (PlayMediaIntentHandlingInvocation.Params) *(required)*: The parameters of this request, including the play media intent.
- `method` (string) *(required)*: The action for your service to take to process this intent.

## Relationships

### Inherits From
- [Invocation](invocation.md)

## See Also

- [object PlayMediaIntent](playmediaintent.md)
  An object that describes the user’s request to play a media item.
- [type PlayMediaIntentHandlingInvocationResponse](playmediaintenthandlinginvocationresponse.md)
  The service’s response to a request to process a play media intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirikitcloudmedia/playmediaintenthandlinginvocation)*