# AddMediaIntentHandlingInvocation

**Framework**: SiriKit Cloud Media  
**Kind**: dictionary

A request to process an add media intent.

**Availability**:
- SiriKit Cloud Media 1.0.2+

## Declaration

```swift
object AddMediaIntentHandlingInvocation
```

## Topics

### Accessing the Intent
- [object AddMediaIntentHandlingInvocation.Params](addmediaintenthandlinginvocation/params-data.dictionary.md)
  The parameters of an add media intent request.

## Properties

- `params` (AddMediaIntentHandlingInvocation.Params) *(required)*: The parameters of this request, including the add media intent.
- `method` (string) *(required)*: An action for your service to take to process this intent.

## Relationships

### Inherits From
- [Invocation](invocation.md)

## See Also

- [object AddMediaIntent](addmediaintent.md)
  An object that describes the user’s request to add media items to their library or to a specific playlist.
- [type AddMediaIntentHandlingInvocationResponse](addmediaintenthandlinginvocationresponse.md)
  The service’s response to a request to process an add media intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirikitcloudmedia/addmediaintenthandlinginvocation)*