# observedBitrate

**Framework**: Media Player  
**Kind**: property  
**Role**: Instance Property

The empirical throughput across all media downloaded for the movie player, in bits per second.

**Availability**:
- iOS 3.2+ - Deprecated in 9.0
- iPadOS 3.2+ - Deprecated in 9.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Use AVPlayerViewController in AVKit

## Declaration

```swift
var observedBitrate: Double { get }
```

```objc
@property (nonatomic, readonly) double observedBitrate;
```

## See Also

### Movie access log event properties
- [var numberOfSegmentsDownloaded: Int](./numberofsegmentsdownloaded.md)
  A count of media segments downloaded from the web server to your app.
- [var playbackStartDate: Date!](./playbackstartdate.md)
  The timestamp for when playback began for the movie log access event.
- [var uri: String!](./uri.md)
  The URI of the playback item.
- [var serverAddress: String!](./serveraddress.md)
  The IPv4 or IPv6 address of the web server that was the source of the last delivered media segment.
- [var numberOfServerAddressChanges: Int](./numberofserveraddresschanges.md)
  A count of changes to the [`serverAddress`](./serveraddress.md) property over the last uninterrupted period of playback.
- [var playbackSessionID: String!](./playbacksessionid.md)
  A GUID that identifies the playback session to use in HTTP requests.
- [var playbackStartOffset: TimeInterval](./playbackstartoffset.md)
  An offset into the playlist where the last uninterrupted period of playback began, in seconds.
- [var segmentsDownloadedDuration: TimeInterval](./segmentsdownloadedduration.md)
  The accumulated duration of the media downloaded, in seconds.
- [var durationWatched: TimeInterval](./durationwatched.md)
  The accumulated duration of the media played, in seconds.
- [var numberOfStalls: Int](./numberofstalls.md)
  The total number of playback stalls encountered.
- [var numberOfBytesTransferred: Int64](./numberofbytestransferred.md)
  The accumulated number of bytes transferred.
- [var indicatedBitrate: Double](./indicatedbitrate.md)
  The throughput required to play the stream, as advertised by the web server, in bits per second.
- [var numberOfDroppedVideoFrames: Int](./numberofdroppedvideoframes.md)
  The total number of dropped video frames.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmovieaccesslogevent/observedbitrate)*