# Encoding media for HLS

**Framework**: HTTP Live Streaming

Encode audio and video for HTTP Live Streaming (HLS) delivery to Apple Podcasts.

#### Overview

Apple Podcasts plays HLS video on many devices and across a range of network conditions. Use these encoder settings for best results.

#### Apply Hls Video Encoding Best Practices

Use adaptive bitrate streaming, efficient codecs, and proper segmentation when you encode video for HLS delivery to Apple Podcasts:

- Provide multiple quality levels to adapt to network conditions.
- Use H.264 (AVC) for broad device compatibility and H.265 (HEVC) for better compression efficiency.
- Use appropriate segment durations for smooth playback.

#### Configure Encoding Settings

Use these settings when preparing video for HLS delivery:

- **Keyframe interval**: 2–6 seconds (60–180 frames at 30 fps)
- **B-frames**: 2–3 for H.264, 3–4 for HEVC
- **GOP structure**: Closed GOP
- **Color space**: Rec. 709 for HD, Rec. 2020 for 4K HDR

Use these settings when encoding podcast audio for HLS delivery:

- **Codec**: AAC-LC (recommended) or HE-AAC v1/v2
- **Sample rate**: 48 kHz (preferred) or 44.1 kHz
- **Channels**: Stereo and bitrate 192 kbps preferred for most content, 5.1 surround sound also supported

## See Also

- [Authoring multivariant and media playlists](multivariant-and-media-playlists.md)
  Author the HTTP Live Streaming (HLS) multivariant and media playlists that Apple Podcasts requires, with the tags and attributes each playlist uses.
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

*[View on Apple Developer](https://developer.apple.com/documentation/http-live-streaming/encoding-media)*