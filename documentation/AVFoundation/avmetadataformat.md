# AVMetadataFormat

**Framework**: AVFoundation  
**Kind**: struct

A structure that defines metadata formats.

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
struct AVMetadataFormat
```

## Mentions

- [Retrieving media metadata](retrieving-media-metadata.md)

## Topics

### Metadata formats
- [static let hlsMetadata: AVMetadataFormat](avmetadataformat/hlsmetadata.md)
  The HLS metadata format.
- [static let iTunesMetadata: AVMetadataFormat](avmetadataformat/itunesmetadata.md)
  The iTunes metadata format.
- [static let id3Metadata: AVMetadataFormat](avmetadataformat/id3metadata.md)
  The ID3 metadata format.
- [static let isoUserData: AVMetadataFormat](avmetadataformat/isouserdata.md)
  The ISO user data metadata format.
- [static let quickTimeMetadata: AVMetadataFormat](avmetadataformat/quicktimemetadata.md)
  The QuickTime metadata format.
- [static let quickTimeUserData: AVMetadataFormat](avmetadataformat/quicktimeuserdata.md)
  The QuickTime user data metadata format.
- [static let unknown: AVMetadataFormat](avmetadataformat/unknown.md)
  An unknown metadata format.
### Initializers
- [init(rawValue: String)](avmetadataformat/init(rawvalue:).md)
  Creates a metadata format with a string value.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Retrieving media metadata](retrieving-media-metadata.md)
  Load descriptive metadata for media assets and their tracks.
- [class AVMetadataItem](avmetadataitem.md)
  A metadata item for an audiovisual asset or one of its tracks.
- [class AVMutableMetadataItem](avmutablemetadataitem.md)
  A mutable metadata item for an audiovisual asset or for one of its tracks.
- [struct AVMetadataIdentifier](avmetadataidentifier.md)
  A structure that defines identifiers for metadata formats.
- [struct AVMetadataKey](avmetadatakey.md)
  A structure that defines a metadata key.
- [struct AVMetadataKeySpace](avmetadatakeyspace.md)
  A structure that defines a metadata key space.
- [struct AVMetadataExtraAttributeKey](avmetadataextraattributekey.md)
  A structure that defines keys for extra metadata attributes.
- [class AVMetadataItemFilter](avmetadataitemfilter.md)
  An object that filters selected information from a metadata item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmetadataformat)*