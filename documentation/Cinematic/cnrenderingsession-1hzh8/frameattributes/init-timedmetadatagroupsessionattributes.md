# init(timedMetadataGroup:sessionAttributes:)

**Framework**: Cinematic  
**Kind**: init

Creates a structure representing a Cinematic rendering session based on meta group and session attributes.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst ?+
- macOS 14.0+
- tvOS 17.0+

## Declaration

```swift
init?(timedMetadataGroup metadataGroup: AVTimedMetadataGroup, sessionAttributes: CNRenderingSession.Attributes)
```

## Parameters

- `metadataGroup`: The meta group read from the timed Cinematic metadata track of a Cinematic asset.
- `sessionAttributes`: Rendering session attributes loaded from a Cinematic asset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cinematic/cnrenderingsession-1hzh8/frameattributes/init(timedmetadatagroup:sessionattributes:))*