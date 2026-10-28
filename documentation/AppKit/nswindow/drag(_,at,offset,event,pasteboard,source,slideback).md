# drag(_:at:offset:event:pasteboard:source:slideBack:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Begins a dragging session.

**Availability**:
- macOS 10.0+ - Deprecated in 27.0

> **Deprecated**: Use -[NSWindow beginDraggingSessionWithItems:event:source:] instead.

## Declaration

```swift
func drag(_ image: NSImage, at baseLocation: NSPoint, offset initialOffset: NSSize, event: NSEvent, pasteboard pboard: NSPasteboard, source sourceObj: Any, slideBack slideFlag: Bool)
```

```objc
- (void) dragImage:(NSImage *) image at:(NSPoint) baseLocation offset:(NSSize) initialOffset event:(NSEvent *) event pasteboard:(NSPasteboard *) pboard source:(id) sourceObj slideBack:(BOOL) slideFlag;
```

## Discussion

This method should be invoked only from within a view’s implementation of the [`mouseDown(with:)`](../nsresponder/mousedown%28with%29.md) or [`mouseDragged(with:)`](../nsresponder/mousedragged%28with%29.md) methods (which overrides the version defined in `NSResponder` class). Essentially the same as the `NSView` method of the same name, except that `baseLocation` is given in the `NSWindow` object’s base coordinate system.

## Parameters

- `image`: The object to be dragged.
- `baseLocation`: Location of the image’s bottom-left corner in the window’s coordinate system. It determines the placement of the dragged image under the pointer.
- `initialOffset`: The pointer’s location relative to the mouse-down location. Not used in macOS 10.4 and later.
- `event`: The left-mouse down event that triggered the dragging operation.
- `pboard`: The pasteboard that holds the data to be transferred to the destination.
- `sourceObj`: The object serving as the controller of the dragging operation. It must conform to the [`NSDraggingSource`](../nsdraggingsource.md) protocol.
- `slideFlag`: Specifies whether the drag image should slide back to `baseLocation` if it’s rejected by the drag destination. Pass [`true`](../../Swift/true.md) to specify slide back behavior or [`false`](../../Swift/false.md) to specify that it should not.

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
- [func disableScreenUpdatesUntilFlush()](./disablescreenupdatesuntilflush%28%29.md)
  Disables the window’s screen updates until the window is flushed.
- [- convertBaseToScreen:](./convertbasetoscreen_.md)
  Converts a given point from the window’s base coordinate system to the screen coordinate system.
- [- convertScreenToBase:](./convertscreentobase_.md)
  Converts a given point from the screen coordinate system to the window’s base coordinate system.
- [- userSpaceScaleFactor](./userspacescalefactor.md)
  Returns the scale factor applied to the window.
### Related Documentation
- [- dragImage:at:offset:event:pasteboard:source:slideBack:](../nsview/dragimage_at_offset_event_pasteboard_source_slideback_.md)
  Initiates a dragging operation from the view, allowing the user to drag arbitrary data with a specified icon into any application that has window or view objects that accept dragged data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/drag(_:at:offset:event:pasteboard:source:slideback:))*