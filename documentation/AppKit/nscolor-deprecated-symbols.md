# Deprecated symbols

**Framework**: AppKit  
**Role**: API Collection

Review symbols that are no longer in active development, and their recommended replacements.

## Overview

Although these symbols are available for use, Apple is no longer actively developing them, and may remove them in a future release. Apple recommends moving away from these symbols and using their indicated replacements instead. Check the individual symbol pages for the recommended replacements.

## Topics

### Deprecated initializers
- [init(forControlTint: NSControlTint)](./nscolor/init%28forcontroltint%29.md)
### Deprecated methods
- [func usingColorSpaceName(NSColorSpaceName) -> NSColor?](./nscolor/usingcolorspacename%28_%29.md)
  Creates a new color object whose color is the same as the receiver’s, except that the new color object is in the specified color space.
- [func usingColorSpaceName(NSColorSpaceName?, device: [NSDeviceDescriptionKey : Any]?) -> NSColor?](./nscolor/usingcolorspacename%28_,device%29.md)
  Creates a new color object for the same color, but in the specified color space and specific to the provided device.
### Deprecated properties
- [class var ignoresAlpha: Bool](./nscolor/ignoresalpha.md)
  A Boolean value that indicates whether the app supports alpha.
- [var colorSpaceName: NSColorSpaceName](./nscolor/colorspacename.md)
  The name of the color space associated with the color.
### Deprecated constants
- [class let currentControlTintDidChangeNotification: NSNotification.Name](./nscolor/currentcontroltintdidchangenotification.md)
  Sent after the user changes control tint preference.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolor-deprecated-symbols)*