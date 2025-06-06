# ContentRating

**Framework**: MusicKit  
**Kind**: enum

The rating of the content that potentially plays while playing a resource.

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
enum ContentRating
```

#### Overview

A nil value means no rating is available for this resource.

## Topics

### Operators
- [static func == (ContentRating, ContentRating) -> Bool](contentrating/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Enumeration Cases
- [ContentRating.clean](contentrating/clean.md)
- [ContentRating.explicit](contentrating/explicit.md)
### Initializers
- [init(from: any Decoder) throws](contentrating/init(from:).md)
  Creates a new instance by decoding from the given decoder.
### Instance Properties
- [var hashValue: Int](contentrating/hashvalue.md)
  The hash value.
### Instance Methods
- [func encode(to: any Encoder) throws](contentrating/encode(to:).md)
  Encodes this value into the given encoder.
- [func hash(into: inout Hasher)](contentrating/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](contentrating/equatable-implementations.md)

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct EditorialNotes](editorialnotes.md)
  An object that represents editorial notes.
- [struct PreviewAsset](previewasset.md)
  An object that represents a preview for resources.


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/contentrating)*