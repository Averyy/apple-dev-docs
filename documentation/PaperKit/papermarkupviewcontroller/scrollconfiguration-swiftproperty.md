# scrollConfiguration

**Framework**: PaperKit  
**Kind**: property

The configuration object that provides access to scroll view functionality.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
@MainActor
@preconcurrency var scrollConfiguration: PaperMarkupViewController.ScrollConfiguration { get }
```

## See Also

- [PaperMarkupViewController.ScrollConfiguration](papermarkupviewcontroller/scrollconfiguration-swift.class.md)
  A cross-platform type that provides access to scroll view functionality.
- [var contentVisibleFrame: CGRect](papermarkupviewcontroller/contentvisibleframe.md)
  The visible area of content in the scroll view.
- [func setContentVisibleFrame(CGRect, animated: Bool)](papermarkupviewcontroller/setcontentvisibleframe(_:animated:).md)
  Zooms to a specific area of the content so that it’s visible in the scroll view.
- [var zoomRange: ClosedRange<CGFloat>](papermarkupviewcontroller/zoomrange.md)
  A floating-point range that specifies the minimum and maximum scale factor that can apply to the canvas’ content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/papermarkupviewcontroller/scrollconfiguration-swift.property)*