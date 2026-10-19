# title

**Framework**: AppKit  
**Kind**: property

The string that is displayed at the status item’s position in the status bar.

**Availability**:
- macOS 10.0+

## Declaration

```swift
var title: String? { get set }
```

#### Discussion

If an image is also set, the title appears to the right of the image.

## See Also

- [var isEnabled: Bool](nsstatusitem/isenabled.md)
  A Boolean that indicates whether the status item is enabled to respond to clicks.
- [var doubleAction: Selector?](nsstatusitem/doubleaction.md)
  The selector that is sent to the status item’s target when the status item is double-clicked.
- [var attributedTitle: NSAttributedString?](nsstatusitem/attributedtitle.md)
  The attributed string that is displayed at the status item’s position in the status bar.
- [var image: NSImage?](nsstatusitem/image.md)
  The image that is displayed at the status item’s position in the status bar.
- [var alternateImage: NSImage?](nsstatusitem/alternateimage.md)
  The alternate image to be displayed when a status bar item is highlighted.
- [var highlightMode: Bool](nsstatusitem/highlightmode.md)
  A Boolean that indicates whether the status item is highlighted when it is clicked.
- [var toolTip: String?](nsstatusitem/tooltip.md)
  The tool tip string that is displayed when the cursor pauses over the status item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsstatusitem/title)*