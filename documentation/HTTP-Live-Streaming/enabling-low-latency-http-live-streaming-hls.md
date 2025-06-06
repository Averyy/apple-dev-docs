# Enabling Low-Latency HTTP Live Streaming (HLS)

**Framework**: HTTP Live Streaming

Add Low-Latency HLS to your content streams to maintain scalability.

#### Overview

The HLS protocol delivers live and on-demand content streams to global-scale audiences. Historically, HLS has favored stream reliability over latency. Low-Latency HLS extends the protocol to enable low-latency video streaming while maintaining scalability. The new low-latency mode lowers video latencies over public networks into the range of standard television broadcasts.

Backend production tools and content delivery systems must implement new rules to enable low-latency stream playback. Low-Latency HLS offers new functionality in these areas:

- Generation of partial segments
- Playlist delta updates
- Blocking of playlist reload
- Using preload hints
- Rendition reports

The HLS specification defines low-latency extensions in [`HTTP Live Streaming 2nd Edition`](https://developer.apple.comhttps://datatracker.ietf.org/doc/html/draft-pantos-hls-rfc8216bis) revision 7 and later.

##### Generate Partial Media Segments

Low-Latency HLS provides a parallel channel for distributing media at the live edge of the Media Playlist, which divides the media into a larger number of smaller files, such as CMAF Chunks. These smaller files are called HLS Partial Segments. Because each Partial Segment has a short duration, it can be packaged, published, and added to the Media Playlist much earlier than its Parent Segment.

While regular Media Segments might be 6 seconds each, an example Partial Segment might be only 200 milliseconds. A first Partial Segment might publish only 200 milliseconds after the previous segment publishes, followed by 29 of its peers, followed at last by a regular-length, 6-second Media Segment containing the same media as the concatenation of its 30 Partial Segments. In order to reduce Playlist bloat, the server removes Partial Segments from the Media Playlist once they’re greater (older) than three target durations from the live edge.

You add Partial Segments to the Media Playlist using the new `EXT-X-PART` tag. You can place other Media Segment Tags (such as `EXT-X-DISCONTINUITY`) at Parent Segment boundaries.

A Partial Segment must be in one of the Supported Media Segment Formats described in section 3.1 of [`HTTP Live Streaming 2nd Edition`](https://developer.apple.comhttps://datatracker.ietf.org/doc/html/draft-pantos-hls-rfc8216bis).

##### Provide Playlist Delta Updates

Clients transfer playlists more frequently with Low-Latency HLS. They can request and servers can provide Playlist Delta Updates, which reduce this transfer cost. These updates replace a considerable portion of the Playlist that the client already has with the new `EXT-X-SKIP` tag.

##### Blocking Playlist Reloads

To support efficient client notification of new Media Segments and Partial Segments, Low-Latency HLS introduces the ability to block a Playlist reload request. When a client issues an HTTP GET to request a Media Playlist update, it can add special query parameters called Delivery Directives to specify that it wants the Playlist response to include a future segment. The server then holds onto the request (blocks) until a version of the Playlist that contains that segment is available. Blocking Playlist Reloads eliminates Playlist polling.

##### Provide Preload Hints and Blocking of Media Downloads

Eliminating unnecessary round trips is critical when delivering low-latency streams at global scale. Servers use a new tag, `EXT-X-PRELOAD-HINT`, to inform clients of upcoming Partial Segments and Media Initialization Sections. A client can issue a GET request for a hinted resource in advance; the server responds to the request as soon as the media becomes available.

##### Provide Rendition Reports

When playing at low latency, the client must be able to switch renditions with a minimum number of round trips in order to perform bit-rate adaptation. To support this, the server adds Rendition Reports on the other renditions in the Multivariant Playlist to each Media Playlist. The `EXT-X-RENDITION-REPORT` tag carries a Rendition Report and provides information, such as the last Media Sequence Number and Part currently in the Media Playlist of that rendition.

##### Add Low Latency Hls Delivery Directives

HLS now defines Delivery Directives, which are special query parameters that can be added to the URL of a GET request for a Playlist. These Delivery Directives include:

##### Utilize New Media Playlist Tags for Low Latency Hls

The following Playlist tags support Low-Latency HLS.

##### Comply with the Low Latency Server Configuration Profile

To support timely delivery of media, Low-Latency HLS requires certain transport features beyond what is necessary for regular HLS. These requirements are defined in the Low-Latency Server Configuration Profile. Because the Low-Latency HLS syntax is backward-compatible with existing HLS, clients fall back to regular-latency HLS playback if they discover that the server doesn’t support an aspect of the required configuration. [`HTTP Live Streaming 2nd Edition`](https://developer.apple.comhttps://datatracker.ietf.org/doc/html/draft-pantos-hls-rfc8216bis) defines the Low-Latency Server Configuration Profile in Appendix B.

##### Expect Delivery From Cdn Tune in

Players of Low-Latency HLS should expect delivery of low-latency streams through CDNs and other HTTP caches. To start playback at low latency, the client must first obtain a reasonably up-to-date version of the Media Playlist. Appendix C of [`HTTP Live Streaming 2nd Edition`](https://developer.apple.comhttps://datatracker.ietf.org/doc/html/draft-pantos-hls-rfc8216bis) describes an efficient approach for obtaining an up-to-date Media Playlist served through an HTTP cache.

##### Examine a Low Latency Hls Playlist

Here’s an example of a low-latency playlist. As mentioned above, the Low-Latency HLS syntax is backward-compatible, so we can use a version number of six. Clients that do not understand the Low-Latency tags will ignore them.

```swift
#EXTM3U
#// This Playlist is a response to:
#//     GET https://example.com/2M/waitForMSN.php?_HLS_msn=273&_HLS_part=2
#EXT-X-TARGETDURATION:4
#EXT-X-VERSION:6
#EXT-X-SERVER-CONTROL:CAN-BLOCK-RELOAD=YES,PART-HOLD-BACK=1.0,CAN-SKIP-UNTIL=24.0
#EXT-X-PART-INF:PART-TARGET=0.33334
#EXT-X-MEDIA-SEQUENCE:264
#EXT-X-PROGRAM-DATE-TIME:2019-02-14T02:13:28.106Z
#EXT-X-MAP:URI="init.mp4"
#EXTINF:4.00008,
fileSequence264.mp4
#EXTINF:4.00008,
fileSequence265.mp4
#EXTINF:4.00008,
fileSequence266.mp4
#EXTINF:4.00008,
fileSequence267.mp4
#EXTINF:4.00008,
fileSequence268.mp4
#EXTINF:4.00008,
fileSequence269.mp4
#EXTINF:4.00008,
fileSequence270.mp4
#EXT-X-PART:DURATION=0.33334,URI="filePart271.0.mp4"
#EXT-X-PART:DURATION=0.33334,URI="filePart271.1.mp4"
#EXT-X-PART:DURATION=0.33334,URI="filePart271.2.mp4"
#EXT-X-PART:DURATION=0.33334,URI="filePart271.3.mp4"
#EXT-X-PART:DURATION=0.33334,URI="filePart271.4.mp4",INDEPENDENT=YES
#EXT-X-PART:DURATION=0.33334,URI="filePart271.5.mp4"
#EXT-X-PART:DURATION=0.33334,URI="filePart271.6.mp4"
#EXT-X-PART:DURATION=0.33334,URI="filePart271.7.mp4"
#EXT-X-PART:DURATION=0.33334,URI="filePart271.8.mp4",INDEPENDENT=YES
#EXT-X-PART:DURATION=0.33334,URI="filePart271.9.mp4"
#EXT-X-PART:DURATION=0.33334,URI="filePart271.10.mp4"
#EXT-X-PART:DURATION=0.33334,URI="filePart271.11.mp4"
#EXTINF:4.00008,
fileSequence271.mp4
#EXT-X-PROGRAM-DATE-TIME:2019-02-14T02:14:00.106Z
#EXT-X-PART:DURATION=0.33334,URI="filePart272.a.mp4"
#EXT-X-PART:DURATION=0.33334,URI="filePart272.b.mp4"
#EXT-X-PART:DURATION=0.33334,URI="filePart272.c.mp4"
#EXT-X-PART:DURATION=0.33334,URI="filePart272.d.mp4"
#EXT-X-PART:DURATION=0.33334,URI="filePart272.e.mp4"
#EXT-X-PART:DURATION=0.33334,URI="filePart272.f.mp4",INDEPENDENT=YES
#EXT-X-PART:DURATION=0.33334,URI="filePart272.g.mp4"
#EXT-X-PART:DURATION=0.33334,URI="filePart272.h.mp4"
#EXT-X-PART:DURATION=0.33334,URI="filePart272.i.mp4"
#EXT-X-PART:DURATION=0.33334,URI="filePart272.j.mp4"
#EXT-X-PART:DURATION=0.33334,URI="filePart272.k.mp4"
#EXT-X-PART:DURATION=0.33334,URI="filePart272.l.mp4"
#EXTINF:4.00008,
fileSequence272.mp4
#EXT-X-PART:DURATION=0.33334,URI="filePart273.0.mp4",INDEPENDENT=YES
#EXT-X-PART:DURATION=0.33334,URI="filePart273.1.mp4"
#EXT-X-PART:DURATION=0.33334,URI="filePart273.2.mp4"
#EXT-X-PRELOAD-HINT:TYPE=PART,URI="filePart273.3.mp4"

#EXT-X-RENDITION-REPORT:URI="../1M/waitForMSN.php",LAST-MSN=273,LAST-PART=2
#EXT-X-RENDITION-REPORT:URI="../4M/waitForMSN.php",LAST-MSN=273,LAST-PART=1
```

##### Examine a Playlist Delta Update

Here’s an example of a playlist delta update. Note that use of tha EXT-X-SKIP tag requires a later version than the basic use of Low-Latency HLS above.

```swift
#EXTM3U
#// Following the example above, this Playlist is a response to:
#//     GET https://example.com/2M/waitForMSN.php?_HLS_msn=273&_HLS_part=3&_HLS_skip=YES
#EXT-X-TARGETDURATION:4
#EXT-X-VERSION:10
#EXT-X-SERVER-CONTROL:CAN-BLOCK-RELOAD=YES,PART-HOLD-BACK=1.0,CAN-SKIP-UNTIL=24.0
#EXT-X-PART-INF:PART-TARGET=0.33334
#EXT-X-MEDIA-SEQUENCE:264
#EXT-X-SKIP:SKIPPED-SEGMENTS=3
#EXTINF:4.00008,
fileSequence267.mp4
#EXTINF:4.00008,
fileSequence268.mp4
#EXTINF:4.00008,
fileSequence269.mp4
#EXTINF:4.00008,
fileSequence270.mp4
#EXT-X-PART:DURATION=0.33334,URI="filePart271.0.mp4"
#EXT-X-PART:DURATION=0.33334,URI="filePart271.1.mp4"
#EXT-X-PART:DURATION=0.33334,URI="filePart271.2.mp4"
#EXT-X-PART:DURATION=0.33334,URI="filePart271.3.mp4"
#EXT-X-PART:DURATION=0.33334,URI="filePart271.4.mp4",INDEPENDENT=YES
#EXT-X-PART:DURATION=0.33334,URI="filePart271.5.mp4"
#EXT-X-PART:DURATION=0.33334,URI="filePart271.6.mp4"
#EXT-X-PART:DURATION=0.33334,URI="filePart271.7.mp4"
#EXT-X-PART:DURATION=0.33334,URI="filePart271.8.mp4",INDEPENDENT=YES
#EXT-X-PART:DURATION=0.33334,URI="filePart271.9.mp4"
#EXT-X-PART:DURATION=0.33334,URI="filePart271.10.mp4"
#EXT-X-PART:DURATION=0.33334,URI="filePart271.11.mp4"
#EXTINF:4.00008,
fileSequence271.mp4
#EXT-X-PROGRAM-DATE-TIME:2019-02-14T02:14:00.106Z
#EXT-X-PART:DURATION=0.33334,URI="filePart272.a.mp4"
#EXT-X-PART:DURATION=0.33334,URI="filePart272.b.mp4"
#EXT-X-PART:DURATION=0.33334,URI="filePart272.c.mp4"
#EXT-X-PART:DURATION=0.33334,URI="filePart272.d.mp4"
#EXT-X-PART:DURATION=0.33334,URI="filePart272.e.mp4"
#EXT-X-PART:DURATION=0.33334,URI="filePart272.f.mp4",INDEPENDENT=YES
#EXT-X-PART:DURATION=0.33334,URI="filePart272.g.mp4"
#EXT-X-PART:DURATION=0.33334,URI="filePart272.h.mp4"
#EXT-X-PART:DURATION=0.33334,URI="filePart272.i.mp4"
#EXT-X-PART:DURATION=0.33334,URI="filePart272.j.mp4"
#EXT-X-PART:DURATION=0.33334,URI="filePart272.k.mp4"
#EXT-X-PART:DURATION=0.33334,URI="filePart272.l.mp4"
#EXTINF:4.00008,
fileSequence272.mp4
#EXT-X-PART:DURATION=0.33334,URI="filePart273.0.mp4",INDEPENDENT=YES
#EXT-X-PART:DURATION=0.33334,URI="filePart273.1.mp4"
#EXT-X-PART:DURATION=0.33334,URI="filePart273.2.mp4"
#EXT-X-PART:DURATION=0.33334,URI="filePart273.3.mp4"
#EXT-X-PRELOAD-HINT:TYPE=PART,URI="filePart273.4.mp4"

#EXT-X-RENDITION-REPORT:URI="../1M/waitForMSN.php",LAST-MSN=273,LAST-PART=3
#EXT-X-RENDITION-REPORT:URI="../4M/waitForMSN.php",LAST-MSN=273,LAST-PART=3
```

##### Examine Byterange Addressed Parts

Here’s an example of a byterange-addressed part. In a real playlist at least some of the EXT-X-PART tags would contain an INDEPENDENT attribute. Those have been removed to make the example clearer.

```swift
#// In these examples only the end of the Playlist is shown.

#// This is Playlist update 1
#EXTINF:4.08,
fs270.mp4
#EXT-X-PART:DURATION=1.02,URI="fs271.mp4",BYTERANGE="20000@0"
#EXT-X-PART:DURATION=1.02,URI="fs271.mp4",BYTERANGE="23000@20000"
#EXT-X-PART:DURATION=1.02,URI="fs271.mp4",BYTERANGE="18000@43000"
#EXT-X-PRELOAD-HINT:TYPE=PART,URI="fs271.mp4",BYTERANGE-START=61000

#// This is Playlist update 2
#EXTINF:4.08,
fs270.mp4
#EXT-X-PART:DURATION=1.02,URI="fs271.mp4",BYTERANGE="20000@0"
#EXT-X-PART:DURATION=1.02,URI="fs271.mp4",BYTERANGE="23000@20000"
#EXT-X-PART:DURATION=1.02,URI="fs271.mp4",BYTERANGE="18000@43000"
#EXT-X-PART:DURATION=1.02,URI="fs271.mp4",BYTERANGE="19000@61000"
#EXTINF:4.08,
fs271.mp4
#EXT-X-PRELOAD-HINT:TYPE=PART,URI="fs272.mp4",BYTERANGE-START=0

#// This is Playlist update 3
#EXTINF:4.08,
fs270.mp4
#EXT-X-PART:DURATION=1.02,URI="fs271.mp4",BYTERANGE="20000@0"
#EXT-X-PART:DURATION=1.02,URI="fs271.mp4",BYTERANGE="23000@20000"
#EXT-X-PART:DURATION=1.02,URI="fs271.mp4",BYTERANGE="18000@43000"
#EXT-X-PART:DURATION=1.02,URI="fs271.mp4",BYTERANGE="19000@61000"
#EXTINF:4.08,
fs271.mp4
#EXT-X-PART:DURATION=1.02,URI="fs272.mp4",BYTERANGE="21000@0"
#EXT-X-PRELOAD-HINT:TYPE=PART,URI="fs272.mp4",BYTERANGE-START=21000
```

##### Revision History

The following table describes the changes to the Protocol Extension for Low-Latency HLS.

| Date | Notes |
| --- | --- |
| 2024-05-21 | Added some clarifying text. |
| 2024-01-16 | Corrected errors in examples. |
| 2021-11-12 | Renamed “primary playlist” to “Multivariant Playlist.” |
| 2021-01-11 | Added missing double quotes around `BYTERANGE` parameters. |
| 2020-05-04 | Moved protocol rules to the HLS spec. This document is now a descriptive supplement. |
| 2020-02-05 | Added additional information related to preload hints and blocking of media downloads. |
| 2019-08-22 | Removed the `_HLS_report` parameter and made Rendition Reports mandatory. Clarified the `LAST-MSN` definition. |
| 2019-07-25 | Added the CDN Tune-in appendix. |
| 2019-07-10 | Updated MSN and part validation rules. Made server response recommended instead of mandatory. Added the requirement of the AGE header when using HTTP proxy caches. |
| 2019-06-03 | Added a new document describing Low-Latency HLS. |

## See Also

- [HTTP Live Streaming (HLS) authoring specification for Apple devices](hls-authoring-specification-for-apple-devices.md)
  Learn the requirements for live and on-demand audio and video content delivery using HLS.
- [Using content protection systems with HLS](using-content-protection-systems-with-hls.md)
  Adding encryption keys to media playlists
- [About the Common Media Application Format with HTTP Live Streaming (HLS)](about-the-common-media-application-format-with-http-live-streaming-hls.md)
  Learn the Common Media Application Format as it applies to HLS.
- [Links to additional specifications and videos](links-to-additional-specifications-and-videos.md)
  Review additional specifications and documents.
- [Videos about HLS](videos-about-hls.md)
  Review informational videos about HTTP Live Streaming.
- [Providing metadata for xHE-AAC video soundtracks](providing-metadata-for-xhe-aac-video-soundtracks.md)
  Ensure volume normalization by including metadata for loudness and dynamic range control.
- [Adjusting anchor loudness](adjusting-anchor-loudness.md)
  Adjust anchor loudness when measurements of speech-gated loudness for a full mix may be inaccurate, such as when speech activity is low.
- [Providing JavaScript Object Notation (JSON) chapters](providing-javascript-object-notation-json-chapters.md)
  Prepare JSON chapters for HTTP Live Streaming.


---

*[View on Apple Developer](https://developer.apple.com/documentation/http-live-streaming/enabling-low-latency-http-live-streaming-hls)*