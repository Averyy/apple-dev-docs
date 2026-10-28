# fileNameType(forPathExtension:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Type Method

Returns a pasteboard type based on the passed file type.

**Availability**:
- macOS

> **Deprecated**: The file contents pboard type allowed you to synthesize a pboard type for a file’s contents based on the file’s extension. Using the UTI of a file to represent its contents now replaces this functionality.

## Declaration

```swift
static func fileNameType(forPathExtension fileType: String) -> NSPasteboard.PasteboardType!
```

```c
extern NSPasteboardTypeNSCreateFilenamePboardType(NSString *fileType);
```

## Discussion

Returns an [`NSString`](../../../Foundation/nsstring.md) to a pasteboard type representing a filename based on the supplied string `fileType`.

## See Also

### Deprecated functions
- [func NSConvertGlyphsToPackedGlyphs(UnsafeMutablePointer<NSGlyph>, Int, NSMultibyteGlyphPacking, UnsafeMutablePointer<CChar>) -> Int](../../nsconvertglyphstopackedglyphs%28_,_,_,_%29.md)
  Prepares a set of glyphs for processing by character-based routines.
- [static func raiseBadArgumentException(Any!, NSAccessibility.Attribute!, Any!)](../../nsaccessibility-swift.struct/raisebadargumentexception%28_,_,_%29.md)
  Raises an error if the parameter is the wrong type or has an illegal value
- [func NSReleaseAlertPanel(Any!)](../../nsreleasealertpanel%28_%29.md)
  Disposes of an alert panel.
- [func NSDisableScreenUpdates()](../../nsdisablescreenupdates%28%29.md)
  Disables screen updates.
- [func NSEnableScreenUpdates()](../../nsenablescreenupdates%28%29.md)
  Enables screen updates.
- [func NSDrawColorTiledRects(NSRect, NSRect, UnsafePointer<NSRectEdge>, AutoreleasingUnsafeMutablePointer<NSColor>, Int) -> NSRect](../../nsdrawcolortiledrects%28_,_,_,_,_%29.md)
  Draws a single-color, bordered rectangle.
- [func NSSetShowsServicesMenuItem(String, Bool) -> Int](../../nssetshowsservicesmenuitem%28_,_%29.md)
  Specifies whether an item should be included in Services menus.
- [func NSCopyBits(Int, NSRect, NSPoint)](../../nscopybits%28_,_,_%29.md)
  Copies a bitmap image to the location specified by a destination point.
- [func NSShowsServicesMenuItem(String) -> Bool](../../nsshowsservicesmenuitem%28_%29.md)
  Specifies whether a Services menu item is currently enabled.
- [func NSDottedFrameRect(NSRect)](../../nsdottedframerect%28_%29.md)
  Draws a bordered rectangle.
- [func NSReadPixel(NSPoint) -> NSColor?](../../nsreadpixel%28_%29.md)
  Reads the color of the pixel at the specified location.
- [func NSGetWindowServerMemory(Int, UnsafeMutablePointer<Int>, UnsafeMutablePointer<Int>, AutoreleasingUnsafeMutablePointer<NSString>) -> Int](../../nsgetwindowservermemory%28_,_,_,_%29.md)
  Returns the amount of memory being used by a context.
- [static func fileContentsType(forPathExtension: String) -> NSPasteboard.PasteboardType!](./filecontentstype%28forpathextension%29.md)
  Returns a pasteboard type based on the passed file type.
- [var representedPathExtension: String?](./representedpathextension.md)
  A file type based on the passed pasteboard type.
- [static func representedPathExtensions(from: [NSPasteboard.PasteboardType]) -> [String]?](./representedpathextensions%28from%29.md)
  Returns an array of file types based on the passed pasteboard types.
- [NSOpenGLGetOption](../../nsopenglgetoption.md)
  Returns global OpenGL options.
- [NSOpenGLGetVersion](../../nsopenglgetversion.md)
  Returns the NSOpenGL version numbers.
- [NSOpenGLSetOption](../../nsopenglsetoption.md)
  Sets global OpenGL options.
- [NSBeginAlertSheet](../../nsbeginalertsheet.md)
  Creates and runs an alert sheet.
- [NSBeginCriticalAlertSheet](../../nsbegincriticalalertsheet.md)
  Creates and runs a critical alert sheet.
- [NSBeginInformationalAlertSheet](../../nsbegininformationalalertsheet.md)
  Creates and runs an informational alert sheet.
- [NSGetAlertPanel](../../nsgetalertpanel.md)
  Returns an alert panel.
- [NSGetCriticalAlertPanel](../../nsgetcriticalalertpanel.md)
  Returns an alert panel to display a critical message.
- [NSGetInformationalAlertPanel](../../nsgetinformationalalertpanel.md)
  Returns an alert panel to display an informational message.
- [NSRunAlertPanel](../../nsrunalertpanel.md)
  Creates an alert panel.
- [NSRunCriticalAlertPanel](../../nsruncriticalalertpanel.md)
  Creates and runs a critical alert panel.
- [NSRunInformationalAlertPanel](../../nsruninformationalalertpanel.md)
  Creates and runs an informational alert panel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspasteboard/pasteboardtype/filenametype(forpathextension:))*