# AddMediaIntentResponseCode

**Framework**: SiriKit Cloud Media  
**Kind**: typealias  
**Role**: Type

Codes your service can return when confirming or handling an add media intent.

**Availability**:
- SiriKit Cloud Media 1.0.2+

## Declaration

```
string AddMediaIntentResponseCode
```

## Possible Values

- `success`: Your service successfully adds the media items to the specified destination. Use this in an [`AddMediaIntentHandlingHandleInvocationResponse.Result`](./addmediaintenthandlinghandleinvocationresponse/result-data.dictionary.md).
- `ready`: Your service is ready and able to add the media items to the specified destination. Use this in an [`AddMediaIntentHandlingConfirmInvocationResponse.Result`](./addmediaintenthandlingconfirminvocationresponse/result-data.dictionary.md).
- `inProgress`: Your service is adding the media items to the specified destination, but it may take some time. Use this in an [`AddMediaIntentHandlingHandleInvocationResponse.Result`](./addmediaintenthandlinghandleinvocationresponse/result-data.dictionary.md).
- `failureRequiringAppLaunch`: The user needs to launch your app on their iOS device to resolve a problem.
- `failure`: A failure occurs while confirming or handling the intent.
- `unspecified`: An unspecified response code.

## See Also

### Confirming and Handling an Add Media Intent
- [object AddMediaIntentResponse](./addmediaintentresponse.md)
  A structure that contains a response code indicating your service’s progress in handling an add media intent.
- [object AddMediaIntentHandlingConfirmInvocationResponse](./addmediaintenthandlingconfirminvocationresponse.md)
  The service’s response to a request to confirm an add media intent.
- [object AddMediaIntentHandlingHandleInvocationResponse](./addmediaintenthandlinghandleinvocationresponse.md)
  Your service’s response to a request to handle a fully resolved add media intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirikitcloudmedia/addmediaintentresponsecode)*