# UIModalPresentationStyle.popover

**Framework**: UIKit  
**Kind**: case

A presentation style where the content is displayed in a popover view.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
case popover
```

#### Discussion

In a horizontally regular environment, this style displays the view controller in a popover view. The background content is dimmed and taps outside the popover cause the popover to be dismissed. If you do not want taps to dismiss the popover, you can assign one or more views to the [`passthroughViews`](uipopoverpresentationcontroller/passthroughviews.md) property of the associated [`UIPopoverPresentationController`](uipopoverpresentationcontroller.md) object, which you can get from the [`popoverPresentationController`](uiviewcontroller/popoverpresentationcontroller.md) property.

In iOS 13 and later, for horizontally or vertically compact environments, this option behaves the same as [`UIModalPresentationStyle.formSheet`](uimodalpresentationstyle/formsheet.md).

In iOS 12 and earlier:

- For horizontally compact environments, this option behaves the same as [`UIModalPresentationStyle.fullScreen`](uimodalpresentationstyle/fullscreen.md).
- For horizontally regular and vertically compact environments, this option behaves the same as [`UIModalPresentationStyle.formSheet`](uimodalpresentationstyle/formsheet.md).

For more information about horizontal and vertical size classes, see [`UIUserInterfaceSizeClass`](uiuserinterfacesizeclass.md).

## See Also

- [UIModalPresentationStyle.automatic](uimodalpresentationstyle/automatic.md)
  The default presentation style chosen by the system.
- [UIModalPresentationStyle.none](uimodalpresentationstyle/none.md)
  A presentation style that indicates no adaptations should be made.
- [UIModalPresentationStyle.fullScreen](uimodalpresentationstyle/fullscreen.md)
  A presentation style in which the presented view covers the screen.
- [UIModalPresentationStyle.pageSheet](uimodalpresentationstyle/pagesheet.md)
  A presentation style that partially covers the underlying content.
- [UIModalPresentationStyle.formSheet](uimodalpresentationstyle/formsheet.md)
  A presentation style that displays the content centered in the screen.
- [UIModalPresentationStyle.currentContext](uimodalpresentationstyle/currentcontext.md)
  A presentation style where the content is displayed over another view controller’s content.
- [UIModalPresentationStyle.custom](uimodalpresentationstyle/custom.md)
  A custom view presentation style that is managed by a custom presentation controller and one or more custom animator objects.
- [UIModalPresentationStyle.overFullScreen](uimodalpresentationstyle/overfullscreen.md)
  A view presentation style in which the presented view covers the screen.
- [UIModalPresentationStyle.overCurrentContext](uimodalpresentationstyle/overcurrentcontext.md)
  A presentation style where the content is displayed over another view controller’s content.
- [UIModalPresentationStyle.blurOverFullScreen](uimodalpresentationstyle/bluroverfullscreen.md)
  A presentation style that blurs the underlying content before displaying new content in a full-screen presentation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uimodalpresentationstyle/popover)*