# isEnabled

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean that indicates whether the status item is enabled to respond to clicks.

**Availability**:
- macOS 10.0+ - Deprecated in 10.14

> **Deprecated**: Use the [`button`](./button.md) property.

## Declaration

```swift
var isEnabled: Bool { get set }
```

```objc
@property (getter=isEnabled) BOOL enabled;
```

## See Also

### Deprecated properties
- [var doubleAction: Selector?](./doubleaction.md)
  The selector that is sent to the status item’s target when the status item is double-clicked.
- [var title: String?](./title.md)
  The string that is displayed at the status item’s position in the status bar.
- [var attributedTitle: NSAttributedString?](./attributedtitle.md)
  The attributed string that is displayed at the status item’s position in the status bar.
- [var image: NSImage?](./image.md)
  The image that is displayed at the status item’s position in the status bar.
- [var alternateImage: NSImage?](./alternateimage.md)
  The alternate image to be displayed when a status bar item is highlighted.
- [var highlightMode: Bool](./highlightmode.md)
  A Boolean that indicates whether the status item is highlighted when it is clicked.
- [var toolTip: String?](./tooltip.md)
  The tool tip string that is displayed when the cursor pauses over the status item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsstatusitem/isenabled)*