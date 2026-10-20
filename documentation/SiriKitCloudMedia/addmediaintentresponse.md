# AddMediaIntentResponse

**Framework**: SiriKit Cloud Media  
**Kind**: dictionary  
**Role**: Object

A structure that contains a response code indicating your service’s progress in handling an add media intent.

**Availability**:
- SiriKit Cloud Media 1.0.2+

## Declaration

```
object AddMediaIntentResponse
```

## Properties

- `class` (string) *(required)*: The specific type of response.

  **Allowed Values**: `AddMediaIntentResponse`
- `code` (AddMediaIntentResponseCode) *(required)*: A response code that indicates whether your service can add the media items to the library or playlist.

## Relationships

### Inherits From
- [IntentResponse](./intentresponse.md)

## See Also

### Confirming and Handling an Add Media Intent
- [type AddMediaIntentResponseCode](./addmediaintentresponsecode.md)
  Codes your service can return when confirming or handling an add media intent.
- [object AddMediaIntentHandlingConfirmInvocationResponse](./addmediaintenthandlingconfirminvocationresponse.md)
  The service’s response to a request to confirm an add media intent.
- [object AddMediaIntentHandlingHandleInvocationResponse](./addmediaintenthandlinghandleinvocationresponse.md)
  Your service’s response to a request to handle a fully resolved add media intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirikitcloudmedia/addmediaintentresponse)*