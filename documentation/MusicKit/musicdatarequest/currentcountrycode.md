# currentCountryCode

**Framework**: MusicKit  
**Kind**: property

Fetches the current country code for the user’s Apple Music account.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
static var currentCountryCode: String { get async throws }
```

#### Discussion

The current country code may be useful to construct the URL for a [`MusicDataRequest`](musicdatarequest.md) because a typical catalog endpoint for Apple Music API requires the inclusion of a country code in the path of the corresponding URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/musicdatarequest/currentcountrycode)*