# Delivering WebVTT subtitles and captions in HLS

**Framework**: HTTP Live Streaming

Add WebVTT subtitle and caption tracks to your HTTP Live Streaming (HLS) streams, and declare their absence when a stream doesn’t carry captions.

#### Overview

WebVTT (Web Video Text Tracks) is the standard format for delivering captions and subtitles in HLS streams. Apple devices running iOS, iPadOS, macOS, and tvOS play WebVTT tracks and support multiple languages.

When your media stream or interstitial doesn’t include subtitles or captions, add `CLOSED-CAPTIONS=NONE` to every `#EXT-X-STREAM-INF` tag in your HLS multivariant playlist.

The following sample stream variant declares that no closed captions are available:

```m3u8
#EXT-X-STREAM-INF:BANDWIDTH=2500000,RESOLUTION=1920x1080,CODECS="avc1.4d401f,mp4a.40.2",CLOSED-CAPTIONS=NONE
```

#### Configure Subtitle Tracks in the Multivariant Playlist

The following attributes apply to `EXT-X-MEDIA` tags with `TYPE=SUBTITLES` in your multivariant playlist:

| # | Attribute | Purpose | Required | Example Value |
| --- | --- | --- | --- | --- |
| 1 | `TYPE` | Media type identifier | Yes | `SUBTITLES` |
| 2 | `GROUP-ID` | Groups related subtitle tracks | Yes | `"subtitles"` |
| 3 | `NAME` | Display name for subtitle track | Yes | `"English"` |
| 4 | `LANGUAGE` | ISO 639-1/639-2 language code | Yes | `"en"` |
| 5 | `URI` | Path to playlist that contains WebVTT segments | Yes | `"subtitles/en.m3u8"` |
| 6 | `DEFAULT` | Sets default caption track | No, but recommended | `YES`/`NO` |
| 7 | `AUTOSELECT` | Auto-selects based on device language | No, but recommended | `YES`/`NO` |
| 8 | `FORCED` | Indicates forced subtitles | If applicable | `YES`/`NO` |

#### Synchronize Subtitle Timing with Video Segments

Follow these guidelines to keep subtitle cues aligned with the audio and video timeline:

- **Segment alignment**: Ensure subtitle timing aligns with video segments.
- **Overlap handling**: Avoid overlapping cue times.
- **Precision**: Align cue start and end times to the actual audio boundaries; WebVTT timestamps use millisecond precision (HH:MM:SS.mmm).

#### Format Caption Text for Readability

Follow these general accessibility guidelines when you author caption text, as targets rather than hard HLS requirements:

- **Line length**: Maximum 32 characters per line for mobile devices.
- **Reading speed**: 160–180 words per minute maximum.
- **Duration**: Minimum 1.5 seconds, maximum 7 seconds per caption.
- **Line count**: Maximum 2 lines per caption for optimal readability.

## See Also

- [Authoring multivariant and media playlists](multivariant-and-media-playlists.md)
  Author the HTTP Live Streaming (HLS) multivariant and media playlists that Apple Podcasts requires, with the tags and attributes each playlist uses.
- [Encoding media for HLS](encoding-media.md)
  Encode audio and video for HTTP Live Streaming (HLS) delivery to Apple Podcasts.
- [Configuring delivery for HLS](configuring-delivery.md)
  Format media URLs and origin domain access for HTTP Live Streaming (HLS) delivery to Apple Podcasts.
- [Delivering ad interstitials in podcast streams](delivering-ad-interstitials.md)
  Insert ad interstitials into HTTP Live Streaming (HLS) media playlists.
- [Reviewing sample playlists and validating streams](examples-and-validation.md)
  Reference sample multivariant and video-on-demand (VOD) media playlists, and validate your HTTP Live Streaming (HLS) streams with Media Stream Validator.
- [Handling downloads and playback](downloads-and-playback.md)
  Handle Apple Podcasts’ download and playback behavior, including hybrid audio/video streaming, non-video modes, and user-agent identification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/http-live-streaming/delivering-subtitles-and-captions)*