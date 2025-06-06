# rulerView(_:didMove:)

**Framework**: AppKit  
**Kind**: method

Modifies the paragraph style of the paragraphs containing the selection to record the new location of the marker.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func rulerView(_ ruler: NSRulerView, didMove marker: NSRulerMarker)
```

#### Discussion

This method records the change by invoking [`didChangeText()`](nstextview/didchangetext().md) after moving the marker.

`NSTextView` checks for permission to make the change in its [`rulerView(_:shouldMove:)`](nstextview/rulerview(_:shouldmove:).md) method, which invokes [`shouldChangeText(in:replacementString:)`](nstextview/shouldchangetext(in:replacementstring:).md) to send out the proper request and notifications, and only invokes this method if permission is granted.

## Parameters

- `ruler`: The ruler view sending the message.
- `marker`: The marker that was moved.

## See Also

- [var representedObject: (any NSCopying)?](nsrulermarker/representedobject.md)
  The object the receiver represents.
- [func rulerView(NSRulerView, willMove: NSRulerMarker, toLocation: CGFloat) -> CGFloat](nstextview/rulerview(_:willmove:tolocation:).md)
  Returns a potentially modified location to which the marker should be moved.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextview/rulerview(_:didmove:))*