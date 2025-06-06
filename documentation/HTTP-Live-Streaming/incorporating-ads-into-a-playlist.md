# Incorporating Ads into a Playlist

**Framework**: HTTP Live Streaming

Add branding or ads to a playlist.

#### Overview

Often you want to deliver a series of movies with some sort of branding (advertisement) displayed in front of each one to let the user know that they originate from your site. One way to do this is to simply merge the ad with each movie. However, if you have hundreds of movies, you’ll have to redo a lot of encoding, and you’ll be duplicating the ad with each movie.

You could deliver the ad as a separate movie that plays first, and then play the intended movie. The problem with that approach, however, is that quality drops during the transition from the ad to the movie. For example, the ad starts playing with a low data rate to ensure that the client can read it, then gradually ramps up to provide the best possible playback experience. When the ad is finished playing, the movie starts at a low data rate (just as the ad did) and ramps up, resulting in a break in quality. Also, if you display the ad in the middle of the movie, you’ll get ongoing drops in quality.

The solution is to let the client know a change is coming, by using the `EXT-X-DISCONTINUITY` tag. This tag informs the client of a change that’s coming to the streaming media so the client can prepare for the change ahead of time.

##### Example

The following example shows a stream that uses the `EXT-X-DISCONTINUITY` tag to play movies that are preceded by an 18-second ad (segments `ad0.ts` and `ad1.ts`):

```swift
#EXTM3U
#EXT-X-TARGETDURATION:10
#EXT-X-VERSION:4
#EXT-X-MEDIA-SEQUENCE:0
#EXTINF:10.0,
ad0.ts
#EXTINF:8.0,
ad1.ts
#EXT-X-DISCONTINUITY
#EXTINF:10.0,
movieA.ts
#EXTINF:10.0,
movieB.ts
```

These are the tags used in the ads playlist example:

 Indicates that the playlist is an extended M3U file. This type of file is distinguished from a basic M3U file by changing the tag on the first line to EXTM3U. All HLS playlists must start with this tag.

 Specifies the maximum media-file duration.

 Indicates the compatibility version of the playlist file. The playlist media and its server must comply with all provisions of the most recent version of the IETF Internet-Draft of the HTTP Live Streaming specification that defines that protocol version.

 Indicates the sequence number of the first URL that appears in a playlist file. Each media file URL in a playlist has a unique integer sequence number. The sequence number of a URL is higher by 1 than the sequence number of the URL that preceded it. The media sequence numbers have no relation to the names of the files.

> ❗ **Important**: The `EXT-X-MEDIA-SEQUENCE` tag value must be incremented by 1 for every media URI that’s removed from the playlist file. Media URIs must be removed from the playlist file in the order that they appear in the playlist. The updated index file presents a moving window into a continuous stream. This type of session is suitable for continuous broadcasts.

The `EXT-X-MEDIA-SEQUENCE` tag value must be incremented by 1 for every media URI that’s removed from the playlist file. Media URIs must be removed from the playlist file in the order that they appear in the playlist. The updated index file presents a moving window into a continuous stream. This type of session is suitable for continuous broadcasts.

 Indicates an encoding discontinuity between the media file that follows it and the one that preceded it.

 Provides synchronization between different variant streams or different renditions of the same variant stream. You must use this tag for live events that have discontinuities.

 A record marker that describes the media file identified by the URL that follows it. Each media file URL must be preceded by an `EXTINF` tag. This tag contains a duration attribute that’s an integer or floating-point number in decimal positional notation that specifies the duration of the media segment in seconds. This value must be less than or equal to the target duration.

## See Also

- [Adding alternate media to a playlist](adding-alternate-media-to-a-playlist.md)
  Specify Rendition Playlists that can override the main presentation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/http-live-streaming/incorporating-ads-into-a-playlist)*