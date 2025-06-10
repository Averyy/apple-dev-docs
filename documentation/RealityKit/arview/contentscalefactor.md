# contentScaleFactor

**Framework**: RealityKit  
**Kind**: property

The scale factor of the content in the view.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- tvOS 26.0+ (Beta)

## Declaration

```swift
@MainActor
@preconcurrency override dynamic var contentScaleFactor: CGFloat { get set }
```

## See Also

- [var frame: NSRect](arview/frame.md)
  The frame rectangle, which describes the view’s location and size in the coordinate system of the view’s superview.
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
- [func viewDidMoveToSuperview()](arview/viewdidmovetosuperview.md)
  Tells the view that it has a new superview or that the view’s superview has been removed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/arview/contentscalefactor)*