# contentsScale

**Framework**: Core Animation  
**Kind**: property

The scale factor applied to the layer.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var contentsScale: CGFloat { get set }
```

#### Discussion

This value defines the mapping between the logical coordinate space of the layer (measured in points) and the physical coordinate space (measured in pixels). Higher scale factors indicate that each point in the layer is represented by more than one pixel at render time. For example, if the scale factor is `2.0` and the layer’s bounds are 50 x 50 points, the size of the bitmap used to present the layer’s content is 100 x 100 pixels.

The default value of this property is 1.0. For layers attached to a view, the view changes the scale factor automatically to a value that is appropriate for the current screen. For layers you create and manage yourself, you must set the value of this property yourself based on the resolution of the screen and the content you are providing. Core Animation uses the value you specify as a cue to determine how to render your content.

## See Also

- [var frame: CGRect](calayer/frame.md)
  The layer’s frame rectangle.
- [var bounds: CGRect](calayer/bounds.md)
  The layer’s bounds rectangle. Animatable.
- [var position: CGPoint](calayer/position.md)
  The layer’s position in its superlayer’s coordinate space. Animatable.
- [var zPosition: CGFloat](calayer/zposition.md)
  The layer’s position on the z axis. Animatable.
- [var anchorPointZ: CGFloat](calayer/anchorpointz.md)
  The anchor point for the layer’s position along the z axis. Animatable.
- [var anchorPoint: CGPoint](calayer/anchorpoint.md)
  Defines the anchor point of the layer’s bounds rectangle. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/calayer/contentsscale)*