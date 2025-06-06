# MusicCatalogSearchSuggestionsResponse.Suggestion

**Framework**: MusicKit  
**Kind**: struct

An item that represents a suggestion in the search suggestions response.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
struct Suggestion
```

## Topics

### Operators
- [static func == (MusicCatalogSearchSuggestionsResponse.Suggestion, MusicCatalogSearchSuggestionsResponse.Suggestion) -> Bool](musiccatalogsearchsuggestionsresponse/suggestion/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Initializers
- [init(from: any Decoder) throws](musiccatalogsearchsuggestionsresponse/suggestion/init(from:).md)
  Creates a new instance by decoding from the given decoder.
### Instance Properties
- [let displayTerm: String](musiccatalogsearchsuggestionsresponse/suggestion/displayterm.md)
  A term to display to the user to select from.
- [var hashValue: Int](musiccatalogsearchsuggestionsresponse/suggestion/hashvalue.md)
  The hash value.
- [var id: String](musiccatalogsearchsuggestionsresponse/suggestion/id-swift.property.md)
  The unique identifier for the suggestion.
- [let searchTerm: String](musiccatalogsearchsuggestionsresponse/suggestion/searchterm.md)
  The term to use as a search input when using this suggestion.
### Instance Methods
- [func encode(to: any Encoder) throws](musiccatalogsearchsuggestionsresponse/suggestion/encode(to:).md)
  Encodes this value into the given encoder.
- [func hash(into: inout Hasher)](musiccatalogsearchsuggestionsresponse/suggestion/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Type Aliases
- [MusicCatalogSearchSuggestionsResponse.Suggestion.ID](musiccatalogsearchsuggestionsresponse/suggestion/id-swift.typealias.md)
  A type representing the stable identity of the entity associated with an instance.
### Default Implementations
- [CustomDebugStringConvertible Implementations](musiccatalogsearchsuggestionsresponse/suggestion/customdebugstringconvertible-implementations.md)
- [CustomStringConvertible Implementations](musiccatalogsearchsuggestionsresponse/suggestion/customstringconvertible-implementations.md)
- [Equatable Implementations](musiccatalogsearchsuggestionsresponse/suggestion/equatable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Identifiable](../Swift/Identifiable.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/musiccatalogsearchsuggestionsresponse/suggestion)*