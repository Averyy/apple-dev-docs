# MusicCatalogSearchSuggestionsResponse

**Framework**: MusicKit  
**Kind**: struct

An object that contains results for a catalog search suggestions request.

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
struct MusicCatalogSearchSuggestionsResponse
```

## Topics

### Structures
- [MusicCatalogSearchSuggestionsResponse.Suggestion](musiccatalogsearchsuggestionsresponse/suggestion.md)
  An item that represents a suggestion in the search suggestions response.
### Instance Properties
- [let suggestions: [MusicCatalogSearchSuggestionsResponse.Suggestion]](musiccatalogsearchsuggestionsresponse/suggestions.md)
  A collection of suggested terms.
- [let topResults: MusicItemCollection<MusicCatalogSearchSuggestionsResponse.TopResult>](musiccatalogsearchsuggestionsresponse/topresults.md)
  A collection of top results.
### Type Aliases
- [MusicCatalogSearchSuggestionsResponse.TopResult](musiccatalogsearchsuggestionsresponse/topresult.md)
  A type alias for an item that represents one of the top results in a catalog search suggestions response.

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/musiccatalogsearchsuggestionsresponse)*