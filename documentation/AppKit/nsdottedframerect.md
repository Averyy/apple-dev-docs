# NSDottedFrameRect(_:)

**Framework**: AppKit  
**Kind**: func

Draws a bordered rectangle.

**Availability**:
- macOS ?+

## Declaration

```swift
func NSDottedFrameRect(_ rect: NSRect)
```

#### Discussion

Deprecated. Use a dashed [`NSBezierPath`](nsbezierpath.md) instead.

## See Also

- [func NSDrawTiledRects(NSRect, NSRect, UnsafePointer<NSRectEdge>, UnsafePointer<CGFloat>, Int) -> NSRect](nsdrawtiledrects(_:_:_:_:_:).md)
  Draws rectangles with borders.
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
- [func NSDrawColorTiledRects(NSRect, NSRect, UnsafePointer<NSRectEdge>, AutoreleasingUnsafeMutablePointer<NSColor>, Int) -> NSRect](nsdrawcolortiledrects(_:_:_:_:_:).md)
  Draws a single-color, bordered rectangle.
- [func NSSetShowsServicesMenuItem(String, Bool) -> Int](nssetshowsservicesmenuitem(_:_:).md)
  Specifies whether an item should be included in Services menus.
- [func NSCopyBits(Int, NSRect, NSPoint)](nscopybits(_:_:_:).md)
  Copies a bitmap image to the location specified by a destination point.
- [func NSShowsServicesMenuItem(String) -> Bool](nsshowsservicesmenuitem(_:).md)
  Specifies whether a Services menu item is currently enabled.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdottedframerect(_:))*