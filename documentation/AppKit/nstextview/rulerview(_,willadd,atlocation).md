# rulerView(_:willAdd:atLocation:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns a potentially modified location to which the marker should be added.

**Availability**:
- macOS

## Declaration

```swift
func rulerView(_ ruler: NSRulerView, willAdd marker: NSRulerMarker, atLocation location: CGFloat) -> CGFloat
```

```objc
- (CGFloat) rulerView:(NSRulerView *) ruler willAddMarker:(NSRulerMarker *) marker atLocation:(CGFloat) location;
```

#### Return Value

The modified location to which the marker should be added.

#### Discussion

This method ensures that the proposed `location` of `aMarker` lies within the appropriate bounds for the receiver’s text container, returning the modified location. Appropriate bounds are those of the text container minus its line fragment padding.

Typically, the ruler view’s width matches that of its text view.

## Parameters

- `ruler`: The ruler view sending the message.
- `marker`: The marker to be added.
- `location`: The new location for the marker, in the ruler view’s coordinates.

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
- [func rulerView(NSRulerView, shouldRemove: NSRulerMarker) -> Bool](./rulerview%28_,shouldremove%29.md)
  Returns whether the marker should be removed.
- [func rulerView(NSRulerView, didAdd: NSRulerMarker)](./rulerview%28_,didadd%29.md)
  Modifies the paragraph style of the paragraphs containing the selection to accommodate a new marker.
- [func rulerView(NSRulerView, shouldAdd: NSRulerMarker) -> Bool](./rulerview%28_,shouldadd%29.md)
  Returns whether a new marker can be added.
- [func rulerView(NSRulerView, handleMouseDownWith: NSEvent)](./rulerview%28_,handlemousedownwith%29.md)
  Adds a left tab marker to the ruler at the location clicked.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextview/rulerview(_:willadd:atlocation:))*