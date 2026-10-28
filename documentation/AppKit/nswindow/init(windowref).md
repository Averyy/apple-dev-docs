# init(windowRef:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Returns a Cocoa window created from a Carbon window.

**Availability**:
- macOS 10.0+ - Deprecated in 15.0

> **Deprecated**: This method should not be used.

## Declaration

```swift
convenience init?(windowRef: UnsafeMutableRawPointer)
```

```objc
- (NSWindow *) initWithWindowRef:(void *) windowRef;
```

## Return Value

A Cocoa window created from `windowRef`.

## Discussion

For more information on Carbon-Cocoa integration, see Using a Carbon User Interface in a Cocoa Application in Carbon-Cocoa Integration Guide.

### Special Considerations

For historical reasons, contrary to normal memory management policy `initWithWindowRef:` does *not* retain `windowRef`. It is therefore recommended that you make sure you retain `windowRef` before calling this method. If `windowRef` is still valid when the Cocoa window is deallocated, the Cocoa window will release it.

## Parameters

- `windowRef`: The Carbon `WindowRef` object to use to create the Cocoa window.

## See Also

### Related Documentation
- [class NSWindow](../nswindow.md)
  A window that an app displays on the screen.
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
- [func disableScreenUpdatesUntilFlush()](./disablescreenupdatesuntilflush%28%29.md)
  Disables the window’s screen updates until the window is flushed.
- [func drag(NSImage, at: NSPoint, offset: NSSize, event: NSEvent, pasteboard: NSPasteboard, source: Any, slideBack: Bool)](./drag%28_,at,offset,event,pasteboard,source,slideback%29.md)
  Begins a dragging session.
- [- convertBaseToScreen:](./convertbasetoscreen_.md)
  Converts a given point from the window’s base coordinate system to the screen coordinate system.
- [- convertScreenToBase:](./convertscreentobase_.md)
  Converts a given point from the screen coordinate system to the window’s base coordinate system.
- [- userSpaceScaleFactor](./userspacescalefactor.md)
  Returns the scale factor applied to the window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/init(windowref:))*