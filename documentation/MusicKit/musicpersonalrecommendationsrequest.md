# MusicPersonalRecommendationsRequest

**Framework**: MusicKit  
**Kind**: struct

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

### Operators
- [static func == (MusicPersonalRecommendationsRequest, MusicPersonalRecommendationsRequest) -> Bool](musicpersonalrecommendationsrequest/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Initializers
- [init()](musicpersonalrecommendationsrequest/init.md)
  Creates a request to fetch default personal recommendations for the user.
- [init<S>(refreshing: S)](musicpersonalrecommendationsrequest/init(refreshing:).md)
  Creates a request to fetch default personal recommendations for the user.
### Instance Properties
- [var hashValue: Int](musicpersonalrecommendationsrequest/hashvalue.md)
  The hash value.
- [var limit: Int?](musicpersonalrecommendationsrequest/limit.md)
  A limit for the number of recommendations to return in the personal recommendations response.
- [var offset: Int?](musicpersonalrecommendationsrequest/offset.md)
  An offet for the request.
### Instance Methods
- [func hash(into: inout Hasher)](musicpersonalrecommendationsrequest/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
- [func response() async throws -> MusicPersonalRecommendationsResponse](musicpersonalrecommendationsrequest/response.md)
  Fetches the music recommendations based on the user’s library and listening history.
### Default Implementations
- [Equatable Implementations](musicpersonalrecommendationsrequest/equatable-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/musicpersonalrecommendationsrequest)*