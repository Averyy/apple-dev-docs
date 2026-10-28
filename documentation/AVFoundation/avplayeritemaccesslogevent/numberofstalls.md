# numberOfStalls

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The total number of playback stalls encountered.

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
var numberOfStalls: Int { get }
```

```objc
@property (nonatomic, readonly) NSInteger numberOfStalls;
```

## Discussion

The property corresponds to “c-stalls”.

The value of this property is negative if unknown.

This property is not compatible with key-value observing.

## See Also

### Getting playback-related log events
- [var playbackStartDate: Date?](./playbackstartdate.md)
  The date and time at which playback began for this event.
- [var playbackSessionID: String?](./playbacksessionid.md)
  A GUID that identifies the playback session.
- [var playbackStartOffset: TimeInterval](./playbackstartoffset.md)
  The offset, in seconds, in the playlist where the last uninterrupted period of playback began.
- [var playbackType: String?](./playbacktype.md)
  The playback type.
- [var startupTime: TimeInterval](./startuptime.md)
  The accumulated duration, in seconds, until the player item is ready to play.
- [var durationWatched: TimeInterval](./durationwatched.md)
  The accumulated duration, in seconds, of the media played.
- [var numberOfDroppedVideoFrames: Int](./numberofdroppedvideoframes.md)
  The total number of dropped video frames
- [var numberOfSegmentsDownloaded: Int](./numberofsegmentsdownloaded.md)
  A count of the media segments downloaded from the server to this client.
- [var segmentsDownloadedDuration: TimeInterval](./segmentsdownloadedduration.md)
  The accumulated duration, in seconds, of the media segments downloaded.
- [var downloadOverdue: Int](./downloadoverdue.md)
  The total number of times that downloading the segments took too long.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritemaccesslogevent/numberofstalls)*