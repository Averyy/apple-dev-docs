# dragImage:at:offset:event:pasteboard:source:slideBack:

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Initiates a dragging operation from the view, allowing the user to drag arbitrary data with a specified icon into any application that has window or view objects that accept dragged data.

**Availability**:
- macOS 10.0+ - Deprecated in 10.7

> **Deprecated**: Use [`beginDraggingSession(with:event:source:)`](./begindraggingsession%28with,event,source%29.md) instead.

## Declaration

```objc
- (void) dragImage:(NSImage *) image at:(NSPoint) viewLocation offset:(NSSize) initialOffset event:(NSEvent *) event pasteboard:(NSPasteboard *) pboard source:(id) sourceObj slideBack:(BOOL) slideFlag;
```

#### Discussion

This method must be invoked only within an implementation of the [`mouseDown(with:)`](../nsresponder/mousedown%28with%29.md) or [`mouseDragged(with:)`](../nsresponder/mousedragged%28with%29.md) methods.

Before invoking this method, you must place the data to be transferred on `pboard`. To do this, get the drag pasteboard object (`NSDragPboard`), declare the types of the data, and then put the data on the pasteboard. This code fragment initiates a dragging operation on an image itself (that is, the image is the data to be transferred):

```objc
- (void)mouseDown:(NSEvent *)theEvent
{
    NSSize dragOffset = NSMakeSize(0.0, 0.0);
    NSPasteboard *pboard;
 
    pboard = [NSPasteboard pasteboardWithName:NSDragPboard];
    [pboard declareTypes:[NSArray arrayWithObject:NSTIFFPboardType]  owner:self];
    [pboard setData:[[self image] TIFFRepresentation] forType:NSTIFFPboardType];
 
    [self dragImage:[self image] at:[self imageLocation] offset:dragOffset
        event:theEvent pasteboard:pboard source:self slideBack:YES];
 
    return;
}
```

See the [`NSDraggingSource`](../nsdraggingsource.md), [`NSDraggingInfo`](../nsdragginginfo.md), and [`NSDraggingDestination`](../nsdraggingdestination.md) protocol specifications for more information on dragging operations.

## Parameters

- `image`: The [`NSImage`](../nsimage.md) object to be dragged.
- `viewLocation`: The location of the image’s lower-left corner, in the view’s coordinate system. It determines the placement of the dragged image under the cursor. When determining the image location you should use the mouse down coordinate, provided in `theEvent`, rather than the current mouse location.
- `initialOffset`: This parameter is ignored.
- `event`: The left mouse-down event that triggered the dragging operation (see discussion below).
- `pboard`: The pasteboard that holds the data to be transferred to the destination (see discussion below).
- `sourceObj`: An object that serves as the controller of the dragging operation. It must conform to the [`NSDraggingSource`](../nsdraggingsource.md) protocol and is typically the view itself or its [`NSWindow`](../nswindow.md) object.
- `slideFlag`: A Boolean that determines whether the drag image should slide back if it’s rejected. The image slides back to `imageLoc` if `slideBack` is [`true`](../../Swift/true.md) and the image isn’t accepted by the dragging destination. If [`false`](../../Swift/false.md) the image doesn’t slide back.

## See Also

### Related Documentation
- [func shouldDelayWindowOrdering(for: NSEvent) -> Bool](./shoulddelaywindowordering%28for%29.md)
  Allows the user to drag objects from the view without activating the app or moving the window of the view forward, possibly obscuring the destination.
### Deprecated methods
- [func lockFocus()](./lockfocus%28%29.md)
  Locks the focus on the view, so subsequent commands take effect in the view’s window and coordinate system.
- [func lockFocusIfCanDraw() -> Bool](./lockfocusifcandraw%28%29.md)
  Locks the focus to the view atomically if the `canDraw` method returns `true` and returns the value of `canDraw`.
- [func lockFocusIfCanDraw(in: NSGraphicsContext) -> Bool](./lockfocusifcandraw%28in%29.md)
  Locks the focus to the view atomically if drawing can occur in the specified graphics context.
- [func unlockFocus()](./unlockfocus%28%29.md)
  Unlocks focus from the current view.
- [func scroll(NSRect, by: NSSize)](./scroll%28_,by%29.md)
  Copies the visible portion of the view’s rendered image within a region and lays that portion down again at a specified offset .
- [- convertPointToBase:](./convertpointtobase_.md)
  Converts the point from the view’s coordinate system to the base coordinate system.
- [- convertPointFromBase:](./convertpointfrombase_.md)
  Converts the point from the base coordinate system to the view’s coordinate system.
- [- convertSizeToBase:](./convertsizetobase_.md)
  Converts the size from the view’s coordinate system to the base coordinate system.
- [- convertSizeFromBase:](./convertsizefrombase_.md)
  Converts the size from the base coordinate system to the view’s coordinate system.
- [- convertRectToBase:](./convertrecttobase_.md)
  Converts the rectangle from the view’s coordinate system to the base coordinate system.
- [- convertRectFromBase:](./convertrectfrombase_.md)
  Converts the rectangle from the base coordinate system to the view’s coordinate system.
- [- performMnemonic:](./performmnemonic_.md)
  Implemented by subclasses to respond to mnemonics.
- [func shouldDrawColor() -> Bool](./shoulddrawcolor%28%29.md)
  Returns a Boolean value indicating whether the view is being drawn to an environment that supports color.
- [func allocateGState()](./allocategstate%28%29.md)
  Causes the view to maintain a private graphics state object, which encapsulates all parameters of the graphics environment.
- [func gState() -> Int](./gstate%28%29.md)
  Returns the identifier for the view’s graphics state object, or 0 if the view doesn’t have a graphics state object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/dragimage:at:offset:event:pasteboard:source:slideback:)*