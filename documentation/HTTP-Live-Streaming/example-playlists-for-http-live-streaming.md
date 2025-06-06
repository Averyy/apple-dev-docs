# Example playlists for HTTP Live Streaming

**Framework**: HTTP Live Streaming

View and compare playlists for different HLS applications.

#### Overview

HTTP Live Streaming sends audio and video as a series of small files, typically of about 6 seconds duration, called . An index file, or playlist, provides an ordered list of the URLs of the media segment files. Index files for HTTP Live Streaming are saved as M3U8 playlists, an extension of the M3U format used for MP3 playlists. The URL of the index file is accessed by clients, which then request the indexed files in sequence.

You can use the Apple HTTP Live Streaming tools to generate playlists. These tools are frequently updated and you can get them from [`Downloads for Apple Developers`](https://developer.apple.comhttps://developer.apple.com/download/more/) if you’re a member of the Apple Developer Program. See [`Using Apple’s HTTP Live Streaming (HLS) Tools`](using-apple-s-http-live-streaming-hls-tools.md) for more information about the individual tools.

## Topics

### Basic playlists
- [Video on Demand playlist construction](video-on-demand-playlist-construction.md)
  Understand the basic composition for a Video on Demand playlist.
- [Live Playlist (sliding window) construction](live-playlist-sliding-window-construction.md)
  Understand the basic composition for a live session playlist.
- [Event playlist construction](event-playlist-construction.md)
  Learn about the basic composition of an event session playlist.
- [Creating a Multivariant Playlist](creating-a-multivariant-playlist.md)
  Offer multiple playlist files to provide different encodings of the same content.
### Modified playlists
- [Incorporating Ads into a Playlist](incorporating-ads-into-a-playlist.md)
  Add branding or ads to a playlist.
- [Adding alternate media to a playlist](adding-alternate-media-to-a-playlist.md)
  Specify Rendition Playlists that can override the main presentation.

## See Also

- [About the EXT-X-VERSION tag](about-the-ext-x-version-tag.md)
  Find the protocol version that corresponds with the HLS features your app supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/http-live-streaming/example-playlists-for-http-live-streaming)*