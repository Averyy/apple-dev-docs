# MPMediaType

**Framework**: Media Player  
**Kind**: struct

The properties for defining the type for a media item.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.12.2+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
struct MPMediaType
```

#### Overview

Media item types are possible values for the [`MPMediaItemPropertyMediaType`](mpmediaitempropertymediatype.md) property. A media item can have more than one media item type.

## Topics

### Constants
- [static var music: MPMediaType](mpmediatype/music.md)
  The media item contains music.
- [static var podcast: MPMediaType](mpmediatype/podcast.md)
  The media item contains a podcast.
- [static var audioBook: MPMediaType](mpmediatype/audiobook.md)
  The media item contains an audio book.
- [static var audioITunesU: MPMediaType](mpmediatype/audioitunesu.md)
  The media item contains an iTunes U audio lesson.
- [static var anyAudio: MPMediaType](mpmediatype/anyaudio.md)
  The media item contains an unspecified type of audio content.
- [static var movie: MPMediaType](mpmediatype/movie.md)
  The media item contains a movie.
- [static var tvShow: MPMediaType](mpmediatype/tvshow.md)
  The media item contains a TV show.
- [static var videoPodcast: MPMediaType](mpmediatype/videopodcast.md)
  The media item contains a video podcast.
- [static var musicVideo: MPMediaType](mpmediatype/musicvideo.md)
  The media item contains a music video.
- [static var videoITunesU: MPMediaType](mpmediatype/videoitunesu.md)
  The media item contains an iTunes U video.
- [static var homeVideo: MPMediaType](mpmediatype/homevideo.md)
  The media item contains a home video.
- [static var anyVideo: MPMediaType](mpmediatype/anyvideo.md)
  The media item contains an unspecified type of video content.
- [static var any: MPMediaType](mpmediatype/any.md)
  The media item contains an unspecified type of media content.
### Initializers
- [init(rawValue: UInt)](mpmediatype/init(rawvalue:).md)
  Creates a new instance with the specified raw value.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [General media item property keys](general-media-item-property-keys.md)
  System-defined properties for obtaining the metadata for a media item.
- [User-defined property keys](user-defined-property-keys.md)
  Properties for obtaining user-defined metadata for a media item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmediatype)*