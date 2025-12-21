# AVPlayerItemAccessLogEvent

**Framework**: AVFoundation  
**Kind**: class

A single entry in a player item’s access log.

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
class AVPlayerItemAccessLogEvent
```

#### Overview

This object provides named properties for accessing the data fields of each log event. Each event is a single entry in an [`AVPlayerItem`](avplayeritem.md) object’s access log.

These properties aren’t observable. For more information about key-value observing, see [`Using Key-Value Observing in Swift`](https://developer.apple.com/documentation/Swift/using-key-value-observing-in-swift).

## Topics

### Getting server-related log events
- [var uri: String?](avplayeritemaccesslogevent/uri.md)
  The URI of the playback item.
- [var serverAddress: String?](avplayeritemaccesslogevent/serveraddress.md)
  The IP address of the server that was the source of the last delivered media segment.
- [var numberOfServerAddressChanges: Int](avplayeritemaccesslogevent/numberofserveraddresschanges.md)
  A count of changes to the server address over the last uninterrupted period of playback.
- [var mediaRequestsWWAN: Int](avplayeritemaccesslogevent/mediarequestswwan.md)
  The number of network read requests over a WWAN.
- [var transferDuration: TimeInterval](avplayeritemaccesslogevent/transferduration.md)
  The accumulated duration, in seconds, of active network transfer of bytes.
- [var numberOfBytesTransferred: Int64](avplayeritemaccesslogevent/numberofbytestransferred.md)
  The accumulated number of bytes transferred by the item.
- [var numberOfMediaRequests: Int](avplayeritemaccesslogevent/numberofmediarequests.md)
  The number of media read requests from the server to this client.
### Getting playback-related log events
- [var playbackStartDate: Date?](avplayeritemaccesslogevent/playbackstartdate.md)
  The date and time at which playback began for this event.
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
### Getting bit rate log events
- [var observedBitrateStandardDeviation: Double](avplayeritemaccesslogevent/observedbitratestandarddeviation.md)
  The standard deviation of the observed segment download bit rates.
- [var observedMaxBitrate: Double](avplayeritemaccesslogevent/observedmaxbitrate.md)
  The maximum observed segment download bit rate.
- [var observedMinBitrate: Double](avplayeritemaccesslogevent/observedminbitrate.md)
  The minimum observed segment download bit rate.
- [var switchBitrate: Double](avplayeritemaccesslogevent/switchbitrate.md)
  The bandwidth value that causes a switch, up or down, in the item’s quality being played.
- [var indicatedBitrate: Double](avplayeritemaccesslogevent/indicatedbitrate.md)
  The throughput, in bits per second, required to play the stream, as advertised by the server.
- [var observedBitrate: Double](avplayeritemaccesslogevent/observedbitrate.md)
  The empirical throughput, in bits per second, across all media downloaded.
- [var averageAudioBitrate: Double](avplayeritemaccesslogevent/averageaudiobitrate.md)
  The audio track’s average bit rate, in bits per second.
- [var averageVideoBitrate: Double](avplayeritemaccesslogevent/averagevideobitrate.md)
  The video track’s average bit rate, in bits per second.
- [var indicatedAverageBitrate: Double](avplayeritemaccesslogevent/indicatedaveragebitrate.md)
  The average throughput, in bits per second, required to play the stream, as advertised by the server.

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
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func accessLog() -> AVPlayerItemAccessLog?](avplayeritem/accesslog.md)
  Returns an object that represents a snapshot of the network access log.
- [class AVPlayerItemAccessLog](avplayeritemaccesslog.md)
  An object used to retrieve the access log associated with a player item.
- [func errorLog() -> AVPlayerItemErrorLog?](avplayeritem/errorlog.md)
  Returns an object that represents a snapshot of the error log.
- [class AVPlayerItemErrorLog](avplayeritemerrorlog.md)
  The error log associated with a player item.
- [class AVPlayerItemErrorLogEvent](avplayeritemerrorlogevent.md)
  A single item in a player item’s error log.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritemaccesslogevent)*