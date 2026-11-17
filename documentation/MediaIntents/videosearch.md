# VideoSearch

**Framework**: Media Intents  
**Kind**: struct  
**Role**: Structure

Results and metadata for a person’s video search and playback request with Siri.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- Mac Catalyst 27.3+ (Beta)
- tvOS 27.3+ (Beta)
- visionOS 27.3+ (Beta)

## Declaration

```swift
struct VideoSearch
```

## Overview

People use Apple Intelligence and Siri to find and play video. By integrating your app’s video catalog with Apple Intelligence and Siri using the [App Intents](../AppIntents/AppIntents.md) framework, the system forwards search and playback requests to your app, and your app returns video search results and allows the system to play your app’s movies, TV shows, episodes, and so on.

The `VideoSearch` structure captures a person’s video search and playback request — movies, TV shows, episodes, or other video content.

Use `VideoSearch` in your [`IntentValueQuery`](../AppIntents/intentvaluequery.md) implementation to find matching video content in your app’s media catalog.

## Topics

### Initializers
- [init(criteria: VideoSearch.Criteria)](./videosearch/init%28criteria%29.md)
  Creates a video search with a person’s search criteria.
### Instance Properties
- [var criteria: VideoSearch.Criteria](./videosearch/criteria-swift.property.md)
  The search criteria for the video request.
### Enumerations
- [VideoSearch.Criteria](./videosearch/criteria-swift.enum.md)
  The metadata and classification of a person’s video search that the system provides.

## Relationships

### Conforms To
- [Decodable](../Swift/decodable.md)
- [Encodable](../Swift/encodable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaintents/videosearch)*