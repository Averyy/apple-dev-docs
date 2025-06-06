# rulerView(_:shouldRemove:)

**Framework**: AppKit  
**Kind**: method

Requests permission for `aRulerView` to remove `aMarker`.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func rulerView(_ ruler: NSRulerView, shouldRemove marker: NSRulerMarker) -> Bool
```

#### Discussion

If the client returns [`true`](https://developer.apple.com/documentation/swift/true) the ruler view allows the user to remove the marker; if the client returns [`false`](https://developer.apple.com/documentation/swift/false) the marker is kept pinned to the ruler’s baseline. This message is sent as many times as needed while the user drags the marker.

The user’s ability to remove a marker is typically set on the marker itself, using NSRulerMarker’s [`isRemovable`](nsrulermarker/isremovable.md) method. You should use this client view method only when the marker’s removability can vary while the user drags it (for example, if the user must press the Shift key to remove a marker).

## See Also

- [func rulerView(NSRulerView, didAdd: NSRulerMarker)](nsview/rulerview(_:didadd:).md)
  Informs the client that `aRulerView` allowed the user to add `aMarker`.
- [func rulerView(NSRulerView, didMove: NSRulerMarker)](nsview/rulerview(_:didmove:).md)
  Informs the client that `aRulerView` allowed the user to move `aMarker`.
- [func rulerView(NSRulerView, didRemove: NSRulerMarker)](nsview/rulerview(_:didremove:).md)
  Informs the client that `aRulerView` allowed the user to remove `aMarker`.
- [func rulerView(NSRulerView, handleMouseDownWith: NSEvent)](nsview/rulerview(_:handlemousedownwith:).md)
  Informs the client that the user has pressed the mouse button while the cursor is in the ruler area of `aRulerView`.
- [func rulerView(NSRulerView, locationFor: NSPoint) -> CGFloat](nsview/rulerview(_:locationfor:).md)
- [func rulerView(NSRulerView, pointForLocation: CGFloat) -> NSPoint](nsview/rulerview(_:pointforlocation:).md)
- [func rulerView(NSRulerView, shouldAdd: NSRulerMarker) -> Bool](nsview/rulerview(_:shouldadd:).md)
  Requests permission for `aRulerView` to add `aMarker`, an NSRulerMarker being dragged onto the ruler by the user.
- [func rulerView(NSRulerView, shouldMove: NSRulerMarker) -> Bool](nsview/rulerview(_:shouldmove:).md)
  Requests permission for `aRulerView` to move `aMarker`.
- [func rulerView(NSRulerView, willAdd: NSRulerMarker, atLocation: CGFloat) -> CGFloat](nsview/rulerview(_:willadd:atlocation:).md)
  Informs the client that `aRulerView` will add the new NSRulerMarker, `aMarker`.
- [func rulerView(NSRulerView, willMove: NSRulerMarker, toLocation: CGFloat) -> CGFloat](nsview/rulerview(_:willmove:tolocation:).md)
  Informs the client that `aRulerView` will move `aMarker`, an NSRulerMarker already on the ruler view.
- [func rulerView(NSRulerView, willSetClientView: NSView)](nsview/rulerview(_:willsetclientview:).md)
  Informs the client view that `aRulerView` is about to be appropriated by `newClient`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/rulerview(_:shouldremove:))*