# AVVideoCodecType

**Framework**: AVFoundation  
**Kind**: struct

A set of constants that describe the codecs the system supports for video capture.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
struct AVVideoCodecType
```

## Mentions

- [Recording movies in alternative formats](recording-movies-in-alternative-formats.md)

## Topics

### Video codecs
- [static let h264: AVVideoCodecType](avvideocodectype/h264.md)
  The H.264 video codec.
- [static let hevc: AVVideoCodecType](avvideocodectype/hevc.md)
  The HEVC video codec.
- [static let hevcWithAlpha: AVVideoCodecType](avvideocodectype/hevcwithalpha.md)
  The HEVC video codec that supports an alpha channel.
- [static let jpeg: AVVideoCodecType](avvideocodectype/jpeg.md)
  The JPEG video codec.
- [static let proRes422: AVVideoCodecType](avvideocodectype/prores422.md)
  The Apple ProRes 422 video codec.
- [static let proRes422LT: AVVideoCodecType](avvideocodectype/prores422lt.md)
  The Apple ProRes 422 LT video codec.
- [static let proRes422HQ: AVVideoCodecType](avvideocodectype/prores422hq.md)
  The Apple ProRes 422 HQ video codec.
- [static let proRes422Proxy: AVVideoCodecType](avvideocodectype/prores422proxy.md)
  The Apple ProRes 422 Proxy video codec.
- [static let proRes4444: AVVideoCodecType](avvideocodectype/prores4444.md)
  The Apple ProRes 4444 video codec.
- [static let appleProRes4444XQ: AVVideoCodecType](avvideocodectype/appleprores4444xq.md)
  The Apple ProRes 4444 XQ video codec.
### Deprecated
- [let AVVideoCodecH264: String](avvideocodech264.md)
  A key to access the name of the H.264 codec for compressing video.
- [let AVVideoCodecHEVC: String](avvideocodechevc.md)
  A key to access the name of the HEVC codec used to encode the video.
- [let AVVideoCodecJPEG: String](avvideocodecjpeg.md)
  A key to access the name of the JPEG codec for compressing video.
- [let AVVideoCodecAppleProRes422: String](avvideocodecappleprores422.md)
  A key to access the name of the Apple ProRes422 codec used to encode the video.
- [let AVVideoCodecAppleProRes4444: String](avvideocodecappleprores4444.md)
  A key to access the name of the Apple ProRes4444 codec used to encode the video.
### Initializers
- [init(rawValue: String)](avvideocodectype/init(rawvalue:).md)
  Creates a codec type from its raw string value.
### Type Properties
- [static let JPEGXL: AVVideoCodecType](avvideocodectype/jpegxl.md)
  The JPEG XL video codec.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [let AVVideoCodecKey: String](avvideocodeckey.md)
  A key to access the name of the codec for compressing video.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avvideocodectype)*