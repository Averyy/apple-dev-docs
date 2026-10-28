# Deprecated symbols

**Framework**: AppKit  
**Role**: API Collection

Review symbols that are no longer in active development, and their recommended replacements.

## Overview

Although these symbols are available for use, Apple is no longer actively developing them, and may remove them in a future release. Apple recommends moving away from these symbols and using their indicated replacements instead. Check the individual symbol pages for the recommended replacements.

## Topics

### Deprecated classes
- [class NSOpenGLView](./nsopenglview.md)
  A view that displays OpenGL content in a view.
- [class NSOpenGLContext](./nsopenglcontext.md)
  An object that represents an OpenGL graphics context, into which all OpenGL calls are rendered.
- [class NSOpenGLLayer](./nsopengllayer.md)
  A subclass of `CAOpenGLLayer` that is suitable for rendering OpenGL into layers.
- [class NSOpenGLPixelFormat](./nsopenglpixelformat.md)
  An object that specifies the types of buffers and other attributes of the OpenGL context.
- [class NSDrawer](./nsdrawer.md)
  A user interface element that contains and displays text, scroll, and browser views, in addition to other view subclasses.
- [class NSForm](./nsform.md)
  An `NSForm` object is a vertical matrix of [`NSFormCell`](./nsformcell.md) objects to implement the fields.
- [class NSFormCell](./nsformcell.md)
  The `NSFormCell` class is used to implement text entry fields in a form. The left part of an `NSFormCell` object contains a title. The right part contains an editable text entry field.
- [class NSMenuItemCell](./nsmenuitemcell.md)
  An object that handles the measurement and display of a single menu item in its encompassing frame.
- [NSOpenGLPixelBuffer](./nsopenglpixelbuffer.md)
  An object that provides access to accelerated offscreen rendering.
- [NSCachedImageRep](./nscachedimagerep.md)
  An object that stores image data in a form that can be readily transferred to the screen.
- [NSInputManager](./nsinputmanager.md)
- [NSInputServer](./nsinputserver.md)
- [NSMovie](./nsmovie.md)
### Deprecated protocols
- [NSAccessibility](./nsaccessibility.md)
  A legacy, informal protocol that Apple doesn’t recommend for active use.
- [protocol NSEditorRegistration](./nseditorregistration.md)
  A set of methods that controllers can implement to enable an editor view to inform the controller when it has uncommitted changes.
- [protocol NSInputServiceProvider](./nsinputserviceprovider.md)
- [protocol NSInputServerMouseTracker](./nsinputservermousetracker.md)
- [protocol NSDrawerDelegate](./nsdrawerdelegate.md)
  A set of methods that drawer delegates implement to open, close, and resize the drawer.
- [NSEditor](./nseditor-deprecated-symbols.md)
  A set of methods that controllers and UI elements can implement to manage editing.
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
- [NSRunAlertPanelRelativeToWindow](./nsrunalertpanelrelativetowindow.md)
- [NSRunCriticalAlertPanelRelativeToWindow](./nsruncriticalalertpanelrelativetowindow.md)
- [NSRunInformationalAlertPanelRelativeToWindow](./nsruninformationalalertpanelrelativetowindow.md)
- [NSInterfaceStyleForKey](./nsinterfacestyleforkey.md)
  Returns an interface style value for the specified key and responder.
- [NSCountWindows](./nscountwindows.md)
  Counts the number of onscreen windows.
- [NSCountWindowsForContext](./nscountwindowsforcontext.md)
  Counts the number of onscreen windows belonging to a particular application.
- [NSWindowList](./nswindowlist.md)
  Gets information about onscreen windows.
- [NSWindowListForContext](./nswindowlistforcontext.md)
  Gets information about an application’s onscreen windows.
### Deprecated enumerations
- [enum NSMultibyteGlyphPacking](./nsmultibyteglyphpacking.md)
  A constant for glyph packing.
- [Glyph Attributes](./glyph-attributes.md)
  Attributes that are used only inside the glyph generation machinery, but must also be shared between components.
- [enum NSOpenGLGlobalOption](./nsopenglglobaloption.md)
  Constants that specify OpenGL options.
- [Data Entry Types](./data-entry-types.md)
  These constants specify how a cell formats numeric data.
- [Anonymous](./nsbuttontypes-anonymous.md)
- [Additional Writing Directions](./additional-writing-directions.md)
  Constants that specify additional options when setting the writing direction of attributed strings.
- [Return values for modal operations](./return-values-for-modal-operations.md)
  Historical return values for [`runModal(for:)`](./nsapplication/runmodal%28for%29.md) and [`runModalSession(_:)`](./nsapplication/runmodalsession%28_%29.md).
- [Tags of Views in the FontPanel](./tags-of-views-in-the-fontpanel.md)
  These constants are obsolete and should not be used.
- [NSInterfaceStyle](./nsinterfacestyle.md)
  These constants are used in `NSResponder`’s [`interfaceStyle`](./nsresponder/interfacestyle.md) method.
- [NSNoUnderlineStyle](./nsnounderlinestyle.md)
- [NSSingleUnderlineStyle](./nssingleunderlinestyle.md)
### Deprecated constants
- [NSAccessibilitySortButtonRole](./nsaccessibilitysortbuttonrole.md)
  The sort button role.
- [NSUnderlineStrikethroughMask](./nsunderlinestrikethroughmask.md)
- [NSCalibratedBlackColorSpace](./nscalibratedblackcolorspace.md)
  Calibrated color space with black and alpha components (pure black is 1.0)
- [NSDeviceBlackColorSpace](./nsdeviceblackcolorspace.md)
  Device-dependent color space with black and alpha components (pure black is 1.0)
- [NSPrintSavePath](./nsprintsavepath.md)
  An `NSString` object that specifies the pathname to which the job file will be saved when the [`jobDisposition`](./nsprintinfo/jobdisposition-swift.property.md) is [`NSPrintSaveJob`](./nsprintinfo/jobdisposition-swift.struct/save.md)..


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/deprecated-symbols)*