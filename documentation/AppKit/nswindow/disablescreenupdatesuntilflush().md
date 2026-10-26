# disableScreenUpdatesUntilFlush()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Disables the window’s screen updates until the window is flushed.

**Availability**:
- macOS 10.0+ - Deprecated in 15.0

> **Deprecated**: This method does not do anything and should not be called.

## Declaration

```swift
func disableScreenUpdatesUntilFlush()
```

```objc
- (void) disableScreenUpdatesUntilFlush;
```

#### Discussion

This method can be invoked to synchronize hardware surface flushes with the window’s flushes. The window immediately disables screen updates using the [`NSDisableScreenUpdates()`](../nsdisablescreenupdates%28%29.md) function and reenables screen updates when the window flushes. Sending this message multiple times during a window update cycle has no effect.

To ensure that screen updates are reenabled in a timely manner, it’s crucial that the window is marked as needing display and that the display will occur soon (that is, within the next second). When you invoke `disableScreenUpdatesUntilFlush`, you can make sure that a marked window gets displayed by returning control to the run loop on the main thread or by sending the window [`displayIfNeeded()`](./displayifneeded%28%29.md) or [`display()`](./display%28%29.md). If it’s unclear whether the window is marked as needing display, you can also ensure that a display occurs by using [`setNeedsDisplay(_:)`](../nsview/setneedsdisplay%28_%29.md) for a view that’s visible in the window.

## See Also

### Deprecated methods
- [func gState() -> Int](./gstate%28%29.md)
  Returns the window’s graphics state object.
- [func canStoreColor() -> Bool](./canstorecolor%28%29.md)
  Indicates whether the window has a depth limit that allows it to store color values.
- [func enableFlushing()](./enableflushing%28%29.md)
  Reenables the [`flush()`](./flush%28%29.md) method for the window after it was disabled through a previous [`disableFlushing()`](./disableflushing%28%29.md) message.
- [func disableFlushing()](./disableflushing%28%29.md)
  Disables the [`flush()`](./flush%28%29.md) method for the window.
- [func flush()](./flush%28%29.md)
  Flushes the window’s offscreen buffer to the screen if the window is buffered and flushing is enabled.
- [func flushIfNeeded()](./flushifneeded%28%29.md)
  Flushes the window’s offscreen buffer to the screen if flushing is enabled and if the last [`flush()`](./flush%28%29.md) message had no effect because flushing was disabled.
- [class func menuChanged(NSMenu)](./menuchanged%28_%29.md)
  This method does nothing; it is here for backward compatibility.
- [func cacheImage(in: NSRect)](./cacheimage%28in%29.md)
  Stores the window’s raster image from a given rectangle expressed in the window’s base coordinate system.
- [func restoreCachedImage()](./restorecachedimage%28%29.md)
  Splices the window’s cached image rectangles, if any, back into its raster image (and buffer if it has one), undoing the effect of any drawing performed within those areas since they were established using [`cacheImage(in:)`](./cacheimage%28in%29.md).
- [func discardCachedImage()](./discardcachedimage%28%29.md)
  Discards all of the window’s cached image rectangles.
- [func useOptimizedDrawing(Bool)](./useoptimizeddrawing%28_%29.md)
  Specifies whether the window is to optimize focusing and drawing when displaying its views.
- [convenience init?(windowRef: UnsafeMutableRawPointer)](./init%28windowref%29.md)
  Returns a Cocoa window created from a Carbon window.
- [func drag(NSImage, at: NSPoint, offset: NSSize, event: NSEvent, pasteboard: NSPasteboard, source: Any, slideBack: Bool)](./drag%28_,at,offset,event,pasteboard,source,slideback%29.md)
  Begins a dragging session.
- [- convertBaseToScreen:](./convertbasetoscreen_.md)
  Converts a given point from the window’s base coordinate system to the screen coordinate system.
- [- convertScreenToBase:](./convertscreentobase_.md)
  Converts a given point from the screen coordinate system to the window’s base coordinate system.
- [- userSpaceScaleFactor](./userspacescalefactor.md)
  Returns the scale factor applied to the window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/disablescreenupdatesuntilflush())*