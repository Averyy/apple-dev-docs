# rulerView(_:didRemove:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Informs the client that `aRulerView` allowed the user to remove `aMarker`.

**Availability**:
- macOS

## Declaration

```swift
func rulerView(_ ruler: NSRulerView, didRemove marker: NSRulerMarker)
```

```objc
- (void) rulerView:(NSRulerView *) ruler didRemoveMarker:(NSRulerMarker *) marker;
```

## Discussion

The client can take whatever action it needs based on this message, such as deleting a tab stop from the paragraph style or removing a layout guideline.

## See Also

### Related Documentation
- [var representedObject: (any NSCopying)?](../nsrulermarker/representedobject.md)
  The object the receiver represents.
### Synchronizing with Ruler Views
- [func rulerView(NSRulerView, didAdd: NSRulerMarker)](./rulerview%28_,didadd%29.md)
  Informs the client that `aRulerView` allowed the user to add `aMarker`.
- [func rulerView(NSRulerView, didMove: NSRulerMarker)](./rulerview%28_,didmove%29.md)
  Informs the client that `aRulerView` allowed the user to move `aMarker`.
- [func rulerView(NSRulerView, handleMouseDownWith: NSEvent)](./rulerview%28_,handlemousedownwith%29.md)
  Informs the client that the user has pressed the mouse button while the cursor is in the ruler area of `aRulerView`.
- [func rulerView(NSRulerView, locationFor: NSPoint) -> CGFloat](./rulerview%28_,locationfor%29.md)
- [func rulerView(NSRulerView, pointForLocation: CGFloat) -> NSPoint](./rulerview%28_,pointforlocation%29.md)
- [func rulerView(NSRulerView, shouldAdd: NSRulerMarker) -> Bool](./rulerview%28_,shouldadd%29.md)
  Requests permission for `aRulerView` to add `aMarker`, an NSRulerMarker being dragged onto the ruler by the user.
- [func rulerView(NSRulerView, shouldMove: NSRulerMarker) -> Bool](./rulerview%28_,shouldmove%29.md)
  Requests permission for `aRulerView` to move `aMarker`.
- [func rulerView(NSRulerView, shouldRemove: NSRulerMarker) -> Bool](./rulerview%28_,shouldremove%29.md)
  Requests permission for `aRulerView` to remove `aMarker`.
- [func rulerView(NSRulerView, willAdd: NSRulerMarker, atLocation: CGFloat) -> CGFloat](./rulerview%28_,willadd,atlocation%29.md)
  Informs the client that `aRulerView` will add the new NSRulerMarker, `aMarker`.
- [func rulerView(NSRulerView, willMove: NSRulerMarker, toLocation: CGFloat) -> CGFloat](./rulerview%28_,willmove,tolocation%29.md)
  Informs the client that `aRulerView` will move `aMarker`, an NSRulerMarker already on the ruler view.
- [func rulerView(NSRulerView, willSetClientView: NSView)](./rulerview%28_,willsetclientview%29.md)
  Informs the client view that `aRulerView` is about to be appropriated by `newClient`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/rulerview(_:didremove:))*