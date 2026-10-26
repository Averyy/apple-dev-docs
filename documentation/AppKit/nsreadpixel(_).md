# NSReadPixel(_:)

**Framework**: AppKit  
**Kind**: func  
**Role**: Function

Reads the color of the pixel at the specified location.

**Availability**:
- macOS 10.0+ - Deprecated in 10.14

> **Deprecated**: Use -[NSBitmapImageRep colorAtX:y:] to interrogate pixel values.  If necessary, use -[NSView cacheDisplayInRect:toBitmapImageRep:] to snapshot a view hierarchy into an NSBitmapImageRep.

## Declaration

```swift
func NSReadPixel(_ passedPoint: NSPoint) -> NSColor?
```

```c
extern NSColor *NSReadPixel(NSPoint passedPoint);
```

#### Return Value

The color of the pixel at the specified location.

#### Discussion

Because the `passedPoint` parameter is relative to the current coordinate system, if you wish to read a pixel from a specific view, you must convert points in the view’s coordinate system to the current coordinate system before calling this function. Alternatively, you can lock focus on the view and then specify the pixel coordinate in the view’s coordinate system.

When mapping the specified point to pixel boundaries, this method rounds to the nearest pixel.

## Parameters

- `passedPoint`: The pixel location to read, specified in the current coordinate system.

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
- [func NSEnableScreenUpdates()](./nsenablescreenupdates%28%29.md)
  Enables screen updates.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsreadpixel(_:))*