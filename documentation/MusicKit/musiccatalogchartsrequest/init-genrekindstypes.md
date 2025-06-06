# init(genre:kinds:types:)

**Framework**: MusicKit  
**Kind**: init

Creates a catalog charts request for a specified genre and list of types to include in the catalog charts response.

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
init(genre: Genre? = nil, kinds: [MusicCatalogChartKind] = [.mostPlayed], types: [any MusicCatalogChartRequestable.Type])
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/musiccatalogchartsrequest/init(genre:kinds:types:))*