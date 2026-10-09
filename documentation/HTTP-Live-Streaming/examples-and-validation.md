# Reviewing sample playlists and validating streams

**Framework**: HTTP Live Streaming

Reference sample multivariant and video-on-demand (VOD) media playlists, and validate your HTTP Live Streaming (HLS) streams with Media Stream Validator.

#### Overview

Use the following playlist examples as a reference when authoring your own HLS streams for Apple Podcasts, and validate your streams with Apple’s command-line tools before publishing.

#### Multivariant Playlist Example

The following multivariant playlist offers an audio rendition group, a subtitle rendition group, and three video variant streams that are paired with audio and subtitles.

```m3u8
#EXTM3U
#EXT-X-VERSION:4
# Define audio rendition group
#EXT-X-MEDIA:TYPE=AUDIO,GROUP-ID="audio_group",NAME="English Stereo",LANGUAGE="en",AUTOSELECT=YES,DEFAULT=YES,URI="audio/en.m3u8"
# Define subtitles/captions rendition group
#EXT-X-MEDIA:TYPE=SUBTITLES,GROUP-ID="subs",NAME="English",LANGUAGE="en",AUTOSELECT=YES,DEFAULT=YES,URI="subtitle/en.m3u8"
# Low quality (480p) - paired with audio_group and subtitles
#EXT-X-STREAM-INF:BANDWIDTH=800000,AVERAGE-BANDWIDTH=750000,RESOLUTION=854x480,CODECS="avc1.4d401f,mp4a.40.2",AUDIO="audio_group",SUBTITLES="subs"
low/media.m3u8
# Medium quality (720p) - paired with audio_group and subtitles
#EXT-X-STREAM-INF:BANDWIDTH=1500000,AVERAGE-BANDWIDTH=1400000,RESOLUTION=1280x720,CODECS="avc1.4d401f,mp4a.40.2",AUDIO="audio_group",SUBTITLES="subs"
medium/media.m3u8
# High quality (1080p) - paired with audio_group and subtitles
#EXT-X-STREAM-INF:BANDWIDTH=2500000,AVERAGE-BANDWIDTH=2350000,RESOLUTION=1920x1080,CODECS="avc1.4d401f,mp4a.40.2",AUDIO="audio_group",SUBTITLES="subs"
high/media.m3u8
# Audio-only variant
#EXT-X-STREAM-INF:BANDWIDTH=131404,CODECS="mp4a.40.2",AUDIO="audio_group"
audio/audio_only.m3u8
# I-frame-only variant, for seeking/scrubbing/FF/RW enhancement
#EXT-X-I-FRAME-STREAM-INF:BANDWIDTH=300000,RESOLUTION=854x480,CODECS="avc1.4d401f",URI="iframe/media.m3u8"
```

#### Vod Media Playlist Example

The following is an example of a VOD media playlist with a 10-second target duration for segments. An `#EXT-X-DATERANGE` tag with a `START` time offset describes a pre-roll advertisement and a mid-roll advertisement.

```m3u8
#EXTM3U
#EXT-X-TARGETDURATION:10
#EXT-X-VERSION:7
#EXT-X-MEDIA-SEQUENCE:1
#EXT-X-PLAYLIST-TYPE:VOD
#EXT-X-INDEPENDENT-SEGMENTS
#EXT-X-MAP:URI="main.mp4",BYTERANGE="1206@0"
#EXT-X-PROGRAM-DATE-TIME:2025-01-01T00:00:00.000Z
#Main Content
#Segment 1
#EXTINF:9.987,
#EXT-X-BYTERANGE:1500000@1206
main.mp4
#Segment 2
#EXTINF:9.987,
#EXT-X-BYTERANGE:1500000@1501206
main.mp4
#Segment 3
#EXTINF:9.987,
#EXT-X-BYTERANGE:1500000@3001206
main.mp4
... more segments ...
#Segment 99
#EXTINF:3.15000,
#EXT-X-BYTERANGE:757516@134587545
main.mp4
#EXT-X-ENDLIST
#Pre-roll Advertisement Marker
#EXT-X-DATERANGE:ID=“preroll-ad-1”,CLASS=“com.apple.hls.interstitial",START-DATE="2025-01-01T00:00:00.000Z",DURATION=30.0,X-ASSET-URI="https://ad-server.example.com/preroll/campaign-123/ad.m3u8",X-RESUME-OFFSET=0,X-TIMELINE-OCCUPIES="RANGE",X-TIMELINE-STYLE="PRIMARY"
#Mid-roll Advertisement Marker
#EXT-X-DATERANGE:ID=“midroll-ad-1”,CLASS=“com.apple.hls.interstitial",START-DATE="2025-01-01T01:23:45.000Z",DURATION=15.0,X-ASSET-URI="https://ad-server.example.com/midroll/campaign-456/ad.m3u8",X-SNAP="OUT,IN",X-RESUME-OFFSET=0,X-TIMELINE-OCCUPIES="RANGE",X-TIMELINE-STYLE="PRIMARY"
```

