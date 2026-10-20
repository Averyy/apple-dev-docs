# makeBackingLayer()

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method

Creates the view’s backing layer.

**Availability**:
- macOS

## Declaration

```swift
@MainActor
@preconcurrency override dynamic func makeBackingLayer() -> CALayer
```

## See Also

### Managing the view
- [var frame: NSRect](./frame.md)
  The frame rectangle, which describes the view’s location and size in the coordinate system of the view’s superview.
- [var contentScaleFactor: CGFloat](./contentscalefactor.md)
  The scale factor of the content in the view.
- [func didMoveToSuperview()](./didmovetosuperview%28%29.md)
  Tells the view that its superview changed.
- [func didMoveToWindow()](./didmovetowindow%28%29.md)
  Tells the view that its window property is set to a new value.
- [func layoutSubviews()](./layoutsubviews%28%29.md)
  Lays out subviews.
- [func layout()](./layout%28%29.md)
- [class var layerClass: AnyClass](./layerclass.md)
  The class used to create the layer for view instances.
- [func viewDidChangeBackingProperties()](./viewdidchangebackingproperties%28%29.md)
  Tells the view when its backing store properties change.
- [func viewDidMoveToSuperview()](./viewdidmovetosuperview%28%29.md)
  Tells the view that it has a new superview or that the view’s superview has been removed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/arview/makebackinglayer())*