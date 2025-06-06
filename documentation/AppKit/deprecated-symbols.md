# Deprecated Symbols

**Framework**: AppKit

Review symbols that are no longer supported, and find the replacements to use instead.

## Topics

### Classes
- [class NSOpenGLView](nsopenglview.md)
  A view that displays OpenGL content in a view.
- [class NSOpenGLContext](nsopenglcontext.md)
  An object that represents an OpenGL graphics context, into which all OpenGL calls are rendered.
- [class NSOpenGLLayer](nsopengllayer.md)
  A subclass of [`CAOpenGLLayer`](https://developer.apple.com/documentation/QuartzCore/CAOpenGLLayer) that is suitable for rendering OpenGL into layers.
- [class NSOpenGLPixelFormat](nsopenglpixelformat.md)
  An object that specifies the types of buffers and other attributes of the OpenGL context.
- [class NSDrawer](nsdrawer.md)
  A user interface element that contains and displays text, scroll, and browser views, in addition to other view subclasses.
- [class NSForm](nsform.md)
  An `NSForm` object is a vertical matrix of [`NSFormCell`](nsformcell.md) objects to implement the fields.
- [class NSFormCell](nsformcell.md)
  The `NSFormCell` class is used to implement text entry fields in a form. The left part of an `NSFormCell` object contains a title. The right part contains an editable text entry field.
- [class NSMenuItemCell](nsmenuitemcell.md)
  An object that handles the measurement and display of a single menu item in its encompassing frame.
### Protocols
- [NSAccessibility](nsaccessibility.md)
  A legacy, informal protocol that Apple doesn’t recommend for active use.
- [NSEditor](nseditor-deprecated-symbols.md)
  A set of methods that controllers and UI elements can implement to manage editing.
- [protocol NSEditorRegistration](nseditorregistration.md)
  A set of methods that controllers can implement to enable an editor view to inform the controller when it has uncommitted changes.
- [protocol NSInputServiceProvider](nsinputserviceprovider.md)
- [protocol NSInputServerMouseTracker](nsinputservermousetracker.md)
- [protocol NSDrawerDelegate](nsdrawerdelegate.md)
  A set of methods that drawer delegates implement to open, close, and resize the drawer.
### Functions
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
### Enumerations
- [enum NSMultibyteGlyphPacking](nsmultibyteglyphpacking.md)
  A constant for glyph packing.
- [Glyph Attributes](glyph-attributes.md)
  Attributes that are used only inside the glyph generation machinery, but must also be shared between components.
- [enum NSOpenGLGlobalOption](nsopenglglobaloption.md)
  Constants that specify OpenGL options.
- [Data Entry Types](data-entry-types.md)
  These constants specify how a cell formats numeric data.
- [Anonymous](nsbuttontypes-anonymous.md)
- [Additional Writing Directions](additional-writing-directions.md)
  Additional values to be added to [`NSWritingDirection.leftToRight`](nswritingdirection/lefttoright.md) or [`NSWritingDirection.rightToLeft`](nswritingdirection/righttoleft.md), when used with [`writingDirection`](https://developer.apple.com/documentation/foundation/nsattributedstring/key/1524497-writingdirection).
- [Return values for modal operations](return-values-for-modal-operations.md)
  Historical return values for [`runModal(for:)`](nsapplication/runmodal(for:).md) and [`runModalSession(_:)`](nsapplication/runmodalsession(_:).md).
- [Tags of Views in the FontPanel](tags-of-views-in-the-fontpanel.md)
  These constants are obsolete and should not be used.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/deprecated-symbols)*