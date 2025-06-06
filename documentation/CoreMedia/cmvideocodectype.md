# CMVideoCodecType

**Framework**: Core Media  
**Kind**: typealias

A video codec type.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
typealias CMVideoCodecType = FourCharCode
```

#### Discussion

Certain codec types are also pixel formats.

There is no “kCMVideoCodecType_Raw”; you should use the appropriate pixel format type as the codec type.

## Topics

### Constants
- [var kCMVideoCodecType_422YpCbCr8: CMVideoCodecType](kcmvideocodectype_422ypcbcr8.md)
  A type that identifies a component with the format of Y’CbCr 8-bit 4:2:2 ordered Cb Y’0 Cr Y’1.
- [var kCMVideoCodecType_Animation: CMVideoCodecType](kcmvideocodectype_animation.md)
  A type that identifies the apple animation format.
- [var kCMVideoCodecType_Cinepak: CMVideoCodecType](kcmvideocodectype_cinepak.md)
  A type that identifies the cinepak format.
- [var kCMVideoCodecType_JPEG: CMVideoCodecType](kcmvideocodectype_jpeg.md)
  A type that identifies the Joint Photographic Experts Group (JPEG) format.
- [var kCMVideoCodecType_JPEG_OpenDML: CMVideoCodecType](kcmvideocodectype_jpeg_opendml.md)
  A type that identifies the JPEG format with Open-DML extensions.
- [var kCMVideoCodecType_SorensonVideo: CMVideoCodecType](kcmvideocodectype_sorensonvideo.md)
  A type that identifies the sorenson video format.
- [var kCMVideoCodecType_SorensonVideo3: CMVideoCodecType](kcmvideocodectype_sorensonvideo3.md)
  A type that identifies the sorenson 3 video format.
- [var kCMVideoCodecType_H263: CMVideoCodecType](kcmvideocodectype_h263.md)
  A type that identifies the ITU-T H.263 format.
- [var kCMVideoCodecType_H264: CMVideoCodecType](kcmvideocodectype_h264.md)
  A type that identifies the ITU-T H.264 format.
- [var kCMVideoCodecType_MPEG4Video: CMVideoCodecType](kcmvideocodectype_mpeg4video.md)
  A type that identifies the Moving Picture Experts Group (MPEG) MPEG-4 Part 2 video format.
- [var kCMVideoCodecType_MPEG2Video: CMVideoCodecType](kcmvideocodectype_mpeg2video.md)
  A type that identifies the MPEG-2 video format.
- [var kCMVideoCodecType_MPEG1Video: CMVideoCodecType](kcmvideocodectype_mpeg1video.md)
  A type that identifies the MPEG-1 video format.
- [var kCMVideoCodecType_DVCNTSC: CMVideoCodecType](kcmvideocodectype_dvcntsc.md)
  A type that identifies the DV NTSC format.
- [var kCMVideoCodecType_DVCPAL: CMVideoCodecType](kcmvideocodectype_dvcpal.md)
  A type that identifies the DV PAL format.
- [var kCMVideoCodecType_DVCProPAL: CMVideoCodecType](kcmvideocodectype_dvcpropal.md)
  A type that identifies the Panasonic DVCPro PAL format.
- [var kCMVideoCodecType_DVCPro50NTSC: CMVideoCodecType](kcmvideocodectype_dvcpro50ntsc.md)
  A type that identifies the Panasonic DVCPro-50 NTSC format.
- [var kCMVideoCodecType_DVCPro50PAL: CMVideoCodecType](kcmvideocodectype_dvcpro50pal.md)
  A type that identifies the Panasonic DVCPro-50 PAL format.
- [var kCMVideoCodecType_DVCPROHD720p60: CMVideoCodecType](kcmvideocodectype_dvcprohd720p60.md)
  A type that identifies the Panasonic DVCPro-HD 720p60 format.
- [var kCMVideoCodecType_DVCPROHD720p50: CMVideoCodecType](kcmvideocodectype_dvcprohd720p50.md)
  A type that identifies the Panasonic DVCPro-HD 720p50 format.
- [var kCMVideoCodecType_DVCPROHD1080i60: CMVideoCodecType](kcmvideocodectype_dvcprohd1080i60.md)
  A type that identifies the Panasonic DVCPro-HD 1080i60 format.
- [var kCMVideoCodecType_DVCPROHD1080i50: CMVideoCodecType](kcmvideocodectype_dvcprohd1080i50.md)
  A type that identifies the Panasonic DVCPro-HD 1080i50 format.
- [var kCMVideoCodecType_DVCPROHD1080p30: CMVideoCodecType](kcmvideocodectype_dvcprohd1080p30.md)
  A type that identifies the Panasonic DVCPro-HD 1080p30 format.
- [var kCMVideoCodecType_DVCPROHD1080p25: CMVideoCodecType](kcmvideocodectype_dvcprohd1080p25.md)
  A type that identifies the Panasonic DVCPro-HD 1080p25 format.

## See Also

- [struct CMVideoDimensions](cmvideodimensions.md)
  A structure that represents video dimensions.
- [typealias CMAudioFormatDescriptionMask](cmaudioformatdescriptionmask.md)
  A type for mask bits that represent parts of an audio format description.
- [typealias CMMediaType](cmmediatype.md)
  Constants that represent media types.
- [typealias CMAudioCodecType](cmaudiocodectype.md)
  An audio codec type.
- [typealias CMTextDisplayFlags](cmtextdisplayflags.md)
  An integer value that describes the display mode flags for text media.
- [typealias CMTextJustificationValue](cmtextjustificationvalue.md)
  An integer value that describes the justification modes for text media.
- [Media Type Constants](media-type-constants.md)
  Constants that represent media types.
- [Muxed Stream Types](muxed-stream-types.md)
  Constants that represent muxed stream types.
- [Audio Codec Types](audio-codec-types.md)
  Constants that represent audio codec types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmvideocodectype)*