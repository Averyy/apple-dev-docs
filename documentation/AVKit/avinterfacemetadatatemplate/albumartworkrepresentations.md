# albumArtworkRepresentations

**Framework**: AVKit  
**Kind**: property  
**Role**: Instance Property

Array of available album artwork representations in various formats and sizes for this media content. Multiple representations allow the system to choose the most appropriate artwork for different display contexts (thumbnails, full-screen, high-DPI displays). Each representation specifies its dimensions, format, and URL for optimal loading and display performance.

## Declaration

```objc
@property (nonatomic, copy, readwrite) NSArray<AVInterfaceAlbumArtwork *> * albumArtworkRepresentations;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avinterfacemetadatatemplate/albumartworkrepresentations)*