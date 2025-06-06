# doubleAction

**Framework**: AppKit  
**Kind**: property

The selector that is sent to the status item’s target when the status item is double-clicked.

**Availability**:
- macOS 10.0+

## Declaration

```swift
var doubleAction: Selector? { get set }
```

## See Also

- [var isEnabled: Bool](nsstatusitem/isenabled.md)
  A Boolean that indicates whether the status item is enabled to respond to clicks.
- [var target: AnyObject?](nsstatusitem/target.md)
  The target object to which the status item’s action message is sent when the status item is clicked.
- [var action: Selector?](nsstatusitem/action.md)
  The selector that is sent to the status item’s target when the status item is clicked.
- [func sendAction(on: NSEvent.EventTypeMask) -> Int](nsstatusitem/sendaction(on:).md)
  Sets the conditions on which the status item sends action messages to its target.
- [func popUpMenu(NSMenu)](nsstatusitem/popupmenu(_:).md)
  Displays a menu under a custom status bar item.
- [var title: String?](nsstatusitem/title.md)
  The string that is displayed at the status item’s position in the status bar.
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
- [var view: NSView?](nsstatusitem/view.md)
  The custom view that is displayed at the status item’s position in the status bar.
- [func drawStatusBarBackground(in: NSRect, withHighlight: Bool)](nsstatusitem/drawstatusbarbackground(in:withhighlight:).md)
  Draws the menu background pattern for a custom status-bar item in regular or highlight pattern.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsstatusitem/doubleaction)*