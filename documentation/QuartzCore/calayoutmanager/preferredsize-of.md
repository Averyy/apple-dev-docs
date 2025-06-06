# preferredSize(of:)

**Framework**: Core Animation  
**Kind**: method

Override to customize layer size.

**Availability**:
- Mac Catalyst 13.1+
- macOS 10.5+

## Declaration

```swift
optional func preferredSize(of layer: CALayer) -> CGSize
```

## See Also

- [func invalidateLayout(of: CALayer)](calayoutmanager/invalidatelayout(of:).md)
  Invalidates the layout of a layer so it knows to refresh its content on the next frame.
- [func layoutSublayers(of: CALayer)](calayoutmanager/layoutsublayers(of:).md)
  Override to customize layout of sublayers whenever the layer needs redrawing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/calayoutmanager/preferredsize(of:))*