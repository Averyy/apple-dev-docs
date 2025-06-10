# About the Common Media Application Format with HTTP Live Streaming (HLS)

**Framework**: HTTP Live Streaming

Learn the Common Media Application Format as it applies to HLS.

#### Overview

The Common Media Application Format (CMAF) for segmented media is an extensible standard for the encoding and packaging of segmented media objects for delivery and decoding on end user devices in adaptive multimedia presentations. Delivery and presentation are abstracted by a hypothetical application model that allows a wide range of implementations including HLS and MPEG’s Dynamic Adaptive Streaming over HTTP (MPEG DASH). The CMAF specification defines several logical media objects:

 Tracks contain encoded media samples, including audio, video, and subtitles. Media samples are stored in a CMAF specified container derived from the ISO Base Media File Format. Media samples may optionally be protected by MPEG Common Encryption. Tracks are made up of a CMAF Header and one or more CMAF Fragments.

 Switching sets contain alternative tracks that can be switched and spliced at CMAF Fragment boundaries to adaptively stream the same content at different bit rates and resolutions.

 Two or more CMAF Switching Sets encoded from the same source with alternative encodings, for example, different codecs, and time aligned to each other.

 A group of switching sets of the same media type that may include alternative content (for example, different languages or camera angles) or alternative encodings (for example, different codecs).

 One or more presentation time synchronized selection sets.

> **Note**: A presentation is the first point where different media types can be combined.

The CMAF Hypothetical Reference Model defines how tracks can be delivered, combined, and synchronized in CMAF Presentations, but the model allows the use of any compatible implementation. It’s possible to create HLS Playlists and a DASH Media Presentation Description that share the same resources, CMAF Addressable Objects, thereby allowing efficient caching even when delivering to multiple platforms. CMAF Addressable Media objects consist of:

 Headers contain information that includes information for initializing a track.

 A sequence of one or more consecutive fragments from the same track.

 A chunk contains a sequential subset of samples from a fragment.

 A complete track in one ISO_BMFF file.

