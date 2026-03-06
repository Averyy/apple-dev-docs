# Report Playback Progress and Activity

**Framework**: SiriKit Cloud Media  
**Kind**: httpRequest

Monitor progress through the playback queue.

**Availability**:
- SiriKit Cloud Media 1.0.2+

## Endpoint

`POST https://cloudextension-testservice.local/api/queues/updateActivity`

## Parameters

- `Accept-Language` (string) *(required)*: The client’s current user interface language. Respond with localized content for this language, if available.
- `User-Agent` (string) *(required)*: The extension protocol running on the client. This is an RFC 7231-compliant string that contains the product name *AppleCloudExtension* and the SiriKit Extension library version running on the client.
- `x-applecloudextension-retry-count` (uint32): The number of previous requests from the client. The client omits this header on the first attempt.
- `x-applecloudextension-session-id` (string) *(required)*: A constant session identifier to include in each request and response. Respond to each request with the session ID the client sends in that request.

## Request Body

The most recent state of the client’s playback queue.

## See Also

- [type QueueActivityReportEvent](queueactivityreportevent.md)
  An event that occurs during content playback.
- [object UpdateActivityRequest](updateactivityrequest.md)
  A report of the client’s current playback state and recent user interaction, and an opportunity for your service to modify the client’s playback queue.
- [object UpdateActivityResponse](updateactivityresponse.md)
  Updates to the client’s queue and user activity in response to a report of playback progress.
- [Process an Update Media Affinity Intent](updatemediaaffinity.md)
  Record the user’s preference for a specific media item or a broader category of media.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirikitcloudmedia/updateactivity)*