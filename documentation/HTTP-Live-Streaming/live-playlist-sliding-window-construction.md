# Live Playlist (sliding window) construction

**Framework**: HTTP Live Streaming

Understand the basic composition for a live session playlist.

#### Overview

In live sessions, the index file is updated by removing media URIs from the file as new media files are created and made available. The `EXT-X-ENDLIST` tag isn’t present in the live playlist, indicating that new media files will be added to the index file as they become available.

##### Example

This code is an example of a Live Playlist as it appears at the beginning of a session:

```swift
#EXTM3U
#EXT-X-TARGETDURATION:10
#EXT-X-VERSION:4
#EXT-X-MEDIA-SEQUENCE:1
#EXTINF:10.0,
fileSequence1.ts
#EXTINF:10.0,
fileSequence2.ts
#EXTINF:10.0,
fileSequence3.ts
#EXTINF:10.0,
fileSequence4.ts
#EXTINF:10.0,
fileSequence5.ts
```

These are the tags used in the live playlist example:

 Indicates that the playlist is an extended M3U file. This type of file is distinguished from a basic M3U file by changing the tag on the first line to `EXTM3U`. All HLS playlists must start with this tag.

 Specifies the maximum media-file duration.

 Indicates the compatibility version of the playlist file. The playlist media and its server must comply with all provisions of the most recent version of the IETF Internet-Draft of the HTTP Live Streaming specification that defines that protocol version.

 Indicates the sequence number of the first URL that appears in a playlist file. Each media file URL in a playlist has a unique integer sequence number. The sequence number of a URL is higher by 1 than the sequence number of the URL that preceded it. The media sequence numbers have no relation to the names of the files.

> ❗ **Important**: The `EXT-X-MEDIA-SEQUENCE` tag value must be incremented by 1 for every media URI that’s removed from the playlist file. Media URIs must be removed from the playlist file in the order that they appear in the playlist. The updated index file presents a moving window into a continuous stream. This type of session is suitable for continuous broadcasts.

The `EXT-X-MEDIA-SEQUENCE` tag value must be incremented by 1 for every media URI that’s removed from the playlist file. Media URIs must be removed from the playlist file in the order that they appear in the playlist. The updated index file presents a moving window into a continuous stream. This type of session is suitable for continuous broadcasts.

 A record marker that describes the media file identified by the URL that follows it. Each media file URL must be preceded by an `EXTINF` tag. This tag contains a duration attribute that’s an integer or floating-point number in decimal positional notation that specifies the duration of the media segment in seconds. This value must be less than or equal to the target duration.

> ❗ **Important**: Always use floating-point `EXTINF` durations (supported in protocol version 3). This allows the client to minimize round-off errors when seeking within the stream.

Always use floating-point `EXTINF` durations (supported in protocol version 3). This allows the client to minimize round-off errors when seeking within the stream.

The following example shows the same playlist after it’s been updated with new media URIs:

```swift
#EXTM3U
#EXT-X-TARGETDURATION:10
#EXT-X-VERSION:4
#EXT-X-MEDIA-SEQUENCE:2
#EXTINF:10.0,
fileSequence2.ts
#EXTINF:10.0,
fileSequence3.ts
#EXTINF:10.00,
fileSequence4.ts
#EXTINF:10.00,
fileSequence5.ts
#EXTINF:10.0,
fileSequence6.ts
```

The playlist continues to be updated as new media URIs are added:

```swift
#EXTM3U
#EXT-X-TARGETDURATION:10
#EXT-X-VERSION:4
#EXT-X-MEDIA-SEQUENCE:4
#EXTINF:10.00,
fileSequence4.ts
#EXTINF:10.00,
fileSequence5.ts
#EXTINF:10.0,
fileSequence6.ts,
#EXTINF:10.0,
fileSequence7.ts,
#EXTINF:10.0,
fileSequence8.ts,
#EXTINF:10.0,
fileSequence9.ts
```

## See Also

- [Video on Demand playlist construction](video-on-demand-playlist-construction.md)
  Understand the basic composition for a Video on Demand playlist.
- [Event playlist construction](event-playlist-construction.md)
  Learn about the basic composition of an event session playlist.
- [Creating a Multivariant Playlist](creating-a-multivariant-playlist.md)
  Offer multiple playlist files to provide different encodings of the same content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/http-live-streaming/live-playlist-sliding-window-construction)*