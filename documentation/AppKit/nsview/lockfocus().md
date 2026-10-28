# lockFocus()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Locks the focus on the view, so subsequent commands take effect in the view’s window and coordinate system.

**Availability**:
- macOS 10.0+ - Deprecated in 10.14

> **Deprecated**: Subclass the view and implement [`draw(_:)`](./draw%28_%29.md) instead.

## Declaration

```swift
func lockFocus()
```

```objc
- (void) lockFocus;
```

## Discussion

If you don’t use a `display` method to draw an `NSView` object, you must invoke [`lockFocus()`](./lockfocus%28%29.md) before invoking methods that send commands to the window server, and must balance it with an [`unlockFocus()`](./unlockfocus%28%29.md) message when finished.

Hiding or miniaturizing a one-shot window causes the backing store for that window to be released. (A one-shot window frees its window device when the window is hidden and another is created when it’s returned to the screen.) If you don’t use the standard display mechanism to draw, you should use [`lockFocusIfCanDraw()`](./lockfocusifcandraw%28%29.md) rather than [`lockFocus()`](./lockfocus%28%29.md) if there is a chance of drawing while the window is either miniaturized or hidden. This method throws an exception if the view is hidden or if drawing cannot happen for some other reason. To ensure that you can lock focus successfully, make sure the [`canDraw`](./candraw.md) property is [`true`](../../Swift/true.md); you can also call [`lockFocusIfCanDraw()`](./lockfocusifcandraw%28%29.md) instead and use the return value of that method to determine if focus was obtained successfully.

## See Also

### Related Documentation
- [func draw(NSRect)](./draw%28_%29.md)
  Overridden by subclasses to draw the view’s image within the specified rectangle.
- [class var focusView: NSView?](./focusview.md)
  The currently focused view object.
- [func display()](./display%28%29.md)
  Displays the view and all its subviews if possible, invoking each of the `NSView` methods [`lockFocus()`](./lockfocus%28%29.md), [`draw(_:)`](./draw%28_%29.md), and [`unlockFocus()`](./unlockfocus%28%29.md) as necessary.
### Deprecated methods
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/lockfocus())*