# AudioSearch.Criteria.searchQuery(_:)

**Framework**: Media Intents  
**Kind**: case

The person’s natural-language search query.

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
case searchQuery(String)
```

## Mentions

- [Responding to audio search and playback requests](responding-to-audio-search-and-playback-requests.md)

#### Discussion

A string representation of a person’s search request. Use it in your app’s search infrastructure to find matching content.

## See Also

- [AudioSearch.Criteria.unspecified](audiosearch/criteria-swift.enum/unspecified.md)
  The request includes a vague search query or no specific search criteria.
- [AudioSearch.Criteria.url(_:)](audiosearch/criteria-swift.enum/url(_:).md)
  URLs that the system provides for matching audio content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaintents/audiosearch/criteria-swift.enum/searchquery(_:))*