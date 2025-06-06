# playbackStartDate

**Framework**: AVFoundation  
**Kind**: property

The date and time at which playback began for this event.

**Availability**:
- iOS 4.3+
- iPadOS 4.3+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
var playbackStartDate: Date? { get }
```

#### Discussion

The property corresponds to “date”.

The value of this property is `nil` if unknown.

This property is not compatible with key-value observing.

## See Also

- [var playbackSessionID: String?](avplayeritemaccesslogevent/playbacksessionid.md)
  A GUID that identifies the playback session.
- [var playbackStartOffset: TimeInterval](avplayeritemaccesslogevent/playbackstartoffset.md)
  The offset, in seconds, in the playlist where the last uninterrupted period of playback began.
- [var playbackType: String?](avplayeritemaccesslogevent/playbacktype.md)
  The playback type.
- [var startupTime: TimeInterval](avplayeritemaccesslogevent/startuptime.md)
  The accumulated duration, in seconds, until the player item is ready to play.
- [var durationWatched: TimeInterval](avplayeritemaccesslogevent/durationwatched.md)
  The accumulated duration, in seconds, of the media played.
- [var numberOfDroppedVideoFrames: Int](avplayeritemaccesslogevent/numberofdroppedvideoframes.md)
  The total number of dropped video frames
- [var numberOfStalls: Int](avplayeritemaccesslogevent/numberofstalls.md)
  The total number of playback stalls encountered.
- [var numberOfSegmentsDownloaded: Int](avplayeritemaccesslogevent/numberofsegmentsdownloaded.md)
  A count of the media segments downloaded from the server to this client.
- [var segmentsDownloadedDuration: TimeInterval](avplayeritemaccesslogevent/segmentsdownloadedduration.md)
  The accumulated duration, in seconds, of the media segments downloaded.
- [var downloadOverdue: Int](avplayeritemaccesslogevent/downloadoverdue.md)
  The total number of times that downloading the segments took too long.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritemaccesslogevent/playbackstartdate)*