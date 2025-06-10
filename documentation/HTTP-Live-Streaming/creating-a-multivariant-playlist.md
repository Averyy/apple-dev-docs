# Creating a Multivariant Playlist

**Framework**: HTTP Live Streaming

Offer multiple playlist files to provide different encodings of the same content.

#### Overview

The Multivariant Playlist describes all of the available variants for your content. Each variant is a version of the stream at a particular bit rate and is contained in a separate playlist. The client switches to the most appropriate variant based on the measured network bit rate. The client’s player is tuned to minimize stalling of playback, to give the user the best possible streaming experience.

![Flow diagram showing an index file splitting into multiple alternate files. Each alternate file creates the appropriate MP4 file.](https://docs-assets.developer.apple.com/published/67d4ae90b92b9dc32deb63ede697684d/creating-a-multivariant-playlist-1%402x.png)

A Multivariant Playlist isn’t re-read. Once the client has read the playlist, it assumes the set of variations isn’t changing. The stream ends as soon as the client sees the `EXT-X-ENDLIST` tag on one of the individual variant playlists.

##### Define Variants

The following example shows a Multivariant Playlist that defines five different variants.

```swift
#EXTM3U
#EXT-X-STREAM-INF:BANDWIDTH=150000,RESOLUTION=416x234,CODECS="avc1.42e00a,mp4a.40.2"
http://example.com/low/index.m3u8
#EXT-X-STREAM-INF:BANDWIDTH=240000,RESOLUTION=416x234,CODECS="avc1.42e00a,mp4a.40.2"
http://example.com/lo_mid/index.m3u8
#EXT-X-STREAM-INF:BANDWIDTH=440000,RESOLUTION=416x234,CODECS="avc1.42e00a,mp4a.40.2"
http://example.com/hi_mid/index.m3u8
#EXT-X-STREAM-INF:BANDWIDTH=640000,RESOLUTION=640x360,CODECS="avc1.42e00a,mp4a.40.2"
http://example.com/high/index.m3u8
#EXT-X-STREAM-INF:BANDWIDTH=64000,CODECS="mp4a.40.5"
http://example.com/audio/index.m3u8
```

The tags used in the playlist example are:

The `EXT-X-STREAM-INF` tag has the following parameters:

> **Note**: While the `CODECS` parameter is optional, every `EXT-X-STREAM-INF` tag should include the attribute. This attribute provides a complete list of codecs that are necessary to decode a particular stream. It allows the client to distinguish between variants that are audio only and those that have both audio and video. The client then makes use of this information to provide a better user experience when switching streams.

## See Also

- [Video on Demand playlist construction](video-on-demand-playlist-construction.md)
  Understand the basic composition for a Video on Demand playlist.
- [Live Playlist (sliding window) construction](live-playlist-sliding-window-construction.md)
  Understand the basic composition for a live session playlist.
- [Event playlist construction](event-playlist-construction.md)
  Learn about the basic composition of an event session playlist.


---

*[View on Apple Developer](https://developer.apple.com/documentation/http-live-streaming/creating-a-multivariant-playlist)*