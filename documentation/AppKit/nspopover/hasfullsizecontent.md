# hasFullSizeContent

**Framework**: AppKit  
**Kind**: property

A Boolean value that indicates whether the content view of the popover extends into the arrow region.

**Availability**:
- macOS 14.0+

## Declaration

```swift
var hasFullSizeContent: Bool { get set }
```

#### Discussion

Setting the value of this property to [`true`](https://developer.apple.com/documentation/swift/true) extends the frame of the content view by the height of the arrow region on all four sides of the frame. This causes the [`contentViewController`](nspopover/contentviewcontroller.md) view to extend to the window’s bounds.

![A diagram that shows the safe area layout guide covering an entire window — including the arrow region along the edge at the top.](/images/com.apple.appkit/media-4304810@2x.png)

Use the [`safeAreaLayoutGuide`](nsview/safearealayoutguide.md) of the [`contentViewController`](nspopover/contentviewcontroller.md) view to ensure that your content is fully visible and doesn’t become clipped when displayed.

![A diagram that shows the safe area layout guide all the the window area except the arrow region along the top edge.](/images/com.apple.appkit/media-4304811@2x.png)

Setting this value to [`false`](https://developer.apple.com/documentation/swift/false) doesn’t extend the [`contentViewController`](nspopover/contentviewcontroller.md) view fully into the arrow region. The default value for this property is [`false`](https://developer.apple.com/documentation/swift/false).

![A diagram that shows the safe area layout guide covering most of a window area. It extends fully to three of the four sides of the window, but doesn’t cover the arrow region along the top.](/images/com.apple.appkit/media-4304812@2x.png)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopover/hasfullsizecontent)*