# rulerView(_:shouldAdd:)

**Framework**: AppKit  
**Kind**: method

Returns whether a new marker can be added.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func rulerView(_ ruler: NSRulerView, shouldAdd marker: NSRulerMarker) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if `aMarker` can be added, [`false`](https://developer.apple.com/documentation/Swift/false) otherwise.

#### Discussion

The receiver checks for permission to make the change by invoking [`shouldChangeText(in:replacementString:)`](nstextview/shouldchangetext(in:replacementstring:).md) and returning the return value of that message. If the change is allowed, the receiver is then sent a [`rulerView(_:didAdd:)`](nstextview/rulerview(_:didadd:).md) message.

## Parameters

- `ruler`: The ruler view sending the message.
- `marker`: The marker to be added.

## See Also

- [func rulerView(NSRulerView, didMove: NSRulerMarker)](nstextview/rulerview(_:didmove:).md)
  Modifies the paragraph style of the paragraphs containing the selection to record the new location of the marker.
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
- [func rulerView(NSRulerView, willAdd: NSRulerMarker, atLocation: CGFloat) -> CGFloat](nstextview/rulerview(_:willadd:atlocation:).md)
  Returns a potentially modified location to which the marker should be added.
- [func rulerView(NSRulerView, handleMouseDownWith: NSEvent)](nstextview/rulerview(_:handlemousedownwith:).md)
  Adds a left tab marker to the ruler at the location clicked.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextview/rulerview(_:shouldadd:))*