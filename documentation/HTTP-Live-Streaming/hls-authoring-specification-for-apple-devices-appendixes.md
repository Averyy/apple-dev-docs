# HTTP Live Streaming (HLS) Authoring Specification for Apple devices appendixes

**Framework**: HTTP Live Streaming

Learn additional information related to the HLS Authoring Specification for Apple Devices.

#### Overview

The appendixes in this article expand on information provided in the [`HTTP Live Streaming (HLS) authoring specification for Apple devices`](hls-authoring-specification-for-apple-devices.md). It is not intended as a standalone document.

##### Testing Your Streams

Apple provides several command-line tools for HTTP Live Streaming at [`https://developer.apple.com/download/all`](https://developer.apple.comhttps://developer.apple.com/download/all). After signing in with your Apple Developer account, search for .

To assist in validating your streams, use the command-line tools `mediastreamvalidator` and `hlsreport`. While these tools are unable to check everything about your streams, the checks they do are fairly comprehensive and Apple continues to improve the tools.

Check the video quality of your streams by visual inspection. The `mediastreamvalidator` tool does not check video quality, so check playback of your streams under a variety of network conditions.

##### Using Hlsreport

Use the binary `hlsreport` to generate an HTML summary report from a JSON file that `mediastreamvalidator` creates. The report includes several tables with details about variants, renditions, and I-frame variants. Each table entry has a unique stream ID number. A list of issues is included, divided into Must Fix and Should Fix categories according to this specification. The issues cross-reference individual variants and renditions using the unique stream IDs.

> **Note**: Earlier versions of the HLS tools used a script called `hlsreport.py` rather than a binary.

Earlier versions of the HLS tools used a script called `hlsreport.py` rather than a binary.

The simplest way to call it is:

`		hlsreport validation_data.json`

where `validation_data.json` is the JSON file that `mediastreamvalidator` generates. This produces a file called `validation_data.html` that is the report. You can change the name of the report file with the `-o` option:

`		hlsreport -o my_report.html validation_data.json`

For further information, see the `hlsreport(1)` man page.

##### Declared Versus Measured Values of Bandwidths

VOD bit rates are measured over the entirety of the content. Live (linear) bit rates are measured over ~1 hour of content.

|  | VOD | Live/Linear |
| --- | --- | --- |
| Measured average bit rate versus AVERAGE-BANDWIDTH (attribute) | within 10% of attribute value | < 110% of attribute value |
| Measured peak bit rate versus BANDWIDTH (attribute) | within 10% of attribute value | < 125% of attribute value |
| Measured peak bit rate versus measured average bit rate | < 200% of measured average | no rule |

##### Audio Compatibility

Additional information about device and audio format compatibility.

> **Note**: Multichannel output depends on the capability of the actual output device.

Multichannel output depends on the capability of the actual output device.

| Devices | AAC (Stereo) | AC-3/E-AC-3 | Dolby Digital Plus with Dolby Atmos |
| --- | --- | --- | --- |
| iOS devices - A12 Bionic based and later | Yes | Yes | Yes |
| Apple TV 4K (1st and 2nd Gen)† | Yes | Yes | Yes |
| OS X devices - 2018 and later | Yes | Yes | Yes |
| iOS and tvOS devices - A7-based or later *, but not listed above | Yes | Yes | Plays as E-AC-3 |
| Older OS X devices | Yes | Yes | Plays as E-AC-3 |
| Apple TV (3rd Gen), iPhone 5, and iPhone 5C | Yes | Only AC-3 via pass-through | No |
| All older iOS and tvOS devices | Yes | No | No |

> **Note**: All of the devices in the above table support AAC (Stereo).

All of the devices in the above table support AAC (Stereo).

See [`https://support.apple.com/specs/`](https://developer.apple.comhttps://support.apple.com/specs/) for actual technical specifications.

*Complete support requires iOS 9.3 or tvOS 9.2, or later. Dolby Digital Plus with Dolby Atmos requires tvOS 12.0 or later.

Dolby Digital Plus with Dolby Atmos† requires tvOS 12.0 or later.

##### On Bit Rates for Variants

A number of factors affect the bit rate needed to encode video:

- Codec (for example, H.264 or HEVC)
- Specific encoder implementation and features used
- Resolution (for example, 1920 x 1080, 1280 x 720, and so on)
- Frame rate (for example, 24, 25, 30, 50, 60)
- Bits per pixel (for example, HDR typically uses more bits than SDR)
- Complexity of the content
- Desired subjective quality

These factors make universal encoding recommendations for content difficult. [`HTTP Live Streaming (HLS) authoring specification for Apple devices`](hls-authoring-specification-for-apple-devices.md) includes initial bit rate recommendations that you can evaluate against your content, constraints and encoding workflow.

##### I Frame Bit Rates Versus Normal Bit Rates

The formula in item 6.5 (for I-frame bit rates) in [`HTTP Live Streaming (HLS) authoring specification for Apple devices`](hls-authoring-specification-for-apple-devices.md) requires some explanation.

During trick play, the player tries to deliver eight frames per second. If the playback rate implies a higher frame rate, frames will be dropped to keep the frame rate at eight frames per second. If fewer frames are available, it will play at a lower frame rate.

The I-frame bit rate is the bit rate of the rendition if it were played at normal speed. The I-frame rendition may be 2 fps, 1 fps, 0.5 fps, 0.2 fps, or something else. Let F be the frame rate of the I-frame rendition. Then, 8/F is the multiplier, that is, how much the bit rate is increased by playing the rendition at eight frames per second. The bit rate doesn’t increase by more than this factor because the player can’t play more than eight frames per second.

The I-frame rendition should have an effective bit rate similar to the normal content. So the normal bit rate divided by the multiplier should be the bit rate for the I-frame. Dividing by a fraction is the same as multiplying by its inverse, so the result is 6.5 — the bit rate of a normal playlist of the same resolution times the fps of the I-frame playlist divided by eight.

##### I Frame Image Sequences

I-frame image sequences using the `mjpg` codec have been added to support some third-party devices. The sequences should be low bandwidth and require minimal processing. Players should prefer video I-frame variants over image sequences.

The recommendations for image sequences are as folows:

- Supply a single `mjpg` variant
- Unencrypted
- 400 pixels wide with height based on the aspect ratio
- One key-frame every 1 to 2 seconds
- Bandwidth should be reasonable for the resolution based on the codec implementation

##### Audio Rendition Groups and Variants

In building up a multivariant playlist, the first step is to choose your video resolutions and codecs. These are your basic variants. Each one will have a video media playlist. The playlist URI may be repeated in multiple `EXT-X-STREAM-INF` tags so that the same video can be associated with different audio content.

You will have some some set of audio languages and codecs. A particular codec may be in stereo, in 5.1 sound, or both. Create one audio group for each pair of codec and channel count. Each group needs to have every language in it.

When you’re making audio groups, there are some things to remember. First, ensure you have a stereo AAC group. This is good fallback because it’s something all devices can play. If you have multichannel in a lossless audio codec, it’s a good practice to have a multichannel AAC codec as well. Lossless requires a high bit rate. You want something available that has a lower bit rate. During playback you don’t want to switch the number of channels. If playback is in multichannel, you want to stay in multichannel.

Generally speaking, the player doesn’t switch between audio codecs, but there are three notable exceptions. The player switches between the AAC variants: AAC-LC, HE-AAC, HE-AACv2, and USAC (also called xHE-AAC). The player will also switch between lossless codecs and AAC codecs. In addition, when rendering audio to Spatial Audio-capable routes on Apple devices, the player may switch between available audio codecs and even channel layouts.

After you have your audio groups, you replicate the variant entries for each group, with some exceptions. If the codecs are switchable, like the AAC codecs, then you can spread the audio groups across the variants using the low audio bit rate group with the low video bit rates and the high audio bit rate group with the high video. But, if the codecs are not switchable, like AC-3 and lossless, then you want each codec to be associated with every variant. This doesn’t create new variant playlists; it just creates new `EXT-X-STREAM-INF` tags in the multivariant playlist, which associate a video playlist with an audio group.

You may encounter a problem where the variants you want to favor aren’t being chosen. The default behavior is to choose the highest bit rate among what’s currently playable. With USAC and with Dolby Digital Plus, this can cause an inversion where the chosen variant is not what you would prefer. To remedy this, Apple added the `SCORE` attribute. The value is a floating-point number. You have to put it on all the variants. If you want to set an order, it has to be complete, otherwise you’ll have situations where you won’t be able to choose. The usual filtering occurs to get down to a set of variants, any of which could be played. At that point, the system uses `SCORE` to decide and the highest `SCORE` wins.

##### Values for the Codecs Attribute

Use the `CODECS` attribute of the `EXT-X-STREAM-INF` tag (and `EXT-X-I-FRAME-STREAM-INF`) to specify media sample types. The value is a quoted-string containing a comma-separated list of formats, where each format specifies a media sample type that is present in a media segment of the playlist or in a media segment of some rendition that the tag references.

Valid format identifiers are those in the ISO Base Media File Format Name Space defined by RFC 6381. A format identifier is a sequence of elements separated by periods. The first element is the base sample type. HLS currently recognizes the following values for the base sample types:

| Base sample type | Description | Notes |
| --- | --- | --- |
| `ac-3` | AC-3 audio |  |
| `alac` | Apple Lossless |  |
| `avc1` | H.264 (Advanced Video Coding) |  |
| `avc3` | H.264 (Advanced Video Coding) | Use not recommended |
| `dvh1` | Dolby Vision (based on `hvc1`) |  |
| `dvhe` | Dolby Vision (based on `hev1`) | Use not recommended |
| `ec-3` | Enhanced AC-3 audio |  |
| `fLaC` | Free Lossless Audio Codec |  |
| `hev1` | HEVC (High-Efficiency Video Coding) | Use not recommended |
| `hvc1` | HEVC (High-Efficiency Video Coding) |  |
| `mjpg` | JPEG image sequence | Limited use |
| `mp4a` | MPEG-4 audio |  |
| `stpp` | Subtitles (Timed Text) |  |
| `wvtt` | WebVTT data |  |

> **Note**: HLS recognizes `'avc3'`, `'dvhe'`, and `'hev1'`, but Apple doesn’t recommend using them.

HLS recognizes `'avc3'`, `'dvhe'`, and `'hev1'`, but Apple doesn’t recommend using them.

The MP4 registration authority ([`mp4ra.org`](https://developer.apple.comhttp://mp4ra.org)) lists a value of `ec+3` for Enhanced AC-3 audio with JOC (Dolby Atmos). That value is not used by HLS. Instead, it uses `ec-3` and marks the presence of the additional JOC content with `JOC` in the `CHANNELS` attribute of the audio rendition. The `JOC` must be capitalized. For example, `CHANNELS="16/JOC"`. The numeric value should match the value of the `complexity_index_type_a` field in the `EC3SpecificBox` of the Dolby Digital Plus audio track.

| Sample type | Description |
| --- | --- |
| `ac-3` | AC-3 audio |
| `alac` | Apple Lossless audio |
| `avc1.42001f` | H.264 Baseline Profile, Level 3.1 video |
| `avc1.4d0028` | H.264 Main Profile, Level 4.0 video |
| `avc1.640029` | H.264 High Profile, Level 4.1 video |
| `dvh1.05.01` | Dolby Vision Profile 5 (10-bit HEVC), Level 1 (720p24) video |
| `dvh1.05.06` | Dolby Vision Profile 5 (10-bit HEVC), Level 6 (2160p24) video |
| `ec-3` | Enhanced AC-3 audio |
| `fLaC` | Free Lossless Audio Codec audio |
| `hvc1.1.4.L126.B0` | HEVC Main Profile, Main Tier, Level 4.2 video |
| `hvc1.2.4.L123.B0` | HEVC Main 10 Profile, Main Tier, Level 4.1 video |
| `hvc1.2.4.L150.B0` | HEVC Main 10 Profile, Main Tier, Level 5.0 video |
| `mjpg` | JPEG image sequence |
| `mp4a.40.2` | AAC-LC audio |
| `mp4a.40.5` | HE-AAC audio |
| `mp4a.40.29` | HE-AACv2 audio |
| `mp4a.40.34` | MP3 audio |
| `mp4a.40.42` | xHE-AAC audio |
| `stpp.ttml.im1t` | IMSC1 text-only subtitles |
| `wvtt` | WebVTT subtitles |

##### Allowed Cpc Values for Fairplay Streaming

The `ALLOWED-CPC` attribute restricts playback of an encrypted variant stream to devices that guarantee a certain level of content protection robustness. The attribute associates a list of Content Protection Configuration (CPC) Labels with a specific `KEYFORMAT` value.

The permitted CPC Labels for FairPlay Streaming are:

|  |  |
| --- | --- |
|  | Any Apple platform that supports FairPlay Streaming. |
|  | Any Apple platform that supports FairPlay Streaming and guarantees enhanced content protection robustness (sufficient for studio 4K/HDR playback). |
|  | Any non-Apple platform that supports FairPlay Streaming. For example, any AirPlay 2-enabled smart TV. |
|  | Any non-Apple platform that supports FairPlay Streaming and guarantees enhanced content protection robustness (sufficient for studio 4K/HDR playback). |

An example of a valid attribute is: `ALLOWED-CPC="com.apple.streamingkeydelivery:AppleMain/Main"`

##### The Supplemental Codecs Attribute

Some codecs are backward-compatible with other codecs. These codecs work by adding metadata that are ignored when being interpreted as the compatible codec, but used by the newer codec. These codecs include Dolby Vision 8.4 and 10.4 (compatible with HLG) and Dolby Vision 8.1 and 10.1 (compatible with HDR10).

To support these codecs on older implementations, the `CODECS` attribute is used to describe the base layer. The enhanced codec is described in the `SUPPLEMENTAL-CODECS` attribute. This allows implementations that support `SUPPLEMENTAL-CODECS` to take advantage of the true codec.

Each element in the `SUPPLEMENTAL-CODECS` attribute is a slash-separated list of fields.  The first field must be a valid `CODECS` format. If more than one field is present, the remaining fields must be compatibility brands that pertain to that codec’s bitstream.

You can indicate the presence of HDR10+ metadata by adding a brand of ‘cdm4’.

Example-codec-values:

|  |  |  |  |
| --- | --- | --- | --- |
| Dolby Vision 8.4 | hvc1.2.4.L153.b0 | dvh1.08.07/db4h | HLG |
| Dolby Vision 8.1 | hvc1.2.4.L150 | dvh1.08.06/db1p | PQ |
| Dolby Vision 10.4 | av01.0.13M.10.0.112 | dav1.10.09/db4h | HLG |
| AV1 w/ HDR10+ | av01.0.05M.10.0.112 | av01.0.05M.10.0.112/cdm4 | PQ |

Note that, for Dolby Vision, the compatibility brand and the `VIDEO-RANGE` attribute act as cross-checks. Leaving out either one is incorrect.

##### Dim Flashing Lights

Dim Flashing Lights is a setting (see [`What’s new in Accessibility`](https://developer.apple.comhttps://developer.apple.com/accessibility/#dim-flashing-lights)) that allows people to indicate that they want to avoid bright, frequent flashes of light in video. As an additional measure, content producers can add markers to their HTTP Live Streaming content that identify the regions likely to cause discomfort.

Regions can be signalled using the standard `#EXT-X-DATERANGE` tag. The `CLASS` attribute should be set to “com.apple.accessibility.video.strobing.general-flash”. Add an additional `X-RISK-LEVEL` attribute. The risk level should be a decimal floating-point value in the range 0 to 100, where 0 is minimal risk and 100 is very risky.

To avoid using a large number of regions, restrict risk-level values to a small set of values. Use a risk level of zero for regions that have very low risk. Don’t mark regions with a risk level unless they have been analyzed. Raw risk values can be computed using an algorithm such as [`VideoFlashingReduction`](https://developer.apple.comhttps://github.com/apple/VideoFlashingReduction).

The [`AVPlayerItemMetadataCollector`](https://developer.apple.com/documentation/AVFoundation/AVPlayerItemMetadataCollector) class can be used in your application to fetch the `#EXT-X-DATERANGE` tag metadata.

If you use the [`AVKit`](https://developer.apple.com/documentation/AVKit) framework the metadata is fetched for you and the timeline is marked with a reddish color. If you display your own timeline you should do something similar.

##### Additional Stereo Video Specifications

Video Extended Usage atom (`'vexu'`) is a sample description extension that conveys extensible information about stereo views. For more information, see [`ISO Base Media File Format and Apple HEVC Stereo Video`](https://developer.apple.comhttps://developer.apple.com/av-foundation/Stereo-Video-ISOBMFF-Extensions.pdf).

You can provide parallax metadata for subtitles or captions as timed metadata tracks within ISOBMFF (ISO Base Media File Format) or QuickTime files. An `'mebx'` atom or box describes the samples in a timed metadata track. The international standard ISO/IEC 14496-12:2022 (“Information technology — Coding of audio-visual objects — Part 12: ISO base media file format”) refers to this box as a `BoxedMetadataSampleEntry` (for more information, see section 12.9  of that document). The [`QuickTime File Format Specification`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/QuickTime/QTFF/QTFFPreface/qtffPreface.html) refers to the `'mebx'` atom as a  (see [`Timed Metadata Media`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/QuickTime/QTFF/QTFFChap3/qtff3.html#//apple_ref/doc/uid/TP40000939-CH205-SW130)). The `'mebx'` atom and its contents are a generic structure.

To learn more on the specific use of `'mebx'` for caption parallax information, see [`ISO Base Media File Format and Apple HEVC Stereo Video`](https://developer.apple.comhttps://developer.apple.com/av-foundation/Stereo-Video-ISOBMFF-Extensions.pdf) and [`Video Contour Map Payload Metadata within the QuickTime Movie File Format`](https://developer.apple.comhttps://developer.apple.com/av-foundation/Video-Contour-Map-Metadata.pdf).

For more information on encoding MV-HEVC video, see [`Apple HEVC Stereo Video`](https://developer.apple.comhttps://developer.apple.com/av-foundation/HEVC-Stereo-Video-Profile.pdf).

You can find also find these resources listed at [`AVFoundation Overview`](https://developer.apple.comhttps://developer.apple.com/av-foundation/).

##### Example Playlist

The following is an example of a playlist with SDR, Dolby Vision, HDR10, and HLG content at resolutions from 720p to 4K. The SUPPLEMENTAL-CODECS attribute is used to indicate that the HDR10 content is compatible with Dolby Vison 8.1 and the HLG content is compatible with Dolby Vision 8.4.

```swift
#EXTM3U
#EXT-X-VERSION:7
#EXT-X-INDEPENDENT-SEGMENTS

#EXT-X-STREAM-INF:AVERAGE-BANDWIDTH=2778321,BANDWIDTH=3971374,VIDEO-RANGE=SDR,CODECS="hvc1.2.4.L123.B0",RESOLUTION=1280x720,FRAME-RATE=23.976,CLOSED-CAPTIONS=NONE,HDCP-LEVEL=NONE
sdr_720/prog_index.m3u8
#EXT-X-STREAM-INF:AVERAGE-BANDWIDTH=6759875,BANDWIDTH=10022043,VIDEO-RANGE=SDR,CODECS="hvc1.2.4.L123.B0",RESOLUTION=1920x1080,FRAME-RATE=23.976,CLOSED-CAPTIONS=NONE,HDCP-LEVEL=TYPE-0
sdr_1080/prog_index.m3u8
#EXT-X-STREAM-INF:AVERAGE-BANDWIDTH=20985770,BANDWIDTH=28058971,VIDEO-RANGE=SDR,CODECS="hvc1.2.4.L150.B0",RESOLUTION=3840x2160,FRAME-RATE=23.976,CLOSED-CAPTIONS=NONE,HDCP-LEVEL=TYPE-1
sdr_2160/prog_index.m3u8

#EXT-X-STREAM-INF:AVERAGE-BANDWIDTH=3385450,BANDWIDTH=5327059,VIDEO-RANGE=PQ,CODECS="dvh1.05.01",RESOLUTION=1280x720,FRAME-RATE=23.976,CLOSED-CAPTIONS=NONE,HDCP-LEVEL=NONE
dolby_720/prog_index.m3u8
#EXT-X-STREAM-INF:AVERAGE-BANDWIDTH=7999361,BANDWIDTH=12876596,VIDEO-RANGE=PQ,CODECS="dvh1.05.03",RESOLUTION=1920x1080,FRAME-RATE=23.976,CLOSED-CAPTIONS=NONE,HDCP-LEVEL=TYPE-0
dolby_1080/prog_index.m3u8
#EXT-X-STREAM-INF:AVERAGE-BANDWIDTH=24975091,BANDWIDTH=30041698,VIDEO-RANGE=PQ,CODECS="dvh1.05.06",RESOLUTION=3840x2160,FRAME-RATE=23.976,CLOSED-CAPTIONS=NONE,HDCP-LEVEL=TYPE-1
dolby_2160/prog_index.m3u8

#EXT-X-STREAM-INF:AVERAGE-BANDWIDTH=3320040,BANDWIDTH=5280654,VIDEO-RANGE=PQ,CODECS="hvc1.2.4.L123.B0",SUPPLEMENTAL-CODECS="dvh1.08.01/db1p",RESOLUTION=1280x720,FRAME-RATE=23.976,CLOSED-CAPTIONS=NONE,HDCP-LEVEL=NONE
hdr10_dolby_720/prog_index.m3u8
#EXT-X-STREAM-INF:AVERAGE-BANDWIDTH=7964551,BANDWIDTH=12886714,VIDEO-RANGE=PQ,CODECS="hvc1.2.4.L123.B0",SUPPLEMENTAL-CODECS="dvh1.08.03/db1p",RESOLUTION=1920x1080,FRAME-RATE=23.976,CLOSED-CAPTIONS=NONE,HDCP-LEVEL=TYPE-0
hdr10_dolby_1080/prog_index.m3u8
#EXT-X-STREAM-INF:AVERAGE-BANDWIDTH=24833402,BANDWIDTH=29983769,VIDEO-RANGE=PQ,CODECS="hvc1.2.4.L150.B0",SUPPLEMENTAL-CODECS="dvh1.08.08/db1p",RESOLUTION=3840x2160,FRAME-RATE=23.976,CLOSED-CAPTIONS=NONE,HDCP-LEVEL=TYPE-1
hdr10_dolby_2160/prog_index.m3u8

#EXT-X-STREAM-INF:AVERAGE-BANDWIDTH=3061873,BANDWIDTH=3109758,VIDEO-RANGE=HLG,CODECS="hvc1.2.20000000.L150.B0",SUPPLEMENTAL-CODECS="dvh1.08.01/db4h",RESOLUTION=1280x720,FRAME-RATE=23.976,CLOSED-CAPTIONS=NONE,HDCP-LEVEL=NONE
hlg_dolby_720_24/prog_index.m3u8
#EXT-X-STREAM-INF:AVERAGE-BANDWIDTH=6759750,BANDWIDTH=6884346,VIDEO-RANGE=HLG,CODECS="hvc1.2.20000000.L153.B0",SUPPLEMENTAL-CODECS="dvh1.08.03/db4h",RESOLUTION=1920x1080,FRAME-RATE=23.976,CLOSED-CAPTIONS=NONE,HDCP-LEVEL=TYPE-0
hlg_dolby_1080_30/prog_index.m3u8
#EXT-X-STREAM-INF:AVERAGE-BANDWIDTH=26472863,BANDWIDTH=28111779,VIDEO-RANGE=HLG,CODECS="hvc1.2.20000000.L183.B0",SUPPLEMENTAL-CODECS="dvh1.08.08/db4h",RESOLUTION=3840x2160,FRAME-RATE=23.976,CLOSED-CAPTIONS=NONE,HDCP-LEVEL=TYPE-1
hlg_dolby_2160_60/prog_index.m3u8

#EXT-X-I-FRAME-STREAM-INF:AVERAGE-BANDWIDTH=248586,BANDWIDTH=593626,VIDEO-RANGE=SDR,CODECS="hvc1.2.4.L123.B0",RESOLUTION=1280x720,HDCP-LEVEL=NONE,URI="sdr_720/iframe_index.m3u8"
#EXT-X-I-FRAME-STREAM-INF:AVERAGE-BANDWIDTH=399790,BANDWIDTH=956552,VIDEO-RANGE=SDR,CODECS="hvc1.2.4.L123.B0",RESOLUTION=1920x1080,HDCP-LEVEL=TYPE-0,URI="sdr_1080/iframe_index.m3u8"
#EXT-X-I-FRAME-STREAM-INF:AVERAGE-BANDWIDTH=826971,BANDWIDTH=1941397,VIDEO-RANGE=SDR,CODECS="hvc1.2.4.L150.B0",RESOLUTION=3840x2160,HDCP-LEVEL=TYPE-1,URI="sdr_2160/iframe_index.m3u8"

#EXT-X-I-FRAME-STREAM-INF:AVERAGE-BANDWIDTH=232253,BANDWIDTH=573073,VIDEO-RANGE=PQ,CODECS="dvh1.05.01",RESOLUTION=1280x720,HDCP-LEVEL=NONE,URI="dolby_720/iframe_index.m3u8"
#EXT-X-I-FRAME-STREAM-INF:AVERAGE-BANDWIDTH=365337,BANDWIDTH=905037,VIDEO-RANGE=PQ,CODECS="dvh1.05.03",RESOLUTION=1920x1080,HDCP-LEVEL=TYPE-0,URI="dolby_1080/iframe_index.m3u8"
#EXT-X-I-FRAME-STREAM-INF:AVERAGE-BANDWIDTH=739114,BANDWIDTH=1893236,VIDEO-RANGE=PQ,CODECS="dvh1.05.06",RESOLUTION=3840x2160,HDCP-LEVEL=TYPE-1,URI="dolby_2160/iframe_index.m3u8"

#EXT-X-I-FRAME-STREAM-INF:AVERAGE-BANDWIDTH=232511,BANDWIDTH=572673,VIDEO-RANGE=PQ,CODECS="hvc1.2.4.L123.B0",SUPPLEMENTAL-CODECS="dvh1.08.01/db1p",RESOLUTION=1280x720,HDCP-LEVEL=NONE,URI="hdr10_dolby_720/iframe_index.m3u8"
#EXT-X-I-FRAME-STREAM-INF:AVERAGE-BANDWIDTH=364552,BANDWIDTH=905053,VIDEO-RANGE=PQ,CODECS="hvc1.2.4.L123.B0",SUPPLEMENTAL-CODECS="dvh1.08.03/db1p",RESOLUTION=1920x1080,HDCP-LEVEL=TYPE-0,URI="hdr10_dolby_1080/iframe_index.m3u8"
#EXT-X-I-FRAME-STREAM-INF:AVERAGE-BANDWIDTH=739757,BANDWIDTH=1895477,VIDEO-RANGE=PQ,CODECS="hvc1.2.4.L150.B0",SUPPLEMENTAL-CODECS="dvh1.08.08/db1p",RESOLUTION=3840x2160,HDCP-LEVEL=TYPE-1,URI="hdr10_dolby_2160/iframe_index.m3u8"

#EXT-X-I-FRAME-STREAM-INF:AVERAGE-BANDWIDTH=214431,BANDWIDTH=337245,VIDEO-RANGE=HLG,CODECS="hvc1.2.20000000.L150.B0",SUPPLEMENTAL-CODECS="dvh1.08.01/db4h",RESOLUTION=1280x720,HDCP-LEVEL=NONE,URI="hlg_dolby_720/prog_index.m3u8"
#EXT-X-I-FRAME-STREAM-INF:AVERAGE-BANDWIDTH=309406,BANDWIDTH=483498,VIDEO-RANGE=HLG,CODECS="hvc1.2.20000000.L153.B0",SUPPLEMENTAL-CODECS="dvh1.08.03/db4h",RESOLUTION=1920x1080,HDCP-LEVEL=TYPE-0,URI="hlg_dolby_1080/prog_index.m3u8"
#EXT-X-I-FRAME-STREAM-INF:AVERAGE-BANDWIDTH=788595,BANDWIDTH=1777136,VIDEO-RANGE=HLG,CODECS="hvc1.2.20000000.L183.B0",SUPPLEMENTAL-CODECS="dvh1.08.08/db4h",RESOLUTION=3840x2160,HDCP-LEVEL=TYPE-1,URI="hlg_dolby_2160/prog_index.m3u8"
```

The HEVC codec values are described in ISO/IEC 14496-15. A short description is `Codec.Profile.Flags.TierLevel.Constraints`, so in `hvc1.2.4.L123.B0`, the `2` means , and the `L123` means .

Information about Dolby Video codec values can be obtained from Dolby. A short description is `Codec.Profile.Level`, so in `dvh1.05.03` the Profile is 5 and the Level is 3.


---

*[View on Apple Developer](https://developer.apple.com/documentation/http-live-streaming/hls-authoring-specification-for-apple-devices-appendixes)*