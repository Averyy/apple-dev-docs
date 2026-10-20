# MusicPersonalRecommendationsRequest

**Framework**: MusicKit  
**Kind**: struct  
**Role**: Structure

A request that your app uses to fetch music recommendations based on the user’s library and listening history.

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
struct MusicPersonalRecommendationsRequest
```

## Topics

### Initializers
- [init()](./musicpersonalrecommendationsrequest/init%28%29.md)
  Creates a request to fetch default personal recommendations for the user.
- [init<S>(refreshing: S)](./musicpersonalrecommendationsrequest/init%28refreshing%29.md)
  Creates a request to fetch default personal recommendations for the user.
### Instance Properties
- [var limit: Int?](./musicpersonalrecommendationsrequest/limit.md)
  A limit for the number of recommendations to return in the personal recommendations response.
- [var offset: Int?](./musicpersonalrecommendationsrequest/offset.md)
  An offset for the request.
### Instance Methods
- [func response() async throws -> MusicPersonalRecommendationsResponse](./musicpersonalrecommendationsrequest/response%28%29.md)
  Fetches the music recommendations based on the user’s library and listening history.

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/musicpersonalrecommendationsrequest)*