# canStoreColor()

**Framework**: AppKit  
**Kind**: method

Indicates whether the window has a depth limit that allows it to store color values.

**Availability**:
- macOS 10.0+

## Declaration

```swift
@MainActor
func canStoreColor() -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) when the window’s depth limit allows it to store color values; otherwise, [`false`](https://developer.apple.com/documentation/swift/false).

## See Also

- [func shouldDrawColor() -> Bool](nsview/shoulddrawcolor.md)
  Returns a Boolean value indicating whether the view is being drawn to an environment that supports color.
- [var depthLimit: NSWindow.Depth](nswindow/depthlimit.md)
  The depth limit of the window.
- [func gState() -> Int](nswindow/gstate.md)
  Returns the window’s graphics state object.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/canstorecolor())*