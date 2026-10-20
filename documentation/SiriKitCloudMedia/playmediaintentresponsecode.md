# PlayMediaIntentResponseCode

**Framework**: SiriKit Cloud Media  
**Kind**: typealias  
**Role**: Type

Codes your service can return when handling a play media intent.

**Availability**:
- SiriKit Cloud Media 1.0.2+

## Declaration

```
string PlayMediaIntentResponseCode
```

## Possible Values

- `success`: Your service can play the media item. When the client receives this [`InvocationResponse`](./invocationresponse.md), it sends a request to [`Get a Media Queue`](./playmedia-1onzj.md) with the [`UserActivity`](./useractivity.md) from this response.
- `failureRestrictedContent`: Your service can’t play the media item because it’s restricted content.
- `failureNoUnplayedContent`: The user asks to resume playback, but there isn’t any unplayed content in the playback queue.
- `failureUnknownMediaType`: Your service doesn’t know how to play media items of this type.
- `failureRequiringAppLaunch`: The user needs to launch your app on their iOS device to resolve a problem.
- `failure`: A failure occurs while handling the intent.
- `unspecified`: An unspecified response code.

## See Also

### Handling a Play Media Intent
- [object PlayMediaIntentHandlingHandleInvocationResponse](./playmediaintenthandlinghandleinvocationresponse.md)
  Your service’s response to a request to handle a fully resolved play media intent.
- [object PlayMediaIntentResponse](./playmediaintentresponse.md)
  A structure that contains a response code indicating how your service handles a play media intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirikitcloudmedia/playmediaintentresponsecode)*