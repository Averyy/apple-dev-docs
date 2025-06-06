# AVPlayerInterstitialEvent

**Framework**: Avfoundation  
**Kind**: class

An object that provides instructions for how a player presents interstitial content.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
class AVPlayerInterstitialEvent
```

#### Overview

An interstitial event defines a [`date`](avplayerinterstitialevent/date.md) or [`time`](avplayerinterstitialevent/time.md), on the timeline of its [`primaryItem`](avplayerinterstitialevent/primaryitem.md), at which playback of interstitial content begins. It specifies the alternative interstitial content to play as an array of one or more template player items. The system uses the configuration of the event’s [`templateItems`](avplayerinterstitialevent/templateitems.md) to build new player item instances to present the interstitial content.

Use [`AVPlayerInterstitialEventMonitor`](avplayerinterstitialeventmonitor.md) to observe the scheduling and progress of interstitial events. If your app requires specifying the schedule of interstitial events, use [`AVPlayerInterstitialEventController`](avplayerinterstitialeventcontroller.md) instead.

> **Note**:  [`AVPlayerInterstitialEvent`](avplayerinterstitialevent.md) was previously an immutable type. Starting in iOS 16, tvOS 16, macOS 13, and watchOS 9, it’s now a mutable type, which allows you to create and customize an event before setting it on an [`AVPlayerInterstitialEventController`](avplayerinterstitialeventcontroller.md).

## Topics

### Creating an event
- [convenience init(primaryItem: AVPlayerItem, time: CMTime)](avplayerinterstitialevent/init(primaryitem:time:).md)
  Creates an interstitial event for the specified time.
- [convenience init(primaryItem: AVPlayerItem, date: Date)](avplayerinterstitialevent/init(primaryitem:date:).md)
  Creates an interstitial event for the specified date.
- [convenience init(primaryItem: AVPlayerItem, identifier: String?, time: CMTime, templateItems: [AVPlayerItem], restrictions: AVPlayerInterstitialEvent.Restrictions, resumptionOffset: CMTime, playoutLimit: CMTime, userDefinedAttributes: [String : Any])](avplayerinterstitialevent/init(primaryitem:identifier:time:templateitems:restrictions:resumptionoffset:playoutlimit:userdefinedattributes:).md)
  Creates an interstitial event, with user-defined attributes, for the specified time.
- [convenience init(primaryItem: AVPlayerItem, identifier: String?, date: Date, templateItems: [AVPlayerItem], restrictions: AVPlayerInterstitialEvent.Restrictions, resumptionOffset: CMTime, playoutLimit: CMTime, userDefinedAttributes: [String : Any])](avplayerinterstitialevent/init(primaryitem:identifier:date:templateitems:restrictions:resumptionoffset:playoutlimit:userdefinedattributes:).md)
  Creates an interstitial event, with user-defined attributes, for the specified date.
### Identifying events
- [var identifier: String](avplayerinterstitialevent/identifier.md)
  An identifier for the event.
### Accessing player items
- [var primaryItem: AVPlayerItem?](avplayerinterstitialevent/primaryitem.md)
  The player item that represents the primary content.
- [var templateItems: [AVPlayerItem]](avplayerinterstitialevent/templateitems.md)
  An array of player item configurations to use as templates for player items that play interstitial content.
### Configuring cues
- [var cue: AVPlayerInterstitialEvent.Cue](avplayerinterstitialevent/cue-swift.property.md)
  A cue to schedule interstitial event playback at a predefined position during primary playback.
- [AVPlayerInterstitialEvent.Cue](avplayerinterstitialevent/cue-swift.struct.md)
  A structure that defines standard cues to play interstitial content.
### Inspecting timing
- [var time: CMTime](avplayerinterstitialevent/time.md)
  A time within the timeline of the primary content that playback of interstitial content begins.
- [var date: Date?](avplayerinterstitialevent/date.md)
  A date within the date range of the primary content that playback of interstitial content begins.
- [var willPlayOnce: Bool](avplayerinterstitialevent/willplayonce.md)
  A Boolean value that indicates whether to schedule this event one time only and suppress subsequent replay.
- [var resumptionOffset: CMTime](avplayerinterstitialevent/resumptionoffset.md)
  A time offset at which playback of primary content resumes after interstitial content finishes.
- [var playoutLimit: CMTime](avplayerinterstitialevent/playoutlimit.md)
  The time offset at which playback of the interstitial ends.
- [var alignsStartWithPrimarySegmentBoundary: Bool](avplayerinterstitialevent/alignsstartwithprimarysegmentboundary.md)
  A Boolean value that indicates whether the start time of interstitial playback should snap to a segment boundary of the primary asset.
- [var alignsResumptionWithPrimarySegmentBoundary: Bool](avplayerinterstitialevent/alignsresumptionwithprimarysegmentboundary.md)
  A Boolean value that indicates whether the resumption time of primary playback should snap to a segment boundary of the primary asset.
### Managing restrictions
- [var restrictions: AVPlayerInterstitialEvent.Restrictions](avplayerinterstitialevent/restrictions-swift.property.md)
  The restrictions the event imposes on the playback of interstitial content.
- [AVPlayerInterstitialEvent.Restrictions](avplayerinterstitialevent/restrictions-swift.struct.md)
  Constants that define restrictions on the playback of interstitial content.
### Accessing asset lists
- [var assetListResponse: [AnyHashable : any Sendable]?](avplayerinterstitialevent/assetlistresponse.md)
  The asset list JSON response as a dictionary.
### Accessing attributes
- [var userDefinedAttributes: [AnyHashable : any Sendable]](avplayerinterstitialevent/userdefinedattributes.md)
  Attributes of the event that the vendor or app defines.
### Inspecting timeline occupancy
- [var timelineOccupancy: AVPlayerInterstitialEvent.TimelineOccupancy](avplayerinterstitialevent/timelineoccupancy-swift.property.md)
  An event’s occupancy on the integrated timeline.
- [AVPlayerInterstitialEvent.TimelineOccupancy](avplayerinterstitialevent/timelineoccupancy-swift.enum.md)
  Constants that specify how an event occupies time on an integrated timeline.
- [var supplementsPrimaryContent: Bool](avplayerinterstitialevent/supplementsprimarycontent.md)
  A Boolean value that indicates whether an event supplements the primary content and should present with the primary item.
- [var contentMayVary: Bool](avplayerinterstitialevent/contentmayvary.md)
  A Boolean value that indicates whether an event’s content is dynamic and the server may respond with different interstitial assets for other participants in a coordinated playback session.
- [var plannedDuration: CMTime](avplayerinterstitialevent/plannedduration.md)
  The planned duration of the event.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Providing an integrated view of your timeline when playing HLS interstitials](providing-an-integrated-view-of-your-timeline-when-playing-hls-interstitials.md)
  Go beyond simple ad insertion with point and fill occupancy HLS interstitials.
- [class AVPlayerInterstitialEventController](avplayerinterstitialeventcontroller.md)
  An object that schedules interstitial events for items played by the primary player.
- [class AVPlayerInterstitialEventMonitor](avplayerinterstitialeventmonitor.md)
  An object that monitors the scheduling and progress of interstitial events.
- [class AVPlayerItemIntegratedTimeline](avplayeritemintegratedtimeline.md)
  An object that models the timeline and playback sequence of a primary player item and scheduled interstitial events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/AVFoundation/avplayerinterstitialevent)*