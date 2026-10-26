# artworkRepresentations

**Framework**: AVKit  
**Kind**: property  
**Role**: Instance Property

Array of available artwork representations in various formats and sizes for this media content. Multiple representations allow the system to choose the most appropriate artwork for different display contexts (thumbnails, full-screen, high-DPI displays). Each representation specifies its dimensions, format, and URL for optimal loading and display performance.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```objc
@property (nonatomic, copy, readwrite) NSArray<AVPlaybackUserInterfaceContentArtwork *> * artworkRepresentations;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplaybackuserinterfacecontentmetadatatemplate/artworkrepresentations)*