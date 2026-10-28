# setUpGState()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Overridden by subclasses to (re)initialize the view’s graphics state object.

**Availability**:
- macOS 10.0+ - Deprecated in 10.10

> **Deprecated**: Manage graphics state using an [`NSGraphicsContext`](../nsgraphicscontext.md) object.

## Declaration

```swift
func setUpGState()
```

```objc
- (void) setUpGState;
```

## Discussion

This method is automatically invoked when the graphics state object created using [`allocateGState()`](./allocategstate%28%29.md) needs to be initialized. The default implementation does nothing. Your subclass can override it to set the current font, line width, or any other graphics state parameter except coordinate transformations and the clipping path—these are established by the frame and bounds rectangles and by methods such as [`scaleUnitSquare(to:)`](./scaleunitsquare%28to%29.md) and [`translateOrigin(to:)`](./translateorigin%28to%29.md). Note that `drawRect:` can further transform the coordinate system and clipping path for whatever temporary effects it needs.

## See Also

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
- [func renewGState()](./renewgstate%28%29.md)
  Invalidates the view’s graphics state object, if it has one.
- [func releaseGState()](./releasegstate%28%29.md)
  Frees the view’s graphics state object, if it has one.
- [func dragFile(String, from: NSRect, slideBack: Bool, event: NSEvent) -> Bool](./dragfile%28_,from,slideback,event%29.md)
  Initiates a dragging operation from the view, allowing the user to drag a file icon to any application that has window or view objects that accept files.
- [func dragPromisedFiles(ofTypes: [String], from: NSRect, source: Any, slideBack: Bool, event: NSEvent) -> Bool](./dragpromisedfiles%28oftypes,from,source,slideback,event%29.md)
  Initiates a dragging operation from the view, allowing the user to drag one or more promised files (or directories) into any application that has window or view objects that accept promised file data.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/setupgstate())*