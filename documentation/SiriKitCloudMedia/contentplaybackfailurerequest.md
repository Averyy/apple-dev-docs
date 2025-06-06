# ContentPlaybackFailureRequest

**Framework**: SiriKit Cloud Media  
**Kind**: dictionary

A request the client sends to recover from failed content playback.

**Availability**:
- SiriKit Cloud Media 1.0.2+

## Declaration

```swift
object ContentPlaybackFailureRequest
```

#### Discussion

If the playback of a queue fails to start, or there’s an error during playback from which the client can recover, the client sends this request to your service to report the failure and retrieve a new queue.

## See Also

- [Recover from Content Playback Failure](contentplaybackfailure.md)
  Provide a recovery queue that allows the client to resume playback after an error.
- [object ContentFailure](contentfailure.md)
  An object that describes why the client can’t play a specific piece of content.
- [object ContentPlaybackFailureResponse](contentplaybackfailureresponse.md)
  A response that allows the client to recover from failed content playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirikitcloudmedia/contentplaybackfailurerequest)*