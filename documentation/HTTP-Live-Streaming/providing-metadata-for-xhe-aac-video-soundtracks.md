# Providing metadata for xHE-AAC video soundtracks

**Framework**: HTTP Live Streaming

Ensure volume normalization by including metadata for loudness and dynamic range control.

#### Overview

Soundtracks that use xHE-AAC (Extended High-Efficiency Advanced Audio Codec) encoding include MPEG-D DRC metadata for loudness and dynamic range control (DRC). When you create video soundtracks with xHE-AAC, provide at least the following metadata to ensure consistent results across different services. For playback, set up the MPEG-D DRC tool at the decoder by following the guidelines below.

> **Note**: Refer to ISO/IEC 23003-4 for additional information about these metadata specifications.

Refer to ISO/IEC 23003-4 for additional information about these metadata specifications.

##### Configure Metadata for Content Generation

The loudness and DRC metadata that you include in video content needs to fulfill the MPEG-D DRC requirements for the Basic DRC Metadata Profile, and always include the following values:

| loudness info fields | value |
| --- | --- |
| Include a `methodValue` for `methodDefinition` == “Anchor Loudness” and `measurementSystem` == “ITU-R BS.1770” | Measure anchor loudness using speech-gating or estimate when speech activity is low. |
| `bs_true_peak_level` or `bs_sample_peak_level` | True peak according to ITU-R BS.1770 or sample peak level. |

Measure anchor loudness of the dialog stem using the ITU-R BS.1770 standard because `methodValue` must reflect the actual anchor loudness of the content. Apply speech-gating to the full mix to obtain the anchor loudness value when only the full mix is available for measurement.

Anchor loudness can be inaccurate when the speech detector can’t find much speech in the full mix. Monitor this situation by computing the speech activity, which is the duration of detected speech divided by the duration of the content. When speech activity is low, ignore this measurement because it can be inaccurate. Instead, derive the anchor loudness value from the program loudness value and other applicable measurements to model the value from statistics of a variety of content. See [`Adjusting anchor loudness`](adjusting-anchor-loudness.md) for additional information.

| `drcSetEffect` of the required DRC metadata | Required minimum level that supports playback with minimal peak limiter engagement (LKFS) | Position of bit in `drcSetEffect` field of `drcInstructions`, which must have a value of `1` |
| --- | --- | --- |
| `Late Night` | -24 | 1 |
| `Noisy Environment` | -16 | 2 |
| `Limited Playback Range` | -16 | 3 |
| `General Compression` | -24 | 6 |

Match as close as possible the output anchor loudness of the DRC-processed versions with the anchor loudness of the unprocessed output.

The DRC for `General Compression` can have several instances to accommodate various target loudness values, which provides just enough compression to reach the target without engaging a limiter. If no compression is necessary or desired for specific loudness targets, include a corresponding DRC for `General Compression` that doesn’t have a compression effect.

> **Note**: Refer to ISO/IEC 23003-4:2020 Table 12 for additional information about these metadata specifications.

Refer to ISO/IEC 23003-4:2020 Table 12 for additional information about these metadata specifications.

##### Configure Metadata for Playback

Configure the MPEG-D DRC decoder for playback according to the specifications below. The configuration occurs completely or partially at the system level and those settings don’t appear at the API level.

Set up the MPEG-D DRC decoder to assign the highest priority to the following loudness metadata:****

| Metadata field | Value (highest priority) |
| --- | --- |
| `methodDefinition` | `Anchor Loudness` |
| `measurementSystem` | `Expert/Panel` |

The `methodDefinition` field defaults to `Program Loudness`, if present, if you don’t specify `Anchor Loudness`. This configuration deviates from the default configuration specified in ISO/IEC 23003-4, which selects `Program Loudness` and `ITU-R BS.1770` with highest priority. However, the standard specifies an interface to customize the configuration, including the loudness metadata priority.

Some previously deployed implementations may use the default ISO/IEC 23003-4 configuration and may not support the interface for customization. These systems may select loudness metadata with a `methodDefinition` value of `Program Loudness`, if present, in addition to other loudness metadata. This can result in a deviation of the output loudness of the same content from systems that select `Anchor Loudness`, if present, in addition to `Program Loudness`.

> **Note**: Refer to ISO/IEC 23003-4:2020 Table 51 for information about the priority order for `measurementSystem` for the `Expert/Panel` value.

Refer to ISO/IEC 23003-4:2020 Table 51 for information about the priority order for `measurementSystem` for the `Expert/Panel` value.

The following table (ANSI/CTA-2075) provides recommended target loudness value settings of the DRC tool to control the integrated loudness at the output:

| Transducer SPL range | Maximum SPL (dBA) | Target loudness (LKFS) |
| --- | --- | --- |
| `small` | below 75 | -16 |
| `medium` | between 70 and 90 | -24 |
| `large` | above 85 | -31 |
| `unknown` | NA | -24 |

To achieve sufficient output SPL, ensure the target loudness value depends on the SPL range of the active transducer, which has three categories (`small`, `medium`, `large`). Choose the SPL range category by measuring the maximum SPL of the transducer at the anticipated listener location using pink noise at -24 LKFS. Assign the category according to the middle column as ANSI/CTA-2075 Annex G describes. For example, micro loudspeakers in portable devices typically fall into the `small` SPL range category.

The following table specifies the appropriate DRC requests for different listening environments and transducer SPL ranges (ANSI/CTA-2075):

| Environment | Transducer SPL range | DRC request |
| --- | --- | --- |
| `ideal`, `unknown` | small | `limited` |
| `ideal`, `unknown` | `large`, `medium`, `unknown` | `general` |
| `noisy` | all | `noisy` |

> **Note**: An `ideal` environment is a quiet listening environment.

An `ideal` environment is a quiet listening environment.

Request `general` for DRC when you want loudness normalization unless a different DRC request is applicable for the playback scenario. This applies appropriate compression to reach the target loudness, such as when applying gain during normalization.

User preferences can override DRC settings. The following table provides examples of two preferences and the conditions, transducer SPL range, and environment under which to apply these preferences:

| User preference | Environment | Transducer SPL range | DRC request |
| --- | --- | --- | --- |
| `max DRC` | all | all | `noisy` |
| `late night` | `ideal`, `unknown` | `large`, `medium`, `unknown` | `late night` |

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
- [Adjusting anchor loudness](adjusting-anchor-loudness.md)
  Adjust anchor loudness when measurements of speech-gated loudness for a full mix may be inaccurate, such as when speech activity is low.
- [Providing JavaScript Object Notation (JSON) chapters](providing-javascript-object-notation-json-chapters.md)
  Prepare JSON chapters for HTTP Live Streaming.


---

*[View on Apple Developer](https://developer.apple.com/documentation/http-live-streaming/providing-metadata-for-xhe-aac-video-soundtracks)*