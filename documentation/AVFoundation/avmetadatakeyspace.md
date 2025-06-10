# AVMetadataKeySpace

**Framework**: AVFoundation  
**Kind**: struct

A structure that defines a metadata key space.

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
struct AVMetadataKeySpace
```

## Topics

### Common Key Space
- [static let common: AVMetadataKeySpace](avmetadatakeyspace/common.md)
  The common key space.
### Format-Specific Key Spaces
- [static let audioFile: AVMetadataKeySpace](avmetadatakeyspace/audiofile.md)
  The AudioToolbox audio file key space.
- [static let hlsDateRange: AVMetadataKeySpace](avmetadatakeyspace/hlsdaterange.md)
  The HTTP Live Streaming key space.
- [static let iTunes: AVMetadataKeySpace](avmetadatakeyspace/itunes.md)
  The iTunes key space.
- [static let icy: AVMetadataKeySpace](avmetadatakeyspace/icy.md)
  The Icecast/ShoutCAST streaming key space.
- [static let id3: AVMetadataKeySpace](avmetadatakeyspace/id3.md)
  The ID3 key space.
- [static let isoUserData: AVMetadataKeySpace](avmetadatakeyspace/isouserdata.md)
  The ISO key space.
- [static let quickTimeMetadata: AVMetadataKeySpace](avmetadatakeyspace/quicktimemetadata.md)
  The QuickTime metadata key space.
- [static let quickTimeUserData: AVMetadataKeySpace](avmetadatakeyspace/quicktimeuserdata.md)
  The QuickTime user data key space.
### Initializers
- [init(String)](avmetadatakeyspace/init(_:).md)
  Creates a key space with a string.
- [init(rawValue: String)](avmetadatakeyspace/init(rawvalue:).md)
  Creates a key space with a raw string value.

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
- [struct AVMetadataExtraAttributeKey](avmetadataextraattributekey.md)
  A structure that defines keys for extra metadata attributes.
- [struct AVMetadataFormat](avmetadataformat.md)
  A structure that defines metadata formats.
- [class AVMetadataItemFilter](avmetadataitemfilter.md)
  An object that filters selected information from a metadata item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmetadatakeyspace)*