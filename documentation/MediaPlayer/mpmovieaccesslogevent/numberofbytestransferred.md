# numberOfBytesTransferred

**Framework**: Media Player  
**Kind**: property

The accumulated number of bytes transferred.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+

## Declaration

```swift
var numberOfBytesTransferred: Int64 { get }
```

#### Discussion

If the number of bytes transferred is unknown, this property’s value is negative.

## See Also

- [var numberOfSegmentsDownloaded: Int](mpmovieaccesslogevent/numberofsegmentsdownloaded.md)
  A count of media segments downloaded from the web server to your app.
- [var playbackStartDate: Date!](mpmovieaccesslogevent/playbackstartdate.md)
  The timestamp for when playback began for the movie log access event.
- [var uri: String!](mpmovieaccesslogevent/uri.md)
  The URI of the playback item.
- [var serverAddress: String!](mpmovieaccesslogevent/serveraddress.md)
  The IPv4 or IPv6 address of the web server that was the source of the last delivered media segment.
- [var numberOfServerAddressChanges: Int](mpmovieaccesslogevent/numberofserveraddresschanges.md)
  A count of changes to the [`serverAddress`](mpmovieaccesslogevent/serveraddress.md) property over the last uninterrupted period of playback.
- [var playbackSessionID: String!](mpmovieaccesslogevent/playbacksessionid.md)
  A GUID that identifies the playback session to use in HTTP requests.
- [var playbackStartOffset: TimeInterval](mpmovieaccesslogevent/playbackstartoffset.md)
  An offset into the playlist where the last uninterrupted period of playback began, in seconds.
- [var segmentsDownloadedDuration: TimeInterval](mpmovieaccesslogevent/segmentsdownloadedduration.md)
  The accumulated duration of the media downloaded, in seconds.
- [var durationWatched: TimeInterval](mpmovieaccesslogevent/durationwatched.md)
  The accumulated duration of the media played, in seconds.
- [var numberOfStalls: Int](mpmovieaccesslogevent/numberofstalls.md)
  The total number of playback stalls encountered.
- [var observedBitrate: Double](mpmovieaccesslogevent/observedbitrate.md)
  The empirical throughput across all media downloaded for the movie player, in bits per second.
- [var indicatedBitrate: Double](mpmovieaccesslogevent/indicatedbitrate.md)
  The throughput required to play the stream, as advertised by the web server, in bits per second.
- [var numberOfDroppedVideoFrames: Int](mpmovieaccesslogevent/numberofdroppedvideoframes.md)
  The total number of dropped video frames.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmovieaccesslogevent/numberofbytestransferred)*