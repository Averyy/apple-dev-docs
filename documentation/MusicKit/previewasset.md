# PreviewAsset

**Framework**: MusicKit  
**Kind**: struct

An object that represents a preview for resources.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
struct PreviewAsset
```

## Topics

### Operators
- [static func == (PreviewAsset, PreviewAsset) -> Bool](previewasset/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [let artwork: Artwork?](previewasset/artwork.md)
  The preview artwork for the associated preview music video.
- [var hashValue: Int](previewasset/hashvalue.md)
  The hash value.
- [let hlsURL: URL?](previewasset/hlsurl.md)
  The HLS preview URL for the content.
- [let url: URL?](previewasset/url.md)
  The preview URL for the content.
### Instance Methods
- [func hash(into: inout Hasher)](previewasset/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [CustomDebugStringConvertible Implementations](previewasset/customdebugstringconvertible-implementations.md)
- [CustomStringConvertible Implementations](previewasset/customstringconvertible-implementations.md)
- [Decodable Implementations](previewasset/decodable-implementations.md)
- [Encodable Implementations](previewasset/encodable-implementations.md)
- [Equatable Implementations](previewasset/equatable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [enum ContentRating](contentrating.md)
  The rating of the content that potentially plays while playing a resource.
- [struct EditorialNotes](editorialnotes.md)
  An object that represents editorial notes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/previewasset)*