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

- **`EXTM3U`**: Indicates that the playlist is an extended M3U file. This type of file is distinguished from a basic M3U file by changing the tag on the first line to `EXTM3U`. All HLS playlists must start with this tag.
- **`EXT-X-STREAM-INF`**: Indicates that the next URL in the playlist file identifies another playlist file.

The `EXT-X-STREAM-INF` tag has the following parameters:

- **`AVERAGE-BANDWIDTH`**: (Optional, but recommended) An integer that represents the average bit rate for the variant stream.
- **`BANDWIDTH`**: (Required) An integer that is the upper bound of the overall bit rate for each media file, in bits per second. The upper bound value is calculated to include any container overhead that appears or will appear in the playlist.
- **`FRAME-RATE`**: (Optional, but recommended) A floating-point value that describes the maximum frame rate in a variant stream.
- **`HDCP-LEVEL`**: (Optional) Indicates the type of encryption used. Valid values are `TYPE-0` and `NONE`. Use `TYPE-0` if the stream may not play unless the output is protected by HDCP.
- **`RESOLUTION`**: (Optional, but recommended) The optional display size, in pixels, at which to display the video in the playlist. This parameter should be included for any stream that includes video.
- **`VIDEO-RANGE`**: (Required depending on encoding) A string with valid values of `SDR` or `PQ`. If transfer characteristic codes 1, 16, or 18 aren’t specified, then this parameter must be omitted.
- **`CODECS`**: (Optional, but recommended) A quoted string containing a comma-separated list of formats, where each format specifies a media sample type that’s present in a media segment in the playlist file. Valid format identifiers are those in the ISO file format name space defined by RFC 6381.

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