# Report Playback Progress and Activity

**Framework**: SiriKit Cloud Media  
**Kind**: httpRequest

Monitor progress through the playback queue.

**Availability**:
- SiriKit Cloud Media 1.0.2+

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