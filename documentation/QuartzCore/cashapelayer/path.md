# path

**Framework**: Core Animation  
**Kind**: property

The path defining the shape to be rendered. Animatable.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var path: CGPath? { get set }
```

#### Discussion

Unlike most animatable properties, [`path`](cashapelayer/path.md) (as with all [`CGPath`](https://developer.apple.com/documentation/CoreGraphics/CGPath) animatable properties) does not support implicit animation.

The path object may be animated using any of the concrete subclasses of [`CAPropertyAnimation`](capropertyanimation.md). Paths will interpolate as a linear blend of  the “on-line” points; “off-line” points may be interpolated non-linearly (e.g. to preserve continuity of the curve’s derivative). If the two paths have a different number of control points or segments the results are undefined. If the path extends outside the layer bounds it will not automatically be clipped to the layer, only if the normal layer masking rules cause that.

The default value of this property is `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/cashapelayer/path)*