# cacheImage(in:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Stores the window’s raster image from a given rectangle expressed in the window’s base coordinate system.

**Availability**:
- macOS 10.0+ - Deprecated in 10.13

> **Deprecated**: This method shouldn’t be used as it doesn’t work in all drawing situations; instead, a subview should be used that implements the desired drawing behavior

## Declaration

```swift
func cacheImage(in rect: NSRect)
```

```objc
- (void) cacheImageInRect:(NSRect) rect;
```

#### Discussion

This method allows the window to perform temporary drawing, such as a band around the selection as the user drags the mouse, and to quickly restore the previous image by invoking [`restoreCachedImage()`](./restorecachedimage%28%29.md) and [`flushIfNeeded()`](./flushifneeded%28%29.md). The next time the window displays, it discards its cached image rectangles. You can also explicitly use [`discardCachedImage()`](./discardcachedimage%28%29.md) to free the memory occupied by cached image rectangles. `rect` is made integral before caching the image to avoid antialiasing artifacts.

Only the last cached rectangle is remembered and can be restored.

## Parameters

- `rect`: The rectangle representing the image to cache.

## See Also

### Related Documentation
- [func display()](./display%28%29.md)
  Passes a display message down the window’s view hierarchy, thus redrawing all views within the window.
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
- [func restoreCachedImage()](./restorecachedimage%28%29.md)
  Splices the window’s cached image rectangles, if any, back into its raster image (and buffer if it has one), undoing the effect of any drawing performed within those areas since they were established using [`cacheImage(in:)`](./cacheimage%28in%29.md).
- [func discardCachedImage()](./discardcachedimage%28%29.md)
  Discards all of the window’s cached image rectangles.
- [func useOptimizedDrawing(Bool)](./useoptimizeddrawing%28_%29.md)
  Specifies whether the window is to optimize focusing and drawing when displaying its views.
- [convenience init?(windowRef: UnsafeMutableRawPointer)](./init%28windowref%29.md)
  Returns a Cocoa window created from a Carbon window.
- [func disableScreenUpdatesUntilFlush()](./disablescreenupdatesuntilflush%28%29.md)
  Disables the window’s screen updates until the window is flushed.
- [func drag(NSImage, at: NSPoint, offset: NSSize, event: NSEvent, pasteboard: NSPasteboard, source: Any, slideBack: Bool)](./drag%28_,at,offset,event,pasteboard,source,slideback%29.md)
  Begins a dragging session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/cacheimage(in:))*