# UIModalPresentationStyle.overCurrentContext

**Framework**: UIKit  
**Kind**: case  
**Role**: Case

A presentation style where the content is displayed over another view controller’s content.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
case overCurrentContext
```

```c
UIModalPresentationOverCurrentContext
```

## Discussion

Using this presentation style, the current view controller’s content is displayed over the view controller whose [`definesPresentationContext`](../uiviewcontroller/definespresentationcontext.md) property is [`true`](../../Swift/true.md). UIKit may walk up the view controller hierarchy to find a view controller that wants to define the presentation context. The views beneath the presented content are not removed from the view hierarchy when the presentation finishes. So if the presented view controller does not fill the screen with opaque content, the underlying content shows through.

When presenting a view controller in a popover, this presentation style is supported only if the transition style is [`UIModalTransitionStyle.coverVertical`](../uimodaltransitionstyle/coververtical.md). Attempting to use a different transition style triggers an exception. However, you may use other transition styles (except the partial curl transition) if the parent view controller is not in a popover.

## See Also

### Presentations
- [UIModalPresentationStyle.automatic](./automatic.md)
  The default presentation style chosen by the system.
- [UIModalPresentationStyle.none](./none.md)
  A presentation style that indicates no adaptations should be made.
- [UIModalPresentationStyle.fullScreen](./fullscreen.md)
  A presentation style in which the presented view covers the screen.
- [UIModalPresentationStyle.pageSheet](./pagesheet.md)
  A presentation style that partially covers the underlying content.
- [UIModalPresentationStyle.formSheet](./formsheet.md)
  A presentation style that displays the content centered in the screen.
- [UIModalPresentationStyle.currentContext](./currentcontext.md)
  A presentation style where the content is displayed over another view controller’s content.
- [UIModalPresentationStyle.custom](./custom.md)
  A custom view presentation style that is managed by a custom presentation controller and one or more custom animator objects.
- [UIModalPresentationStyle.overFullScreen](./overfullscreen.md)
  A view presentation style in which the presented view covers the screen.
- [UIModalPresentationStyle.popover](./popover.md)
  A presentation style where the content is displayed in a popover view.
- [UIModalPresentationStyle.blurOverFullScreen](./bluroverfullscreen.md)
  A presentation style that blurs the underlying content before displaying new content in a full-screen presentation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uimodalpresentationstyle/overcurrentcontext)*