# About the EXT-X-VERSION tag

**Framework**: HTTP Live Streaming

Find the protocol version that corresponds with the HLS features your app supports.

#### Overview

The `EXT-X-VERSION` tag indicates the compatibility version of the Playlist file. This file, its associated media, and its server must comply with all provisions of the IETF Internet-Draft of [`HTTP Live Streaming 2nd Edition`](https://developer.apple.comhttps://tools.ietf.org/html/draft-pantos-hls-rfc8216bis) (or earlier specifications) describing the protocol version indicated by the tag value. A Playlist file that doesn’t contain an `EXT-X-VERSION` tag must comply with version 1 of this protocol. Support for M3U8 Playlists was introduced with iOS 3.0, Mac OS X 10.6, and Safari 4.

##### High Level Features

| EXT-X-VERSION | Features and usage notes |
| --- | --- |
| 2 | IV attribute of the `EXT-X-KEY` tag |
| 3 | Floating-point `EXTINF` duration values |
| 4 | `EXT-X-BYTERANGE`, `EXT-X-I-FRAME-STREAM-INF`,` EXT-X-I-FRAMES-ONLY`, `EXT-X-MEDIA`, the `AUDIO` and `VIDEO` attributes of the `EXT-X-STREAM-INF` tag |
| 5 | `KEYFORMAT` and `KEYFORMATVERSIONS` attributes of the `EXT-X-KEY` tag. The `EXT-X-MAP` tag. `SUBTITLES` media type. `SAMPLE-AES` encryption method `EXT-X-KEY` |
| 6 | `CLOSED-CAPTIONS` media type. Allow` EXT-X-MAP` for subtitle playlists |
| 7 | `EXT-X-SESSION-DATA`, `EXT-X-SESSION-KEY`, `EXT-X-DATERANGE`, `SERVICE` values of `INSTREAM-ID`, `AVERAGE-BANDWIDTH`, `FRAME-RATE`, `CHANNELS`, and `HDCP-LEVEL` attributes. |
| 8 | `EXT-X-GAP`, `EXT-X-DEFINE`, Variable Substitution, `VIDEO-RANGE` attribute. |
| 9 | `EXT-X-SKIP` |
| 10 | `EXT-X-SERVER-CONTROL`, `EXT-X-PART-INF`, `EXT-X-PRELOAD-HINT`, `EXT-X-RENDITION-REPORT`, the `CUE` attribute of `EXT-X-DATERANGE`, the `STABLE-RENDITION-ID` of `EXT-X-MEDIA`, the `SUPPLEMENTAL-CODECS` attribute of `EXT-X-STREAM-INF`, and the `SCORE` and `STABLE-VARIANT-ID` attributes of `EXT-X-STREAM-INF` and `EXT-X-I-FRAME-STREAM-INF` tags |
| 11 | `QUERYPARAM` attribute of `EXT-X-DEFINE` |
| 12 | Attributes starting with ‘`REQ-`’ |

##### Backward Compatibility

> ❗ **Important**: Older clients ignore backward-compatible features and will still play back the content in some form. Specify only the protocol version that’s required for backward compatibility in a given feature. For example, you don’t have to specify protocol version 5 if you’ve just added SUBTITLES.

The following features aren’t backward compatible. Older clients may fail to play the content if you use these features but don’t specify the protocol version where they were introduced:

- You must use at least protocol version 2 if you have `IV` in `EXT-X-KEY`.
- You must use at least protocol version 3 if you have floating point `EXTINF` duration values.
- You must use at least protocol version 4 if you have `EXT-X-BYTERANG`E or `EXT-X-IFRAME-ONLY`.
- You must use at least protocol version 5 if you specify the `SAMPLE-AES` encryption method in `EXT-X-KEY`, or if you have `KEYFORMAT` and `KEYFORMATVERSIONS` attributes in `EXT-X-KEY`, or if you have `EXT-X-MAP`.
- You must use at least protocol version 6 if you have `EXT-X-MAP` in a Media Playlist that does not contain `EXT-X-I-FRAMES-ONLY`.
- You must use at least protocol version 7 if you specify `SERVICE` values for the `INSTREAM-ID` attribute of `EXT-X-MEDIA`.
- You must use at least protocol version 8 if you use variable substitution.
- You must use at least protocol version 9 if you have `EXT-X-SKIP`.
- You must use at least protocol version 10 if you have `EXT-X-SKIP` that replaces `EXT-X-DATERANGE` tags in a Playlist Delta Update.
- You must use at least protocol version 11 if you have `QUERYPARAM` attribute in `EXT-X-DEFINE`.
- You must use at least protocol version 12 if you have attributes that start with  “`REQ-`”.

##### Specifications

The following tables list the versions of specifications where specific features are described, along with the corresponding iOS release that supports those features.

> **Note**: Over time, HLS has been described by different documents: draft-pantos-http-live-streaming, which became [`RFC 8216`](https://developer.apple.comhttps://datatracker.ietf.org/doc/html/rfc8216), and now [`draft-pantos-hls-rfc8216bis`](https://developer.apple.comhttps://datatracker.ietf.org/doc/html/draft-pantos-hls-rfc8216bis).

##### Draft Pantos Http Live Streaming and Rfc 8216

| Revision | iOS Version | Notes |
| --- | --- | --- |
| 00, 01 | 3.0 | . Initial version. |
| 02 | 3.1 | Added `EXT-X-DISCONTINUITY`. Changed Content-Type. Added redundant streams. |
| 03, 04 | 3.2 | . Added `EXT-X-VERSION`. Added IV attribute to `EXT-X-KEY`; `RESOLUTION` attribute to `EXT-X-STREAM-INF`. Corrected `CODECS` attribute values. |
| — | 4.0 | Added timed metadata APIs, custom protocols for keys. |
| 05 | 4.2 | . Added `EXTINF` floating point durations. Support for CEA-608 Closed captions. |
| — | 4.3 | Added `AccessLog` & `ErrorLog` objects to APIs. |
| 06 | 4.3.2 | Added `EXT-X-PLAYLIST-TYPE`. |
| 07, 08 | 5.0 | . Added `EXT-X-I-FRAMES-ONLY`; `EXT-X-I-FRAME-STREAM-INF`; `EXT-X-MEDIA`; `EXT-X-BYTERANGE`. Added `AUDIO` and `VIDEO` attributes to `EXT-X-STREAM-INF`. |
| 09, 10, 11 | 6.0 | . Added `EXT-X-MAP`. Added `KEYFORMAT` and `KEYFORMATVERSIONS` attributes to `EXT-X-KEY`; `SUBTITLES` attribute to `EXT-X-STREAM-INF`; `FORCED` and `CHARACTERISTICS` attributes to `EXT-X-MEDIA`. Added `SUBTITLES` value to `TYPE` attribute of` EXT-X-MEDIA`; `SAMPLE-AES` value to `METHOD` attribute of `EXT-X-KEY`. Added `X-TIMESTAMP-MAP` to WebVTT. Added AC-3 support. |
| 12 | 7.0 | . Added `EXT-X-DISCONTINUITY-SEQUENCE`; `EXT-X-START`. Added `ASSOC-LANGUAGE` and `INSTREAM-ID` attributes to `EXT-X-MEDIA`; `CLOSED-CAPTIONS` attribute to `EXT-X-STREAM-INF`. Removed `PROGRAM-ID` attribute of `EXT-X-STREAM-INF` and `EXT-X-I-FRAME-STREAM-INF`. Added `CLOSED-CAPTIONS` value to `TYPE` attribute of `EXT-X-MEDIA`. Allow `EXT-X-MAP` to be used in subtitle playlists. |
| 13 | 7.1 | Added `EXT-X-INDEPENDENT-SEGMENTS`. |
| 14, 15, 16 | 8.0 | P. Major re-write of spec. Added `EXT-X-SESSION-DATA`. Removed `EXT-X-ALLOW-CACHE`. Added `AVERAGE-BANDWIDTH` attribute to `EXT-X-STREAM-INF` and `EXT-X-I-FRAME-STREAM-INF`. Added `SERVICE` values to `INSTREAM-ID` attribute of `EXT-X-MEDIA`. Added support for Enhanced AC-3. Support for CEA-708 Closed captions. |
| 17, 18 | 9.0 | Added `EXT-X-SESSION-KEY`. Added `FRAME-RATE` to `EXT-X-STREAM-INF` and `EXT-X-IFRAME-STREAM-INF`. New peak bit-rate calculation. |
| 19 | 9.3 | Added `EXT-X-DATERANGE`. |
| 20 | 10.0 | Added `CHANNELS` attribute to `EXT-X-MEDIA`; `HDCP-LEVEL` attribute to `EXT-X-STREAM-INF` and `EXT-X-I-FRAME-STREAM-INF`. Added fMP4 support. |
| 21, 22, 23 | 10.3.1 | Clarified `AUTOSELECT=YES` uniqueness. Added mention of CMAF. |
| RFC8216 | 10.3.1 | Wording changes and clarifications. |

##### Draft Pantos Hls Rfc8216bis

| Revision | iOS Version | Notes |
| --- | --- | --- |
| 00 | 11.0 | . Added `EXT-X-GAP`; `EXT-X-DEFINE` and Variable Substitution. Added `VIDEO-RANGE` attribute to `EXT-X-STREAM-INF` and `EXT-X-I-FRAME-STREAM-INF`. Added `TYPE-1` value to `HDCP-LEVEL` attribute. Support for `IMSC1` subtitles. |
| 01 | - | Clarified the `X-TIMESTAMP-MAP` for non-MPEG-2 content. Added semantic change for `EXT-X-TARGETDURATION` tag. Updated the JSON RFC format requirement. |
| 02 | 12.0 | Added second `CHANNELS` parameter. Added unrecognized `CHANNELS` parameters guidance. |
| 03 | - | Added `EXT-X-BITRATE` tag. Minor clarification about the use of Movie Extends Box in Fragmented MPEG-4 files. |
| 04 | - | Add note about PES timestamp wraps. |
| 05 | 13.0 | Revise definition of peak segment bit rate. Add `ALLOWED-CPC` attribute to `EXT-X-STREAM-INF` and `EXT-X-I-FRAME-STREAM-INF`. Allow Media Metadata tags to be removed from playlists. |
| 06 | - | Rearranged Playlist Tags subsections. Minor rewording. |
| 07 | 13.5 | . Support for Low-Latency HLS, including Partial Segments, Delivery Directives, Playlist Delta Updates, and the Low-Latency Server Configuration Profile. Adds tags: `EXT-X-PART-INF`, `EXT-X-SERVER-CONTROL`, `EXT-X-PART`, `EXT-X-SKIP`, `EXT-X-PRELOAD-HINT`, and `EXT-X-RENDITION-REPORT`. Adds `HLG` enum value to `VIDEO-RANGE` attribute. Reserves query parameters that begin with “`_HLS_`”. |
| 08 | 14.0 | Add `SCORE` and `STABLE-VARIANT-ID` attributes to `EXT-X-STREAM-INF` and `EXT-X-I-FRAME-STREAM-INF`. Add `STABLE-RENDITION-ID` attribute to `EXT-X-MEDIA`. `CHARACTERISTICS` values are Media Characteristic Tags, not Uniform Type Identifiers. A few minor clarifications. |
| 09 | - | Minor clarifications. Preload hint request should use 2^53-1 for unknown byte range length. |
| 10 | 15.0 | Rename to “Multivariant Playlist”. Add Content Steering (`EXT-X-CONTENT-STEERING` tag, `PATHWAY-ID` attribute, and fetching Steering Manifests). Add Interstitials (specialized `EXT-X-DATERANGE` tags, asset list interstitial JSON files, and the enumerated-string-list type). Minor clarifications. |
| 11 | 15.5 | Update Content Steering to add Pathway Cloning. Add `CUE` attribute to `EXT-X-DATERANGE`. Add `SUPPLEMENTAL-CODECS` attribute to `EXT-X-STREAM-INF` and `EXT-X-I-FRAME-STREAM-INF`. Minor clarifications. |
| 12 | 16.0 | Document `_HLS_start_offset`. Modify rules for Partial Segments near `GAP`s. Relax `EXT-X-DATERANGE` rules for Renditions. Minor clarifications. |
| 13 | 16.5 | . Add `QUERYPARAM` attibute to `EXT-X_DEFINE`. Add `FORMAT` attribute to `EXT-X-SESSION-DATA`. Add special behavior for attributes with a prefix of “`REQ-`”. Some clarifications. |
| 14 | 17.0 | Added `BIT-DEPTH` and `SAMPLE-RATE` attributes to `EXT-X-MEDIA`.  Extended `CHANNELS` attribute of `EXT-X-MEDIA` to allow a third parameter.  Added `REQ-VIDEO-LAYOUT` attribute to `EXT-X-STREAM-INF` and `EXT-X-I-FRAME-STREAM-INF`.  Added mention of the extensible priority scheme.  Added appendix on “Displaying Rendition Names”. Minor clarifications. |
| 15 | 17.5 | Added mention of `SAMPLE-AES-CTR` method of `EXT-X-KEY`.  Some clarifications. |

> ❗ **Important**: Always use the most recent version of the [`HTTP Live Streaming tools`](https://developer.apple.comhttps://developer.apple.com/go/?id=http-live-streaming-tools) to generate or test your HTTP Live Streams.

## See Also

- [Example playlists for HTTP Live Streaming](example-playlists-for-http-live-streaming.md)
  View and compare playlists for different HLS applications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/http-live-streaming/about-the-ext-x-version-tag)*