# Artwork

**Framework**: MusicKit  
**Kind**: struct

An object that represents artwork for a music item.

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
struct Artwork
```

## Topics

### Operators
- [static func == (Artwork, Artwork) -> Bool](artwork/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [let alternateText: String?](artwork/alternatetext.md)
  A textual description for the image.
- [let backgroundColor: CGColor?](artwork/backgroundcolor.md)
  The average background color of the image.
- [var hashValue: Int](artwork/hashvalue.md)
  The hash value.
- [let maximumHeight: Int](artwork/maximumheight.md)
  The maximum height available for the image.
- [let maximumWidth: Int](artwork/maximumwidth.md)
  The maximum width available for the image.
- [let primaryTextColor: CGColor?](artwork/primarytextcolor.md)
  The primary text color to use when displaying the background color.
- [let quaternaryTextColor: CGColor?](artwork/quaternarytextcolor.md)
  The final posttertiary text color to use when displaying the background color.
- [let secondaryTextColor: CGColor?](artwork/secondarytextcolor.md)
  The secondary text color to use when displaying the background color.
- [let tertiaryTextColor: CGColor?](artwork/tertiarytextcolor.md)
  The tertiary text color to use when displaying the background color.
### Instance Methods
- [func hash(into: inout Hasher)](artwork/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
- [func url(width: Int, height: Int) -> URL?](artwork/url(width:height:).md)
  Returns a URL to request the image asset for a specified width and height.
### Default Implementations
- [CustomDebugStringConvertible Implementations](artwork/customdebugstringconvertible-implementations.md)
- [CustomStringConvertible Implementations](artwork/customstringconvertible-implementations.md)
- [Decodable Implementations](artwork/decodable-implementations.md)
- [Encodable Implementations](artwork/encodable-implementations.md)
- [Equatable Implementations](artwork/equatable-implementations.md)

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

- [struct ArtworkImage](artworkimage.md)
  A view that displays the image for a music item’s artwork.


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/artwork)*