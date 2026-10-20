# UpdateMediaAffinityIntentHandlingHandleInvocationResponse

**Framework**: SiriKit Cloud Media  
**Kind**: dictionary  
**Role**: Object

Your service’s response to a request to handle a fully resolved update media affinity intent.

**Availability**:
- SiriKit Cloud Media 1.0.2+

## Declaration

```
object UpdateMediaAffinityIntentHandlingHandleInvocationResponse
```

## Topics

### Specifying the Result
- [object UpdateMediaAffinityIntentHandlingHandleInvocationResponse.Result](./updatemediaaffinityintenthandlinghandleinvocationresponse/result-data.dictionary.md)
  The result of handling an intent to update media affinity.

## Properties

- `result` (UpdateMediaAffinityIntentHandlingHandleInvocationResponse.Result) *(required)*: The results of processing the intent.
- `method` (string) *(required)*: The action your service takes to process this intent.

  **Allowed Values**: `UpdateMediaAffinityIntentHandling.handle`

## Relationships

### Inherits From
- [InvocationResponse](./invocationresponse.md)

## See Also

### Handling an Update Media Affinity Intent
- [object UpdateMediaAffinityIntentResponse](./updatemediaaffinityintentresponse.md)
  A structure that contains a response code indicating how your service handles an update media affinity intent.
- [type UpdateMediaAffinityIntentResponseCode](./updatemediaaffinityintentresponsecode.md)
  Codes your service can return when handling an update media affinity intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirikitcloudmedia/updatemediaaffinityintenthandlinghandleinvocationresponse)*