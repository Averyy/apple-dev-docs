# AVMetadataExtraAttributeKey

**Framework**: AVFoundation  
**Kind**: struct

A structure that defines keys for extra metadata attributes.

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
struct AVMetadataExtraAttributeKey
```

## Topics

### Extra Attribute Keys
- [static let valueURI: AVMetadataExtraAttributeKey](avmetadataextraattributekey/valueuri.md)
  A key that identifies a resource to use as the item’s value.
- [static let baseURI: AVMetadataExtraAttributeKey](avmetadataextraattributekey/baseuri.md)
  A key that identifies the base URI the item uses to resolve its related URIs.
- [static let info: AVMetadataExtraAttributeKey](avmetadataextraattributekey/info.md)
  A key that identifies more information about the item.
### Initializers
- [init(String)](avmetadataextraattributekey/init(_:).md)
  Creates an extra attribute key with a string.
- [init(rawValue: String)](avmetadataextraattributekey/init(rawvalue:).md)
  Creates an extra attribute key with a raw string value.

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
- [struct AVMetadataFormat](avmetadataformat.md)
  A structure that defines metadata formats.
- [class AVMetadataItemFilter](avmetadataitemfilter.md)
  An object that filters selected information from a metadata item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmetadataextraattributekey)*