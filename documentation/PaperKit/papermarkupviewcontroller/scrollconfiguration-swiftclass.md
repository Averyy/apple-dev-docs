# PaperMarkupViewController.ScrollConfiguration

**Framework**: PaperKit  
**Kind**: class

A cross-platform type that provides access to scroll view functionality.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
final class ScrollConfiguration
```

## Topics

### Configuring scroll indicators
- [var visibleScrollIndicators: PaperMarkupViewController.ScrollConfiguration.Axis](papermarkupviewcontroller/scrollconfiguration-swift.class/visiblescrollindicators.md)
  The axes for which scroll indicators are visible.
- [PaperMarkupViewController.ScrollConfiguration.Axis](papermarkupviewcontroller/scrollconfiguration-swift.class/axis.md)
  The axes you use to specify scroll view behavior.
### Configuring bouncing behavior
- [var bounces: PaperMarkupViewController.ScrollConfiguration.Axis](papermarkupviewcontroller/scrollconfiguration-swift.class/bounces.md)
  The axes for which the scroll view bounces past the edge of content and back again.
- [var alwaysBounces: PaperMarkupViewController.ScrollConfiguration.Axis](papermarkupviewcontroller/scrollconfiguration-swift.class/alwaysbounces.md)
  The axes for which bouncing always occurs when scrolling reaches the end of the content.
- [var bouncesZoom: Bool](papermarkupviewcontroller/scrollconfiguration-swift.class/bounceszoom.md)
  A Boolean value that controls whether the scroll view animates the content scaling when the scaling exceeds the maximum or minimum limits.
### Configuring content insets
- [var contentInset: NSEdgeInsets](papermarkupviewcontroller/scrollconfiguration-swift.class/contentinset-1ktjn.md)
  The custom distance to inset the content view from the scroll view edges.
- [var contentInset: UIEdgeInsets](papermarkupviewcontroller/scrollconfiguration-swift.class/contentinset-3vn4v.md)
  The custom distance to inset the content view from the safe area or scroll view edges.
- [var adjustedContentInset: UIEdgeInsets](papermarkupviewcontroller/scrollconfiguration-swift.class/adjustedcontentinset.md)
  The insets that the system derives from the content insets and safe area insets.
- [var contentInsetAdjustmentBehavior: UIScrollView.ContentInsetAdjustmentBehavior](papermarkupviewcontroller/scrollconfiguration-swift.class/contentinsetadjustmentbehavior.md)
  The behavior for determining the adjusted content inset.
### Configuring scroll state
- [var isScrollEnabled: Bool](papermarkupviewcontroller/scrollconfiguration-swift.class/isscrollenabled.md)
  A Boolean value that determines whether scrolling is enabled.
- [var isDirectionalLockEnabled: Bool](papermarkupviewcontroller/scrollconfiguration-swift.class/isdirectionallockenabled.md)
  A Boolean value that determines whether scrolling is disabled in a particular direction.
- [var scrollsToTop: Bool](papermarkupviewcontroller/scrollconfiguration-swift.class/scrollstotop.md)
  A Boolean value that controls whether the scroll-to-top gesture is enabled.
### Configuring scroll indicator insets
- [var verticalScrollIndicatorInsets: NSEdgeInsets](papermarkupviewcontroller/scrollconfiguration-swift.class/verticalscrollindicatorinsets-4gy4y.md)
  The vertical scroll indicator’s insets.
- [var verticalScrollIndicatorInsets: UIEdgeInsets](papermarkupviewcontroller/scrollconfiguration-swift.class/verticalscrollindicatorinsets-79jxb.md)
  The vertical scroll indicator’s insets.
- [var horizontalScrollIndicatorInsets: UIEdgeInsets](papermarkupviewcontroller/scrollconfiguration-swift.class/horizontalscrollindicatorinsets-5nzvz.md)
  The horizontal scroll indicator’s insets.
- [var horizontalScrollIndicatorInsets: NSEdgeInsets](papermarkupviewcontroller/scrollconfiguration-swift.class/horizontalscrollindicatorinsets-6inpv.md)
  The horizontal scroll indicator’s insets.
### Configuring zoom scale
- [var zoomScale: CGFloat](papermarkupviewcontroller/scrollconfiguration-swift.class/zoomscale.md)
  The current scale factor applied to the scroll view’s content.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Escapable](../Swift/Escapable.md)
- [Observable](../Observation/Observable.md)

## See Also

- [var scrollConfiguration: PaperMarkupViewController.ScrollConfiguration](papermarkupviewcontroller/scrollconfiguration-swift.property.md)
  The configuration object that provides access to scroll view functionality.
- [var contentVisibleFrame: CGRect](papermarkupviewcontroller/contentvisibleframe.md)
  The visible area of content in the scroll view.
- [func setContentVisibleFrame(CGRect, animated: Bool)](papermarkupviewcontroller/setcontentvisibleframe(_:animated:).md)
  Zooms to a specific area of the content so that it’s visible in the scroll view.
- [var zoomRange: ClosedRange<CGFloat>](papermarkupviewcontroller/zoomrange.md)
  A floating-point range that specifies the minimum and maximum scale factor that can apply to the canvas’ content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/papermarkupviewcontroller/scrollconfiguration-swift.class)*