# invalidateLayout(of:)

**Framework**: Core Animation  
**Kind**: method  
**Role**: Instance Method

Invalidates the layout of a layer so it knows to refresh its content on the next frame.

**Availability**:
- Mac Catalyst 13.1+
- macOS 10.5+

## Declaration

```swift
optional func invalidateLayout(of layer: CALayer)
```

```objc
- (void) invalidateLayoutOfLayer:(CALayer *) layer;
```

## See Also

### Managing Layout
- [func layoutSublayers(of: CALayer)](./layoutsublayers%28of%29.md)
  Override to customize layout of sublayers whenever the layer needs redrawing.
- [func preferredSize(of: CALayer) -> CGSize](./preferredsize%28of%29.md)
  Override to customize layer size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/calayoutmanager/invalidatelayout(of:))*