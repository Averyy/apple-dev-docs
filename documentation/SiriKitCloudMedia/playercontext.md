# PlayerContext

**Framework**: SiriKit Cloud Media  
**Kind**: dictionary

Information about the current playback content.

**Availability**:
- SiriKit Cloud Media 1.0.2+

## Declaration

```swift
object PlayerContext
```

## Properties

- `activityIdentifier` (string): The ID for the client’s current [`UserActivity`](useractivity.md).
- `queueIdentifier` (QueueIdentifier): The ID of the playback queue that contains the current content.
- `contentIdentifier` (ContentIdentifier): The ID for the content the client is playing.
- `offsetInMillis` (int64): The number of milliseconds into the playback progress of the current content.
- `playbackSpeed` (double): The content’s playback speed.

## See Also

- [object Invocation](invocation.md)
  Properties that clients include in requests to all intent endpoints.
- [object Session](session.md)
  Information the client provides about a sequence of requests and responses to process an intent.
- [object Constraints](constraints.md)
  Client-originated limitations on how to process a request, such as including explicit content and how much content the client device can receive in a response.
- [object InvocationResponse](invocationresponse.md)
  Properties to include in responses from all intent endpoints.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirikitcloudmedia/playercontext)*