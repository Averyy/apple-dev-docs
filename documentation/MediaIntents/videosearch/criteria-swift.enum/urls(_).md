# VideoSearch.Criteria.urls(_:)

**Framework**: Media Intents  
**Kind**: case  
**Role**: Case

URLs that the system provides for matching video content.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- Mac Catalyst 27.3+ (Beta)
- tvOS 27.3+ (Beta)
- visionOS 27.3+ (Beta)

## Declaration

```swift
case urls([URL])
```

## Discussion

The system provides URLs for matching content if:

- A person’s search request includes a URL.
- Spotlight was able to find matching content with a URL you donated to the Spotlight index.
- The system was able to provide URLs for matching video content; for example, from onscreen context.

Use the provided URL in your [`IntentValueQuery`](../../../AppIntents/intentvaluequery.md) implementation to find content and return app entities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaintents/videosearch/criteria-swift.enum/urls(_:))*