# UIModalPresentationStyle.none

**Framework**: UIKit  
**Kind**: case

A presentation style that indicates no adaptations should be made.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
case none
```

#### Discussion

Do not use this style to present a view controller. Instead, return it from the [`adaptivePresentationStyle(for:)`](uiadaptivepresentationcontrollerdelegate/adaptivepresentationstyle(for:).md) method of an adaptive delegate when you do not want a presentation controller to adapt the style of an already presented view controller.

## See Also

- [UIModalPresentationStyle.automatic](uimodalpresentationstyle/automatic.md)
  The default presentation style chosen by the system.
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
- [UIModalPresentationStyle.popover](uimodalpresentationstyle/popover.md)
  A presentation style where the content is displayed in a popover view.
- [UIModalPresentationStyle.blurOverFullScreen](uimodalpresentationstyle/bluroverfullscreen.md)
  A presentation style that blurs the underlying content before displaying new content in a full-screen presentation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uimodalpresentationstyle/none)*