![Flow diagram showing the relationship between specified CMAF objects and non-specified CMAF objects. Manifests have resources that point to addressable CMAF media objects.](https://docs-assets.developer.apple.com/published/c16d062ae472249b042d2ae0e6a6a93e/about-the-common-media-application-format-with-http-live-streaming-hls-1%402x.png)

##### Support for Cmaf

Apple’s HLS specification is a published RFC, [`RFC 8216`](https://developer.apple.comhttps://www.rfc-editor.org/info/rfc8216). However, HLS continues to evolve, so there’s an updated draft specification — [`draft-pantos-hls-rfc8216bis`](https://developer.apple.comhttps://tools.ietf.org/html/draft-pantos-hls-rfc8216bis).

The HLS specification defined support for fragmented MPEG-4 Segments (ISO_BMFF) in September 2016. Clients based on earlier revisions will likely not be able to handle CMAF content. Apple hardware running iOS 10.0, macOS 10.12, and tvOS 10.0 or later OS versions should support CMAF content.

> **Note**: HLS was originally specified in [`draft-pantos-http-live-streaming`](https://developer.apple.comhttps://tools.ietf.org/html/draft-pantos-http-live-streaming). That document was superseded by RFC 8216.

##### Manifests Resources and Cmaf Presentations

In HLS, the role of the Manifest is divided between the HLS Multivariant Playlist and the Media Playlists it references. They describe a single CMAF Presentation or a sequence of CMAF Presentations.

In an HLS Multivariant Playlist, `EXT-X-STREAM-INF` tags define different tiers of the presentation. Tiers are distinguished by bit rate, required codecs, resolution, and other attributes. Each tier specifies an HLS Media Playlist. Each tier may also indicate additional HLS Renditions, which are Media Playlists described in `EXT-X-MEDIA` tags that are available for selection while playing that tier. For example, an audio Rendition can be used to supply audio if the tier’s Media Playlist only contains video; a group of audio Renditions can be used to offer a selection of different language tracks.

Because CMAF Segments can’t, in general, contain multiple media types, `EXT-X-MEDIA` tags need to be used to associate audio and subtitle Playlists with video, which is usually in the `EXT-X-STREAM-INF` tag’s Media Playlist. The same Rendition can be used by several `EXT-X-STREAM-INF` tags; for instance, multiple video tiers can specify the same audio Rendition. Alternately, higher bit rate video tiers can specify separate, higher bit rate audio Renditions so that audio quality scales with video quality.

##### Cmaf Tracks Segments Headers and Fragments

There should be one HLS Media Playlist per CMAF Track. In HLS Media Playlists, CMAF Segments are used as HLS Segments. There has to be an `EXT-X-MAP` tag applied to each HLS Segment; the tag points to a CMAF Header that’s appropriate for all CMAF Fragments inside the HLS Segment. Since all CMAF Fragments are independently decodable, their HLS Playlists should contain an `EXT-X-INDEPENDENT-SEGMENTS` tag. When the media is encrypted, EXT-X-SESSION-KEY tags should be included in the Multivariant Playlist to enable prefetching of keys.

The `EXT-X-BYTERANGE` tag can be used to indicate that an HLS Segment is a byte range inside a larger resource.

Media Segments inside `EXT-X-I-FRAMES-ONLY` Playlists start on a CMAF Fragment boundary.

The` EXT-X-DISCONTINUITY` tag can be used to concatenate multiple CMAF Tracks of the same media type in a Media Playlist. Each discontinuity demarcates a boundary between successive CMAF Presentations. A discontinuity allows the resetting of presentation timestamps and other characteristics. Many changes can require a discontinuity, for example, switching from Sample Encryption to unencrypted. A new `EXT-X-MAP` tag is usually required after a discontinuity. For further information, see the [`draft-pantos-hls-rfc8216bis`](https://developer.apple.comhttps://tools.ietf.org/html/draft-pantos-hls-rfc8216bis).

> **Note**: For fragmented MPEG-4 Segments, an `EXT-X-KEY` tag with a `METHOD=SAMPLE-AES` attribute indicates that the Segment is encrypted using the `‘cbcs’` scheme  in ISO/IEC 23001-7.

HLS supports all CMAF subtitle and caption formats, except for IMSC1 Image Tracks.

You can include one or more Event Message boxes (`‘emsg’`) in each segment. You must use version 1 of the Event Message box standard found in ISO-23009-1. The following values define the semantics:

##### Cmaf Switching Sets

Each Track in a video CMAF Switching Set should appear in the Multivariant Playlist as a Media Playlist URI prefixed by an `EXT-X-STREAM-INF` tag describing it. The `EXT-X-STREAM-INF` tag should also specify any other renditions, such as audio that are intended to play with the video by indicating an appropriate `EXT-X-MEDIA GROUP-ID`.

Each Track in an audio CMAF Switching Set should be represented in the Multivariant Playlist by an `EXT-X-MEDIA` tag. The URI attribute of the `EXT-X-MEDIA` tag should be a URI to that Track’s Media Playlist. It has to have a `GROUP-ID` attribute that allows it to be associated with one or more `EXT-X-STREAM-INF` tags, which specify video tiers.

##### Cmaf Selection Sets

In HLS, when multiple codecs are offered, `EXT-X-STREAM-INF` tags in the Multivariant Playlist are typically arranged in sets of parallel tiers, for example, `low-bitrate-codec-A`,` high-bitrate-codec-A`, `low-bitrate-codec-B`, `high-bitrate-codec-B`.

CMAF Selection Sets generally offer either alternate encodings of the same source content (for example, encoded with different codecs) or homogenous encodings of different versions of the source content (for example, different audio language tracks).

For Selection Sets offering codec variants, each Switching Set in the Selection Set should appear as a set of `EXT-X-STREAM-INF` tags, for video, or a set of `EXT-X-MEDIA` tags, for other media types. See [`CMAF Switching Sets`](about-the-common-media-application-format-with-http-live-streaming-hls#CMAF-Switching-Sets.md).

For Selection Sets offering source variants, each Track of a member Switching Set should appear as an `EXT-X-MEDIA` tag. Tracks encoded with the same settings should get the same `EXT-X-MEDIA GROUP-ID`. For example, a Selection Set containing French and English Switching Sets, with just one Track in each Switching Set, should appear as two `EXT-X-MEDIA` tags with the same `GROUP-ID`. For more `EXT_X_MEDIA` tag rules, see [`RFC 8216`](https://developer.apple.comhttps://www.rfc-editor.org/info/rfc8216) and [`draft-pantos-hls-rfc8216bis`](https://developer.apple.comhttps://tools.ietf.org/html/draft-pantos-hls-rfc8216bis).

##### Cmaf Presentation Profiles

The CMAF specification defines three presentation profiles: unencrypted, encrypted with `‘cbcs’`, and encrypted with `‘cenc’`. HLS supports unencrypted and encrypted with `‘cbcs’`.

##### Hls Example

In this example, there’s a video CMAF Track containing 29.97 fps video in 60-frame GOPs, each 2.002 seconds long. Each GOP forms a CMAF Fragment. The CMAF Fragments, V1, V2, V3, V4, and V5, total 10.010 seconds of video. Their CMAF Header is `VH`.

Accompanying the video is an English audio CMAF Track consisting of an English CMAF Header, `EH`, and five audio CMAF Fragments: E1, E2, E3, E4, and E5, encoded at a sample rate of 44.1 Khz. Each CMAF Segment is 86 AAC frames, with a duration of 1.997 seconds each, except for E5, which has 87 frames, for a total of 10.008 seconds of audio. There are also five French audio CMAF Fragments — F1, F2, F3, F4, and F5 — and a French CMAF Header, `FH`.

The CMAF Fragments have been packaged into three CMAF Segments per track for delivery and those CMAF Resources identified as HLS segments: `V1andV`2, `V3andV4`, and `V5`; `E1andE2`, `E3andE4`, and `E5`; and so on.

In addition, there’s a high quality video Track containing CMAF Fragments: `VHQ1`, `VHQ2`, `VHQ3`, `VHQ4`, and `VHQ5`, with Header `VHQH`, packaged and identified similarly.

The two video Tracks, V and VHQ, are CMAF Switching Sets. Each audio Track can also be considered a Switching Set, with only one member. Together, both audio Switching Sets form a CMAF Selection Set.

The HLS Media Playlist for the regular video Track `video.m3u8` would be as follows.

```swift
#EXTM3U
#EXT-X-TARGETDURATION:4
#EXT-X-VERSION:6
#EXT-X-PLAYLIST-TYPE:VOD
#EXT-X-MAP:URI="VH"
#EXTINF:4.004,
V1andV2
#EXTINF:4.004,
V3andV4
#EXTINF:2.002,
V5
#EXT-X-ENDLIST
```

The Media Playlist for the high quality video Track `video-hq.m3u8` would be similar.

The Media Playlist for the English audio Track `english.m3u8` would be as follows.

```swift
#EXTM3U
#EXT-X-TARGETDURATION:4
#EXT-X-VERSION:6
#EXT-X-PLAYLIST-TYPE:VOD
#EXT-X-MAP:URI="EH"
#EXTINF:3.9938,
E1andE2
#EXTINF:3.9938,
E3andE4
#EXTINF:2.0201,
E5
#EXT-X-ENDLIST
```

The Media Playlist the French audio Track `french.m3u8` would be similar.

The HLS Multivariant Playlist might look like the following example.

```swift
#EXTM3U
#EXT-X-VERSION:6
#EXT-X-INDEPENDENT-SEGMENTS

#EXT-X-MEDIA:NAME="English",TYPE=AUDIO,GROUP-ID="audio-stereo-64",LANGUAGE="en",DEFAULT=YES,AUTOSELECT=YES,URI="english.m3u8"
#EXT-X-MEDIA:NAME="Français",TYPE=AUDIO,GROUP-ID="audio-stereo-64",LANGUAGE="fr",DEFAULT=NO,AUTOSELECT=YES,URI="french.m3u8"

#EXT-X-STREAM-INF:BANDWIDTH=1123000,CODECS="avc1.64001f,mp4a.40.2",AUDIO="audio-stereo-64",RESOLUTION=620x334
video.m3u8

#EXT-X-STREAM-INF:BANDWIDTH=8123000,CODECS="avc1.640028,mp4a.40.2",AUDIO="audio-stereo-64",RESOLUTION=1916x1032
video-hq.m3u8
```

We could also supply HEVC versions of `video.m3u8` and `video-hq.m3u8`, and perhaps give the high-bandwidth tier better-quality audio. Then the Multivariant Playlist might look like the following example.

```swift
#EXTM3U
#EXT-X-VERSION:6
#EXT-X-INDEPENDENT-SEGMENTS

#EXT-X-MEDIA:NAME="English",TYPE=AUDIO,GROUP-ID="audio-stereo-64",LANGUAGE="en",DEFAULT=YES,AUTOSELECT=YES,URI="english.m3u8"
#EXT-X-MEDIA:NAME="Français",TYPE=AUDIO,GROUP-ID="audio-stereo-64",LANGUAGE="fr",DEFAULT=NO,AUTOSELECT=YES,URI="french.m3u8"

#EXT-X-MEDIA:NAME="English",TYPE=AUDIO,GROUP-ID="audio-stereo-128",LANGUAGE="en",DEFAULT=YES,AUTOSELECT=YES,URI="english-hi.m3u8"
#EXT-X-MEDIA:NAME="Français",TYPE=AUDIO,GROUP-ID="audio-stereo-128",LANGUAGE="fr",DEFAULT=NO,AUTOSELECT=YES,URI="french-hi.m3u8"

#EXT-X-STREAM-INF:BANDWIDTH=1123000,CODECS="avc1.64001f,mp4a.40.2",AUDIO="audio-stereo-64",RESOLUTION=620x334
video.m3u8

#EXT-X-STREAM-INF:BANDWIDTH=8187000,CODECS="avc1.640028,mp4a.40.2",AUDIO="audio-stereo-128",RESOLUTION=1916x1032
video-hq.m3u8

#EXT-X-STREAM-INF:BANDWIDTH=623000, CODECS="hvc1.1.6.L120.B0,mp4a.40.2",AUDIO="audio-stereo-64",RESOLUTION=620x334
hevc-video.m3u8

#EXT-X-STREAM-INF:BANDWIDTH=4187000, CODECS="hvc1.1.6.L120.B0,mp4a.40.2",AUDIO="audio-stereo-128",RESOLUTION=1916x1032
hevc-video-hq.m3u8
```

This example illustrates how CMAF Selection Sets can appear as separate Renditions, `english.m3u8` and `french.m3u8`, or as separate sets of tiers distinguished by different required codecs: `{video.m3u8, video-hq.m3u8}` is the AVC Switching Set; `{hevc-video.m3u8, hevc-video-hq.m3u8`} is the HEVC Switching Set. Together they form a Selection Set that allows selection by codec.

## See Also

- [HTTP Live Streaming (HLS) authoring specification for Apple devices](hls-authoring-specification-for-apple-devices.md)
  Learn the requirements for live and on-demand audio and video content delivery using HLS.
- [Using content protection systems with HLS](using-content-protection-systems-with-hls.md)
  Adding encryption keys to media playlists
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

*[View on Apple Developer](https://developer.apple.com/documentation/http-live-streaming/about-the-common-media-application-format-with-http-live-streaming-hls)*