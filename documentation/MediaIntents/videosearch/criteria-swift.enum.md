# VideoSearch.Criteria

**Framework**: Media Intents  
**Kind**: enum  
**Role**: Enumeration

The metadata and classification of a person’s video search that the system provides.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- Mac Catalyst 27.3+ (Beta)
- tvOS 27.3+ (Beta)
- visionOS 27.3+ (Beta)

## Declaration

```swift
enum Criteria
```

## Overview

The `Criteria` enum describes the nature of a person’s video search and playback request. A person might speak a natural-language query, provide a direct URL to content, or make a vague request without specifying anything; for example, they might say “Play something”. Inspect the `criteria` to determine how to resolve the person’s request.

## Topics

### Enumeration Cases
- [VideoSearch.Criteria.searchQuery(_:)](./criteria-swift.enum/searchquery%28_%29.md)
  The person’s natural-language search query.
- [VideoSearch.Criteria.unspecified](./criteria-swift.enum/unspecified.md)
  The request includes a vague search query or no specific search criteria.
- [VideoSearch.Criteria.urls(_:)](./criteria-swift.enum/urls%28_%29.md)
  URLs that the system provides for matching video content.

## Relationships

### Conforms To
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaintents/videosearch/criteria-swift.enum)*