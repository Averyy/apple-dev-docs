# Invocation

**Framework**: SiriKit Cloud Media  
**Kind**: dictionary

Properties that clients include in requests to all intent endpoints.

**Availability**:
- SiriKit Cloud Media 1.0.2+

## Declaration

```swift
object Invocation
```

## Topics

### Accessing the Details of a Request
- [object Invocation.Params](invocation/params-data.dictionary.md)
  The parameters of a client’s request.

## Relationships

### Inherited By
- [AddMediaIntentHandlingInvocation](addmediaintenthandlinginvocation.md)
- [PlayMediaIntentHandlingInvocation](playmediaintenthandlinginvocation.md)
- [UpdateMediaAffinityIntentHandlingInvocation](updatemediaaffinityintenthandlinginvocation.md)

## See Also

- [object Session](session.md)
  Information the client provides about a sequence of requests and responses to process an intent.
- [object Constraints](constraints.md)
  Client-originated limitations on how to process a request, such as including explicit content and how much content the client device can receive in a response.
- [object PlayerContext](playercontext.md)
  Information about the current playback content.
- [object InvocationResponse](invocationresponse.md)
  Properties to include in responses from all intent endpoints.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirikitcloudmedia/invocation)*