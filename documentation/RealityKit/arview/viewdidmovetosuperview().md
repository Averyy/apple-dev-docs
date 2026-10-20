# viewDidMoveToSuperview()

**Framework**: RealityKit  
**Kind**: method

Tells the view that it has a new superview or that the view’s superview has been removed.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
@preconcurrency override dynamic func viewDidMoveToSuperview()
```

## See Also

- [var frame: NSRect](arview/frame.md)
  The frame rectangle, which describes the view’s location and size in the coordinate system of the view’s superview.
- [var contentScaleFactor: CGFloat](arview/contentscalefactor.md)
  The scale factor of the content in the view.
- [func didMoveToSuperview()](arview/didmovetosuperview.md)
  Tells the view that its superview changed.
- [func didMoveToWindow()](arview/didmovetowindow.md)
  Tells the view that its window property is set to a new value.
- [func layoutSubviews()](arview/layoutsubviews.md)
  Lays out subviews.
- [func layout()](arview/layout.md)
- [class var layerClass: AnyClass](arview/layerclass.md)
  The class used to create the layer for view instances.
- [func makeBackingLayer() -> CALayer](arview/makebackinglayer.md)
  Creates the view’s backing layer.
- [func viewDidChangeBackingProperties()](arview/viewdidchangebackingproperties.md)
  Tells the view when its backing store properties change.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/arview/viewdidmovetosuperview())*