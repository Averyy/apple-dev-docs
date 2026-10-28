# NSEnableScreenUpdates()

**Framework**: AppKit  
**Kind**: func  
**Role**: Function

Enables screen updates.

**Availability**:
- macOS 10.0+ - Deprecated in 10.11

> **Deprecated**: As of 10.11 it is not generally necessary to take explicit action to achieve visual atomicity. +[NSAnimationContext runAnimationGroup:] and other similar methods can be used when a stronger than normal need for visual atomicity is required. The NSAnimationContext methods do not suffer from the same performance problems as NSEnableScreenUpdates.

## Declaration

```swift
func NSEnableScreenUpdates()
```

```c
extern void NSEnableScreenUpdates();
```

## Discussion

Reenables, for all windows of a process, the flushing of drawing operations to the screen that was previously disabled by [`NSDisableScreenUpdates()`](./nsdisablescreenupdates%28%29.md). Successive calls to [`NSDisableScreenUpdates()`](./nsdisablescreenupdates%28%29.md) are placed on a stack and must be popped off that stack by matching calls to this function.

## See Also

### Deprecated functions
- [func NSConvertGlyphsToPackedGlyphs(UnsafeMutablePointer<NSGlyph>, Int, NSMultibyteGlyphPacking, UnsafeMutablePointer<CChar>) -> Int](./nsconvertglyphstopackedglyphs%28_,_,_,_%29.md)
  Prepares a set of glyphs for processing by character-based routines.
- [static func raiseBadArgumentException(Any!, NSAccessibility.Attribute!, Any!)](./nsaccessibility-swift.struct/raisebadargumentexception%28_,_,_%29.md)
  Raises an error if the parameter is the wrong type or has an illegal value
- [func NSReleaseAlertPanel(Any!)](./nsreleasealertpanel%28_%29.md)
  Disposes of an alert panel.
- [func NSDisableScreenUpdates()](./nsdisablescreenupdates%28%29.md)
  Disables screen updates.
- [func NSDrawColorTiledRects(NSRect, NSRect, UnsafePointer<NSRectEdge>, AutoreleasingUnsafeMutablePointer<NSColor>, Int) -> NSRect](./nsdrawcolortiledrects%28_,_,_,_,_%29.md)
  Draws a single-color, bordered rectangle.
- [func NSSetShowsServicesMenuItem(String, Bool) -> Int](./nssetshowsservicesmenuitem%28_,_%29.md)
  Specifies whether an item should be included in Services menus.
- [func NSCopyBits(Int, NSRect, NSPoint)](./nscopybits%28_,_,_%29.md)
  Copies a bitmap image to the location specified by a destination point.
- [func NSShowsServicesMenuItem(String) -> Bool](./nsshowsservicesmenuitem%28_%29.md)
  Specifies whether a Services menu item is currently enabled.
- [func NSDottedFrameRect(NSRect)](./nsdottedframerect%28_%29.md)
  Draws a bordered rectangle.
- [func NSReadPixel(NSPoint) -> NSColor?](./nsreadpixel%28_%29.md)
  Reads the color of the pixel at the specified location.
- [func NSGetWindowServerMemory(Int, UnsafeMutablePointer<Int>, UnsafeMutablePointer<Int>, AutoreleasingUnsafeMutablePointer<NSString>) -> Int](./nsgetwindowservermemory%28_,_,_,_%29.md)
  Returns the amount of memory being used by a context.
- [static func fileContentsType(forPathExtension: String) -> NSPasteboard.PasteboardType!](./nspasteboard/pasteboardtype/filecontentstype%28forpathextension%29.md)
  Returns a pasteboard type based on the passed file type.
- [static func fileNameType(forPathExtension: String) -> NSPasteboard.PasteboardType!](./nspasteboard/pasteboardtype/filenametype%28forpathextension%29.md)
  Returns a pasteboard type based on the passed file type.
- [var representedPathExtension: String?](./nspasteboard/pasteboardtype/representedpathextension.md)
  A file type based on the passed pasteboard type.
- [static func representedPathExtensions(from: [NSPasteboard.PasteboardType]) -> [String]?](./nspasteboard/pasteboardtype/representedpathextensions%28from%29.md)
  Returns an array of file types based on the passed pasteboard types.
- [NSOpenGLGetOption](./nsopenglgetoption.md)
  Returns global OpenGL options.
- [NSOpenGLGetVersion](./nsopenglgetversion.md)
  Returns the NSOpenGL version numbers.
- [NSOpenGLSetOption](./nsopenglsetoption.md)
  Sets global OpenGL options.
- [NSBeginAlertSheet](./nsbeginalertsheet.md)
  Creates and runs an alert sheet.
- [NSBeginCriticalAlertSheet](./nsbegincriticalalertsheet.md)
  Creates and runs a critical alert sheet.
- [NSBeginInformationalAlertSheet](./nsbegininformationalalertsheet.md)
  Creates and runs an informational alert sheet.
- [NSGetAlertPanel](./nsgetalertpanel.md)
  Returns an alert panel.
- [NSGetCriticalAlertPanel](./nsgetcriticalalertpanel.md)
  Returns an alert panel to display a critical message.
- [NSGetInformationalAlertPanel](./nsgetinformationalalertpanel.md)
  Returns an alert panel to display an informational message.
- [NSRunAlertPanel](./nsrunalertpanel.md)
  Creates an alert panel.
- [NSRunCriticalAlertPanel](./nsruncriticalalertpanel.md)
  Creates and runs a critical alert panel.
- [NSRunInformationalAlertPanel](./nsruninformationalalertpanel.md)
  Creates and runs an informational alert panel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsenablescreenupdates())*