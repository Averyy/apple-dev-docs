# Deprecated symbols

**Framework**: AppKit

Review symbols that are no longer in active development, and their recommended replacements.

#### Overview

Although these symbols are available for use, Apple is no longer actively developing them, and may remove them in a future release. Apple recommends moving away from these symbols and using their indicated replacements instead. Check the individual symbol pages for the recommended replacements.

## Topics

### Deprecated methods
- [func helpRequested(with: NSEvent)](nsmenu/helprequested(with:).md)
  Overridden by subclasses to implement specialized context-sensitive help behavior.
- [class func menuZone() -> NSZone!](nsmenu/menuzone.md)
  Returns the zone from which `NSMenu` objects should be allocated.
### Deprecated properties
- [var isTornOff: Bool](nsmenu/istornoff.md)
  Indicates whether the menu is offscreen or attached to another menu (or if it’s the main menu).
- [var menuChangedMessagesEnabled: Bool](nsmenu/menuchangedmessagesenabled.md)
  Indicates whether messages are sent to the application’s windows each time the menu changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenu-deprecated-symbols)*