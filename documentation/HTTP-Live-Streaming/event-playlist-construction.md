# Event playlist construction

**Framework**: HTTP Live Streaming

Learn about the basic composition of an event session playlist.

#### Overview

An event playlist is specified by the `EXT-X-PLAYLIST-TYPE` tag with a value of `EVENT`. It doesn’t initially have an `EXT-X-ENDLIST` tag, indicating that new media files will be added to the playlist as they become available.

##### Example

The following code shows an example of an event playlist as it appears at the beginning of a session:

```swift
#EXTM3U
#EXT-X-PLAYLIST-TYPE:EVENT
#EXT-X-TARGETDURATION:10
#EXT-X-VERSION:4
#EXT-X-MEDIA-SEQUENCE:0
#EXTINF:10.00,
fileSequence0.ts
#EXTINF:10.0,
fileSequence1.ts
#EXTINF:10.0,
fileSequence2.ts
#EXTINF:10.0,
fileSequence3.ts
#EXTINF:10.0,
fileSequence4.ts
```

These are the tags used in the event playlist example:

 Indicates that the playlist is an extended M3U file. This type of file is distinguished from a basic M3U file by changing the tag on the first line to `EXTM3U`. All HLS playlists must start with this tag.

 Provides mutability information that applies to the entire playlist file. This tag may contain a value of either `EVENT` or `VOD`. If the tag is present and has a value of `EVENT`, the server must not change or delete any part of the playlist file (although it may append lines to it). If the tag is present and has a value of `VOD`, the playlist file must not change.

 Specifies the maximum media-file duration.

 Indicates the compatibility version of the playlist file. The playlist media and its server must comply with all provisions of the most recent version of the IETF Internet-Draft of the HTTP Live Streaming specification that defines that protocol version.

 Indicates the sequence number of the first URL that appears in a playlist file. Each media file URL in a playlist has a unique integer sequence number. The sequence number of a URL is higher by 1 than the sequence number of the URL that preceded it. The media sequence numbers have no relation to the names of the files.

 A record marker that describes the media file identified by the URL that follows it. Each media file URL must be preceded by an EXTINF tag. This tag contains a duration attribute that’s an integer or floating-point number in decimal positional notation that specifies the duration of the media segment in seconds. This value must be less than or equal to the target duration.

> ❗ **Important**: Always use floating-point `EXTINF` durations (supported in protocol version 3). This allows the client to minimize round-off errors when seeking within the stream.

Always use floating-point `EXTINF` durations (supported in protocol version 3). This allows the client to minimize round-off errors when seeking within the stream.

You can’t remove anything from the playlist when using the `EVENT` tag; you may only append new segments to the end of the file. New segments are added to the end of the file until the event has concluded, at which time the `EXT-X-ENDLIST` tag is appended. The following example shows the same playlist after it’s been updated with new media URIs and the event has ended:

```swift
#EXTM3U
#EXT-X-PLAYLIST-TYPE:EVENT
#EXT-X-TARGETDURATION:10
#EXT-X-VERSION:4
#EXT-X-MEDIA-SEQUENCE:0
#EXTINF:10.0,
fileSequence0.ts
#EXTINF:10.0,
fileSequence1.ts
#EXTINF:10.0,
fileSequence2.ts
#EXTINF:10.0,
fileSequence3.ts
#EXTINF:10.0,
fileSequence4.ts

// List of files between 4 and 120 go here.

#EXTINF:10.0,
fileSequence120.ts
#EXTINF:10.0,
fileSequence121.ts
#EXT-X-ENDLIST
```

Event playlists are typically used when you want to allow the user to seek to any point in the event, such as for a concert or sports event.

## See Also

- [Video on Demand playlist construction](video-on-demand-playlist-construction.md)
  Understand the basic composition for a Video on Demand playlist.
- [Live Playlist (sliding window) construction](live-playlist-sliding-window-construction.md)
  Understand the basic composition for a live session playlist.
- [Creating a Multivariant Playlist](creating-a-multivariant-playlist.md)
  Offer multiple playlist files to provide different encodings of the same content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/http-live-streaming/event-playlist-construction)*