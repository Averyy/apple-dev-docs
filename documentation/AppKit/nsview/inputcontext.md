# inputContext

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The text input context object for the view.

**Availability**:
- macOS 10.6+

## Declaration

```swift
var inputContext: NSTextInputContext? { get }
```

```objc
@property (strong, readonly, nullable) NSTextInputContext * inputContext;
```

#### Discussion

The value of this property is `nil` when the view does not conform to the [`NSTextInputClient`](../nstextinputclient.md) protocol.

## See Also

### Handling Events in the View
- [func acceptsFirstMouse(for: NSEvent?) -> Bool](./acceptsfirstmouse%28for%29.md)
  Returns a Boolean value that indicates whether the view accepts the initial mouse-down event.
- [func hitTest(NSPoint) -> NSView?](./hittest%28_%29.md)
  Returns the farthest descendant of the view in the view hierarchy (including itself) that contains a specified point, or `nil` if that point lies completely outside the view.
- [func isMousePoint(NSPoint, in: NSRect) -> Bool](./ismousepoint%28_,in%29.md)
  Returns whether a region of the view contains a specified point, accounting for whether the view is flipped or not.
- [func performKeyEquivalent(with: NSEvent) -> Bool](./performkeyequivalent%28with%29.md)
  Implemented by subclasses to respond to key equivalents (also known as keyboard shortcuts).
- [func rightMouseDown(with: NSEvent)](../nsresponder/rightmousedown%28with%29.md)
  Informs the receiver that the user has pressed the right mouse button.
- [var mouseDownCanMoveWindow: Bool](./mousedowncanmovewindow.md)
  A Boolean value indicating whether the view can pass mouse down events through to its superviews.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/inputcontext)*