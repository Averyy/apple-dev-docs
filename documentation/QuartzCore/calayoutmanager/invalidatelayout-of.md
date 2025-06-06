# invalidateLayout(of:)

**Framework**: Core Animation  
**Kind**: method

Invalidates the layout of a layer so it knows to refresh its content on the next frame.

**Availability**:
- Mac Catalyst 13.1+
- macOS 10.5+

## Declaration

```swift
optional func invalidateLayout(of layer: CALayer)
```

## See Also

- [func layoutSublayers(of: CALayer)](calayoutmanager/layoutsublayers(of:).md)
  Override to customize layout of sublayers whenever the layer needs redrawing.
- [func preferredSize(of: CALayer) -> CGSize](calayoutmanager/preferredsize(of:).md)
  Override to customize layer size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/calayoutmanager/invalidatelayout(of:))*