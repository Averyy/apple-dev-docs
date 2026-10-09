# Delivering ad interstitials in podcast streams

**Framework**: HTTP Live Streaming

Insert ad interstitials into HTTP Live Streaming (HLS) media playlists.

#### Overview

An HLS interstitial is alternate content, such as an advertisement, that the player inserts into a stream at a specific point without altering the primary media. Use the `#EXT-X-DATERANGE` tag in your HLS media playlists to deliver client-side interstitial advertising. Place an exact segment boundary at each interstitial cue point in your encoded media when possible. Use `X-SNAP` to let the player correct splice timing automatically. Include `CUE=POST` when you deliver a post-roll interstitial.

Use the following attributes with `#EXT-X-DATERANGE` for interstitial delivery:

| # | Attribute | Description | Required | Example Value |
| --- | --- | --- | --- | --- |
| 1 | `CLASS` | Identifies the DATERANGE as an interstitial. Must be set to `com.apple.hls.interstitial`. | Required | `CLASS="com.apple.hls.interstitial"` |
| 2 | `START-DATE` | A timestamp indicating the exact point in time, relative to the `#EXT-X-PROGRAM-DATE-TIME` of the playlist, where the interstitial should begin playback. | Required | `START-DATE="2023-10-27T10:00:00Z"` |
| 3 | `PLANNED-DURATION` | A float value representing the intended (but not-to-exceed) duration of the interstitial. | See Note below. | `PLANNED-DURATION=30.0` |
| 4 | `DURATION` | A float value representing the known, exact duration of the interstitial. If both `PLANNED-DURATION` and `DURATION` are present, `DURATION` takes precedence. | See Note below. | `DURATION=28.5` |
| 5 | `X-SNAP` | Instructs the player to snap the interstitial splice point to the nearest segment boundary in the primary content. Accepts `OUT`, `IN`, or `OUT,IN` to apply snapping at the exit point, resume point, or both. | Recommended | `X-SNAP="OUT,IN"` |
| 6 | `X-RESUME-OFFSET` | Specifies the offset time from the primary media. For interstitials, this is typically set to 0. | Required for Podcasts | `X-RESUME-OFFSET=0` |
| 7 | `X-TIMELINE-OCCUPIES` | Indicates how the interstitial is displayed within the episode timeline. For seamless integration, set to `RANGE`. | Required for Podcasts | `X-TIMELINE-OCCUPIES="RANGE"` |
| 8 | `X-TIMELINE-STYLE` | Defines the style of the interstitial’s timeline representation. For primary media, set to `PRIMARY`. | Required for Podcasts | `X-TIMELINE-STYLE="PRIMARY"` |

> **Note**: Include either `PLANNED-DURATION` or `DURATION` for interstitials delivered with `X-ASSET-URI`; choose the option that best aligns with your ad decisioning process. If both are provided, `DURATION` takes precedence. For interstitials delivered with `X-ASSET-LIST`, the duration comes from the JSON response instead.

Interstitial media can be delivered using one of two methods:

#### Reference the Interstitial Directly with the Asset Uri

Use `X-ASSET-URI` when you know the interstitial media playlist and it’s available when you create the HLS playlist. This attribute points directly to the interstitial’s HLS media playlist.

```m3u8
#EXT-X-DATERANGE:ID="ad_break_1",CLASS="com.apple.hls.interstitial",START-DATE="2023-10-27T10:00:00Z",PLANNED-DURATION=30.0,X-ASSET-URI="https://ad-server.example.com/ads/midroll1.m3u8",X-RESUME-OFFSET=0,X-TIMELINE-OCCUPIES="RANGE",X-TIMELINE-STYLE="PRIMARY"
```

#### Resolve Interstitials at Playback

Use `X-ASSET-LIST` when you need flexibility to determine the interstitial media at playback or download time, or when no interstitial may be available. This attribute points to a JSON response that contains the interstitial media playlist information.

```m3u8
#EXT-X-DATERANGE:ID="ad_break_1",CLASS="com.apple.hls.interstitial",START-DATE="2023-10-27T10:00:00Z",PLANNED-DURATION=30.0,X-ASSET-LIST="https://ad-server.example.com/ads/midroll1.json",X-RESUME-OFFSET=0,X-TIMELINE-OCCUPIES="RANGE",X-TIMELINE-STYLE="PRIMARY"
```

The JSON response specified by `X-ASSET-LIST` must contain an `ASSETS` array. Each object in the array represents an interstitial asset and includes the following keys:

- **`URI`**: The URL of the interstitial’s HLS media playlist.
- **`DURATION`**: A float value indicating the exact duration of the interstitial in seconds.

```json
{
  "ASSETS": [
    {
      "URI": "https://example.com/ads/interstitial_1.m3u8",
      "DURATION": 15.0
    }
  ]
}
```

When you have no ad to place, use an empty list. The player skips the ad break and continues playing the main media.

```json
{
  "ASSETS": []
}
```

## See Also

- [Authoring multivariant and media playlists](multivariant-and-media-playlists.md)
  Author the HTTP Live Streaming (HLS) multivariant and media playlists that Apple Podcasts requires, with the tags and attributes each playlist uses.
- [Encoding media for HLS](encoding-media.md)
  Encode audio and video for HTTP Live Streaming (HLS) delivery to Apple Podcasts.
- [Configuring delivery for HLS](configuring-delivery.md)
  Format media URLs and origin domain access for HTTP Live Streaming (HLS) delivery to Apple Podcasts.
- [Delivering WebVTT subtitles and captions in HLS](delivering-subtitles-and-captions.md)
  Add WebVTT subtitle and caption tracks to your HTTP Live Streaming (HLS) streams, and declare their absence when a stream doesn’t carry captions.
- [Reviewing sample playlists and validating streams](examples-and-validation.md)
  Reference sample multivariant and video-on-demand (VOD) media playlists, and validate your HTTP Live Streaming (HLS) streams with Media Stream Validator.
- [Handling downloads and playback](downloads-and-playback.md)
  Handle Apple Podcasts’ download and playback behavior, including hybrid audio/video streaming, non-video modes, and user-agent identification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/http-live-streaming/delivering-ad-interstitials)*