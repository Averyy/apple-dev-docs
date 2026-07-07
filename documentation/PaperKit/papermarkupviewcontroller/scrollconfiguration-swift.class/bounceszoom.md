# bouncesZoom

**Framework**: PaperKit  
**Kind**: property

A Boolean value that controls whether the scroll view animates the content scaling when the scaling exceeds the maximum or minimum limits.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
final var bouncesZoom: Bool { get set }
```

#### Discussion

When enabled, a person can zoom past the minimum or maximum scale while gesturing, and the scale animates to the minimum or maximum value when the gesture ends. Default is `true`.

## See Also

- [var bounces: PaperMarkupViewController.ScrollConfiguration.Axis](papermarkupviewcontroller/scrollconfiguration-swift.class/bounces.md)
  The axes for which the scroll view bounces past the edge of content and back again.
- [var alwaysBounces: PaperMarkupViewController.ScrollConfiguration.Axis](papermarkupviewcontroller/scrollconfiguration-swift.class/alwaysbounces.md)
  The axes for which bouncing always occurs when scrolling reaches the end of the content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/papermarkupviewcontroller/scrollconfiguration-swift.class/bounceszoom)*