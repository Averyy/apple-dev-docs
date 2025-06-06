# toolTip(forSegment:)

**Framework**: AppKit  
**Kind**: method

Returns the tooltip of the specified segment.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func toolTip(forSegment segment: Int) -> String?
```

#### Return Value

The text of the tooltip.

#### Discussion

Tooltips are currently not displayed.

## Parameters

- `segment`: The index of the segment whose tooltip you want to get. This method raises an exception ( ) if the index is out of bounds.

## See Also

- [func setLabel(String, forSegment: Int)](nssegmentedcell/setlabel(_:forsegment:).md)
  Sets the label for the specified segment.
- [func label(forSegment: Int) -> String?](nssegmentedcell/label(forsegment:).md)
  Returns the label of the specified segment.
- [func setImage(NSImage?, forSegment: Int)](nssegmentedcell/setimage(_:forsegment:).md)
  Sets the image for the specified segment.
- [func image(forSegment: Int) -> NSImage?](nssegmentedcell/image(forsegment:).md)
  Returns the image associated with the specified segment.
- [func setImageScaling(NSImageScaling, forSegment: Int)](nssegmentedcell/setimagescaling(_:forsegment:).md)
  Sets the image scaling mode for the specified segment.
- [func imageScaling(forSegment: Int) -> NSImageScaling](nssegmentedcell/imagescaling(forsegment:).md)
  Returns the image scaling mode associated with the specified segment.
- [func setWidth(CGFloat, forSegment: Int)](nssegmentedcell/setwidth(_:forsegment:).md)
  Sets the width of the specified segment.
- [func width(forSegment: Int) -> CGFloat](nssegmentedcell/width(forsegment:).md)
  Returns the width of the specified segment.
- [func setEnabled(Bool, forSegment: Int)](nssegmentedcell/setenabled(_:forsegment:).md)
  Sets the enabled state of the specified segment
- [func isEnabled(forSegment: Int) -> Bool](nssegmentedcell/isenabled(forsegment:).md)
  Returns a Boolean value indicating whether the specified segment is enabled.
- [func setMenu(NSMenu?, forSegment: Int)](nssegmentedcell/setmenu(_:forsegment:).md)
  Sets the menu for the specified segment.
- [func menu(forSegment: Int) -> NSMenu?](nssegmentedcell/menu(forsegment:).md)
  Returns the menu for the specified segment.
- [func setToolTip(String?, forSegment: Int)](nssegmentedcell/settooltip(_:forsegment:).md)
  Sets the tooltip for the specified segment.
- [func setTag(Int, forSegment: Int)](nssegmentedcell/settag(_:forsegment:).md)
  Sets the tag for the specified segment.
- [func tag(forSegment: Int) -> Int](nssegmentedcell/tag(forsegment:).md)
  Returns the tag of the specified segment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssegmentedcell/tooltip(forsegment:))*