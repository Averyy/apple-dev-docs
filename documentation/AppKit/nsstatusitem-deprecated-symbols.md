# Deprecated symbols

**Framework**: AppKit  
**Role**: API Collection

Review symbols that are no longer in active development, and their recommended replacements.

## Overview

Although these symbols are available for use, Apple is no longer actively developing them, and may remove them in a future release. Apple recommends moving away from these symbols and using their indicated replacements instead. Check the individual symbol pages for the recommended replacements.

## Topics

### Deprecated methods
- [func sendAction(on: NSEvent.EventTypeMask) -> Int](./nsstatusitem/sendaction%28on%29.md)
  Sets the conditions on which the status item sends action messages to its target.
- [func popUpMenu(NSMenu)](./nsstatusitem/popupmenu%28_%29.md)
  Displays a menu under a custom status bar item.
- [func drawStatusBarBackground(in: NSRect, withHighlight: Bool)](./nsstatusitem/drawstatusbarbackground%28in,withhighlight%29.md)
  Draws the menu background pattern for a custom status-bar item in regular or highlight pattern.
### Deprecated properties
- [var isEnabled: Bool](./nsstatusitem/isenabled.md)
  A Boolean that indicates whether the status item is enabled to respond to clicks.
- [var doubleAction: Selector?](./nsstatusitem/doubleaction.md)
  The selector that is sent to the status item’s target when the status item is double-clicked.
- [var title: String?](./nsstatusitem/title.md)
  The string that is displayed at the status item’s position in the status bar.
- [var attributedTitle: NSAttributedString?](./nsstatusitem/attributedtitle.md)
  The attributed string that is displayed at the status item’s position in the status bar.
- [var image: NSImage?](./nsstatusitem/image.md)
  The image that is displayed at the status item’s position in the status bar.
- [var alternateImage: NSImage?](./nsstatusitem/alternateimage.md)
  The alternate image to be displayed when a status bar item is highlighted.
- [var highlightMode: Bool](./nsstatusitem/highlightmode.md)
  A Boolean that indicates whether the status item is highlighted when it is clicked.
- [var toolTip: String?](./nsstatusitem/tooltip.md)
  The tool tip string that is displayed when the cursor pauses over the status item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsstatusitem-deprecated-symbols)*