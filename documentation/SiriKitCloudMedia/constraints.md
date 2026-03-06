# Constraints

**Framework**: SiriKit Cloud Media  
**Kind**: dictionary

Client-originated limitations on how to process a request, such as including explicit content and how much content the client device can receive in a response.

**Availability**:
- SiriKit Cloud Media 1.0.2+

## Declaration

```swift
object Constraints
```

## Properties

- `allowExplicitContent` (boolean): An indicator of whether it’s OK for your service to provide explicit content.
- `maximumQueueSegmentItemCount` (uint32): The maximum number of pieces to provide in a [`Queue`](queue.md).
- `updateUserTasteProfile` (boolean): An indicator of whether to use these interactions to update your service’s model of the user’s likes and dislikes.

## See Also

- [object Invocation](invocation.md)
  Properties that clients include in requests to all intent endpoints.
- [object Session](session.md)
  Information the client provides about a sequence of requests and responses to process an intent.
- [object PlayerContext](playercontext.md)
  Information about the current playback content.
- [object InvocationResponse](invocationresponse.md)
  Properties to include in responses from all intent endpoints.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirikitcloudmedia/constraints)*