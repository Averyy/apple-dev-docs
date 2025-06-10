# Adding alternate media to a playlist

**Framework**: HTTP Live Streaming

Specify Rendition Playlists that can override the main presentation.

#### Overview

Adding alternate media to a Multivariant Playlist allows a provider to specify one of a set of variant playlists as an  of the main presentation. The client plays only the override media (audio or video), and suppresses any media of the same type from the main presentation, if present. This allows a presentation to offer multiple versions of the media without requiring the provider to store duplicate media, or requiring the client to download all variants when it only needs one. It also allows additional media to be offered subsequently without remastering the original content.

##### Add Alternate Media

Here’s an example of a Multivariant Playlist that provides additional audio renditions:

```swift
#EXTM3U
#EXT-X-MEDIA:TYPE=AUDIO,GROUP-ID="audio",LANGUAGE="eng",NAME="English",AUTOSELECT=YES,DEFAULT=YES,URI="eng/prog_index.m3u8"
#EXT-X-MEDIA:TYPE=AUDIO,GROUP-ID="audio",LANGUAGE="fre",NAME="Français",AUTOSELECT=YES,DEFAULT=NO,URI="fre/prog_index.m3u8"
#EXT-X-MEDIA:TYPE=AUDIO,GROUP-ID="audio",LANGUAGE="sp",NAME="Espanol",AUTOSELECT=YES,DEFAULT=NO,URI="sp/prog_index.m3u8"

#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=195023,CODECS="avc1.42e00a,mp4a.40.2",AUDIO="audio"
lo/prog_index.m3u8
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=591680,CODECS="avc1.42e01e,mp4a.40.2",AUDIO="audio"
hi/prog_index.m3u8
```

The tags used in this Multivariant Playlist example include:

The EXT-X-MEDIA tag has the following parameters:

When its URI attribute is omitted, the `EXT-X-MEDIA` tag can indicate that the media described is included in the URI of the `EXT-X-STREAM-INF` tag.

The `EXT-X-STREAM-INF` tag has the following parameters:

You can have multiple audio groups to allow changes in codes or bit rate. However, each audio group in a variant must have the same alternates in it. For example, you can’t have English in one audio group and leave it out of the other group. The following example defines two audio groups, one for low bit rates and one for high bit rates. Both audio groups define the same set of languages but are called based on the available bandwidth.

```swift
#EXTM3U
#EXT-X-MEDIA:TYPE=AUDIO,GROUP-ID="audio-lo",LANGUAGE="eng",NAME="English",AUTOSELECT=YES,DEFAULT=YES,URI="englo/prog_index.m3u8"
#EXT-X-MEDIA:TYPE=AUDIO,GROUP-ID="audio-lo",LANGUAGE="fre",NAME="Français",AUTOSELECT=YES,DEFAULT=NO,URI="frelo/prog_index.m3u8"
#EXT-X-MEDIA:TYPE=AUDIO,GROUP-ID="audio-lo",LANGUAGE="es",NAME="Espanol",AUTOSELECT=YES,DEFAULT=NO,URI="splo/prog_index.m3u8"

#EXT-X-MEDIA:TYPE=AUDIO,GROUP-ID="audio-hi",LANGUAGE="eng",NAME="English",AUTOSELECT=YES,DEFAULT=YES,URI="eng/prog_index.m3u8"
#EXT-X-MEDIA:TYPE=AUDIO,GROUP-ID="audio-hi",LANGUAGE="fre",NAME="Français",AUTOSELECT=YES,DEFAULT=NO,URI="fre/prog_index.m3u8"
#EXT-X-MEDIA:TYPE=AUDIO,GROUP-ID="audio-hi",LANGUAGE="es",NAME="Espanol",AUTOSELECT=YES,DEFAULT=NO,URI="sp/prog_index.m3u8"

#EXT-X-STREAM-INF:BANDWIDTH=195023,CODECS="mp4a.40.5",AUDIO="audio-lo"
lo/prog_index.m3u8
#EXT-X-STREAM-INF:BANDWIDTH=260000,CODECS="avc1.42e01e,mp4a.40.2",AUDIO="audio-lo"
hi/prog_index.m3u8
#EXT-X-STREAM-INF:BANDWIDTH=591680,CODECS="mp4a.40.2,avc1.64001e",AUDIO="audio-hi"
lo/prog_index.m3u8
#EXT-X-STREAM-INF:BANDWIDTH=650000,CODECS="avc1.42e01e,mp4a.40.2",AUDIO="audio-hi"
hi/prog_index.m3u8
```

