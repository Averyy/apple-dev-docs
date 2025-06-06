# anchorPointZ

**Framework**: Core Animation  
**Kind**: property

The anchor point for the layer’s position along the z axis. Animatable.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var anchorPointZ: CGFloat { get set }
```

#### Discussion

This property specifies the anchor point on the z axis around which geometric manipulations occur. The point is expressed as a distance (measured in points) along the z axis. The default value of this property is `0`.

## See Also

- [var frame: CGRect](calayer/frame.md)
  The layer’s frame rectangle.
- [var bounds: CGRect](calayer/bounds.md)
  The layer’s bounds rectangle. Animatable.
- [var position: CGPoint](calayer/position.md)
  The layer’s position in its superlayer’s coordinate space. Animatable.
- [var zPosition: CGFloat](calayer/zposition.md)
  The layer’s position on the z axis. Animatable.
- [var anchorPoint: CGPoint](calayer/anchorpoint.md)
  Defines the anchor point of the layer’s bounds rectangle. Animatable.
- [var contentsScale: CGFloat](calayer/contentsscale.md)
  The scale factor applied to the layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/calayer/anchorpointz)*