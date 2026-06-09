# setContentVisibleFrame(_:animated:)

**Framework**: PaperKit  
**Kind**: method

Zooms to a specific area of the content so that it’s visible in the scroll view.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
@MainActor
@preconcurrency func setContentVisibleFrame(_ rect: CGRect, animated: Bool)
```

#### Discussion

- rect: A rectangle defining an area of the content view. The rectangle should be in the coordinate space of the data model.
- animated: `true` if the scrolling should be animated, `false` if it should be immediate.

This method scrolls the content so that the area defined by rect is just visible. If the area is already visible, the method does nothing.

## See Also

- [var scrollConfiguration: PaperMarkupViewController.ScrollConfiguration](papermarkupviewcontroller/scrollconfiguration-swift.property.md)
  The configuration object that provides access to scroll view functionality.
- [PaperMarkupViewController.ScrollConfiguration](papermarkupviewcontroller/scrollconfiguration-swift.class.md)
  A cross-platform type that provides access to scroll view functionality.
- [var contentVisibleFrame: CGRect](papermarkupviewcontroller/contentvisibleframe.md)
  The visible area of content in the scroll view.
- [var zoomRange: ClosedRange<CGFloat>](papermarkupviewcontroller/zoomrange.md)
  A floating-point range that specifies the minimum and maximum scale factor that can apply to the canvas’ content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/papermarkupviewcontroller/setcontentvisibleframe(_:animated:))*