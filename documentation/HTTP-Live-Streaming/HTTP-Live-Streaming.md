# HTTP Live Streaming

**Framework**: HTTP Live Streaming

Send audio and video to iOS, tvOS, and macOS devices.

#### Overview

HTTP Live Streaming (HLS) sends audio and video over HTTP from an ordinary web server for playback on iOS-based devices—including iPhone, iPad, iPod touch, and Apple TV—and on desktop computers (macOS). Using the same protocol that powers the web, HLS deploys content using ordinary web servers and content delivery networks. HLS is designed for reliability and dynamically adapts to network conditions by optimizing playback for the available speed of wired and wireless connections.

HLS supports the following:

- Live broadcasts and prerecorded content (video on demand, or VOD)
- Multiple alternate streams at different bit rates
- Intelligent switching of streams in response to network bandwidth changes
- Media encryption and user authentication

##### Encode and Deliver Streaming Media

The following figure shows the three components of an HTTP Live Stream: the server component, the distribution component, and the client software.

![Flow diagram showing the four parts of an HTTP Live Stream. The media recording is sent to a server, distributed over the web, and sent to the client app.](https://docs-assets.developer.apple.com/published/80fd0d84ea04e487087af24c24190c5d/http-live-streaming-1%402x.png)

In a typical configuration, a hardware encoder takes audio-video input, encodes it as HEVC video and AC-3 audio, and outputs a fragmented MPEG-4 file or an MPEG-2 transport stream. A software stream segmenter then breaks the stream into a series of short media files, which are placed on a web server. The segmenter also creates and maintains an index file containing a list of the media files. The URL of the index file is published on the web server. Client software reads the index, then requests the listed media files in order and displays them without any pauses or gaps between segments.

##### Prepare Media with the Server Component

The server component is responsible for taking input streams of media and encoding them digitally. It encapsulates them in a format suitable for delivery and prepares the encapsulated media for distribution.

For live events, the server requires a media encoder, which can be off-the-shelf hardware, and a way to break the encoded media into segments and save them as files, which can either be software such as the media stream segmenter provided by Apple or part of an integrated third-party solution.

##### Deliver Files with the Distribution Component

The distribution system is a web server or a web-caching system that delivers the media files and index files to the client over HTTP. No custom server modules are required to deliver the content, and typically very little configuration is needed on the web server. To actually deploy HTTP Live Streaming, you need to create either an HTML page for browsers or a client app to act as a receiver. You also need the use of a web server and a way to encode live streams as fragmented MPEG-4 media files containing HEVC or H.264 video, and AAC or AC-3 audio.

##### Access Media Through Client Software

Client software is responsible for determining the appropriate media to request, downloading those resources, and then reassembling them so that the media can be presented to the user in a continuous stream. For the rules governing the interaction between an HLS player and its server, see [`HTTP Live Streaming 2nd Edition`](https://developer.apple.comhttps://datatracker.ietf.org/doc/html/draft-pantos-hls-rfc8216bis).

Apple provides several frameworks that support HTTP Live Streaming, including [`AVKit`](https://developer.apple.com/documentation/AVKit), [`AVFoundation`](https://developer.apple.com/documentation/AVFoundation), and [`WebKit`](https://developer.apple.com/documentation/WebKit). Support has been available since iOS 3.0 and Safari 4.0, so there’s no need to develop your own client software.

However, if you do develop your own client software, begin by fetching the index file using a URL that identifies the stream. The index file, in turn, specifies the location of the available media files, decryption keys, and any alternate streams available. For the selected stream, download each available media file in sequence. Each file contains a consecutive segment of the stream. Once it has a sufficient amount of data downloaded, present the reassembled stream to the user.

> ❗ **Important**: Your client is responsible for fetching any decryption keys, authenticating or presenting a user interface to allow authentication, and decrypting media files as needed.

Continue this process until your client encounters the `EXT-X-ENDLIST` tag in the index file. If no `EXT-X-ENDLIST` tag is present, the index file is part of an ongoing broadcast. During ongoing broadcasts, load a new version of the index file periodically. Look for new media files and encryption keys in the updated index and add these URLs to the playback queue.

## Topics

### Essentials
- [Deploying a Basic HTTP Live Streaming (HLS) Stream](deploying-a-basic-http-live-streaming-hls-stream.md)
  Create a basic webpage to deliver HLS.
- [Preparing Audio for HTTP Live Streaming](preparing-audio-for-http-live-streaming.md)
  Encode your media properly to ensure synchronized audio and video playback.
### Stream creation
- [Example playlists for HTTP Live Streaming](example-playlists-for-http-live-streaming.md)
  View and compare playlists for different HLS applications.
- [About the EXT-X-VERSION tag](about-the-ext-x-version-tag.md)
  Find the protocol version that corresponds with the HLS features your app supports.
### Tool usage and validation
- [Using Apple’s HTTP Live Streaming (HLS) Tools](using-apple-s-http-live-streaming-hls-tools.md)
  Segment your video stream and create media playlists for successful transmission with Apple’s provided tools.
### Specifications and other documents
- [HTTP Live Streaming (HLS) authoring specification for Apple devices](hls-authoring-specification-for-apple-devices.md)
  Learn the requirements for live and on-demand audio and video content delivery using HLS.
- [Using content protection systems with HLS](using-content-protection-systems-with-hls.md)
  Adding encryption keys to media playlists
- [About the Common Media Application Format with HTTP Live Streaming (HLS)](about-the-common-media-application-format-with-http-live-streaming-hls.md)
  Learn the Common Media Application Format as it applies to HLS.
- [Enabling Low-Latency HTTP Live Streaming (HLS)](enabling-low-latency-http-live-streaming-hls.md)
  Add Low-Latency HLS to your content streams to maintain scalability.
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

*[View on Apple Developer](https://developer.apple.com/documentation/HTTP-Live-Streaming)*