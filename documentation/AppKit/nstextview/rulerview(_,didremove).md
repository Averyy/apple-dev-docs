# rulerView(_:didRemove:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Modifies the paragraph style of the paragraphs containing the selection—if possible—by removing the specified marker.

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

This method records the change by invoking [`didChangeText()`](./didchangetext%28%29.md) after removing the marker.

`NSTextView` checks for permission to move or remove a tab stop in its [`rulerView(_:shouldMove:)`](./rulerview%28_,shouldmove%29.md) method, which invokes [`shouldChangeText(in:replacementString:)`](./shouldchangetext%28in,replacementstring%29.md) to send out the proper request and notifications, and only invokes this method if permission is granted.

## Parameters

- `ruler`: The ruler view sending the message.
- `marker`: The marker that was removed.

## See Also

### Related Documentation
- [var representedObject: (any NSCopying)?](../nsrulermarker/representedobject.md)
  The object the receiver represents.
- [func shouldChangeText(in: NSRange, replacementString: String?) -> Bool](./shouldchangetext%28in,replacementstring%29.md)
  Initiates a series of delegate messages (and general notifications) to determine whether modifications can be made to the characters and attributes of the receiver’s text.
### Supporting the ruler view
- [func rulerView(NSRulerView, didMove: NSRulerMarker)](./rulerview%28_,didmove%29.md)
  Modifies the paragraph style of the paragraphs containing the selection to record the new location of the marker.
- [func rulerView(NSRulerView, willMove: NSRulerMarker, toLocation: CGFloat) -> CGFloat](./rulerview%28_,willmove,tolocation%29.md)
  Returns a potentially modified location to which the marker should be moved.
- [func rulerView(NSRulerView, shouldMove: NSRulerMarker) -> Bool](./rulerview%28_,shouldmove%29.md)
  Returns whether the marker should be moved.
- [func rulerView(NSRulerView, shouldRemove: NSRulerMarker) -> Bool](./rulerview%28_,shouldremove%29.md)
  Returns whether the marker should be removed.
- [func rulerView(NSRulerView, didAdd: NSRulerMarker)](./rulerview%28_,didadd%29.md)
  Modifies the paragraph style of the paragraphs containing the selection to accommodate a new marker.
- [func rulerView(NSRulerView, shouldAdd: NSRulerMarker) -> Bool](./rulerview%28_,shouldadd%29.md)
  Returns whether a new marker can be added.
- [func rulerView(NSRulerView, willAdd: NSRulerMarker, atLocation: CGFloat) -> CGFloat](./rulerview%28_,willadd,atlocation%29.md)
  Returns a potentially modified location to which the marker should be added.
- [func rulerView(NSRulerView, handleMouseDownWith: NSEvent)](./rulerview%28_,handlemousedownwith%29.md)
  Adds a left tab marker to the ruler at the location clicked.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextview/rulerview(_:didremove:))*