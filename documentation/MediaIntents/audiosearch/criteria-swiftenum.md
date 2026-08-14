# AudioSearch.Criteria

**Framework**: Media Intents  
**Kind**: enum

The metadata and classification of a person’s audio search that the system provides.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
enum Criteria
```

#### Overview

The `Criteria` enum describes the nature of a person’s audio search and playback request. A person might speak a natural-language query, provide a direct URL to content, or make a vague request without specifying anything; for example, they might say “Play something”. Inspect the `criteria` to determine how to resolve the person’s request.

## Topics

### Audio search types
- [AudioSearch.Criteria.searchQuery(_:)](audiosearch/criteria-swift.enum/searchquery(_:).md)
  The person’s natural-language search query.
- [AudioSearch.Criteria.unspecified](audiosearch/criteria-swift.enum/unspecified.md)
  The request includes a vague search query or no specific search criteria.
- [AudioSearch.Criteria.url(_:)](audiosearch/criteria-swift.enum/url(_:).md)
  URLs that the system provides for matching audio content.

## Relationships

### Conforms To
- [Decodable](../swift/decodable.md)
- [Encodable](../swift/encodable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [var criteria: AudioSearch.Criteria](audiosearch/criteria-swift.property.md)
  The search criteria for the audio request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaintents/audiosearch/criteria-swift.enum)*