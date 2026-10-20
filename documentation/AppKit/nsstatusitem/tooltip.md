# toolTip

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The tool tip string that is displayed when the cursor pauses over the status item.

**Availability**:
- macOS 10.0+ - Deprecated in 10.14

> **Deprecated**: Use the [`button`](./button.md) property.

## Declaration

```swift
var toolTip: String? { get set }
```

```objc
@property (copy, nullable) NSString * toolTip;
```

## See Also

### Deprecated properties
- [var isEnabled: Bool](./isenabled.md)
  A Boolean that indicates whether the status item is enabled to respond to clicks.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsstatusitem/tooltip)*