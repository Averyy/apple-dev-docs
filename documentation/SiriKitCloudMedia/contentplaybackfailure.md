# Recover from Content Playback Failure

**Framework**: SiriKit Cloud Media  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Provide a recovery queue that allows the client to resume playback after an error.

**Availability**:
- SiriKit Cloud Media 1.0.2+

## Discussion

If the playback of a queue fails to start, or there’s an error during playback that the client can recover from, the client reports the failure by sending a request to this endpoint. Configure your service to respond with a recovery queue that the client can use to restart playback.

Examples of recoverable playback failures include:

- The client is unable to load the media using the provided URL.
- The client is unable to acquire a content key for a protected asset.
- The number of items in the queue segment exceeds the configured maximum.

## Endpoint

`POST https://cloudextension-testservice.local/api/queues/contentPlaybackFailure`

## Parameters

### Header Parameters

- `Accept-Language` (string): The client’s current user interface language. If possible, respond with localized content for this language.
- `User-Agent` (string) *(required)*: The client’s extension protocol. This is an RFC 7231-compliant string that contains the product name `AppleCloudExtension` and the version of the SiriKit extension library that’s running on the client.

  **Maximum Length**: `250`; **Allowed Values**: `/AppleCloudExtension/([0-9]+\.[0-9]+\.[0-9]+) *.*/`
- `x-applecloudextension-retry-count` (uint32): The number of previous requests from the client. The client omits this header on the first attempt.

  **Minimum**: `1`
- `x-applecloudextension-session-id` (string) *(required)*: A session identifier to pair each request and response. Respond to requests with the value the client provides.

  **Minimum Length**: `1`; **Maximum Length**: `128`

## Request Body

**Content-Type**: `application/json`  
**Type**: `ContentPlaybackFailureRequest`

A JSON object that describes the playback failure, the state of the current queue, and the constraints to apply to the recovery queue.

## Responses

- `200` OK (`Queue`, `application/json`): The request is successful.
- `204` No Content: The service is unable to provide a recovery queue segment.
- `401` Unauthorized: The request requires authorization. The client can attempt to reauthorize and then retry the request.
- `410` Gone: The request includes an expired [`UserActivity`](./useractivity.md), which the service is unable to use to provide a recovery queue segment.

## See Also

### Playback Failure
- [object ContentFailure](./contentfailure.md)
  An object that describes why the client can’t play a specific piece of content.
- [object ContentPlaybackFailureRequest](./contentplaybackfailurerequest.md)
  A request the client sends to recover from failed content playback.
- [object ContentPlaybackFailureResponse](./contentplaybackfailureresponse.md)
  A response that allows the client to recover from failed content playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirikitcloudmedia/contentplaybackfailure)*