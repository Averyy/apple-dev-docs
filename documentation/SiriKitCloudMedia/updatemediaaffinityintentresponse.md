# UpdateMediaAffinityIntentResponse

**Framework**: SiriKit Cloud Media  
**Kind**: dictionary

A structure that contains a response code indicating how your service handles an update media affinity intent.

**Availability**:
- SiriKit Cloud Media 1.0.2+

## Declaration

```swift
object UpdateMediaAffinityIntentResponse
```

## Properties

- `class` (string) *(required)*: The specific type of response.
- `code` (UpdateMediaAffinityIntentResponseCode) *(required)*: A response code that indicates whether your service can play the media item.

## Relationships

### Inherits From
- [IntentResponse](intentresponse.md)

## See Also

- [object UpdateMediaAffinityIntentHandlingHandleInvocationResponse](updatemediaaffinityintenthandlinghandleinvocationresponse.md)
  Your service’s response to a request to handle a fully resolved update media affinity intent.
- [type UpdateMediaAffinityIntentResponseCode](updatemediaaffinityintentresponsecode.md)
  Codes your service can return when handling an update media affinity intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirikitcloudmedia/updatemediaaffinityintentresponse)*