##### Combine Groups and Single Options

You can have both a group and a single stream in a playlist. This is often done when you have multiple camera angles that all use the same audio. Create a group for the video streams and then declare the single audio stream. The following example shows a playlist with three camera angles and a single audio stream:

```swift
#EXTM3U
#EXT-X-MEDIA:TYPE=VIDEO,GROUP-ID="500kbs",NAME="Angle1",AUTOSELECT=YES,DEFAULT=YES
#EXT-X-MEDIA:TYPE=VIDEO,GROUP-ID="500kbs",NAME="Angle2",AUTOSELECT=YES,DEFAULT=NO,URI="Angle2/500kbs/prog_index.m3u8"
#EXT-X-MEDIA:TYPE=VIDEO,GROUP-ID="500kbs",NAME="Angle3",AUTOSELECT=YES,DEFAULT=NO,URI="Angle3/500kbs/prog_index.m3u8"

#EXT-X-MEDIA:TYPE=AUDIO,GROUP-ID="aac",LANGUAGE="en",NAME="English",AUTOSELECT=YES,DEFAULT=YES,URI="eng/prog_index.m3u8"
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=754857,CODECS="mp4a.40.2,avc1.4d401e",VIDEO="500kbs",AUDIO="aac"
Angle1/500kbs/prog_index.m3u8
```

To provide different streams for different bit rates, a different video group ID is needed for each bit rate.

```swift
#EXTM3U
#EXT-X-MEDIA:TYPE=VIDEO,GROUP-ID="200kbs",NAME="Angle1",AUTOSELECT=YES,DEFAULT=YES
#EXT-X-MEDIA:TYPE=VIDEO,GROUP-ID="200kbs",NAME="Angle2",AUTOSELECT=YES,DEFAULT=NO,URI="Angle2/200kbs/prog_index.m3u8"
#EXT-X-MEDIA:TYPE=VIDEO,GROUP-ID="200kbs",NAME="Angle3",AUTOSELECT=YES,DEFAULT=NO,URI="Angle3/200kbs/prog_index.m3u8"

#EXT-X-MEDIA:TYPE=VIDEO,GROUP-ID="500kbs",NAME="Angle1",AUTOSELECT=YES,DEFAULT=YES
#EXT-X-MEDIA:TYPE=VIDEO,GROUP-ID="500kbs",NAME="Angle2",AUTOSELECT=YES,DEFAULT=NO,URI="Angle2/500kbs/prog_index.m3u8"
#EXT-X-MEDIA:TYPE=VIDEO,GROUP-ID="500kbs",NAME="Angle3",AUTOSELECT=YES,DEFAULT=NO,URI="Angle3/500kbs/prog_index.m3u8"

#EXT-X-MEDIA:TYPE=AUDIO,GROUP-ID="aac",LANGUAGE="en",NAME="English",AUTOSELECT=YES,DEFAULT=YES,URI="eng/prog_index.m3u8"

#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=300000,CODECS="mp4a.40.2,avc1.4d401e",VIDEO="200kbs",AUDIO="aac"
Angle1/200kbs/prog_index.m3u

#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=754857,CODECS="mp4a.40.2,avc1.4d401e",VIDEO="500kbs",AUDIO="aac"
Angle1/500kbs/prog_index.m3u8

```

## See Also

- [Incorporating Ads into a Playlist](incorporating-ads-into-a-playlist.md)
  Add branding or ads to a playlist.


---

*[View on Apple Developer](https://developer.apple.com/documentation/http-live-streaming/adding-alternate-media-to-a-playlist)*