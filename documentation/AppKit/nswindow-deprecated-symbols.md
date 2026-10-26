# Deprecated symbols

**Framework**: AppKit  
**Role**: API Collection

Review symbols that are no longer in active development, and their recommended replacements.

#### Overview

Although these symbols are available for use, Apple is no longer actively developing them, and may remove them in a future release. Apple recommends moving away from these symbols and using their indicated replacements instead. Check the individual symbol pages for the recommended replacements.

## Topics

### Deprecated methods
- [func gState() -> Int](./nswindow/gstate%28%29.md)
  Returns the window’s graphics state object.
- [func canStoreColor() -> Bool](./nswindow/canstorecolor%28%29.md)
  Indicates whether the window has a depth limit that allows it to store color values.
- [func enableFlushing()](./nswindow/enableflushing%28%29.md)
  Reenables the [`flush()`](./nswindow/flush%28%29.md) method for the window after it was disabled through a previous [`disableFlushing()`](./nswindow/disableflushing%28%29.md) message.
- [func disableFlushing()](./nswindow/disableflushing%28%29.md)
  Disables the [`flush()`](./nswindow/flush%28%29.md) method for the window.
- [func flush()](./nswindow/flush%28%29.md)
  Flushes the window’s offscreen buffer to the screen if the window is buffered and flushing is enabled.
- [func flushIfNeeded()](./nswindow/flushifneeded%28%29.md)
  Flushes the window’s offscreen buffer to the screen if flushing is enabled and if the last [`flush()`](./nswindow/flush%28%29.md) message had no effect because flushing was disabled.
- [class func menuChanged(NSMenu)](./nswindow/menuchanged%28_%29.md)
  This method does nothing; it is here for backward compatibility.
- [func cacheImage(in: NSRect)](./nswindow/cacheimage%28in%29.md)
  Stores the window’s raster image from a given rectangle expressed in the window’s base coordinate system.
- [func restoreCachedImage()](./nswindow/restorecachedimage%28%29.md)
  Splices the window’s cached image rectangles, if any, back into its raster image (and buffer if it has one), undoing the effect of any drawing performed within those areas since they were established using [`cacheImage(in:)`](./nswindow/cacheimage%28in%29.md).
- [func discardCachedImage()](./nswindow/discardcachedimage%28%29.md)
  Discards all of the window’s cached image rectangles.
- [func useOptimizedDrawing(Bool)](./nswindow/useoptimizeddrawing%28_%29.md)
  Specifies whether the window is to optimize focusing and drawing when displaying its views.
- [convenience init?(windowRef: UnsafeMutableRawPointer)](./nswindow/init%28windowref%29.md)
  Returns a Cocoa window created from a Carbon window.
- [func disableScreenUpdatesUntilFlush()](./nswindow/disablescreenupdatesuntilflush%28%29.md)
  Disables the window’s screen updates until the window is flushed.
- [func drag(NSImage, at: NSPoint, offset: NSSize, event: NSEvent, pasteboard: NSPasteboard, source: Any, slideBack: Bool)](./nswindow/drag%28_,at,offset,event,pasteboard,source,slideback%29.md)
  Begins a dragging session.
- [- convertBaseToScreen:](./nswindow/convertbasetoscreen_.md)
  Converts a given point from the window’s base coordinate system to the screen coordinate system.
- [- convertScreenToBase:](./nswindow/convertscreentobase_.md)
  Converts a given point from the screen coordinate system to the window’s base coordinate system.
- [- userSpaceScaleFactor](./nswindow/userspacescalefactor.md)
  Returns the scale factor applied to the window.
### Deprecated properties
- [var backingLocation: NSWindow.BackingLocation](./nswindow/backinglocation-swift.property.md)
  The location of the window’s backing store.
- [var preferredBackingLocation: NSWindow.BackingLocation](./nswindow/preferredbackinglocation.md)
  A Boolean value that indicates the preferred location for the window’s backing store.
- [var isOneShot: Bool](./nswindow/isoneshot.md)
  A Boolean value that indicates whether the window device the window manages is freed when it’s removed from the screen list.
- [var drawers: [NSDrawer]?](./nswindow/drawers.md)
  The collection of drawers associated with the window.
- [var showsResizeIndicator: Bool](./nswindow/showsresizeindicator.md)
  A Boolean value that indicates whether the window’s resize indicator is visible.
- [var isFlushWindowDisabled: Bool](./nswindow/isflushwindowdisabled.md)
  A Boolean value that indicates whether the window’s flushing ability is disabled.
- [var isAutodisplay: Bool](./nswindow/isautodisplay.md)
  A Boolean value that indicates whether the window automatically displays views that need to be displayed.
- [var graphicsContext: NSGraphicsContext?](./nswindow/graphicscontext.md)
  The graphics context associated with the window for the current thread.
- [var windowRef: UnsafeMutableRawPointer](./nswindow/windowref.md)
  The Carbon window reference associated with the window, creating one if necessary.
- [var showsToolbarButton: Bool](./nswindow/showstoolbarbutton.md)
  A Boolean value that indicates whether the toolbar control button is currently displayed.
### Deprecated constants
- [NSWindow.BackingLocation](./nswindow/backinglocation-swift.enum.md)
  The following constants and the related data type represent a window’s possible backing locations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow-deprecated-symbols)*