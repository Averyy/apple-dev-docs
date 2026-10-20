# rulerView(_:handleMouseDownWith:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Adds a left tab marker to the ruler at the location clicked.

**Availability**:
- macOS

## Declaration

```swift
func rulerView(_ ruler: NSRulerView, handleMouseDownWith event: NSEvent)
```

```objc
- (void) rulerView:(NSRulerView *) ruler handleMouseDown:(NSEvent *) event;
```

#### Discussion

A subclass can override this method to provide other behavior, such as creating guidelines. This method is invoked once with `theEvent` when the user first clicks the ruler area of `aRulerView`, as described in the [`NSRulerView`](../nsrulerview.md) class specification.

## Parameters

- `ruler`: The ruler view sending the message.
- `event`: The mouse down event.

## See Also

### Supporting the ruler view
- [func rulerView(NSRulerView, didMove: NSRulerMarker)](./rulerview%28_,didmove%29.md)
  Modifies the paragraph style of the paragraphs containing the selection to record the new location of the marker.
- [func rulerView(NSRulerView, willMove: NSRulerMarker, toLocation: CGFloat) -> CGFloat](./rulerview%28_,willmove,tolocation%29.md)
  Returns a potentially modified location to which the marker should be moved.
- [func rulerView(NSRulerView, shouldMove: NSRulerMarker) -> Bool](./rulerview%28_,shouldmove%29.md)
  Returns whether the marker should be moved.
- [func rulerView(NSRulerView, didRemove: NSRulerMarker)](./rulerview%28_,didremove%29.md)
  Modifies the paragraph style of the paragraphs containing the selection—if possible—by removing the specified marker.
- [func rulerView(NSRulerView, shouldRemove: NSRulerMarker) -> Bool](./rulerview%28_,shouldremove%29.md)
  Returns whether the marker should be removed.
- [func rulerView(NSRulerView, didAdd: NSRulerMarker)](./rulerview%28_,didadd%29.md)
  Modifies the paragraph style of the paragraphs containing the selection to accommodate a new marker.
- [func rulerView(NSRulerView, shouldAdd: NSRulerMarker) -> Bool](./rulerview%28_,shouldadd%29.md)
  Returns whether a new marker can be added.
- [func rulerView(NSRulerView, willAdd: NSRulerMarker, atLocation: CGFloat) -> CGFloat](./rulerview%28_,willadd,atlocation%29.md)
  Returns a potentially modified location to which the marker should be added.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextview/rulerview(_:handlemousedownwith:))*