# disableScreenUpdatesUntilFlush()

**Framework**: AppKit  
**Kind**: method

Disables the window’s screen updates until the window is flushed.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func disableScreenUpdatesUntilFlush()
```

#### Discussion

This method can be invoked to synchronize hardware surface flushes with the window’s flushes. The window immediately disables screen updates using the [`NSDisableScreenUpdates()`](nsdisablescreenupdates().md) function and reenables screen updates when the window flushes. Sending this message multiple times during a window update cycle has no effect.

To ensure that screen updates are reenabled in a timely manner, it’s crucial that the window is marked as needing display and that the display will occur soon (that is, within the next second). When you invoke `disableScreenUpdatesUntilFlush`, you can make sure that a marked window gets displayed by returning control to the run loop on the main thread or by sending the window [`displayIfNeeded()`](nswindow/displayifneeded().md) or [`display()`](nswindow/display().md). If it’s unclear whether the window is marked as needing display, you can also ensure that a display occurs by using [`setNeedsDisplay(_:)`](nsview/setneedsdisplay(_:).md) for a view that’s visible in the window.

## See Also

- [func gState() -> Int](nswindow/gstate.md)
  Returns the window’s graphics state object.
- [func canStoreColor() -> Bool](nswindow/canstorecolor.md)
  Indicates whether the window has a depth limit that allows it to store color values.
- [func enableFlushing()](nswindow/enableflushing.md)
  Reenables the [`flush()`](nswindow/flush().md) method for the window after it was disabled through a previous [`disableFlushing()`](nswindow/disableflushing().md) message.
- [func disableFlushing()](nswindow/disableflushing.md)
  Disables the [`flush()`](nswindow/flush().md) method for the window.
- [func flush()](nswindow/flush.md)
  Flushes the window’s offscreen buffer to the screen if the window is buffered and flushing is enabled.
- [func flushIfNeeded()](nswindow/flushifneeded.md)
  Flushes the window’s offscreen buffer to the screen if flushing is enabled and if the last [`flush()`](nswindow/flush().md) message had no effect because flushing was disabled.
- [class func menuChanged(NSMenu)](nswindow/menuchanged(_:).md)
  This method does nothing; it is here for backward compatibility.
- [func cacheImage(in: NSRect)](nswindow/cacheimage(in:).md)
  Stores the window’s raster image from a given rectangle expressed in the window’s base coordinate system.
- [func restoreCachedImage()](nswindow/restorecachedimage.md)
  Splices the window’s cached image rectangles, if any, back into its raster image (and buffer if it has one), undoing the effect of any drawing performed within those areas since they were established using [`cacheImage(in:)`](nswindow/cacheimage(in:).md).
- [func discardCachedImage()](nswindow/discardcachedimage.md)
  Discards all of the window’s cached image rectangles.
- [func useOptimizedDrawing(Bool)](nswindow/useoptimizeddrawing(_:).md)
  Specifies whether the window is to optimize focusing and drawing when displaying its views.
- [convenience init?(windowRef: UnsafeMutableRawPointer)](nswindow/init(windowref:).md)
  Returns a Cocoa window created from a Carbon window.
- [func drag(NSImage, at: NSPoint, offset: NSSize, event: NSEvent, pasteboard: NSPasteboard, source: Any, slideBack: Bool)](nswindow/drag(_:at:offset:event:pasteboard:source:slideback:).md)
  Begins a dragging session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/disablescreenupdatesuntilflush())*