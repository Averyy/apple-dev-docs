# bounces

**Framework**: PaperKit  
**Kind**: property

The axes for which the scroll view bounces past the edge of content and back again.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
final var bounces: PaperMarkupViewController.ScrollConfiguration.Axis { get set }
```

#### Discussion

Default is `[.vertical, .horizontal]`.

## See Also

- [var alwaysBounces: PaperMarkupViewController.ScrollConfiguration.Axis](papermarkupviewcontroller/scrollconfiguration-swift.class/alwaysbounces.md)
  The axes for which bouncing always occurs when scrolling reaches the end of the content.
- [var bouncesZoom: Bool](papermarkupviewcontroller/scrollconfiguration-swift.class/bounceszoom.md)
  A Boolean value that controls whether the scroll view animates the content scaling when the scaling exceeds the maximum or minimum limits.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/papermarkupviewcontroller/scrollconfiguration-swift.class/bounces)*