# HTTP Live Streaming (HLS) authoring specification for Apple devices

**Framework**: HTTP Live Streaming

Learn the requirements for live and on-demand audio and video content delivery using HLS.

#### Overview

For a deeper discussion of the features available in HLS, refer to [`Apple’s streaming resource page`](https://developer.apple.comhttp://developer.apple.com/streaming/), which contains pointers to the overview document, the HLS specification, technical notes, tools, presentations, and examples.

##### About Hls Authoring

The HLS specification is a published RFC ([`RFC 8216`](https://developer.apple.comhttps://datatracker.ietf.org/doc/html/rfc8216)). However, HLS continues to evolve, so there’s an updated draft specification — [`draft-pantos-hls-rfc8216bis (HLS2)`](https://developer.apple.comhttps://datatracker.ietf.org/doc/html/draft-pantos-hls-rfc8216bis).

Please see [`Documentation`](https://developer.apple.comhttps://developer.apple.com/streaming/), which may contain a reference to a preliminary version of the draft specification.

This document always uses the most up-to-date version, which is, either the preliminary version or the draft specification (whichever has a higher version number).

> **Note**: HLS was originally specified in draft-pantos-http-live-streaming (HLS1). That document was superseded by RFC 8216.

The key words “MUST,” “MUST NOT,” “REQUIRED,” “SHALL,” “SHALL NOT,” “SHOULD,” “SHOULD NOT,” “RECOMMENDED,” “MAY,” and “OPTIONAL” in this document are to be interpreted as described in [`RFC 2119`](https://developer.apple.comhttps://datatracker.ietf.org/doc/html/rfc8219).

Find additional information for HLS specifications at [`HTTP Live Streaming (HLS) Authoring Specification for Apple devices appendixes`](hls-authoring-specification-for-apple-devices-appendixes.md).

##### About Spatial Video

Spatial video is intended to produce a richer experience for the user. Spatial video MUST use the REQ-VIDEO-LAYOUT attribute to specify desired channel and projection specifiers. Please see [`HLS specification`](https://developer.apple.comhttps://developer.apple.com/streaming/HLS-draft-pantos.pdf) for valid channel and projection specifiers.

Spatial video media is split into following categories.

This video relies on a special projection type, known as ‘PROJ-AIV’ which is defined outside the core HLS specification. For details, see [`QuickTime and ISO Base Media File Formats and Spatial and Immersive Media`](https://developer.apple.comhttps://developer.apple.com/av-foundation/Stereo-Video-ISOBMFF-Extensions.pdf)

> **Note**: Stereo, Immersive and stereo APMP video is only supported in visionOS. See amended requirements for visionOS.

##### About Multi Format Audio Codecs

Multi-format audio codecs support combinations of channels, audio objects, and ambisonics as opposed to multi-channel codecs that just support channels. Examples of such a multi-format codec are:

- Apple Positional Audio Codec [`APAC`](https://developer.apple.comhttps://developer.apple.com/av-foundation/Apple-Positional-Audio-Codec.pdf)
- Dolby Digital Plus JOC

##### General Authoring Requirements

A stream that matches these requirements should be compatible with iOS, tvOS, macOS or visionOS. Rules with a leading asterisk (*) are modified by one or more of the Amended Requirements listed below.

Support for a specific video Profile and Level doesn’t imply that any particular device supports the maximum bit rate for that Level.

###### Video

1. 

1.1. All video MUST be encoded using H.264/AVC, HEVC/H.265, Dolby Vision, or AV1.

1.2. The container format for H.264 video MUST be fragmented MP4 (fMP4) files or MPEG transport streams.

1.3.

1.3a. * For maximum compatibility, some H.264 variants SHOULD be less than or equal to High Profile, Level 4.1.

1.3b. * Profile and Level for H.264 MUST be less than or equal to High Profile, Level 5.2.

1.4. For H.264, you SHOULD use High Profile in preference to Main or Baseline Profile.

1.5. The container format for HEVC video MUST be fMP4.

1.6.

1.6a. * For maximum compatibility, some HEVC variants SHOULD be less than or equal to Main 10 Profile, Level 4.0, Main Tier.

1.6b. * Profile, Level, and Tier for HEVC MUST be less than or equal to Main 10 Profile, Level 5.1, High Tier.

1.7. High Dynamic Range (HDR) HEVC video MUST be HDR10, HLG, or Dolby Vision.

1.8. For HDR10 video, the `SEI NAL` units (that is, static metadata) SHOULD be in the HEVC Configuration Box (`'hvcC'`) and not in the individual sample data.

1.9. * Profile and Level for Dolby Vision MUST be Profile 5 (single layer 10-bit HEVC) and less than or equal to Level 7.

1.10. You SHOULD use video formats in which the parameter sets are stored in the sample descriptions, rather than the samples. (That is, use `'avc1'`, `'hvc1'`, or `'dvh1'` rather than `'avc3'`, `'hev1'`, or `'dvhe'`.)

1.11. For backward compatibility, content SHOULD NOT use a higher level than required by the content resolution and frame rate.

1.12. * For backward compatibility, some video content SHOULD be encoded with H.264.

1.13. Key frames (IDRs) SHOULD be present every two seconds.

1.14. All interlaced source content MUST be deinterlaced.

1.15. You SHOULD deinterlace 30i content to 60p instead of 30p.

1.16. Live (linear) video from NTSC or ATSC source SHOULD be 60 or 59.94 fps.

1.17. Live (linear) video from PAL source SHOULD be 50 fps.

1.18. Video on Demand (VOD) content SHOULD use a natural frame rate for the content. Frame rates 23.976, 24, 25, 29.97, 30, 50, 59.94, and 60 fps are supported.

1.19. Frame rates above 60 fps SHALL NOT be used.

1.20. * For HDR content, frame rates less than or equal to 30 fps SHOULD be provided.

1.21. Streams SHOULD use a single color space — one of either Rec. 601, Rec. 709, DCI-P3, or Rec. 2020.

1.22.  For VOD, the color space SHOULD be the original color space of the material.

1.23. * If multiple video streams are provided (H.264, HEVC, HDR), each stream SHOULD provide all anticipated bandwidths. Clients SHOULD NOT be required to switch codecs.

1.24. * For backward compatibility, SDR streams MUST be provided. (See also item 6.16.)

1.25. * There are many possible choices of bit rates for variants. The following tables provide one possible set of bit rate variants. (See [`On bit rates for variants`](hls-authoring-specification-for-apple-devices-appendixes#On-bit-rates-for-variants.md) for additional considerations.)

| 16:9 aspect ratio | H.264/AVC | Frame rate |
| --- | --- | --- |
| 416 x 234 | 145 | ≤ 30 fps |
| 640 x 360 | 365 | ≤ 30 fps |
| 768 x 432 | 730 | ≤ 30 fps |
| 768 x 432 | 1100 | ≤ 30 fps |
| 960 x 540 | 2000 | Same as source |
| 1280 x 720 | 3000 | Same as source |
| 1280 x 720 | 4500 | Same as source |
| 1920 x 1080 | 6000 | Same as source |
| 1920 x 1080 | 7800 | Same as source |

| 16:9 aspect ratio | HEVC/H.265 30 fps | HDR (HEVC) 30 fps | Frame rate |
| --- | --- | --- | --- |
| 640 x 360 | 145 | 160 | ≤ 30 fps |
| 768 x 432 | 300 | 360 | ≤ 30 fps |
| 960 x 540 | 600 | 730 | ≤ 30 fps |
| 960 x 540 | 900 | 1090 | ≤ 30 fps |
| 960 x 540 | 1600 | 1930 | Same as source |
| 1280 x 720 | 2400 | 2900 | Same as source |
| 1280 x 720 | 3400 | 4080 | Same as source |
| 1920 x 1080 | 4500 | 5400 | Same as source |
| 1920 x 1080 | 5800 | 7000 | Same as source |
| 2560 x 1440 | 8100 | 9700 | Same as source |
| 3840 x 2160 | 11600 | 13900 | Same as source |
| 3840 x 2160 | 16800 | 20000 | Same as source |

Following tables provide a possible bit rate recommendations for APMP videos.

###### Apmp Monoscopic Videos

| Tier | Resolution | Bit rate | Projection specifier | fps |
| --- | --- | --- | --- | --- |
| 1 | 8k x 4k | 80 Mbps | PROJ-EQUI | 60 |
| 2 | 8k x 4k | 60 Mbps | PROJ-EQUI | 60 |
| 3 | 8k x 4k | 40 Mbps | PROJ-EQUI | 60 |

If the quality of the 3rd tier is not acceptable, or you are working with very high motion content, one can lower the resolution and bitrate combination further.

| Tier | Resolution | Bit rate | Projection specifier | fps |
| --- | --- | --- | --- | --- |
| 4 | 5760 x 2880 | 60 Mbps | PROJ-EQUI | 60 |
| 5 | 5760 x 2880 | 40 Mbps | PROJ-EQUI | 60 |
| 6 | 5760 x 2880 | 30 Mbps | PROJ-EQUI | 60 |
| 7 | 4096 x 2048 | 20 Mbps | PROJ-EQUI | 60 |

###### Apmp Stereoscopic Videos

| Tier | Resolution | Bit rate | Projection specifier | fps |
| --- | --- | --- | --- | --- |
| 1 | 4k x 4k | 80 Mbps | PROJ-HEQU | 60 |
| 2 | 4k x 4k | 60 Mbps | PROJ-HEQU | 60 |
| 3 | 4k x 4k | 40 Mbps | PROJ-HEQU | 60 |

If the quality of the 3rd tier is not acceptable, or you are working with very high motion content, one can lower the resolution and bitrate combination further.

| Tier | Resolution | Bit rate | Projection specifier | fps |
| --- | --- | --- | --- | --- |
| 4 | 2880 x 2880 | 60 Mbps | PROJ-EQUI | 60 |
| 5 | 2880 x 2880 | 40 Mbps | PROJ-EQUI | 60 |
| 6 | 2880 x 2880 | 30 Mbps | PROJ-EQUI | 60 |
| 7 | 2048 x 2048 | 20 Mbps | PROJ-EQUI | 60 |

Following table provides a possible bit rate recommendations for AIV.

| Tier | Average bandwith | Peak bandwidth | Resolution | fps |
| --- | --- | --- | --- | --- |
| 1 | 100 Mbps | 150 Mbps | 4320 x 4320 | 90 |
| 2 | 80  Mbps | 120 Mbps | 4320 x 4320 | 90 |
| 3 | 50  Mbps | 100 Mbps | 4320 x 4320 | 90 |
| 4 | 32  Mbps | 64  Mbps | 4320 x 4320 | 90 |
| 5 | 25  Mbps | 50  Mbps | 4320 x 4320 | 90 |

> **Note**: The above bit rates are initial encoding targets for typical content delivered via HLS. Apple recommends that you evaluate them against your specific content and encoding workflow, then adjust accordingly. 30i source content is considered to have a source frame rate of 60 fps. 24 fps HEVC content should use bit rates reduced by about 20% from the values above.

1.26. For VOD content, the average segment bit rate MUST be within 10% of the `AVERAGE-BANDWIDTH` attribute. (See [`Declared versus measured values of bandwidths`](hls-authoring-specification-for-apple-devices-appendixes#Declared-versus-measured-values-of-bandwidths.md).)

1.27. For VOD content, the measured peak bit rate MUST be within 10% of the `BANDWIDTH` attribute.

1.28. For live (linear) content, the average segment bit rate over a long (~1 hour) period of time MUST be less than 110% of the `AVERAGE-BANDWIDTH` attribute.

1.29. For live (linear) content, the measured peak bit rate MUST be less than 125% of the `BANDWIDTH` attribute.

1.30. For VOD content, the peak bit rate SHOULD be no more than 200% of the average bit rate.

1.31. Different variants MAY have different frame rates.

1.32. * The default video variants SHOULD be the 2000 kbit/s (average bit rate) variant. (Defaults are the first variant listed in the Multivariant Playlist within a group of variants having compatible audio).

1.33. All video variants SHOULD have identical aspect ratios.

1.34. For maximum compatibility when UHD video resolution is provided, some UHD variants SHOULD be less than or equal to 15 Mbit/s.

1.35. For HDR10 content, the Mastering Display Color Volume and Content Light Level Information SEI messages SHOULD be present.

1.36. MV-HEVC video MUST NOT be used for anything other than stereo video.

1.37. Level for AV1 MUST be less than or equal to Level 6.2

1.38. All APMP monoscopic videos MUST be encoded using HEVC/H.265.

1.39. The container format for AV1 video MUST be fMP4.

###### Audio

2. 

2.1. Audio data SHOULD be provided as an elementary audio stream or in fMP4.

2.2. Codecs that provide stereo audio are:

- Apple Positional Audio Codec (APAC)
- AAC-LC
- HE-AAC v1
- HE-AAC v2
- xHE-AAC
- Apple Lossless
- FLAC

2.3. * Stereo audio in AAC, HE-AAC v1, or HE-AAC v2 format MUST be provided.

2.4. You SHOULD NOT use HE-AAC if your audio bit rate is above 64 kbit/s.

2.5. Supported multichannel audio codecs are:

- APAC
- AAC-LC
- HE-AAC v1
- Apple Lossless
- FLAC
- Dolby Digital (AC-3)
- Dolby Digital Plus (E-AC-3)(ec-3)
- Dolby Digital Plus JOC (ec+3)

(See [`Values for the CODECS attribute`](hls-authoring-specification-for-apple-devices-appendixes#Values-for-the-CODECS-attribute.md) for more information about specifying Dolby Digital Plus JOC.)

2.6. * If Dolby Digital Plus is provided and your streams are delivered to devices that don’t support Dolby Digital Plus, then Dolby Digital MUST be provided also. See [`Audio compatibility`](hls-authoring-specification-for-apple-devices-appendixes#Audio-compatibility.md).

2.7. Stereo audio MAY be provided at multiple bit rates.

2.8. * Multichannel audio using a particular codec MAY be provided at multiple bit rates.

2.9. Overall bit rate recommendations are as follows:

###### Bitrate Recommendations for Stereo Are As Follows

| Audio channels | Codec | Total (kbit/s) |
| --- | --- | --- |
| 2.0 (stereo) | APAC | 32 to 160 |
| 2.0 (stereo) | AAC | 32 to 160 |
| 2.0 (stereo) | xHE-AAC | 24 to 160 |
| 2.0 (stereo) | Dolby Digital Plus | 96 to 160 |

###### Bitrate Recommendations for Multi Channel Surround Formats Are As Follows

| Audio channels | Codec | Total (kbit/s) |
| --- | --- | --- |
| 5.1 (surround) | APAC | 320 |
| 5.1 (surround) | AAC | 320 |
| 5.1 (surround) | Dolby Digital | 384 |
| 5.1 (surround) | Dolby Digital Plus | 192 |
| 7.1 (surround) | APAC | 384 |
| 7.1 (surround) | Dolby Digital Plus | 384 |

###### Bitrate Recommendations for Ambisonics Are As Follows

| Ambisonic order | Codec | Audio coding identifier | Total (kbit/s) |
| --- | --- | --- | --- |
| 1 | APAC | 1OA | 192 to 384 |
| 2 | APAC | 2OA | 240 to 512 |
| 3 | APAC | 3OA | /270 to 768 |

See [`APAC`](https://developer.apple.comhttps://developer.apple.com/av-foundation/Apple-Positional-Audio-Codec.pdf) for more information about ambisonics.

2.10. * You MAY change channel layout within a stream.

2.11. Channel layout changes MUST be in conjunction with an `EXT-X-DISCONTINUITY` tag.

2.12. If you provide Descriptive Video Service (DVS), also called “Audio Description”, it MUST be marked with the attribute `CHARACTERISTICS="public.accessibility.describes-video"`.

2.13. If you provide DVS, the `AUTOSELECT` attribute MUST have a value of “`YES"`.

2.14. The name of DVS audio SHOULD indicate that the stream is DVS content.

2.15. If you provide alternative audio or DVS, you MUST provide it for the entire content duration, even if it only really exists for a portion of the main content.

2.16. Alternative audio or DVS MAY reuse the audio segments of regular content when the alternative content isn’t available.

2.17. A single Media Segment MUST NOT contain multiple audio streams.

2.18. Loudness management or Dynamic range control SHOULD be present unless all content (including ads) has been encoded at the same audio levels.

2.19. In fMP4 files, except for the APAC codec, you SHOULD provide loudness information by way of a loudness box (’`ludt`’). When present, the loudness box takes precedence over any loudness information in the audio stream. For APAC, a loudness box SHALL not be used.

2.20. In the absence of a loudness box, Dolby Digital and Dolby Digital Plus loudness SHOULD be specified by the `dialnorm` field (ATSC A/52:2012). 

2.21. For AAC, in the absence of a loudness box, AAC dialog loudness SHOULD be specified by either AAC `prog_ref_level` (ISO 14496-3 subclause 4.5.2.7), as specified by SCTE 193-1 section 7.4.1, or by the `loudnessInfo()` payload as specified by ISO 23003-4, in which case, `samplePeakLevel` or `truePeakLevel` MUST be present, `measurementSystem` MUST be 2, and `methodDefinition` MUST be 1 or 2, while for video content it SHOULD be 2.

2.22. For xHE-AAC, loudness metadata MUST be present according to the Basic Loudness Metadata specified in ISO 23003-4 Table I.5; `samplePeakLevel` or `truePeakLevel` MUST be present. The `methodDefinition` SHOULD be 2 for video content.

2.23. The loudness value MUST indicate the actual loudness of the content.

2.24. HE-AAC in fMP4 files MUST use explicit signaling of SBR data.

2.25. The container format for xHE-AAC, Apple Lossless, FLAC, and APAC audio MUST be fMP4.

2.26. If you provide non-Dolby multichannel audio, you SHOULD provide multichannel AAC also.

2.27. For audio description, the LANGUAGE attribute MUST be present and indicate the primary language used to convey the descriptions.

2.28. Audio that has been prepared or otherwise processed to heighten the intelligibility of speech MAY be marked with the attribute `CHARACTERISTICS="public.accessibility.enhances-speech-intelligibility"`.

2.29. Supported multi-format audio codecs that carry the combination of two or more formats out of channels, objects and Ambisonics are:

- APAC
- Dolby Digital Plus JOC

2.30. APAC encoded content MUST have in-stream loudness and DRC metadata.

2.31. If you provide APAC immersive audio, you SHOULD provide stereo AAC also.

###### Ads and Pre Mid Post Rolls

3.  (See also the Media Playlists section of [`HTTP Live Streaming (HLS) authoring specification for Apple devices`](hls-authoring-specification-for-apple-devices.md).)

3.1. Your ads and other nonprimary media MAY be inserted in the Media Playlists or as Interstitials.

3.2. Inserted media SHOULD be encoded with the same codecs as the other content in the Media Playlist.

3.3. Inserted media SHOULD be encoded with the same aspect ratio as the other content in the Media Playlist.

3.4. Inserted media SHOULD be at or under the specified bandwidths for that variant.

###### Accessibility

4. 

4.1. Captions SHOULD be provided with your streams to make content accessible to people who are deaf or hard of hearing.

4.2. Supported caption formats are:

- CEA-608 closed captions
- CEA-708 closed captions
- WebVTT subtitles
- IMSC1 subtitles (text profile only)

4.3. Closed captions (if any) MUST be included in the video Media Segments.

4.4. The presence of closed captions MUST be declared via an `EXT-X-MEDIA` tag that contains a `LANGUAGE` attribute.

4.5. If a subtitles track is intended to provide accessibility for people who are deaf or hard of hearing, it MUST be marked with the attribute `CHARACTERISTICS="public.accessibility.transcribes-spoken-dialog,public.accessibility.describes-music-and-sound"`. (Subtitles with this attribute value are treated the same as closed captions.)

4.6. If a subtitles track is intended to provide accessibility for people who are deaf or hard of hearing, the `AUTOSELECT` attribute MUST have a value of `"YES"`.

4.7. The `LANGUAGE` attribute MUST be included in the `EXT-X-MEDIA` tag for a subtitles track.

4.8. For information on including audio descriptions with your streams, see items 2.12 through 2.16.

###### Subtitles

5. 

5.1. Subtitles MAY be provided.

5.2. * Subtitles MUST be WebVTT (according to the HLS specification) or IMSC1 in fMP4.

5.3. WebVTT subtitles MUST be in text files, with an `X-TIMESTAMP-MAP` according to the HLS specification.

5.4. IMSC1 subtitles MUST be in fMP4 files.

5.5. The subtitle playlist MUST exist for the entirety of the main content, even if the actual subtitles only exist for a portion of the content.

5.6. For live (linear) content, target durations for subtitle playlists MUST be identical to other media.

5.7. For VOD content, target durations of subtitle playlists MAY be longer than the other media.

5.8. If the content has forced subtitles and regular subtitles in a given language, the regular subtitles track in that language MUST contain both the forced subtitles and the regular subtitles for that language.

5.9. If your videos contain text burnt into the video and you have access to a version without the burn-in, you SHOULD use forced subtitles instead. (This allows you to easily translate into multiple languages. An example of when you might use forced subtitles is a science fiction film, where alien languages are translated into English.)

5.10. The kind of subtitles SHOULD be specified in the `CODECS` attribute of the associated `EXT-X-STREAM-INF` tags. You SHOULD use `"stpp.ttml.im1t"` to identify IMSC1 subtitles. You MAY use `"wvtt"` to identify WebVTT subtitles.

5.11. Forced subtitles SHOULD always have `AUTOSELECT=YES`.

###### Trick Play

6. 

6.1. I-frame playlists (`EXT-X-I-FRAME-STREAM-INF`) MUST be provided to support scrubbing and scanning UI.

6.2. You SHOULD have one frame per second  I-frame renditions. These are dedicated renditions that only contain I-frames.

6.3. Alternatively, you MAY use the I-frames from your normal content, but trick play performance is improved with a higher density of I-frames.

6.4. If you provide multiple bit rates at the same spatial resolution for your regular video, you SHOULD create the I-frame playlist for that resolution from the same source used for the lowest bit rate in that group.

6.5. The bit rate of I-frame playlists SHOULD be the bit rate of a normal playlist of the same resolution times the fps of the I-frame playlist divided by eight. (See [`I-frame bit rates versus normal bit rates`](hls-authoring-specification-for-apple-devices-appendixes#I-frame-bit-rates-versus-normal-bit-rates.md).)

6.6. * You SHOULD provide multiple I-frame Media Playlists with different bit rates.

6.7. As with normal video, there are many possible choices of bit rates for dense I-frame variants. The following tables provide one possible set of variants. (See [`On bit rates for variants`](hls-authoring-specification-for-apple-devices-appendixes#On-bit-rates-for-variants.md).)

| 16:9 aspect ratio | H.264/AVC |
| --- | --- |
| 640 x 360 | 45 |
| 768 x 432 | 90 |
| 960 x 540 | 250 |
| 1280 x 720 | 375 |
| 1920 x 1080 | 580 |

| 16:9 aspect ratio | HEVC/H.265 | HDR (HEVC) |
| --- | --- | --- |
| 768 x 432 | 40 | 55 |
| 960 x 540 | 75 | 94 |
| 960 x 540 | 200 | 238 |
| 1280 x 720 | 300 | 360 |
| 1920 x 1080 | 525 | 650 |

> **Note**: These bit rates are based on the assumption of a 1 fps dense I-frame track. The values should be modified based on the actual frame rate of the I-frame rendition. (See item 6.5.) The above tables are average bit rates. Earlier versions of this specification used peak bit rates.

6.8. I-frame playlists MUST contain the `EXT-X-I-FRAMES-ONLY` tag.

6.9. The peak segment bit rate MUST be calculated according to the HLS specification.

6.10. If using fMP4, I-frame segments MUST include the ‘moof’ header associated with the I-frame.

6.11. For live (linear) content, target durations for I-frame playlists MUST be identical to other media.

6.12. For VOD content, target durations of I-frame playlists MAY be different from the other media.

6.13. * I-frame playlists MAY use a different video codec than the normal video segments.

6.14. * For backward compatibility, some trick play content SHOULD be encoded with H.264.

6.15. If HDR trick play streams are provided, they SHOULD be provided at all resolutions.

6.16. * For backward compatibility, SDR trick play streams MUST be provided.

6.17. I-frame content MAY be encoded using the fMP4 ‘mjpg’ codec. (See [`I-frame image sequences`](hls-authoring-specification-for-apple-devices-appendixes#I-frame-image-sequences.md).)

###### Media Segmentation

7. 

7.1. Your media MUST be continuous across segments, with the exception of transitions for ads and other inserted material.

7.2. If using a transport stream, continuity counters and timestamps MUST be sequential.

7.3. If using fMP4, the track fragment decode time MUST be consistent with the decode time and duration of the previous segment.

7.4. Video segments MUST start with an IDR frame.

7.5. Target durations SHOULD be 6 seconds.

7.6. Segment durations SHOULD be nominally 6 seconds (for example, NTSC 29.97 may be 6.006 seconds).

7.7. Media Segments MUST NOT exceed the target duration by more than 0.5 seconds.

7.8. Each xHE-AAC segment SHOULD start with an Immediate Playout Frame (IPF).

7.9. Each APAC segment MUST start with an Audio Synchronization Packet (ASP).

###### Media Playlists

8. 

8.1. You MUST use sufficiently accurate segment durations to ensure that the sum of the `EXTINF` durations of any contiguous group of segments is within one video frame duration of the actual duration of the content.

8.2. Audio and video playlists MUST all use the same target duration.

8.3. Audio and video playlists MUST contain the same duration of the content.

8.4. The `EXT-X-PROGRAM-DATE-TIME` tag MUST be present in every live (linear) Media Playlist.

8.5. The date-time value of an `EXT-X-PROGRAM-DATE-TIME` tag SHOULD be aligned with the airtime of the content.

8.6. If your Media Playlists are created from static source content (VOD), you MUST add the `EXT-X-PLAYLIST-TYPE` with the value `VOD`.

8.7. Within one asset, all Media Playlists with an `EXT-X-PLAYLIST-TYPE` of `VOD` MUST cover exactly the same media time range.

8.8. If your Media Playlists are event style (start from a fixed point with segments never removed), you MUST add the `EXT-X-PLAYLIST-TYPE` with the value `EVENT`.

8.9. Separate audio streams MUST be declared using `EXT-X-MEDIA` tags.

8.10. The `LANGUAGE` attribute MUST be included in every `EXT-X-MEDIA` tag that doesn’t have `TYPE=VIDEO`.

8.11. You MUST provide at least six segments in a live (linear) playlist.

8.12. * You SHOULD provide at least 15 minutes of content in a live (linear) playlist.

8.13. Breaks of encoding continuity MUST be indicated with the `EXT-X-DISCONTINUITY` tag.

8.14. Video frame rate changes MUST be marked as a discontinuity using `EXT-X-DISCONTINUITY` tags.

8.15. All variants and renditions MUST have discontinuities at the same points in time.

8.16. * You SHOULD avoid switching codecs at discontinuities, for example, switching between HEVC and H.264, or between AAC and Dolby Digital.

8.17. If live (linear) content will ever contain an `EXT-X-DISCONTINUITY` tag, the `EXT-X-DISCONTINUITY-SEQUENCE` tag MUST always be present.

8.18. Your media requests MUST NOT use HTTP redirects, with the exception of ad content to allow dynamic selection of ads.

8.19. You SHOULD identify interstitial and program boundaries using the `EXT-X-DATERANGE` tag.

8.20. If using fMP4, `EXT-X-MAP` tags MUST be present.

8.21. Metadata SHOULD be in the playlist (using `EXT-X-DATERANGE`) rather than in the media (using Timed Metadata).

8.22. * For maximum interoperability, all audio/video variants and renditions SHOULD have segment boundaries at the same points in time.

8.23. If your xHE-AAC segments start with an IPF, you SHOULD use the `EXT-X-INDEPENDENT-SEGMENTS` tag in the Media Playlist.

8.24. A live (linear) playlist update SHOULD be considered invalid when the Last-Modified HTTP header, if supplied, is more than three target durations from the Date HTTP header.

8.25. If your APAC segments start with an ASP, you SHOULD use the `EXT-X-INDEPENDENT-SEGMENTS` tag in the Media Playlist.

###### Multivariant Playlist

9. 

9.1. Your `EXT-X-STREAM-INF` tag MUST always provide the `CODECS` attribute.

9.2. Your `EXT-X-STREAM-INF` tag MUST always provide the `RESOLUTION` attribute if the rendition includes video.

9.3. Your `EXT-X-I-FRAME-STREAM-INF` tag MUST always provide the `CODECS` attribute.

9.4. Your `EXT-X-I-FRAME-STREAM-INF` tag MUST always provide the `RESOLUTION` attribute.

9.5. You SHOULD deliver video and audio as separate streams.

9.6. If you have multichannel audio, you MUST use separate audio streams.

9.7. If you have alternative audio content (languages/commentary/DVS), you MUST use separate audio streams.

9.8. If you have different video angles, you MUST use separate audio streams.

9.9. You MUST provide multiple bit rates of video (that is, variants).

9.10. For HD content, there SHOULD be at least two variants encoded at the highest-available resolution.

9.11. If your video segments start with an IDR, you SHOULD use the `EXT-X-INDEPENDENT-SEGMENTS` tag in the Multivariant Playlist. (See item 7.4.)

9.12. If your video segments start with an IDR and the `EXT-X-INDEPENDENT-SEGMENTS` tag isn’t in the Multivariant Playlist, you MUST use the `EXT-X-INDEPENDENT-SEGMENTS` tag in all video Media Playlists. (See item 7.4.)

9.13. The `BANDWIDTH` attribute MUST be the largest sum of peak segment bit rates that’s produced by any playable combination of renditions.

9.14. You MUST include the `AVERAGE-BANDWIDTH` attribute.

9.15. Each `EXT-X-STREAM-INF` tag that includes video content MUST have a `FRAME-RATE` attribute.

9.16. The `VIDEO-RANGE` attribute MUST be specified unless all variants and renditions are SDR.

9.17. Within a group of Renditions (`EXT-X-MEDIA` tags having the same `TYPE` and `GROUP-ID`), those tags having the same `LANGUAGE` value should be ordered from most general to most specific. (Because `CHARACTERISTICS` are open-ended, the matching algorithm needs the ordering since it can’t interpret all the semantics.)

9.18. An `EXT-X-CONTENT-STEERING` tag SHOULD always have a `PATHWAY-ID` attribute.

9.19. The `SCORE` attribute (if present) MUST be on every variant. Otherwise, the `SCORE` attribute will be ignored.

9.20. For APAC, the APAC profile and level MUST be provided as a part of Codec string. See [`APAC`](https://developer.apple.comhttps://developer.apple.com/av-foundation/Apple-Positional-Audio-Codec.pdf) for more information about APAC profile and level.

###### Delivery

10. 

10.1. The server MUST deliver playlists using `gzip` content-encoding.

10.2. You SHOULD support stream failover, for example by listing duplicate streams in the Multivariant Playlist.

10.3. Media data SHOULD NOT be delivered to the application through a local server.

10.4. You SHOULD use the recommended MIME types for content. The recommendations are in the following table:

| Media type | Format | Recommended MIME type | Typical file extension |
| --- | --- | --- | --- |
| Playlist | HLS playlist | `application/vnd.apple.mpegurl` | `m3u8` |
| Playlist | M3U playlist | `audio/mpegurl` | `m3u` |
| Video | MPEG transport stream | `video/mp2t` | `ts` |
| Media Initializaton | Fragmented MP4 | `video/mp4` | mp4 |
| Video or audio | Fragmented MP4 | `video/iso.segment` | m4s |
| Video | Fragmented MP4 | `video/mp4` | `mp4` |
| Audio | MPEG transport stream | `video/mp2t` | `ts` |
| Audio | Fragmented MP4 | `audio/mp4` | `mp4` |
| Audio | Packed audio | `audio/aac` | `aac` |
| Audio | Packed audio | `audio/mpeg` | `mp3` |
| Audio | Packed audio | `audio/ac3` | `ac3` |
| Audio | Packed audio | `audio/eac3` | `ec3` |
| Subtitles | WebVTT | `text/vtt` or `text/plain` | `vtt` |
| Subtitles | IMSC1 | `application/mp4` | `mp4` |
| Content Steering Manifest | JSON file | `application/vnd.apple.steering-list` | json |
| `X-ASSET-LIST` response | JSON file | `application/json` | json |

> **Note**: The M3U playlist MIME type `audio/mpegurl` isn’t registered with the IANA. According to the IANA, the `audio/aac` MIME type allows LATM/LOAS or ADTS. HLS only supports ADTS. Some older players are known to reject `text/vtt` as an illegal type. For compatibility, `text/plain` is acceptable.

###### Privacy

> **Note**: In a future release, Apple may require delivery over TLS.

11. 

11.1. Multivariant Playlists SHOULD be delivered using Transport Layer Security (TLS).

11.2. Media Playlists SHOULD be delivered using TLS.

11.3. Media Segments SHOULD be delivered using TLS.

11.4. Media Segment URLs requested over unencrypted transport SHOULD NOT contain revealing strings, such as movie title, show title, episode name, episode number, genre, advertiser, or product.

###### Security

12. 

12.1. Transport Layer Security (TLS) MUST be version 1.2 or later with forward secrecy.

12.2. TLS MUST NOT use known-insecure cryptographic primitives (such as, RC4 encryption, SHA-1 certificate signatures).

12.3. Within TLS, key sizes MUST be 2048 bits for RSA and 256 bits for EC.

12.4. The URLs for Media Segments SHOULD NOT be completely static. URLs should be issued per device or changed over time.

###### Content Protection

13. 

13.1. Content protection of video and audio SHOULD follow the FairPlay Streaming (FPS) specification.

13.2. If the content is encrypted with FPS, the method MUST be `SAMPLE-AES`.

13.3. If the content is encrypted with FPS, the key format MUST be `"com.apple.streamingkeydelivery"`.

13.4. The `IV` attribute SHOULD NOT be used with FPS unless necessary for interoperability.

13.5. Content with `HD` resolutions SHOULD use `HDCP-LEVEL` of `TYPE-0`.

13.6. Content with greater than `HD` resolutions SHOULD use `HDCP-LEVEL` of `TYPE-1`.

13.7. Video encrypted with Common Encryption MUST use an `encrypt:skip` pattern of 1:9 (10% partial encryption).

13.8. Content encrypted with FPS MAY use the `ALLOWED-CPC` attribute. (See [`ALLOWED-CPC values for FairPlay Streaming`](hls-authoring-specification-for-apple-devices-appendixes#ALLOWED-CPC-values-for-FairPlay-Streaming.md).)

13.9. Common encryption MUST NOT use content sensitive encryption.

13.10. Content authors MAY mix encrypted and unencrypted samples in a single HLS fMP4 segment with a single Media Initialization Section by supplying both an encrypted SampleDescription at index 0 and an unencrypted SampleDescription at index 1 for each track. The sample index field of each sample should point to the appropriate SampleDescription.

13.11. Encryption with `SAMPLE-AES-CTR` SHALL NOT be used on Apple devices.

> **Note**: HD is approximately the range of 720p to 1080p.

###### Low Latency Hls

14. 

14.1. Low-Latency stream delivery MUST meet all requirements of the Low-Latency Server Configuration Profile in Appendix B of [`draft-pantos-hls-rfc8216bis-07`](https://developer.apple.comhttps://tools.ietf.org/html/draft-pantos-hls-rfc8216bis-07) or later.

14.2.

14.2a. The Part Target Duration MUST be at least the maximum round-trip time (RTT) to the server that 95% of the clients are expected to see (P95 RTT).

14.2b. The Part Target Duration SHOULD be at least three times the P95 RTT.

14.2c. The RECOMMENDED Part Target Duration is one second.

14.3. The `PART-HOLD-BACK` value MUST be at least three times the Part Target Duration.

14.4. Services with Playlist windows longer than two minutes SHOULD offer Playlist Delta Updates.

14.5. Services that offer Playlist Delta Updates and use `EXT-X-DATERANGE` tags SHOULD also use `CAN-SKIP-DATERANGES=YES`.

###### Shareplay

> **Note**: Other requirements only apply to the playlists and media received by a single client. SharePlay adds requirements that apply to all participants in the SharePlay session.

15. 

15.1. For live (linear) content, the timeline derived from the EXT-X-PROGRAM-DATE-TIME tag is used for synchronization. That timeline MUST be in agreement for all participants.

15.2. For VOD content, the timeline based on the start of the playlist is used for synchronization. That timeline MUST be in agreement for all participants.

15.3. Interstitials delivered to participants in a SharePlay session SHOULD match in duration. If they do not, participants receiving longer duration interstitials will miss some of the primary content. This behavior can only be overridden when all participants are using apps that support control of coordinated media playback.

###### Spatial Stereo Immersive and Projected Video

> **Note**: Please see [`About spatial video`](hls-authoring-specification-for-apple-devices#About-spatial-video.md) for information regarding Spatial Video.

16. 

16.1. All variants containing spatial video MUST be marked with a REQ-VIDEO-LAYOUT attribute.

16.2. All spatial video content MUST include Video Extended Usage (`'vexu'`) atoms/boxes. (See [`Additional spatial video specifications`](hls-authoring-specification-for-apple-devices-appendixes#Additional-spatial-video-specifications.md).)

16.3. Switches between spatial and non-spatial video content MUST be marked with an EXT-X-DISCONTINUITY tag, or the Media Initialization Section MUST contain sample descriptions for both kinds of content.

16.4. Stereo and Immersive video content SHOULD include parallax metadata if your content has subtitles. (See [`Additional spatial video specifications`](hls-authoring-specification-for-apple-devices-appendixes#Additional-spatial-video-specifications.md).)

16.5. If spatial video content includes sections of monoscopic video content, then the REQ-VIDEO-LAYOUT attribute MUST include “CH-MONO” as one entry.

##### Amended Requirements for Macos

All general rules apply except as expressly modified by a rule with the same number in this section. Rules with a leading plus sign (+) are additional rules.

###### Video

1. 

1.3.

1.3b. Profile and Level for H.264 MUST be less than or equal to High Profile, Level 5.0.

##### Amended Requirements for Ios

All general rules apply except as expressly modified by a rule with the same number in this section. Rules with a leading plus sign (+) are additional rules.

###### Video

1. 

1.6.

1.6b. Profile and Level for H.264 MUST be less than or equal to High Profile, Level 6.0.

1.9.

1.9a. Profile and Level for Dolby Vision MUST be Profile 5 (single layer 10-bit HEVC) or Profile 10 (single layer 10-bit AV1) and less than or equal to Level 9.

1.9b. + For maximum compatibility, some Dolby Vision variants SHOULD be Profile 5 and less than or equal to Level 7.

1.32.

1.32a. For Wi-Fi delivery, the default video variant SHOULD be the 2000 kbit/s (average bit rate) variant.

1.32b. For cellular delivery, the default video variant SHOULD be the 730 kbit/s (average bit rate) variant.

###### Multivariant Playlist

9. 

9.21. + Multivariant Playlists that are delivered over cellular networks MUST contain a variant whose peak `BANDWIDTH` is less than or equal to 192 kbit/s.

9.22. + For backward compatibility, a peak 192 kbit/s H.264 variant packaged in a transport stream SHOULD be provided for cellular.

##### Amended Requirements for Visionos

All general rules apply except as expressly modified by a rule with the same number in this section. Rules with a leading plus sign (+) are additional rules.

The following general rules regarding compatibility aren’t applicable in visionOS if all variants contain stereo video content: 1.3a, 1.6a, 1.9b, 1.12, 1.24, 2.3, 2.6, 6.14, 6.16.

###### Video

1. 

1.9.

1.9a. Dolby Vision monoscopic content MUST be Profile 5 (single layer 10-bit HEVC) and less than or equal to Level 9.

1.9c. + Dolby Vision stereo video MUST be Profile 20 (MV-HEVC) and less than or equal to Level 9.

1.25. Suggested bit rates for MV-HEVC variants.

| 16:9 aspect ratio | MV-HEVC SDR 30 fps | MV-HEVC HDR 30 fps | Frame rate |
| --- | --- | --- | --- |
| 640 x 360 | 246 | 272 | ≤ 30 fps |
| 768 x 432 | 510 | 612 | ≤ 30 fps |
| 960 x 540 | 1020 | 1241 | ≤ 30 fps |
| 960 x 540 | 1530 | 1853 | ≤ 30 fps |
| 960 x 540 | 2720 | 3281 | Same as source |
| 1280 x 720 | 4080 | 4930 | Same as source |
| 1280 x 720 | 5780 | 6936 | Same as source |
| 1920 x 1080 | 7650 | 9180 | Same as source |
| 1920 x 1080 | 9660 | 11900 | Same as source |
| 2560 x 1440 | 13770 | 16490 | Same as source |
| 3840 x 2160 | 19720 | 23630 | Same as source |
| 3840 x 2160 | 28560 | 34000 | Same as source |

1.40. + Stereo video MUST be encoded using Dolby Vision Profile 20 (MV-HEVC).

###### Trick Play

6. 

6.6. If your only content is stereo video, then you SHOULD provide only one I-frame Media Playlist. (See item 6.19.)

6.18. + Trick play content SHOULD be monoscopic and rectilinear.

6.19. + In visionOS, a thumbnail list is produced for scrubbing and scanning. These thumbnails are 160px height with a width that matches the aspect ratio of the main content. For better performance, you MAY provide an I-frame playlist having exactly this height.

###### Spatial Stereo Immersive and Projected Video

16. 

16.6. + All Stereo (including APMP) video MUST be encoded using MV-HEVC.

16.7. + Immersive video content MUST use CH-STEREO and PROJ-AIV for channel and projection specifier in REQ-VIDEO-LAYOUT.

##### Amended Requirements for Tvos

All general rules apply except as expressly modified by a rule with the same number in this section. Rules with a leading plus sign (+) are additional rules.

###### Video

1. 

1.3.

1.3b. Profile and Level for H.264 MUST be less than or equal to High Profile, Level 5.1.

1.20. For HDR content, frame rates less than or equal to 30 fps MUST be provided.

1.25. The 145 kbit/s variant SHOULD NOT be provided.

###### Audio

2. Audio encoding requirements

2.8. Multichannel audio using a particular codec MAY be provided at multiple bit rates. However, Dolby Atmos content SHOULD be restricted to a single bit rate.

###### Trick Play

6. 

6.16. SDR trick play streams MUST be provided.

###### Media Playlists

8. 

8.12. You SHOULD provide at least 120 minutes of content in a live (linear) playlist.

###### Multivariant Playlist

9. 

9.20. + You MUST have no audio-only variants listed in the Multivariant Playlist.

##### Amended Requirements for Airplay 2 Enabled Tvs

All general rules apply except as expressly modified by a rule with the same number in this section. Rules with a leading plus sign (+) are additional rules.

> **Note**: AirPlay on older third-party TVs does  support the Sample Group Description Box (`'sgpd'`) and Sample to Group Box (`'sbgp'`) for encrypted content. You must remove them from encrypted CMAF content to enable playback.

###### Video

1. 

1.23. If multiple video streams are provided (H.264, HEVC, HDR), each stream MUST provide all anticipated bandwidths.

1.41. + Encrypted fMP4 content MUST contain either a Sample Encryption Box (`'senc'`), or both a Sample Auxiliary Information Sizes Box (`'saiz'`) and a Sample Auxiliary Information Offsets Box (`'saio'`).

###### Audio

2. 

2.10. Channel layout SHOULD NOT change within a stream.

###### Ads and Pre Mid Post Rolls

3. 

3.5. + Inserted media SHOULD be at a similar frame rate (x, 2x, x/2) as the other content in the Media Playlist.

###### Subtitles

5. 

5.2. Subtitles MUST be WebVTT.

###### Trick Play

6. 

6.13. If a normal video variant uses a video codec, one or more I-frame variants MUST exist with the same video codec or the `mjpg` codec.

###### Media Playlists

8. 

8.16. You SHOULD NOT switch codecs at discontinuities. For example, don’t switch between HEVC and H.264, or between AAC and Dolby Digital.

8.22. All video variants and renditions MUST have segment boundaries at the same points in time.

8.25. + Frame rate changes at discontinuities SHOULD use a similar frame rate (x, 2x, x/2).

###### Multivariant Playlist

9. 

9.23. + You SHOULD provide a full range of variants for each codec type and frame rate. Similar frame rates (x, 2x, x/2) are compatible, nonsimilar frame rates may cause playback issues.

9.24. + If you supply HDR content, you SHOULD provide both Dolby Vision and HDR10.

##### Revision History

The following table describes the changes to this document.

| Date | Notes |
| --- | --- |
| 2025-06-26 | Fixed malformed URLs. |
| 2025-06-24 | Added container format rule for AV1. |
| 2025-05-08 | Added AIV bit-rate tiers. |
| 2025-05-02 | Added Offline download guidelines. |
| 2025-04-30 | Added APAC authoring guidelines. |
| 2025-04-18 | Added Spatial (Stereo, APMP and AIV) authoring guidelines. |
| 2025-03-25 | Clarified use of DV20 for Stereo video for VisionOS. |
| 2023-05-24 | Minor changes. |
| 2023-08-15 | Added visionOS requirements. Added note about audio/aac. |
| 2023-06-27 | Added stereo video rules and MV-HEVC bit rate. |
| 2023-05-19 | Added detail about I-frame image sequences. |
| 2022-08-22 | Added “Audio rendition groups and variants” section to the appendix, clarified language around the LANGUAGE attribute, and added additional information about Apple TV and Dolby ATMOS. |
| 2021-11-12 | Renamed “primary playlist” to “Multivariant Playlist.” |
| 2020-06-22 | Added new sections: Low-Latency HLS and ALLOWED-CPC Values for FairPlay Streaming. |
| 2019-06-03 | Added new table describing MIME types. |
| 2019-03-04 | Added new rules for Airplay 2-enabled TVs. Moved appendixes into child article. |
| 2018-09-11 | Added new rules for content protection and media playlists. |
| 2018-06-18 | Added Dolby Digital Plus with Dolby Atmos information. Added codec value section. |
| 2018-04-09 | Made several minor changes to individual spec points. Updated the variant bit rate table and broke it into two separate tables. |
| 2018-01-16 | Fixed several typos and made a couple of minor changes to audio encoding requirements. |
| 2017-09-19 | Updated document with HDR (HEVC) information. |
| 2017-06-06 | Updated document with HEVC/H.265 information. |
| 2016-09-13 | Added rules for fragmented MP4 files. |
| 2016-06-13 | Updated for iOS and macOS specifications. |
| 2016-03-21 | Updated Dolby Digital bit rate recommendation to 384 kbit/s. |
| 2016-01-11 | Fixed typo in section 10.2. |
| 2015-12-17 | Added section on using the `hlsreport` tool. |
| 2015-12-08 | Corrected a mistake in Table 2-3, Column 2 heading. Changed to 16:9 aspect from 19:0. |
| 2015-10-21 | Published the first edition of this document describing the HTTP Live Streaming specifications for audio and video content delivery for Apple TV. |

## Topics

### Appendixes
- [HTTP Live Streaming (HLS) Authoring Specification for Apple devices appendixes](hls-authoring-specification-for-apple-devices-appendixes.md)
  Learn additional information related to the HLS Authoring Specification for Apple Devices.

## See Also

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

*[View on Apple Developer](https://developer.apple.com/documentation/http-live-streaming/hls-authoring-specification-for-apple-devices)*