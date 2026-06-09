# AudioSearch.Criteria.url(_:)

**Framework**: Media Intents  
**Kind**: case

URLs that the system provides for matching audio content.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst ?+
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
case url([URL])
```

## Mentions

- [Responding to audio search and playback requests](responding-to-audio-search-and-playback-requests.md)

#### Discussion

The system provides URLs for matching content if:

- A person’s search request includes a URL.
- Spotlight was able to find matching content with a URL you donated to the Spotlight index.
- The system was able to provide URLs for matching audio content; for example, from onscreen context.

Use the provided URL in your [`IntentValueQuery`](https://developer.apple.com/documentation/AppIntents/IntentValueQuery) implementation to find content and return app entities.

## See Also

- [AudioSearch.Criteria.searchQuery(_:)](audiosearch/criteria-swift.enum/searchquery(_:).md)
  The person’s natural-language search query.
- [AudioSearch.Criteria.unspecified](audiosearch/criteria-swift.enum/unspecified.md)
  The request includes a vague search query or no specific search criteria.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaintents/audiosearch/criteria-swift.enum/url(_:))*