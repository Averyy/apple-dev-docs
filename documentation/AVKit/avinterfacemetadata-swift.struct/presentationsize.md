# presentationSize

**Framework**: AVKit  
**Kind**: property

The natural pixel dimensions of the video content for display purposes.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
var presentationSize: CGSize
```

#### Discussion

This represents the encoded size of the video stream and can be used to determine aspect ratio and optimal presentation layout. For audio-only content, this value is `.zero`.

## See Also

- [var title: String?](avinterfacemetadata-swift.struct/title.md)
  Primary title or name of the media content.
- [var subtitle: String?](avinterfacemetadata-swift.struct/subtitle.md)
  Secondary descriptive text such as artist name or episode description.
- [var isAudioOnly: Bool](avinterfacemetadata-swift.struct/isaudioonly.md)
  Indicates whether the content is audio-only (no video component).
- [var albumArtworkRepresentations: [AVInterfaceAlbumArtwork]](avinterfacemetadata-swift.struct/albumartworkrepresentations.md)
  Array of available album artwork representations in various formats and sizes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avinterfacemetadata-swift.struct/presentationsize)*