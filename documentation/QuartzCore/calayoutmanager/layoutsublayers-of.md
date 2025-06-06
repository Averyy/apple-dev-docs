# layoutSublayers(of:)

**Framework**: Core Animation  
**Kind**: method

Override to customize layout of sublayers whenever the layer needs redrawing.

**Availability**:
- Mac Catalyst 13.1+
- macOS 10.5+

## Declaration

```swift
optional func layoutSublayers(of layer: CALayer)
```

## See Also

- [func invalidateLayout(of: CALayer)](calayoutmanager/invalidatelayout(of:).md)
  Invalidates the layout of a layer so it knows to refresh its content on the next frame.
- [func preferredSize(of: CALayer) -> CGSize](calayoutmanager/preferredsize(of:).md)
  Override to customize layer size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/calayoutmanager/layoutsublayers(of:))*