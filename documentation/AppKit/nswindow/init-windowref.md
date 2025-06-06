# init(windowRef:)

**Framework**: AppKit  
**Kind**: init

Returns a Cocoa window created from a Carbon window.

**Availability**:
- macOS 10.0+

## Declaration

```swift
@MainActor
convenience init?(windowRef: UnsafeMutableRawPointer)
```

#### Return Value

A Cocoa window created from `windowRef`.

#### Discussion

For more information on Carbon-Cocoa integration, see Using a Carbon User Interface in a Cocoa Application in Carbon-Cocoa Integration Guide.

##### Special Considerations

For historical reasons, contrary to normal memory management policy `initWithWindowRef:` does  retain `windowRef`. It is therefore recommended that you make sure you retain `windowRef` before calling this method. If `windowRef` is still valid when the Cocoa window is deallocated, the Cocoa window will release it.

## Parameters

- `windowRef`: The Carbon   object to use to create the Cocoa window.

## See Also

- [class NSWindow](nswindow.md)
  A window that an app displays on the screen.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/init(windowref:))*