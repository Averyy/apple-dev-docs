# content

**Framework**: Now Playing  
**Kind**: property  
**Required**: Yes

The content being played in this session.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
@MainActor
var content: (any MediaContentRepresentable)? { get }
```

## Mentions

- [Publishing media sessions](publishing-media-sessions.md)

#### Discussion

Use a content type like [`MusicContent`](musiccontent.md), [`PodcastContent`](podcastcontent.md), [`MovieContent`](moviecontent.md), [`TVShowContent`](tvshowcontent.md), or [`GenericContent`](genericcontent.md) to describe the media being played. You can provide additional metadata using the content type’s trailing closure.

The system displays content information on the device’s Lock Screen, in Control Center, and on connected accessories. Provide as much information as possible to ensure compatibility with a wide range of accessories and system interfaces.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nowplaying/mediasessionrepresentable/content)*