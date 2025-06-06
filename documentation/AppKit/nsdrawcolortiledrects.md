# NSDrawColorTiledRects(_:_:_:_:_:)

**Framework**: AppKit  
**Kind**: func

Draws a single-color, bordered rectangle.

**Availability**:
- macOS ?+

## Declaration

```swift
func NSDrawColorTiledRects(_ boundsRect: NSRect, _ clipRect: NSRect, _ sides: UnsafePointer<NSRectEdge>, _ colors: AutoreleasingUnsafeMutablePointer<NSColor>, _ count: Int) -> NSRect
```

#### Return Value

The rectangle that lies within the resulting border.

#### Discussion

Behaves the same as [`NSDrawTiledRects(_:_:_:_:_:)`](nsdrawtiledrects(_:_:_:_:_:).md) except it draws its border using colors from the `colors` array.

## Parameters

- `boundsRect`: The bounding rectangle (in the current coordinate system) in which to draw. Since this function is often used to draw the border of a view, this rectangle will typically be that view’s bounds rectangle. Only those parts of   that lie within the   are actually drawn.
- `clipRect`: The clipping rectangle to use during drawing.
- `sides`: The sides of the rectangle for which you want to specify custom colors. Each side must have a corresponding entry in the   parameter.
- `colors`: The colors to draw for each of the edges listed in the   parameter.
- `count`: The number of 1.0-unit-wide slices to draw on the specified sides.

## See Also

- [func NSConvertGlyphsToPackedGlyphs(UnsafeMutablePointer<NSGlyph>, Int, NSMultibyteGlyphPacking, UnsafeMutablePointer<CChar>) -> Int](nsconvertglyphstopackedglyphs(_:_:_:_:).md)
  Prepares a set of glyphs for processing by character-based routines.
- [static func raiseBadArgumentException(Any!, NSAccessibility.Attribute!, Any!)](nsaccessibility-swift.struct/raisebadargumentexception(_:_:_:).md)
  Raises an error if the parameter is the wrong type or has an illegal value
- [func NSReleaseAlertPanel(Any!)](nsreleasealertpanel(_:).md)
  Disposes of an alert panel.
- [func NSDisableScreenUpdates()](nsdisablescreenupdates().md)
  Disables screen updates.
- [func NSEnableScreenUpdates()](nsenablescreenupdates().md)
  Enables screen updates.
- [func NSSetShowsServicesMenuItem(String, Bool) -> Int](nssetshowsservicesmenuitem(_:_:).md)
  Specifies whether an item should be included in Services menus.
- [func NSCopyBits(Int, NSRect, NSPoint)](nscopybits(_:_:_:).md)
  Copies a bitmap image to the location specified by a destination point.
- [func NSShowsServicesMenuItem(String) -> Bool](nsshowsservicesmenuitem(_:).md)
  Specifies whether a Services menu item is currently enabled.
- [func NSDottedFrameRect(NSRect)](nsdottedframerect(_:).md)
  Draws a bordered rectangle.
- [func NSReadPixel(NSPoint) -> NSColor?](nsreadpixel(_:).md)
  Reads the color of the pixel at the specified location.
- [func NSGetWindowServerMemory(Int, UnsafeMutablePointer<Int>, UnsafeMutablePointer<Int>, AutoreleasingUnsafeMutablePointer<NSString>) -> Int](nsgetwindowservermemory(_:_:_:_:).md)
  Returns the amount of memory being used by a context.
- [static func fileContentsType(forPathExtension: String) -> NSPasteboard.PasteboardType!](nspasteboard/pasteboardtype/filecontentstype(forpathextension:).md)
  Returns a pasteboard type based on the passed file type.
- [static func fileNameType(forPathExtension: String) -> NSPasteboard.PasteboardType!](nspasteboard/pasteboardtype/filenametype(forpathextension:).md)
  Returns a pasteboard type based on the passed file type.
- [var representedPathExtension: String?](nspasteboard/pasteboardtype/representedpathextension.md)
  A file type based on the passed pasteboard type.
- [static func representedPathExtensions(from: [NSPasteboard.PasteboardType]) -> [String]?](nspasteboard/pasteboardtype/representedpathextensions(from:).md)
  Returns an array of file types based on the passed pasteboard types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdrawcolortiledrects(_:_:_:_:_:))*