#### Validate a Stream with Media Stream Validator

Media Stream Validator (`mediastreamvalidator`) simulates an HLS session and verifies that the index file and media segments conform to the HLS specification. It checks for several best practices to ensure reliable streaming. If it finds errors or problems, it displays a detailed diagnostic report. To write validation data to a JSON file, pass the `--validation-data-path` argument.

You can use [`this Apple Podcasts sample manifest`](https://developer.apple.comhttps://devstreaming-cdn.apple.com/videos/streaming/examples/podcast-sample/mvp_podcast_sample.m3u8) as a reference for development and troubleshooting.

Download Media Stream Validator from [`HLS downloads`](https://developer.apple.comhttps://developer.apple.com/download/all/?q=hls).

Use the `--include-settings` option to specify a file containing configuration settings for Media Stream Validator to use:

```shell
mediastreamvalidator --include-settings podcasts.json <stream-url>
```

For the `podcasts.json` file, copy and paste the following code block:

```json
// Configuration to validate the Podcast specification
// Version: 1.05 (Sep, 2026)
{
	"@REQUIRED-VERSION": "mediastreamvalidator:2.0.263",
	"errors.ignore": [
		// ignore the following HLSReport errors (passed on to HLSReport)
		"1024", // Language attribute missing
		"1038", // No 192k Variant
		"1072", // Channel Layout Changed
		"1075", // Bad Frame Rate Switch
		"1076", // Need Both HDR Codecs
		"1077", // Full Variant Range
		"1082", // Wrong Default Variant for iOS WiFi
		"1083"  // Wrong Default Variant for iOS Cellular
	],
	"rules": {
		"enable" : [
			// Enable optional RuleSets that are not configured below
			"33087",// Interstitial Duration: Validate the interstitial duration is declared accurately
			"42507"	// AV Muxed: Checks that there are no muxed audio/video variants or playlists
		],
		// configure EXT-X-DATERANGE validation
		"24060": {
			"boundary-check": "must",	// date ranges MUST not appear before the beginning or after or close to the end of stream
			"boundary-margin": 2.0		// 2s are considsered "close to the end of stream"
		},
		// configure and enable AV Variant Type Rule
		"33053" : { 
			"audioVideo": "require",
			"audioOnly": "require",
			"videoOnly": "forbid",
			"interstitials": "superset"	// interstitials must *at least* contain variants for all AV types the main stream contains
		},
		// configure subtitle rule to not log a SHOULD for streams no providing subtitles or captions
		"33088": {
			"captioning": "allow"	// default is prefer
		},		
		// configure Interstitial Duration: Validate the interstitial duration is declared accurately
		"33087": {
			"duration-err": 10	// Percent error allowed between the date range duration and the actual duration of the interstitial playlist
		},
		// Verify target durations for segments and media playlists.
		"35023": {  
			"range" : {"min":4, "max":10}	// TargetDuration must be between 4 and 10seconds
		},
		// configure Interstitial Date Range Attributes Validation
		"42508": {
			"require": ["X-TIMELINE-OCCUPIES", "X-TIMELINE-STYLE"],
			"limit": {
				"CUE": ["POST"],	// only CUE="POST" is allowed
				"X-RESTRICT": [],	// X-RESTRICT is forbidden
				"X-DEBUG": [],		// X-DEBUG is forbidden
				"X-TIMELINE-OCCUPIES": ["RANGE"],
				"X-TIMELINE-STYLE": ["PRIMARY"]
			}
		},
		// Check for stream properties to be in a configurable range
		"42518": {
			"types" : ["VOD"],			// only allow VOD playlists
		}
	}, // "rules"
	
	// configure to return a non zero exit code if MUST Fix Authoring or more sever errors are found
	"exit-code.threshold": "must_auth",

	// ensure HLSReport compatible output (for now)
	"compatible-output": ["v1.x"]
}
```

## See Also

- [Authoring multivariant and media playlists](multivariant-and-media-playlists.md)
  Author the HTTP Live Streaming (HLS) multivariant and media playlists that Apple Podcasts requires, with the tags and attributes each playlist uses.
- [Encoding media for HLS](encoding-media.md)
  Encode audio and video for HTTP Live Streaming (HLS) delivery to Apple Podcasts.
- [Configuring delivery for HLS](configuring-delivery.md)
  Format media URLs and origin domain access for HTTP Live Streaming (HLS) delivery to Apple Podcasts.
- [Delivering ad interstitials in podcast streams](delivering-ad-interstitials.md)
  Insert ad interstitials into HTTP Live Streaming (HLS) media playlists.
- [Delivering WebVTT subtitles and captions in HLS](delivering-subtitles-and-captions.md)
  Add WebVTT subtitle and caption tracks to your HTTP Live Streaming (HLS) streams, and declare their absence when a stream doesn’t carry captions.
- [Handling downloads and playback](downloads-and-playback.md)
  Handle Apple Podcasts’ download and playback behavior, including hybrid audio/video streaming, non-video modes, and user-agent identification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/http-live-streaming/examples-and-validation)*