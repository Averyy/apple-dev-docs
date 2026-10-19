# drag(_:at:offset:event:pasteboard:source:slideBack:)

**Framework**: AppKit  
**Kind**: method

Begins a dragging session.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func drag(_ image: NSImage, at baseLocation: NSPoint, offset initialOffset: NSSize, event: NSEvent, pasteboard pboard: NSPasteboard, source sourceObj: Any, slideBack slideFlag: Bool)
```

#### Discussion

This method should be invoked only from within a view’s implementation of the [`mouseDown(with:)`](nsresponder/mousedown(with:).md) or [`mouseDragged(with:)`](nsresponder/mousedragged(with:).md) methods (which overrides the version defined in `NSResponder` class). Essentially the same as the `NSView` method of the same name, except that `baseLocation` is given in the `NSWindow` object’s base coordinate system.

## Parameters

- `image`: The object to be dragged.
- `baseLocation`: Location of the image’s bottom-left corner in the window’s coordinate system. It determines the placement of the dragged image under the pointer.
- `initialOffset`: The pointer’s location relative to the mouse-down location. Not used in macOS 10.4 and later.
- `event`: The left-mouse down event that triggered the dragging operation.
- `pboard`: The pasteboard that holds the data to be transferred to the destination.
- `sourceObj`: The object serving as the controller of the dragging operation. It must conform to the [`NSDraggingSource`](nsdraggingsource.md) protocol.
- `slideFlag`: Specifies whether the drag image should slide back to `baseLocation` if it’s rejected by the drag destination. Pass [`true`](https://developer.apple.com/documentation/swift/true) to specify slide back behavior or [`false`](https://developer.apple.com/documentation/swift/false) to specify that it should not.

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
- [func disableScreenUpdatesUntilFlush()](nswindow/disablescreenupdatesuntilflush.md)
  Disables the window’s screen updates until the window is flushed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/drag(_:at:offset:event:pasteboard:source:slideback:))*