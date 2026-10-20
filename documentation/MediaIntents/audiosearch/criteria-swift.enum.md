# AudioSearch.Criteria

**Framework**: Media Intents  
**Kind**: enum  
**Role**: Enumeration

The metadata and classification of a person’s audio search that the system provides.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
enum Criteria
```

#### Overview

The `Criteria` enum describes the nature of a person’s audio search and playback request. A person might speak a natural-language query, provide a direct URL to content, or make a vague request without specifying anything; for example, they might say “Play something”. Inspect the `criteria` to determine how to resolve the person’s request.

## Topics

### Audio search types
- [AudioSearch.Criteria.searchQuery(_:)](./criteria-swift.enum/searchquery%28_%29.md)
  The person’s natural-language search query.
- [AudioSearch.Criteria.unspecified](./criteria-swift.enum/unspecified.md)
  The request includes a vague search query or no specific search criteria.
- [AudioSearch.Criteria.url(_:)](./criteria-swift.enum/url%28_%29.md)
  URLs that the system provides for matching audio content.

## Relationships

### Conforms To
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Describing result criteria
- [var criteria: AudioSearch.Criteria](./criteria-swift.property.md)
  The search criteria for the audio request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaintents/audiosearch/criteria-swift.enum)*