# AudioSearch.Criteria.unspecified

**Framework**: Media Intents  
**Kind**: case

The request includes a vague search query or no specific search criteria.

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
case unspecified
```

## Mentions

- [Responding to audio search and playback requests](responding-to-audio-search-and-playback-requests.md)

#### Discussion

The person says something like “Play something” without specifying particular content. Provide recommended or recently played content in your response.

## See Also

- [AudioSearch.Criteria.searchQuery(_:)](audiosearch/criteria-swift.enum/searchquery(_:).md)
  The person’s natural-language search query.
- [AudioSearch.Criteria.url(_:)](audiosearch/criteria-swift.enum/url(_:).md)
  URLs that the system provides for matching audio content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaintents/audiosearch/criteria-swift.enum/unspecified)*