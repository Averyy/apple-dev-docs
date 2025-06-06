# EditorialNotes

**Framework**: MusicKit  
**Kind**: struct

An object that represents editorial notes.

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
struct EditorialNotes
```

## Topics

### Operators
- [static func == (EditorialNotes, EditorialNotes) -> Bool](editorialnotes/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var hashValue: Int](editorialnotes/hashvalue.md)
  The hash value.
- [let name: String?](editorialnotes/name.md)
  The name for the editorial notes.
- [let short: String?](editorialnotes/short.md)
  Abbreviated notes that display inline or when the content appears alongside other content.
- [let standard: String?](editorialnotes/standard.md)
  Notes that appear when the content displays prominently.
- [let tagline: String?](editorialnotes/tagline.md)
  The tag line for the editorial notes.
### Instance Methods
- [func hash(into: inout Hasher)](editorialnotes/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [CustomDebugStringConvertible Implementations](editorialnotes/customdebugstringconvertible-implementations.md)
- [CustomStringConvertible Implementations](editorialnotes/customstringconvertible-implementations.md)
- [Decodable Implementations](editorialnotes/decodable-implementations.md)
- [Encodable Implementations](editorialnotes/encodable-implementations.md)
- [Equatable Implementations](editorialnotes/equatable-implementations.md)

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

## See Also

- [enum ContentRating](contentrating.md)
  The rating of the content that potentially plays while playing a resource.
- [struct PreviewAsset](previewasset.md)
  An object that represents a preview for resources.


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/editorialnotes)*