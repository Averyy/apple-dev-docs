# cacheImage(in:)

**Framework**: AppKit  
**Kind**: method

Stores the window’s raster image from a given rectangle expressed in the window’s base coordinate system.

**Availability**:
- macOS 10.0+

## Declaration

```swift
@MainActor
func cacheImage(in rect: NSRect)
```

#### Discussion

This method allows the window to perform temporary drawing, such as a band around the selection as the user drags the mouse, and to quickly restore the previous image by invoking [`restoreCachedImage()`](nswindow/restorecachedimage().md) and [`flushIfNeeded()`](nswindow/flushifneeded().md). The next time the window displays, it discards its cached image rectangles. You can also explicitly use [`discardCachedImage()`](nswindow/discardcachedimage().md) to free the memory occupied by cached image rectangles. `rect` is made integral before caching the image to avoid antialiasing artifacts.

Only the last cached rectangle is remembered and can be restored.

## Parameters

- `rect`: The rectangle representing the image to cache.

## See Also

- [func display()](nswindow/display.md)
  Passes a display message down the window’s view hierarchy, thus redrawing all views within the window.
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
- [func restoreCachedImage()](nswindow/restorecachedimage.md)
  Splices the window’s cached image rectangles, if any, back into its raster image (and buffer if it has one), undoing the effect of any drawing performed within those areas since they were established using [`cacheImage(in:)`](nswindow/cacheimage(in:).md).
- [func discardCachedImage()](nswindow/discardcachedimage.md)
  Discards all of the window’s cached image rectangles.
- [func useOptimizedDrawing(Bool)](nswindow/useoptimizeddrawing(_:).md)
  Specifies whether the window is to optimize focusing and drawing when displaying its views.
- [convenience init?(windowRef: UnsafeMutableRawPointer)](nswindow/init(windowref:).md)
  Returns a Cocoa window created from a Carbon window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/cacheimage(in:))*