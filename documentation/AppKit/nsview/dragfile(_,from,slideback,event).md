# dragFile(_:from:slideBack:event:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Initiates a dragging operation from the view, allowing the user to drag a file icon to any application that has window or view objects that accept files.

**Availability**:
- macOS 10.0+ - Deprecated in 10.13

> **Deprecated**: Use [`beginDraggingSession(with:event:source:)`](./begindraggingsession%28with,event,source%29.md) instead.

## Declaration

```swift
func dragFile(_ filename: String, from rect: NSRect, slideBack flag: Bool, event: NSEvent) -> Bool
```

```objc
- (BOOL) dragFile:(NSString *) filename fromRect:(NSRect) rect slideBack:(BOOL) flag event:(NSEvent *) event;
```

#### Return Value

[`true`](../../Swift/true.md) if the view successfully initiates the dragging operation (which doesn’t necessarily mean the dragging operation concluded successfully). Otherwise, this method returns [`false`](../../Swift/false.md).

#### Discussion

This method must be invoked only within an implementation of the [`mouseDown(with:)`](../nsresponder/mousedown%28with%29.md) method.

See the [`NSDraggingSource`](../nsdraggingsource.md), [`NSDraggingInfo`](../nsdragginginfo.md), and [`NSDraggingDestination`](../nsdraggingdestination.md) protocol specifications for more information on dragging operations.

## Parameters

- `filename`: A string that specifies the absolute path for the file that is dragged.
- `rect`: A rectangle that describes the position of the icon in the view’s coordinate system.
- `flag`: A Boolean that indicates whether the icon being dragged should slide back to its position in the view if the file isn’t accepted. The icon slides back to `aRect` if `slideBack` is [`true`](../../Swift/true.md), the file is not accepted by the dragging destination, and the user has not disabled icon animation; otherwise it simply disappears.
- `event`: The mouse-down event object from which to initiate the drag operation. In particular, its mouse location is used for the offset of the icon being dragged.

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
- [func shouldDrawColor() -> Bool](./shoulddrawcolor%28%29.md)
  Returns a Boolean value indicating whether the view is being drawn to an environment that supports color.
- [func allocateGState()](./allocategstate%28%29.md)
  Causes the view to maintain a private graphics state object, which encapsulates all parameters of the graphics environment.
- [func gState() -> Int](./gstate%28%29.md)
  Returns the identifier for the view’s graphics state object, or 0 if the view doesn’t have a graphics state object.
- [func setUpGState()](./setupgstate%28%29.md)
  Overridden by subclasses to (re)initialize the view’s graphics state object.
- [func renewGState()](./renewgstate%28%29.md)
  Invalidates the view’s graphics state object, if it has one.
- [func releaseGState()](./releasegstate%28%29.md)
  Frees the view’s graphics state object, if it has one.
- [func dragPromisedFiles(ofTypes: [String], from: NSRect, source: Any, slideBack: Bool, event: NSEvent) -> Bool](./dragpromisedfiles%28oftypes,from,source,slideback,event%29.md)
  Initiates a dragging operation from the view, allowing the user to drag one or more promised files (or directories) into any application that has window or view objects that accept promised file data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/dragfile(_:from:slideback:event:))*