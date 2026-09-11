# appEntityIdentifiers

**Framework**: Now Playing  
**Kind**: property

The entities that represent this content, making them available to Siri and Apple Intelligence.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
var appEntityIdentifiers: [EntityIdentifier] { get set }
```

#### Discussion

Associate one or more `EntityIdentifier` values with the content so the system can connect the currently playing media to your app’s `AppEntity` types.

```swift
var content: any MediaContentRepresentable {
    var musicContent = MusicContent(id: song.id, songTitle: song.title, artistName: song.artist)
    musicContent.appEntityIdentifiers = [EntityIdentifier(for: SongEntity.self, identifier: song.id)]
    return musicContent
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/nowplaying/mediacontentrepresentable/appentityidentifiers)*