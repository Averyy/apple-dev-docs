# ContentPlaybackFailureResponse

**Framework**: SiriKit Cloud Media  
**Kind**: dictionary

A response that allows the client to recover from failed content playback.

**Availability**:
- SiriKit Cloud Media 1.0.2+

## Declaration

```swift
object ContentPlaybackFailureResponse
```

## Properties

- `version` (string): The version of the client’s `SiriKitMediaAPI` library.
- `queue` (Queue): The [`Queue`](queue.md) segment the client uses to recover from the playback failure.

## See Also

- [Recover from Content Playback Failure](contentplaybackfailure.md)
  Provide a recovery queue that allows the client to resume playback after an error.
- [object ContentFailure](contentfailure.md)
  An object that describes why the client can’t play a specific piece of content.
- [object ContentPlaybackFailureRequest](contentplaybackfailurerequest.md)
  A request the client sends to recover from failed content playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirikitcloudmedia/contentplaybackfailureresponse)*