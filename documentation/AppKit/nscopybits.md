# NSCopyBits(_:_:_:)

**Framework**: AppKit  
**Kind**: func

Copies a bitmap image to the location specified by a destination point.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func NSCopyBits(_ srcGState: Int, _ srcRect: NSRect, _ destPoint: NSPoint)
```

#### Discussion

Copies the pixels in the rectangle specified by `srcRect` to the location specified by `destPoint`. The source rectangle is defined in the graphics state designated by `srcGState`. If `srcGState` is `NSNullObject`, the current graphics state is assumed. The `destPoint` destination is defined in the current graphics state.

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
- [func NSDrawColorTiledRects(NSRect, NSRect, UnsafePointer<NSRectEdge>, AutoreleasingUnsafeMutablePointer<NSColor>, Int) -> NSRect](nsdrawcolortiledrects(_:_:_:_:_:).md)
  Draws a single-color, bordered rectangle.
- [func NSSetShowsServicesMenuItem(String, Bool) -> Int](nssetshowsservicesmenuitem(_:_:).md)
  Specifies whether an item should be included in Services menus.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscopybits(_:_:_:))*