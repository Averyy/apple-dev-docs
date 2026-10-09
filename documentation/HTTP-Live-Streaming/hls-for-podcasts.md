# HLS for Apple Podcasts

**Framework**: HTTP Live Streaming

Deliver HTTP Live Streaming (HLS) video-on-demand content to Apple Podcasts.

#### Overview

Apple Podcasts supports HTTP Live Streaming (HLS) video-on-demand media playback with interstitial advertising. This guide covers how the Apple Podcasts player interprets HLS fields, where Apple Podcasts requirements differ from the general HLS specification, and best practices for delivering your content.

#### Structure a Podcast Episode

An HLS podcast episode begins with a multivariant playlist. This describes the basic content as variant streams, each of which describes a different version of the same content — for example, video at a particular bit rate, in a particular format, and a particular resolution. You can extend each variant with media renditions, which are alternate versions of part of the content, such as audio produced in different languages.

The player chooses variants automatically, based on download speed, codec support, preferred pathway, and display characteristics. User input is used to choose renditions, and you need to provide identically named renditions for every variant.

#### Deliver Hls Video Using the Podcasts Connect Api

The Podcasts Connect API provides the capabilities to associate HLS video Primary Playlist URLs with your standard RSS-based episodes. If you host podcasts and want access to the Podcasts Connect API documentation, complete [`this survey`](https://developer.apple.comhttps://survey.apple.com/axm/survey/as/6984af5e34487c4f235c595f). If you already have access, see the [`Podcasts Connect API documentation`](https://developer.apple.comhttps://amp-partner-docs.apple.com/docs/podcasts-connect-api-user-guide).

#### Apple Developer Hls Resources

See the [`HTTP Live Streaming`](https://developer.apple.comhttps://developer.apple.com/streaming/) technology landing page for additional reference material, such as [`Getting Started with HLS Interstitials`](https://developer.apple.comhttps://developer.apple.com/streaming/GettingStartedWithHLSInterstitials.pdf) and [`HLS Streaming Examples`](https://developer.apple.comhttps://developer.apple.com/streaming/examples/).

## Topics

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
- [Reviewing sample playlists and validating streams](examples-and-validation.md)
  Reference sample multivariant and video-on-demand (VOD) media playlists, and validate your HTTP Live Streaming (HLS) streams with Media Stream Validator.
- [Handling downloads and playback](downloads-and-playback.md)
  Handle Apple Podcasts’ download and playback behavior, including hybrid audio/video streaming, non-video modes, and user-agent identification.

## See Also

- [HTTP Live Streaming (HLS) authoring specification for Apple devices](hls-authoring-specification-for-apple-devices.md)
  Learn the requirements for live and on-demand audio and video content delivery using HLS.
- [Using content protection systems with HLS](using-content-protection-systems-with-hls.md)
  Adding encryption keys to media playlists
- [About the Common Media Application Format with HTTP Live Streaming (HLS)](about-the-common-media-application-format-with-http-live-streaming-hls.md)
  Learn the Common Media Application Format as it applies to HLS.
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

*[View on Apple Developer](https://developer.apple.com/documentation/http-live-streaming/hls-for-podcasts)*