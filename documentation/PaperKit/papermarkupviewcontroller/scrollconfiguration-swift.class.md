# PaperMarkupViewController.ScrollConfiguration

**Framework**: PaperKit  
**Kind**: class  
**Role**: Class

A cross-platform type that provides access to scroll view functionality.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
final class ScrollConfiguration
```

## Topics

### Configuring scroll indicators
- [var visibleScrollIndicators: PaperMarkupViewController.ScrollConfiguration.Axis](./scrollconfiguration-swift.class/visiblescrollindicators.md)
  The axes for which scroll indicators are visible.
- [PaperMarkupViewController.ScrollConfiguration.Axis](./scrollconfiguration-swift.class/axis.md)
  The axes you use to specify scroll view behavior.
### Configuring bouncing behavior
- [var bounces: PaperMarkupViewController.ScrollConfiguration.Axis](./scrollconfiguration-swift.class/bounces.md)
  The axes for which the scroll view bounces past the edge of content and back again.
- [var alwaysBounces: PaperMarkupViewController.ScrollConfiguration.Axis](./scrollconfiguration-swift.class/alwaysbounces.md)
  The axes for which bouncing always occurs when scrolling reaches the end of the content.
- [var bouncesZoom: Bool](./scrollconfiguration-swift.class/bounceszoom.md)
  A Boolean value that controls whether the scroll view animates the content scaling when the scaling exceeds the maximum or minimum limits.
### Configuring content insets
- [var contentInset: NSEdgeInsets](./scrollconfiguration-swift.class/contentinset-1ktjn.md)
  The custom distance to inset the content view from the scroll view edges.
- [var contentInset: UIEdgeInsets](./scrollconfiguration-swift.class/contentinset-3vn4v.md)
  The custom distance to inset the content view from the safe area or scroll view edges.
- [var adjustedContentInset: UIEdgeInsets](./scrollconfiguration-swift.class/adjustedcontentinset.md)
  The insets that the system derives from the content insets and safe area insets.
- [var contentInsetAdjustmentBehavior: UIScrollView.ContentInsetAdjustmentBehavior](./scrollconfiguration-swift.class/contentinsetadjustmentbehavior.md)
  The behavior for determining the adjusted content inset.
### Configuring scroll state
- [var isScrollEnabled: Bool](./scrollconfiguration-swift.class/isscrollenabled.md)
  A Boolean value that determines whether scrolling is enabled.
- [var isDirectionalLockEnabled: Bool](./scrollconfiguration-swift.class/isdirectionallockenabled.md)
  A Boolean value that determines whether scrolling is disabled in a particular direction.
- [var scrollsToTop: Bool](./scrollconfiguration-swift.class/scrollstotop.md)
  A Boolean value that controls whether the scroll-to-top gesture is enabled.
### Configuring scroll indicator insets
- [var verticalScrollIndicatorInsets: NSEdgeInsets](./scrollconfiguration-swift.class/verticalscrollindicatorinsets-4gy4y.md)
  The vertical scroll indicator’s insets.
- [var verticalScrollIndicatorInsets: UIEdgeInsets](./scrollconfiguration-swift.class/verticalscrollindicatorinsets-79jxb.md)
  The vertical scroll indicator’s insets.
- [var horizontalScrollIndicatorInsets: UIEdgeInsets](./scrollconfiguration-swift.class/horizontalscrollindicatorinsets-5nzvz.md)
  The horizontal scroll indicator’s insets.
- [var horizontalScrollIndicatorInsets: NSEdgeInsets](./scrollconfiguration-swift.class/horizontalscrollindicatorinsets-6inpv.md)
  The horizontal scroll indicator’s insets.
### Configuring zoom scale
- [var zoomScale: CGFloat](./scrollconfiguration-swift.class/zoomscale.md)
  The current scale factor applied to the scroll view’s content.

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [Escapable](../../Swift/escapable.md)
- [Observable](../../Observation/observable.md)

## See Also

### Scrolling and zooming
- [var scrollConfiguration: PaperMarkupViewController.ScrollConfiguration](./scrollconfiguration-swift.property.md)
  The configuration object that provides access to scroll view functionality.
- [var contentVisibleFrame: CGRect](./contentvisibleframe.md)
  The visible area of content in the scroll view.
- [func setContentVisibleFrame(CGRect, animated: Bool)](./setcontentvisibleframe%28_,animated%29.md)
  Zooms to a specific area of the content so that it’s visible in the scroll view.
- [var zoomRange: ClosedRange<CGFloat>](./zoomrange.md)
  A floating-point range that specifies the minimum and maximum scale factor that can apply to the canvas’ content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/papermarkupviewcontroller/scrollconfiguration-swift.class)*