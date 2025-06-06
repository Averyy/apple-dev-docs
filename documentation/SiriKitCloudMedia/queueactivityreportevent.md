# QueueActivityReportEvent

**Framework**: Sirikitcloudmedia  
**Kind**: typealias

An event that occurs during content playback.

**Availability**:
- SiriKit Cloud Media 1.0.2+

## Declaration

```swift
string QueueActivityReportEvent
```

#### Discussion

Events represent a user controlling playback or a natural transition at the end of a piece of content. The client handles playback controls, such as pausing and resuming, then sends these event reports to your service.

To customize which controls are available during playback of a piece of [`Content`](content.md), set its `control` property to a scheme you define in [`QueueControlMapping`](queuecontrolmapping.md).

> **Note**:  The like and dislike events above indicate when the user presses a corresponding control. These are separate from the user telling Siri they like or dislike some content, which the client reports to the [`Process an Update Media Affinity Intent`](updatemediaaffinity.md) endpoint.

## See Also

- [Report Playback Progress and Activity](updateactivity.md)
  Monitor progress through the playback queue.
- [object UpdateActivityRequest](updateactivityrequest.md)
  A report of the client’s current playback state and recent user interaction, and an opportunity for your service to modify the client’s playback queue.
- [object UpdateActivityResponse](updateactivityresponse.md)
  Updates to the client’s queue and user activity in response to a report of playback progress.
- [Process an Update Media Affinity Intent](updatemediaaffinity.md)
  Record the user’s preference for a specific media item or a broader category of media.


---

*[View on Apple Developer](https://developer.apple.com/documentation/SiriKitCloudMedia/queueactivityreportevent)*