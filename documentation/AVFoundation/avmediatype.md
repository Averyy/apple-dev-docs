# AVMediaType

**Framework**: AVFoundation  
**Kind**: struct  
**Role**: Structure

An identifier for various media types.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
struct AVMediaType
```

```c
typedef NSString * AVMediaType;
```

## Topics

### Media types
- [static let audio: AVMediaType](./avmediatype/audio.md)
  The media contains audio media.
- [static let auxiliaryPicture: AVMediaType](./avmediatype/auxiliarypicture.md)
- [static let closedCaption: AVMediaType](./avmediatype/closedcaption.md)
  The media contains closed-caption content.
- [static let depthData: AVMediaType](./avmediatype/depthdata.md)
  The media contains depth data.
- [static let haptic: AVMediaType](./avmediatype/haptic.md)
  The media contains haptic content.
- [static let metadata: AVMediaType](./avmediatype/metadata.md)
  The media contains metadata.
- [static let metadataObject: AVMediaType](./avmediatype/metadataobject.md)
  The media contains metadata objects.
- [static let muxed: AVMediaType](./avmediatype/muxed.md)
  The media contains muxed media.
- [static let subtitle: AVMediaType](./avmediatype/subtitle.md)
  The media contains subtitles.
- [static let text: AVMediaType](./avmediatype/text.md)
  The media contains text.
- [static let timecode: AVMediaType](./avmediatype/timecode.md)
  The media contains a time code.
- [static let video: AVMediaType](./avmediatype/video.md)
  The media contains video.
### Initializers
- [init(String)](./avmediatype/init%28_%29.md)
  Creates a media type with a string.
- [init(rawValue: String)](./avmediatype/init%28rawvalue%29.md)
  Creates a media type with a raw string value.

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Media types
- [struct AVMediaCharacteristic](./avmediacharacteristic.md)
  A structure that defines media data characteristics.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmediatype)*