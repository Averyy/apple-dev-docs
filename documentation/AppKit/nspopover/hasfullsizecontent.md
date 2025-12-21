# hasFullSizeContent

**Framework**: AppKit  
**Kind**: property

A Boolean value that indicates whether the content view of the popover extends into the arrow region.

**Availability**:
- macOS 14.0+

## Declaration

```swift
@MainActor
var hasFullSizeContent: Bool { get set }
```

#### Discussion

Setting the value of this property to [`true`](https://developer.apple.com/documentation/Swift/true) extends the frame of the content view by the height of the arrow region on all four sides of the frame. This causes the [`contentViewController`](nspopover/contentviewcontroller.md) view to extend to the window’s bounds.

![A diagram that shows the safe area layout guide covering an entire window — including the arrow region along the edge at the top.](https://docs-assets.developer.apple.com/published/f5de80659170e982eeae9fc31f84f0f1/media-4304810%402x.png)

Use the [`safeAreaLayoutGuide`](nsview/safearealayoutguide.md) of the [`contentViewController`](nspopover/contentviewcontroller.md) view to ensure that your content is fully visible and doesn’t become clipped when displayed.

![A diagram that shows the safe area layout guide all the the window area except the arrow region along the top edge.](https://docs-assets.developer.apple.com/published/bdf177c3528c4e2abc109757ae5004e9/media-4304811%402x.png)

Setting this value to [`false`](https://developer.apple.com/documentation/Swift/false) doesn’t extend the [`contentViewController`](nspopover/contentviewcontroller.md) view fully into the arrow region. The default value for this property is [`false`](https://developer.apple.com/documentation/Swift/false).

![A diagram that shows the safe area layout guide covering most of a window area. It extends fully to three of the four sides of the window, but doesn’t cover the arrow region along the top.](https://docs-assets.developer.apple.com/published/23bb3a878c1614af970edc681e850ecc/media-4304812%402x.png)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopover/hasfullsizecontent)*