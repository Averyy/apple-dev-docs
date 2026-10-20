# zoomRange

**Framework**: PaperKit  
**Kind**: property  
**Role**: Instance Property

A floating-point range that specifies the minimum and maximum scale factor that can apply to the canvas’ content.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
@MainActor
@preconcurrency var zoomRange: ClosedRange<CGFloat> { get set }
```

#### Discussion

The default value is `1.0...1.0`.

## See Also

### Scrolling and zooming
- [var scrollConfiguration: PaperMarkupViewController.ScrollConfiguration](./scrollconfiguration-swift.property.md)
  The configuration object that provides access to scroll view functionality.
- [PaperMarkupViewController.ScrollConfiguration](./scrollconfiguration-swift.class.md)
  A cross-platform type that provides access to scroll view functionality.
- [var contentVisibleFrame: CGRect](./contentvisibleframe.md)
  The visible area of content in the scroll view.
- [func setContentVisibleFrame(CGRect, animated: Bool)](./setcontentvisibleframe%28_,animated%29.md)
  Zooms to a specific area of the content so that it’s visible in the scroll view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/papermarkupviewcontroller/zoomrange)*