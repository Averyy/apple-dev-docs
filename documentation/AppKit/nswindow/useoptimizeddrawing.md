# useOptimizedDrawing(_:)

**Framework**: AppKit  
**Kind**: method

Specifies whether the window is to optimize focusing and drawing when displaying its views.

**Availability**:
- macOS 10.0+

## Declaration

```swift
@MainActor
func useOptimizedDrawing(_ flag: Bool)
```

#### Discussion

The optimizations may prevent sibling subviews from being displayed in the correct order—which matters only if the subviews overlap. You should always set `flag` to [`true`](https://developer.apple.com/documentation/Swift/true) when there are no overlapping subviews within the window. The default is [`false`](https://developer.apple.com/documentation/Swift/false).

## Parameters

- `flag`: If  , the window will optimize focusing and drawing for its views; if  , it will not, in which case, the window does not preserve the Z-ordering of overlapping views when an object explicitly sends   to a view and draws directly to it, instead of using the AppKit standard display mechanism.

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
- [convenience init?(windowRef: UnsafeMutableRawPointer)](nswindow/init(windowref:).md)
  Returns a Cocoa window created from a Carbon window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/useoptimizeddrawing(_:))*