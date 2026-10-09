# Authoring multivariant and media playlists

**Framework**: HTTP Live Streaming

Author the HTTP Live Streaming (HLS) multivariant and media playlists that Apple Podcasts requires, with the tags and attributes each playlist uses.

#### Overview

An HLS presentation for Apple Podcasts consists of two playlist types: a multivariant playlist that lists the available variant streams and media renditions, and a media playlist for each variant stream or rendition that lists its individual segments. Author both playlist types using the tags described below. For general information about video-on-demand playlists, see [`Video on Demand playlist construction`](video-on-demand-playlist-construction.md).

#### Declare Multivariant Playlist Tags

The multivariant playlist describes all the available variant streams (different video bit rate tiers and formats) and media renditions (audio languages, subtitles, and others) for the presentation. A URI and descriptive tags specify each variant stream and media rendition. The URI tells the player where to download the media playlist for the variant stream or media rendition.

| # | Tag Name | Description | Parameters | Required/Optional | Example |
| --- | --- | --- | --- | --- | --- |
| 1 | `#EXTM3U` | Identifies the file as an M3U playlist | None | Required (must be first line) | `#EXTM3U` |
| 2 | `#EXT-X-VERSION` | Indicates HLS protocol compatibility version | None | Minimum required version is 4. You may need a higher version depending on the features you use. | `#EXT-X-VERSION:4` |
| 3 | `#EXT-X-STREAM-INF` | Defines a variant stream with its attributes | `BANDWIDTH` (required), `RESOLUTION` (required), `CODECS` (required), `AVERAGE-BANDWIDTH` (required), `FRAME-RATE`, `AUDIO`, `SUBTITLES`, `VIDEO`, `CLOSED-CAPTIONS` (Include “NONE” if not available) | Apple Podcasts requires an audio-only variant stream along with video variant streams. For better performance, include multiple video renditions. 1080p (required) and 720p (required), but consider including 480p and 360p for network-constrained devices. | `#EXT-X-STREAM-INF:BANDWIDTH=2500000,RESOLUTION=1920x1080,CODECS="avc1.4d401f,mp4a.40.2",CLOSED-CAPTIONS=NONE` |
| 4 | `#EXT-X-MEDIA` | Defines audio grouping and alternative renditions (audio, subtitles, and others) | `TYPE` (required), `GROUP-ID` (required), `NAME` (required), `URI` (required), `LANGUAGE` (required), `AUTOSELECT` (recommended), `DEFAULT` (recommended), `FORCED`, `CHANNELS` | Required for audio-only grouping. Optional for providing alternate audio language renditions or subtitles. | `#EXT-X-MEDIA:TYPE=AUDIO,GROUP-ID="en-audio",NAME="en-audio",LANGUAGE="en",DEFAULT=YES,CHANNELS="2",URI="audio/en.m3u8"``#EXT-X-MEDIA:TYPE=SUBTITLES,GROUP-ID="subs",NAME="English",LANGUAGE="en",DEFAULT=YES,URI="captions/english.m3u8"` |
| 5 | `#EXT-X-I-FRAME-STREAM-INF` | Defines an iframe-only variant stream for trick play (fast forward, rapid rewind, scrubbing) | `BANDWIDTH` (required), `URI` (required), `CODECS` (recommended), `RESOLUTION` (recommended), `AVERAGE-BANDWIDTH` (recommended) | Required for seeking enhancement. Target capturing 2 frames per second but no more than 8 frames per second. | `#EXT-X-I-FRAME-STREAM-INF:BANDWIDTH=200000,URI="iframes.m3u8",CODECS="avc1.4d401f"` |

#### Declare Media Playlist Tags

The media playlist contains a list of media segments (video or audio chunks) for a specific variant stream or media rendition, along with a group of descriptive tags. Each media segment is specified by URI and optional byte range, telling the player exactly which files and byte ranges to download and play in sequence. A media playlist can contain advertising markers or HLS interstitials specified by media metadata tags.

