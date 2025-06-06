# rulerView(_:willMove:toLocation:)

**Framework**: AppKit  
**Kind**: method

Informs the client that `aRulerView` will move `aMarker`, an NSRulerMarker already on the ruler view.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func rulerView(_ ruler: NSRulerView, willMove marker: NSRulerMarker, toLocation location: CGFloat) -> CGFloat
```

#### Discussion

`location` is the marker’s tentative new location, expressed in the client view’s coordinate system. The value returned by the client view is actually used; the client can simply return `location` unchanged or adjust it as needed. For example, it may snap the location to a grid. This message is sent repeatedly to the client as the user drags the marker.

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
- [func rulerView(NSRulerView, shouldRemove: NSRulerMarker) -> Bool](nsview/rulerview(_:shouldremove:).md)
  Requests permission for `aRulerView` to remove `aMarker`.
- [func rulerView(NSRulerView, willAdd: NSRulerMarker, atLocation: CGFloat) -> CGFloat](nsview/rulerview(_:willadd:atlocation:).md)
  Informs the client that `aRulerView` will add the new NSRulerMarker, `aMarker`.
- [func rulerView(NSRulerView, willSetClientView: NSView)](nsview/rulerview(_:willsetclientview:).md)
  Informs the client view that `aRulerView` is about to be appropriated by `newClient`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/rulerview(_:willmove:tolocation:))*