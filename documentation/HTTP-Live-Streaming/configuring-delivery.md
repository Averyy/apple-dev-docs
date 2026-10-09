# Configuring delivery for HLS

**Framework**: HTTP Live Streaming

Format media URLs and origin domain access for HTTP Live Streaming (HLS) delivery to Apple Podcasts.

#### Overview

Apple Podcasts requests your media from multiple domains, so correctly formatted URLs and Cross-Origin Resource Sharing (CORS) headers ensure your streams resolve and play without errors.

#### Structure Media Urls for Apple Podcasts

Apple Podcasts supports multiple URL formats and redirection mechanisms:

- **Parameterized URLs**: Apple Podcasts supports URLs containing query parameters (for example, `low/media.m3u8?campaign=midroll-8`).
- **Prefix services**: Apple Podcasts recognizes and handles redirect services that use URL prefixes, such as link shorteners or analytics redirect services.
- **HTTP redirects**: Apple Podcasts automatically follows standard HTTP redirect responses to resolve the final destination URL.

#### Configure Cors for Apple Domains

To support media playback on Apple sites, allow Cross-Origin Resource Sharing (CORS) from Apple-owned domains on your media hosts. You can configure your environment using either origin pattern matching or server-side origin validation.

Both configuration options have the following requirements:

- Configure headers for all hosts in the delivery chain, including playlist and manifest servers, media segment hosts, and all HTTP redirect targets.
- Handle cache keys as follows: - Include the `Origin` header in your CDN cache key.
- Return `Vary: Origin` on all responses containing `Access-Control-Allow-Origin`.
- Expose byte-range headers by returning `Access-Control-Expose-Headers: Content-Range, Content-Length` to enable media seeking.
- Do not return `Access-Control-Allow-Credentials: true`, as playback doesn’t require it.

##### Configure Origin Pattern Matching

Use this approach if your CDN or cloud storage provider supports origin matching rules. If you’re using an origin storage service behind a CDN, configure CORS headers in one layer only (typically at the CDN) to prevent header conflicts or duplicate values.

Configure your platform’s allowed origin field using one of the following options:

- **Apple subdomains only**: Use `https://*.apple.com` to restrict access to Apple-owned origins. The platform verifies the request pattern and automatically reflects the specific requesting origin in the response header.
- **Universal access**: If your media assets are public and don’t require domain restriction, use the universal wildcard `*` to simplify delivery to Apple Podcasts.

> **Note**: Never return `Access-Control-Allow-Origin: https://*.apple.com` as a literal header value. Browsers reject wildcard subdomains in HTTP responses.

##### Configure Server Side Origin Validation

If your hosting platform does not support origin pattern matching, or if you need application-level control, validate the incoming `Origin` header directly in server code:

1. Inspect the incoming `Origin` request header.
2. Validate that the value strictly matches an Apple domain — it starts with `https://` and ends with `.apple.com` (with the leading dot), or is exactly `https://apple.com`. Avoid checks without the leading dot, as they could match untrusted domains. For example, `https://not-apple.com` and `https://apple.com.example.com` would defeat checks that omit the leading dot.
3. If the domain matches, set `Access-Control-Allow-Origin` to the exact value received in the request’s `Origin` header.
4. If the domain doesn’t match or is omitted, don’t return any `Access-Control-*` headers.

Alternatively, if your media is fully public, your server can return `Access-Control-Allow-Origin: *` for all `GET` and `HEAD` requests.

## See Also

- [Authoring multivariant and media playlists](multivariant-and-media-playlists.md)
  Author the HTTP Live Streaming (HLS) multivariant and media playlists that Apple Podcasts requires, with the tags and attributes each playlist uses.
- [Encoding media for HLS](encoding-media.md)
  Encode audio and video for HTTP Live Streaming (HLS) delivery to Apple Podcasts.
- [Delivering ad interstitials in podcast streams](delivering-ad-interstitials.md)
  Insert ad interstitials into HTTP Live Streaming (HLS) media playlists.
- [Delivering WebVTT subtitles and captions in HLS](delivering-subtitles-and-captions.md)
  Add WebVTT subtitle and caption tracks to your HTTP Live Streaming (HLS) streams, and declare their absence when a stream doesn’t carry captions.
- [Reviewing sample playlists and validating streams](examples-and-validation.md)
  Reference sample multivariant and video-on-demand (VOD) media playlists, and validate your HTTP Live Streaming (HLS) streams with Media Stream Validator.
- [Handling downloads and playback](downloads-and-playback.md)
  Handle Apple Podcasts’ download and playback behavior, including hybrid audio/video streaming, non-video modes, and user-agent identification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/http-live-streaming/configuring-delivery)*