| # | Tag Name | Description | Parameters | Required/Optional | Example |
| --- | --- | --- | --- | --- | --- |
| 1 | `#EXTM3U` | Identifies the file as an M3U playlist | None | Required (must be first line) | `#EXTM3U` |
| 2 | `#EXT-X-VERSION` | Indicates HLS protocol compatibility version | Version number | Minimum required version is 7. You may need a higher version depending on the features you use. | `#EXT-X-VERSION:7` |
| 3 | `#EXT-X-TARGETDURATION` | Maximum segment duration in seconds | Duration in seconds | Required, range should be 4 to 10 seconds. 6 seconds is recommended. | `#EXT-X-TARGETDURATION:10` |
| 4 | `#EXT-X-MEDIA-SEQUENCE` | Sequence number of first segment | Sequence number | Optional (default 0) | `#EXT-X-MEDIA-SEQUENCE:0` |
| 5 | `#EXT-X-PLAYLIST-TYPE` | Indicates playlist type | `VOD` or `EVENT` | Required for Apple Podcasts, use `VOD` | `#EXT-X-PLAYLIST-TYPE:VOD` |
| 6 | `#EXTINF` | Specifies segment duration and optional title | Duration in seconds, optional title | Required for each segment | `#EXTINF:9.987,` |
| 7 | `#EXT-X-ENDLIST` | Indicates the list of segments is complete | None | Required for VOD | `#EXT-X-ENDLIST` |
| 8 | `#EXT-X-PROGRAM-DATE-TIME` | Defines a base time for the next segment | A time in ISO 8601 format. Note that this is not a wall clock time. | Required if you use date ranges. Do not use the UNIX start time (Jan 1, 1970). | `#EXT-X-PROGRAM-DATE-TIME:2023-10-27T09:50:00Z` |
| 9 | `#EXT-X-DATERANGE` | Media Metadata Tag. Defines a date range for metadata or for HLS interstitials. | `ID` (required), `X-RESUME-OFFSET=0` (required), `X-TIMELINE-OCCUPIES="RANGE"` (required), `X-TIMELINE-STYLE="PRIMARY"` (required), `CLASS` (required), `X-SNAP` (recommended), `START-DATE`, `END-DATE`, `DURATION`, `PLANNED-DURATION`, `CUE`, `X-*` custom attributes. `X-RESTRICT` ignored in Apple Podcasts. | See `#EXT-X-DATERANGE` in [`Delivering ad interstitials in podcast streams`](delivering-ad-interstitials.md). | `#EXT-X-DATERANGE:ID="ad_break_1",CLASS="com.apple.hls.interstitial",START-DATE="2026-04-01T10:09:00Z",PLANNED-DURATION=30.0,X-ASSET-URI="https://ad-server.example.com/ads/midroll1.m3u8",X-RESUME-OFFSET=0,X-SNAP="OUT,IN",X-TIMELINE-OCCUPIES="RANGE",X-TIMELINE-STYLE="PRIMARY"` |

## See Also

- [Encoding media for HLS](encoding-media.md)
  Encode audio and video for HTTP Live Streaming (HLS) delivery to Apple Podcasts.
- [Configuring delivery for HLS](configuring-delivery.md)
  Format media URLs and origin domain access for HTTP Live Streaming (HLS) delivery to Apple Podcasts.
- [Delivering ad interstitials in podcast streams](delivering-ad-interstitials.md)
  Insert ad interstitials into HTTP Live Streaming (HLS) media playlists.
- [Delivering WebVTT subtitles and captions in HLS](delivering-subtitles-and-captions.md)
  Add WebVTT subtitle and caption tracks to your HTTP Live Streaming (HLS) streams, and declare their absence when a stream doesn’t carry captions.
- [Reviewing sample playlists and validating streams](examples-and-validation.md)
  Reference sample multivariant and video-on-demand (VOD) media playlists, and validate your HTTP Live Streaming (HLS) streams with Media Stream Validator.
- [Handling downloads and playback](downloads-and-playback.md)
  Handle Apple Podcasts’ download and playback behavior, including hybrid audio/video streaming, non-video modes, and user-agent identification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/http-live-streaming/multivariant-and-media-playlists)*