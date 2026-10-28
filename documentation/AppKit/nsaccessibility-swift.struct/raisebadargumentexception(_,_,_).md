# raiseBadArgumentException(_:_:_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Type Method

Raises an error if the parameter is the wrong type or has an illegal value

**Availability**:
- macOS 10.1+ - Deprecated in 10.11

> **Deprecated**: Exceptions are no longer appropriate for indicating errors in accessibility API. Unexpected values should be handled through appropriate type checking.

## Declaration

```swift
static func raiseBadArgumentException(_ element: Any!, _ attribute: NSAccessibility.Attribute!, _ value: Any!)
```

```c
extern void NSAccessibilityRaiseBadArgumentException(id element, NSAccessibilityAttributeName attribute, id value);
```

## Discussion

Raises an error if a parameter is the wrong type or has an illegal value. This function can also be used to raise an error if an attempt is made to set an attribute’s value with the wrong type or an illegal value.

## See Also

### Deprecated functions
- [func NSConvertGlyphsToPackedGlyphs(UnsafeMutablePointer<NSGlyph>, Int, NSMultibyteGlyphPacking, UnsafeMutablePointer<CChar>) -> Int](../nsconvertglyphstopackedglyphs%28_,_,_,_%29.md)
  Prepares a set of glyphs for processing by character-based routines.
- [func NSReleaseAlertPanel(Any!)](../nsreleasealertpanel%28_%29.md)
  Disposes of an alert panel.
- [func NSDisableScreenUpdates()](../nsdisablescreenupdates%28%29.md)
  Disables screen updates.
- [func NSEnableScreenUpdates()](../nsenablescreenupdates%28%29.md)
  Enables screen updates.
- [func NSDrawColorTiledRects(NSRect, NSRect, UnsafePointer<NSRectEdge>, AutoreleasingUnsafeMutablePointer<NSColor>, Int) -> NSRect](../nsdrawcolortiledrects%28_,_,_,_,_%29.md)
  Draws a single-color, bordered rectangle.
- [func NSSetShowsServicesMenuItem(String, Bool) -> Int](../nssetshowsservicesmenuitem%28_,_%29.md)
  Specifies whether an item should be included in Services menus.
- [func NSCopyBits(Int, NSRect, NSPoint)](../nscopybits%28_,_,_%29.md)
  Copies a bitmap image to the location specified by a destination point.
- [func NSShowsServicesMenuItem(String) -> Bool](../nsshowsservicesmenuitem%28_%29.md)
  Specifies whether a Services menu item is currently enabled.
- [func NSDottedFrameRect(NSRect)](../nsdottedframerect%28_%29.md)
  Draws a bordered rectangle.
- [func NSReadPixel(NSPoint) -> NSColor?](../nsreadpixel%28_%29.md)
  Reads the color of the pixel at the specified location.
- [func NSGetWindowServerMemory(Int, UnsafeMutablePointer<Int>, UnsafeMutablePointer<Int>, AutoreleasingUnsafeMutablePointer<NSString>) -> Int](../nsgetwindowservermemory%28_,_,_,_%29.md)
  Returns the amount of memory being used by a context.
- [static func fileContentsType(forPathExtension: String) -> NSPasteboard.PasteboardType!](../nspasteboard/pasteboardtype/filecontentstype%28forpathextension%29.md)
  Returns a pasteboard type based on the passed file type.
- [static func fileNameType(forPathExtension: String) -> NSPasteboard.PasteboardType!](../nspasteboard/pasteboardtype/filenametype%28forpathextension%29.md)
  Returns a pasteboard type based on the passed file type.
- [var representedPathExtension: String?](../nspasteboard/pasteboardtype/representedpathextension.md)
  A file type based on the passed pasteboard type.
- [static func representedPathExtensions(from: [NSPasteboard.PasteboardType]) -> [String]?](../nspasteboard/pasteboardtype/representedpathextensions%28from%29.md)
  Returns an array of file types based on the passed pasteboard types.
- [NSOpenGLGetOption](../nsopenglgetoption.md)
  Returns global OpenGL options.
- [NSOpenGLGetVersion](../nsopenglgetversion.md)
  Returns the NSOpenGL version numbers.
- [NSOpenGLSetOption](../nsopenglsetoption.md)
  Sets global OpenGL options.
- [NSBeginAlertSheet](../nsbeginalertsheet.md)
  Creates and runs an alert sheet.
- [NSBeginCriticalAlertSheet](../nsbegincriticalalertsheet.md)
  Creates and runs a critical alert sheet.
- [NSBeginInformationalAlertSheet](../nsbegininformationalalertsheet.md)
  Creates and runs an informational alert sheet.
- [NSGetAlertPanel](../nsgetalertpanel.md)
  Returns an alert panel.
- [NSGetCriticalAlertPanel](../nsgetcriticalalertpanel.md)
  Returns an alert panel to display a critical message.
- [NSGetInformationalAlertPanel](../nsgetinformationalalertpanel.md)
  Returns an alert panel to display an informational message.
- [NSRunAlertPanel](../nsrunalertpanel.md)
  Creates an alert panel.
- [NSRunCriticalAlertPanel](../nsruncriticalalertpanel.md)
  Creates and runs a critical alert panel.
- [NSRunInformationalAlertPanel](../nsruninformationalalertpanel.md)
  Creates and runs an informational alert panel.
- [NSRunAlertPanelRelativeToWindow](../nsrunalertpanelrelativetowindow.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibility-swift.struct/raisebadargumentexception(_:_:_:))*