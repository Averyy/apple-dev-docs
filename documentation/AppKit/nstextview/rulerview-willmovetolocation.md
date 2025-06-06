# rulerView(_:willMove:toLocation:)

**Framework**: AppKit  
**Kind**: method

Returns a potentially modified location to which the marker should be moved.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func rulerView(_ ruler: NSRulerView, willMove marker: NSRulerMarker, toLocation location: CGFloat) -> CGFloat
```

#### Return Value

The modified location to which the marker should be moved.

#### Discussion

This method ensures that the proposed `location` of `aMarker` lies within the appropriate bounds for the receiver’s text container. Appropriate bounds are those of the text container minus its line fragment padding.

Typically, the ruler view’s width matches that of its text view.

## Parameters

- `ruler`: The ruler view sending the message.
- `marker`: The marker to be moved.
- `location`: The new location for the marker, in the ruler view’s coordinates.

## See Also

- [func rulerView(NSRulerView, didMove: NSRulerMarker)](nstextview/rulerview(_:didmove:).md)
  Modifies the paragraph style of the paragraphs containing the selection to record the new location of the marker.
- [func rulerView(NSRulerView, shouldMove: NSRulerMarker) -> Bool](nstextview/rulerview(_:shouldmove:).md)
  Returns whether the marker should be moved.
- [func rulerView(NSRulerView, didRemove: NSRulerMarker)](nstextview/rulerview(_:didremove:).md)
  Modifies the paragraph style of the paragraphs containing the selection—if possible—by removing the specified marker.
- [func rulerView(NSRulerView, shouldRemove: NSRulerMarker) -> Bool](nstextview/rulerview(_:shouldremove:).md)
  Returns whether the marker should be removed.
- [func rulerView(NSRulerView, didAdd: NSRulerMarker)](nstextview/rulerview(_:didadd:).md)
  Modifies the paragraph style of the paragraphs containing the selection to accommodate a new marker.
- [func rulerView(NSRulerView, shouldAdd: NSRulerMarker) -> Bool](nstextview/rulerview(_:shouldadd:).md)
  Returns whether a new marker can be added.
- [func rulerView(NSRulerView, willAdd: NSRulerMarker, atLocation: CGFloat) -> CGFloat](nstextview/rulerview(_:willadd:atlocation:).md)
  Returns a potentially modified location to which the marker should be added.
- [func rulerView(NSRulerView, handleMouseDownWith: NSEvent)](nstextview/rulerview(_:handlemousedownwith:).md)
  Adds a left tab marker to the ruler at the location clicked.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextview/rulerview(_:willmove:tolocation:))*