# UpdateMediaAffinityIntentHandlingInvocation

**Framework**: SiriKit Cloud Media  
**Kind**: dictionary

A request to process an update media affinity intent.

**Availability**:
- SiriKit Cloud Media 1.0.2+

## Declaration

```swift
object UpdateMediaAffinityIntentHandlingInvocation
```

## Topics

### Accessing the Intent
- [object UpdateMediaAffinityIntentHandlingInvocation.Params](updatemediaaffinityintenthandlinginvocation/params-data.dictionary.md)
  The parameters of an update media affinity intent request.

## Properties

- `params` (UpdateMediaAffinityIntentHandlingInvocation.Params) *(required)*: The parameters of this request, including the update media affinity intent.
- `method` (string) *(required)*: The action for your service to take to process this intent.

## Relationships

### Inherits From
- [Invocation](invocation.md)

## See Also

- [object UpdateMediaAffinityIntent](updatemediaaffinityintent.md)
  An object that describes a user’s stated preference regarding media items.
- [type UpdateMediaAffinityIntentHandlingInvocationResponse](updatemediaaffinityintenthandlinginvocationresponse.md)
  The service’s response to a request to process an update media affinity intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirikitcloudmedia/updatemediaaffinityintenthandlinginvocation)*