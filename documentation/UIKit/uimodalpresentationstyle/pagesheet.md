# UIModalPresentationStyle.pageSheet

**Framework**: UIKit  
**Kind**: case  
**Role**: Case

A presentation style that partially covers the underlying content.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
case pageSheet
```

```c
UIModalPresentationPageSheet
```

#### Discussion

In a regular-width, regular-height size class, the system adds a dimming layer over the background content and centers the view controller’s content on top of this layer. The content is roughly the size of a page, where the height is greater than the width. The actual dimensions vary depending on several factors including the device’s screen size and orientation. A part of the background content always remains visible.

To provide a custom content size, use the [`UIModalPresentationStyle.formSheet`](./formsheet.md) style instead, and set the modal view controller’s [`preferredContentSize`](../uiviewcontroller/preferredcontentsize.md) property.

In a compact-width, regular-height size class, the system displays the view controller as a sheet with part of the background content visible near the top of the screen.

In a compact-height size class, the behavior is the same as [`UIModalPresentationStyle.fullScreen`](./fullscreen.md).

Where the background content remains visible, the system doesn’t call the presenting view controller’s [`viewWillDisappear(_:)`](../uiviewcontroller/viewwilldisappear%28_%29.md) and [`viewDidDisappear(_:)`](../uiviewcontroller/viewdiddisappear%28_%29.md) methods.

## See Also

### Presentations
- [UIModalPresentationStyle.automatic](./automatic.md)
  The default presentation style chosen by the system.
- [UIModalPresentationStyle.none](./none.md)
  A presentation style that indicates no adaptations should be made.
- [UIModalPresentationStyle.fullScreen](./fullscreen.md)
  A presentation style in which the presented view covers the screen.
- [UIModalPresentationStyle.formSheet](./formsheet.md)
  A presentation style that displays the content centered in the screen.
- [UIModalPresentationStyle.currentContext](./currentcontext.md)
  A presentation style where the content is displayed over another view controller’s content.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uimodalpresentationstyle/pagesheet)*