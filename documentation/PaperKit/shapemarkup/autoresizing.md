# autoresizing

**Framework**: PaperKit  
**Kind**: property

Automatic sizing behaviors for this markup.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var autoresizing: MarkupAutoresizing { get set }
```

#### Discussion

Controls whether the markup automatically adjusts its dimensions to fit content changes.

> **Note**: The layout mode (centered vs. top-anchored) is decided at init time and preserved across reassignment; setting `.flexibleHeight` here on a shape that didn’t have `.flexibleHeight` at init will use the legacy top-anchored layout. New shapes should express the mode through `init(...autoresizing:)` instead.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/shapemarkup/autoresizing)*