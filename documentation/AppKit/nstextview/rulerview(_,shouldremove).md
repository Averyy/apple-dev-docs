# rulerView(_:shouldRemove:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns whether the marker should be removed.

**Availability**:
- macOS

## Declaration

```swift
func rulerView(_ ruler: NSRulerView, shouldRemove marker: NSRulerMarker) -> Bool
```

```objc
- (BOOL) rulerView:(NSRulerView *) ruler shouldRemoveMarker:(NSRulerMarker *) marker;
```

#### Return Value

[`true`](../../Swift/true.md) if `aMarker` can be removed, [`false`](../../Swift/false.md) otherwise.

#### Discussion

Only markers that represent tab stops can be removed. This method returns [`true`](../../Swift/true.md) if `aMarker` represents an [`NSTextTab`](../nstexttab.md) object, [`false`](../../Swift/false.md) otherwise. Because this method can be invoked repeatedly as the user drags a ruler marker, it returns that value immediately. If the change is allowed and the user actually removes the marker, the receiver is also sent a [`rulerView(_:didRemove:)`](./rulerview%28_,didremove%29.md) message.

## Parameters

- `ruler`: The ruler view sending the message.
- `marker`: The marker to be removed.

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
- [func rulerView(NSRulerView, didAdd: NSRulerMarker)](./rulerview%28_,didadd%29.md)
  Modifies the paragraph style of the paragraphs containing the selection to accommodate a new marker.
- [func rulerView(NSRulerView, shouldAdd: NSRulerMarker) -> Bool](./rulerview%28_,shouldadd%29.md)
  Returns whether a new marker can be added.
- [func rulerView(NSRulerView, willAdd: NSRulerMarker, atLocation: CGFloat) -> CGFloat](./rulerview%28_,willadd,atlocation%29.md)
  Returns a potentially modified location to which the marker should be added.
- [func rulerView(NSRulerView, handleMouseDownWith: NSEvent)](./rulerview%28_,handlemousedownwith%29.md)
  Adds a left tab marker to the ruler at the location clicked.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextview/rulerview(_:shouldremove:))*