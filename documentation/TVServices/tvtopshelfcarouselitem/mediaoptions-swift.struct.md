# TVTopShelfCarouselItem.MediaOptions

**Framework**: TV Services  
**Kind**: struct  
**Role**: Structure

Constants indicating the item’s audio and video capabilities.

**Availability**:
- tvOS 13.0+

## Declaration

```swift
struct MediaOptions
```

```c
enum TVTopShelfCarouselItemMediaOptions : NSUInteger;
```

## Topics

### Media Options
- [static var videoResolutionHD: TVTopShelfCarouselItem.MediaOptions](./mediaoptions-swift.struct/videoresolutionhd.md)
  High-definition video resolution.
- [static var videoResolution4K: TVTopShelfCarouselItem.MediaOptions](./mediaoptions-swift.struct/videoresolution4k.md)
  Ultra-high-definition 4K video resolution.
- [static var videoColorSpaceHDR: TVTopShelfCarouselItem.MediaOptions](./mediaoptions-swift.struct/videocolorspacehdr.md)
  High-dynamic-range video.
- [static var videoColorSpaceDolbyVision: TVTopShelfCarouselItem.MediaOptions](./mediaoptions-swift.struct/videocolorspacedolbyvision.md)
  Dolby Vision video.
- [static var audioDolbyAtmos: TVTopShelfCarouselItem.MediaOptions](./mediaoptions-swift.struct/audiodolbyatmos.md)
  Audio content with Dolby Atmos.
- [static var audioTranscriptionClosedCaptioning: TVTopShelfCarouselItem.MediaOptions](./mediaoptions-swift.struct/audiotranscriptionclosedcaptioning.md)
  Audio content with closed captioning.
- [static var audioTranscriptionSDH: TVTopShelfCarouselItem.MediaOptions](./mediaoptions-swift.struct/audiotranscriptionsdh.md)
  Audio content with subtitles for people who are deaf or hard of hearing.
- [static var audioDescription: TVTopShelfCarouselItem.MediaOptions](./mediaoptions-swift.struct/audiodescription.md)
  Audio content with audio descriptions.
### Initializers
- [init(rawValue: UInt)](./mediaoptions-swift.struct/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [SetAlgebra](../../Swift/setalgebra.md)

## See Also

### Adding Media Badges
- [var mediaOptions: TVTopShelfCarouselItem.MediaOptions](./mediaoptions-swift.property.md)
  Information about the media format and presentation options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvservices/tvtopshelfcarouselitem/mediaoptions-swift.struct)*