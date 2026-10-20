# UpdateMediaAffinityIntentResponseCode

**Framework**: SiriKit Cloud Media  
**Kind**: typealias  
**Role**: Type

Codes your service can return when handling an update media affinity intent.

**Availability**:
- SiriKit Cloud Media 1.0.2+

## Declaration

```
string UpdateMediaAffinityIntentResponseCode
```

## Possible Values

- `success`: Your service successfully updates information about the media affinity.
- `inProgress`: Your service is handling the intent, but it may take some time.
- `failureRequiringAppLaunch`: The user needs to launch your app on their iOS device to resolve a problem.
- `failure`: A failure occurs while handling the intent.
- `unspecified`: An unspecified response code.

## See Also

### Handling an Update Media Affinity Intent
- [object UpdateMediaAffinityIntentHandlingHandleInvocationResponse](./updatemediaaffinityintenthandlinghandleinvocationresponse.md)
  Your service’s response to a request to handle a fully resolved update media affinity intent.
- [object UpdateMediaAffinityIntentResponse](./updatemediaaffinityintentresponse.md)
  A structure that contains a response code indicating how your service handles an update media affinity intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirikitcloudmedia/updatemediaaffinityintentresponsecode)*