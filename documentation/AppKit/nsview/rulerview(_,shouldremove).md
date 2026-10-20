# rulerView(_:shouldRemove:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Requests permission for `aRulerView` to remove `aMarker`.

**Availability**:
- macOS

## Declaration

```swift
func rulerView(_ ruler: NSRulerView, shouldRemove marker: NSRulerMarker) -> Bool
```

```objc
- (BOOL) rulerView:(NSRulerView *) ruler shouldRemoveMarker:(NSRulerMarker *) marker;
```

#### Discussion

If the client returns [`true`](../../Swift/true.md) the ruler view allows the user to remove the marker; if the client returns [`false`](../../Swift/false.md) the marker is kept pinned to the ruler’s baseline. This message is sent as many times as needed while the user drags the marker.

The user’s ability to remove a marker is typically set on the marker itself, using NSRulerMarker’s [`isRemovable`](../nsrulermarker/isremovable.md) method. You should use this client view method only when the marker’s removability can vary while the user drags it (for example, if the user must press the Shift key to remove a marker).

## See Also

### Synchronizing with Ruler Views
- [func rulerView(NSRulerView, didAdd: NSRulerMarker)](./rulerview%28_,didadd%29.md)
  Informs the client that `aRulerView` allowed the user to add `aMarker`.
- [func rulerView(NSRulerView, didMove: NSRulerMarker)](./rulerview%28_,didmove%29.md)
  Informs the client that `aRulerView` allowed the user to move `aMarker`.
- [func rulerView(NSRulerView, didRemove: NSRulerMarker)](./rulerview%28_,didremove%29.md)
  Informs the client that `aRulerView` allowed the user to remove `aMarker`.
- [func rulerView(NSRulerView, handleMouseDownWith: NSEvent)](./rulerview%28_,handlemousedownwith%29.md)
  Informs the client that the user has pressed the mouse button while the cursor is in the ruler area of `aRulerView`.
- [func rulerView(NSRulerView, locationFor: NSPoint) -> CGFloat](./rulerview%28_,locationfor%29.md)
- [func rulerView(NSRulerView, pointForLocation: CGFloat) -> NSPoint](./rulerview%28_,pointforlocation%29.md)
- [func rulerView(NSRulerView, shouldAdd: NSRulerMarker) -> Bool](./rulerview%28_,shouldadd%29.md)
  Requests permission for `aRulerView` to add `aMarker`, an NSRulerMarker being dragged onto the ruler by the user.
- [func rulerView(NSRulerView, shouldMove: NSRulerMarker) -> Bool](./rulerview%28_,shouldmove%29.md)
  Requests permission for `aRulerView` to move `aMarker`.
- [func rulerView(NSRulerView, willAdd: NSRulerMarker, atLocation: CGFloat) -> CGFloat](./rulerview%28_,willadd,atlocation%29.md)
  Informs the client that `aRulerView` will add the new NSRulerMarker, `aMarker`.
- [func rulerView(NSRulerView, willMove: NSRulerMarker, toLocation: CGFloat) -> CGFloat](./rulerview%28_,willmove,tolocation%29.md)
  Informs the client that `aRulerView` will move `aMarker`, an NSRulerMarker already on the ruler view.
- [func rulerView(NSRulerView, willSetClientView: NSView)](./rulerview%28_,willsetclientview%29.md)
  Informs the client view that `aRulerView` is about to be appropriated by `newClient`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/rulerview(_:shouldremove:))*