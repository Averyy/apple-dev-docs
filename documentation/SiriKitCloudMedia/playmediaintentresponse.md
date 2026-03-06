# PlayMediaIntentResponse

**Framework**: SiriKit Cloud Media  
**Kind**: dictionary

A structure that contains a response code indicating how your service handles a play media intent.

**Availability**:
- SiriKit Cloud Media 1.0.2+

## Declaration

```swift
object PlayMediaIntentResponse
```

## Properties

- `class` (string) *(required)*: The specific type of response.
- `code` (PlayMediaIntentResponseCode) *(required)*: A response code that indicates whether your service can play the media item.

## Relationships

### Inherits From
- [IntentResponse](intentresponse.md)

## See Also

- [object PlayMediaIntentHandlingHandleInvocationResponse](playmediaintenthandlinghandleinvocationresponse.md)
  Your service’s response to a request to handle a fully resolved play media intent.
- [type PlayMediaIntentResponseCode](playmediaintentresponsecode.md)
  Codes your service can return when handling a play media intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirikitcloudmedia/playmediaintentresponse)*