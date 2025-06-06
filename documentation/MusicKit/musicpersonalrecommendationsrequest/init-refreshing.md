# init(refreshing:)

**Framework**: MusicKit  
**Kind**: init

Creates a request to fetch default personal recommendations for the user.

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
init<S>(refreshing recommendations: S) where S : Sequence, S.Element == MusicPersonalRecommendation
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/musicpersonalrecommendationsrequest/init(refreshing:))*