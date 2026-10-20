# preferredSize(of:)

**Framework**: Core Animation  
**Kind**: method  
**Role**: Instance Method

Override to customize layer size.

**Availability**:
- Mac Catalyst 13.1+
- macOS 10.5+

## Declaration

```swift
optional func preferredSize(of layer: CALayer) -> CGSize
```

```objc
- (CGSize) preferredSizeOfLayer:(CALayer *) layer;
```

## See Also

### Managing Layout
- [func invalidateLayout(of: CALayer)](./invalidatelayout%28of%29.md)
  Invalidates the layout of a layer so it knows to refresh its content on the next frame.
- [func layoutSublayers(of: CALayer)](./layoutsublayers%28of%29.md)
  Override to customize layout of sublayers whenever the layer needs redrawing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/calayoutmanager/preferredsize(of:))*