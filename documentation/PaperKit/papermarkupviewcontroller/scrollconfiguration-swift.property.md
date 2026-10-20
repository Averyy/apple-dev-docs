# scrollConfiguration

**Framework**: PaperKit  
**Kind**: property  
**Role**: Instance Property

The configuration object that provides access to scroll view functionality.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
@MainActor
@preconcurrency var scrollConfiguration: PaperMarkupViewController.ScrollConfiguration { get }
```

## See Also

### Scrolling and zooming
- [PaperMarkupViewController.ScrollConfiguration](./scrollconfiguration-swift.class.md)
  A cross-platform type that provides access to scroll view functionality.
- [var contentVisibleFrame: CGRect](./contentvisibleframe.md)
  The visible area of content in the scroll view.
- [func setContentVisibleFrame(CGRect, animated: Bool)](./setcontentvisibleframe%28_,animated%29.md)
  Zooms to a specific area of the content so that it’s visible in the scroll view.
- [var zoomRange: ClosedRange<CGFloat>](./zoomrange.md)
  A floating-point range that specifies the minimum and maximum scale factor that can apply to the canvas’ content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/papermarkupviewcontroller/scrollconfiguration-swift.property)*