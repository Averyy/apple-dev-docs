# setEnabled(_:forSegment:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Sets the enabled state of the specified segment

**Availability**:
- macOS

## Declaration

```swift
func setEnabled(_ enabled: Bool, forSegment segment: Int)
```

```objc
- (void) setEnabled:(BOOL) enabled forSegment:(NSInteger) segment;
```

## Parameters

- `enabled`: [`true`](../../Swift/true.md) to enable the segment; otherwise, [`false`](../../Swift/false.md) to disable it.
- `segment`: The index of the segment you want to enable or disable. This method raises an exception ([`rangeException`](../../Foundation/nsexceptionname/rangeexception.md)) if the index is out of bounds.

## See Also

### Configuring Individual Segments
- [func setLabel(String, forSegment: Int)](./setlabel%28_,forsegment%29.md)
  Sets the label for the specified segment.
- [func label(forSegment: Int) -> String?](./label%28forsegment%29.md)
  Returns the label of the specified segment.
- [func setImage(NSImage?, forSegment: Int)](./setimage%28_,forsegment%29.md)
  Sets the image for the specified segment.
- [func image(forSegment: Int) -> NSImage?](./image%28forsegment%29.md)
  Returns the image associated with the specified segment.
- [func setImageScaling(NSImageScaling, forSegment: Int)](./setimagescaling%28_,forsegment%29.md)
  Sets the image scaling mode for the specified segment.
- [func imageScaling(forSegment: Int) -> NSImageScaling](./imagescaling%28forsegment%29.md)
  Returns the image scaling mode associated with the specified segment.
- [func setWidth(CGFloat, forSegment: Int)](./setwidth%28_,forsegment%29.md)
  Sets the width of the specified segment.
- [func width(forSegment: Int) -> CGFloat](./width%28forsegment%29.md)
  Returns the width of the specified segment.
- [func isEnabled(forSegment: Int) -> Bool](./isenabled%28forsegment%29.md)
  Returns a Boolean value indicating whether the specified segment is enabled.
- [func setMenu(NSMenu?, forSegment: Int)](./setmenu%28_,forsegment%29.md)
  Sets the menu for the specified segment.
- [func menu(forSegment: Int) -> NSMenu?](./menu%28forsegment%29.md)
  Returns the menu for the specified segment.
- [func setToolTip(String?, forSegment: Int)](./settooltip%28_,forsegment%29.md)
  Sets the tooltip for the specified segment.
- [func toolTip(forSegment: Int) -> String?](./tooltip%28forsegment%29.md)
  Returns the tooltip of the specified segment.
- [func setTag(Int, forSegment: Int)](./settag%28_,forsegment%29.md)
  Sets the tag for the specified segment.
- [func tag(forSegment: Int) -> Int](./tag%28forsegment%29.md)
  Returns the tag of the specified segment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssegmentedcell/setenabled(_:forsegment:))*