# albumArtworkRepresentations

**Framework**: AVKit  
**Kind**: property

Array of available album artwork representations in various formats and sizes.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
var albumArtworkRepresentations: [AVInterfaceAlbumArtwork]
```

#### Discussion

Multiple representations allow the system to choose the most appropriate artwork for different display contexts (thumbnails, full-screen, high-DPI displays). Each representation specifies its dimensions, format, and URL for optimal loading and display performance.

## See Also

- [var title: String?](avinterfacemetadata-swift.struct/title.md)
  Primary title or name of the media content.
- [var subtitle: String?](avinterfacemetadata-swift.struct/subtitle.md)
  Secondary descriptive text such as artist name or episode description.
- [var isAudioOnly: Bool](avinterfacemetadata-swift.struct/isaudioonly.md)
  Indicates whether the content is audio-only (no video component).
- [var presentationSize: CGSize](avinterfacemetadata-swift.struct/presentationsize.md)
  The natural pixel dimensions of the video content for display purposes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avinterfacemetadata-swift.struct/albumartworkrepresentations)*