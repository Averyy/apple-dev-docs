# UIModalPresentationStyle.currentContext

**Framework**: UIKit  
**Kind**: case  
**Role**: Case

A presentation style where the content is displayed over another view controller’s content.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
case currentContext
```

```c
UIModalPresentationCurrentContext
```

#### Discussion

Using this presentation style, the current view controller’s content is displayed over the view controller whose [`definesPresentationContext`](../uiviewcontroller/definespresentationcontext.md) property is [`true`](../../Swift/true.md). UIKit may walk up the view controller hierarchy to find a view controller that wants to define the presentation context. The views belonging to the presenting view controller are removed after the presentation completes.

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
- [UIModalPresentationStyle.custom](./custom.md)
  A custom view presentation style that is managed by a custom presentation controller and one or more custom animator objects.
- [UIModalPresentationStyle.overFullScreen](./overfullscreen.md)
  A view presentation style in which the presented view covers the screen.
- [UIModalPresentationStyle.overCurrentContext](./overcurrentcontext.md)
  A presentation style where the content is displayed over another view controller’s content.
- [UIModalPresentationStyle.popover](./popover.md)
  A presentation style where the content is displayed in a popover view.
- [UIModalPresentationStyle.blurOverFullScreen](./bluroverfullscreen.md)
  A presentation style that blurs the underlying content before displaying new content in a full-screen presentation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uimodalpresentationstyle/currentcontext)*