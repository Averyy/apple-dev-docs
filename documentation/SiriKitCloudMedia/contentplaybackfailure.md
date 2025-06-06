# Recover from Content Playback Failure

**Framework**: SiriKit Cloud Media  
**Kind**: httpRequest

Provide a recovery queue that allows the client to resume playback after an error.

**Availability**:
- SiriKit Cloud Media 1.0.2+

#### Discussion

If the playback of a queue fails to start, or there’s an error during playback that the client can recover from, the client reports the failure by sending a request to this endpoint. Configure your service to respond with a recovery queue that the client can use to restart playback.

Examples of recoverable playback failures include:

- The client is unable to load the media using the provided URL.
- The client is unable to acquire a content key for a protected asset.
- The number of items in the queue segment exceeds the configured maximum.

## Request Body

A JSON object that describes the playback failure, the state of the current queue, and the constraints to apply to the recovery queue.

## See Also

- [object ContentFailure](contentfailure.md)
  An object that describes why the client can’t play a specific piece of content.
- [object ContentPlaybackFailureRequest](contentplaybackfailurerequest.md)
  A request the client sends to recover from failed content playback.
- [object ContentPlaybackFailureResponse](contentplaybackfailureresponse.md)
  A response that allows the client to recover from failed content playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirikitcloudmedia/contentplaybackfailure)*