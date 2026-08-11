# collectionID

**Framework**: Now Playing  
**Kind**: property  
**Required**: Yes

An opaque identifier for the collection this content belongs to, such as an album, playlist, or podcast show.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
var collectionID: String? { get set }
```

#### Discussion

The system uses this identifier to group related content and to ask the app to resume playback of the collection. For example, this could be an album identifier for a song, a show identifier for a podcast episode, or a playlist identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nowplaying/mediacontentrepresentable/collectionid)*