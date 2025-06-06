# UserActivity

**Framework**: SiriKit Cloud Media  
**Kind**: dictionary

The context for playing a media queue.

**Availability**:
- SiriKit Cloud Media 1.0.2+

## Declaration

```swift
object UserActivity
```

#### Discussion

Create a `UserActivity` and provide it in your response to a [`Process a Play Media Intent`](playmedia-1g2o9.md). When the client receives your response, it includes this activity in its request to [`Get a Media Queue`](playmedia-1onzj.md) to define the queue it’s requesting.

## Topics

### Maintaining State
- [object UserActivity.UserActivityUserInfo](useractivity/useractivityuserinfo.md)
  A dictionary that contains service-specific state information necessary to continue an activity in a separate request.

## See Also

- [object Intent](intent.md)
  A user request for your service to fulfill.
- [object IntentResponse](intentresponse.md)
  Your service’s response to an intent.
- [object IntentResolutionResult](intentresolutionresult.md)
  An object that matches a parameter of an intent, or information about why your service can’t determine a value for the parameter.
- [object BooleanResolutionResult](booleanresolutionresult.md)
  A Boolean value that matches an intent parameter, or information about why your service can’t determine the value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirikitcloudmedia/useractivity)*