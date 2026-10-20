# QueueActivityReportEvent

**Framework**: SiriKit Cloud Media  
**Kind**: typealias  
**Role**: Type

An event that occurs during content playback.

**Availability**:
- SiriKit Cloud Media 1.0.2+

## Declaration

```
string QueueActivityReportEvent
```

## Possible Values

- `local.playing.elapsed`: A periodic report of playback progress. Use [`PlayMediaControlActivity`](./playmediacontrolactivity.md) to schedule these reports.
- `local.playing.paused`: The user pauses playback.
- `local.playing.continued`: The user resumes playback after a pause.
- `local.playing.fastForward`: The user fast-forwards the content.
- `local.playing.fastRewind`: The user rewinds the content.
- `local.playing.scrub`: The user uses the `seekToPlaybackPosition` control.
- `local.playing.transitioned.skip_next`: The user skips forward to the next content.
- `local.playing.transitioned.skip_previous`: The user skips backward to the previous content or to the start of the current content.
- `local.stopped.skip_past_end`: Playback ends because the user skips forward while playing the last content in the queue.
- `local.playing.transitioned.naturally`: The current content starts playing because the previous content ends.
- `local.playing.transitioned.queue_replaced`: The client receives a new queue from your service and starts playing that queue.
- `local.stopped.naturally`: The last content in the playback queue finishes playing.
- `local.command.like`: The user selects the like control.
- `local.command.dislike`: The user selects the dislike control.
- `local.command.bookmark`: The user bookmarks the content.
- `local.stopped.content_failure`

#### Discussion

Events represent a user controlling playback or a natural transition at the end of a piece of content. The client handles playback controls, such as pausing and resuming, then sends these event reports to your service.

To customize which controls are available during playback of a piece of [`Content`](./content.md), set its `control` property to a scheme you define in [`QueueControlMapping`](./queuecontrolmapping.md).

> **Note**:  The like and dislike events above indicate when the user presses a corresponding control. These are separate from the user telling Siri they like or dislike some content, which the client reports to the [`Process an Update Media Affinity Intent`](./updatemediaaffinity.md) endpoint.

## See Also

### Playback Events
- [Report Playback Progress and Activity](./updateactivity.md)
  Monitor progress through the playback queue.
- [object UpdateActivityRequest](./updateactivityrequest.md)
  A report of the client’s current playback state and recent user interaction, and an opportunity for your service to modify the client’s playback queue.
- [object UpdateActivityResponse](./updateactivityresponse.md)
  Updates to the client’s queue and user activity in response to a report of playback progress.
- [Process an Update Media Affinity Intent](./updatemediaaffinity.md)
  Record the user’s preference for a specific media item or a broader category of media.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirikitcloudmedia/queueactivityreportevent)*