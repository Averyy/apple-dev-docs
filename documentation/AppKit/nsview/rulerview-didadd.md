# rulerView(_:didAdd:)

**Framework**: AppKit  
**Kind**: method

Informs the client that `aRulerView` allowed the user to add `aMarker`.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func rulerView(_ ruler: NSRulerView, didAdd marker: NSRulerMarker)
```

#### Discussion

The client can take whatever action it needs based on this message, such as adding a new tab stop to the selected paragraph or creating a layout guideline.

## See Also

- [var representedObject: (any NSCopying)?](nsrulermarker/representedobject.md)
  The object the receiver represents.
- [var markerLocation: CGFloat](nsrulermarker/markerlocation.md)
  The location of the receiver in the coordinate system of the ruler view’s client view.
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
- [func rulerView(NSRulerView, willMove: NSRulerMarker, toLocation: CGFloat) -> CGFloat](nsview/rulerview(_:willmove:tolocation:).md)
  Informs the client that `aRulerView` will move `aMarker`, an NSRulerMarker already on the ruler view.
- [func rulerView(NSRulerView, willSetClientView: NSView)](nsview/rulerview(_:willsetclientview:).md)
  Informs the client view that `aRulerView` is about to be appropriated by `newClient`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/rulerview(_:didadd:))*