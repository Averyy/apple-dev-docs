# MusicRecentlyPlayedRequest

**Framework**: MusicKit  
**Kind**: struct

A request that your app uses to fetch items the user has recently played.

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
struct MusicRecentlyPlayedRequest<MusicItemType> where MusicItemType : MusicRecentlyPlayedRequestable, MusicItemType : Decodable
```

## Topics

### Initializers
- [init()](musicrecentlyplayedrequest/init.md)
  Creates a request for items the user has recently played.
### Instance Properties
- [var limit: Int?](musicrecentlyplayedrequest/limit.md)
  A limit for the number of items to return in the response that contains items the user has recently played.
- [var offset: Int?](musicrecentlyplayedrequest/offset.md)
  An offet for the request.
### Instance Methods
- [func response() async throws -> MusicRecentlyPlayedResponse<MusicItemType>](musicrecentlyplayedrequest/response.md)
  Fetches items the user has recently played.


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/musicrecentlyplayedrequest)*