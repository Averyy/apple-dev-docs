# Handling downloads and playback

**Framework**: HTTP Live Streaming

Handle Apple Podcasts’ download and playback behavior, including hybrid audio/video streaming, non-video modes, and user-agent identification.

#### Overview

Apple Podcasts supports a flexible download model that balances cellular data usage with the best available playback experience.

#### Deliver Audio Only Downloads to Followers By Default

When followers of a show have auto-downloads enabled, Apple Podcasts delivers audio-only downloads by default. This preserves current behavior and avoids unexpected increases in data usage.

- Apple Podcasts doesn’t enable video auto-download automatically for followers.
- Followers who want to receive video downloads can opt in to include video in future episodes.
- Followers who haven’t opted in can still access video by streaming on demand.

Apple Podcasts downloads audio from the media playlist and from each interstitial to the listener’s device. The player fetches and caches only the sub-playlists for the downloaded content type — for example, an audio-only download caches the audio media playlist and its interstitials. The player doesn’t crawl media playlists for variants that weren’t downloaded, such as video; instead, it resolves and fetches them live over the network at playback time.

Because of this, keep your main media and interstitial media URLs resolvable and replayable at a later date. If a URL fails to resolve later, playback errors occur.

#### Stream Video When Only Audio Is on Device

When a user requests video playback but only has an audio version downloaded on device, Apple Podcasts fetches and streams the video version over the network.

- The downloaded audio track continues to play without interruption if a network disruption occurs while the player streams the video.
- This ensures a seamless listening experience even under poor network conditions.

To support this hybrid playback model, keep the HLS multivariant playlist and all associated interstitials accessible and consistent when Apple Podcasts fetches the video version. A mismatch between the audio download state and the HLS manifest may result in playback issues.

#### Continue Audio Playback in Non Video Contexts

When a user is streaming a video episode and transitions to a non-video context — such as locking the device or connecting to CarPlay — the player automatically adjusts:

- Video network traffic stops streaming; audio continues to stream uninterrupted.
- Video streaming resumes only when the user returns to an active video context.

This behavior optimizes bandwidth usage and ensures uninterrupted audio playback across all listening environments.

#### Recognize Apple Podcasts User Agent Strings

Apple Podcasts identifies itself to hosting providers by sending a user-agent header with every media request. Hosting providers should expect to see two distinct user-agent formats:

- **Standard playback:** `Podcasts/#### CFNetwork/####.###.# Darwin/##.#.#` — Apple Podcasts sends this user agent for every media request during user-initiated downloads and streaming playback. Hosting providers don’t need to change how they handle it.
- **Scout:** `Podcasts/#### CFNetwork/####.###.# Darwin/##.#.# Scout/#.#` — The player uses this user agent to align timed features such as transcripts, chapters, and timed links with episode playback. The player issues Scout requests against the audio track only, retrieving a minimal amount of data. These requests aren’t associated with user-initiated playback or full media delivery.

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
- [Reviewing sample playlists and validating streams](examples-and-validation.md)
  Reference sample multivariant and video-on-demand (VOD) media playlists, and validate your HTTP Live Streaming (HLS) streams with Media Stream Validator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/http-live-streaming/downloads-and-playback)*