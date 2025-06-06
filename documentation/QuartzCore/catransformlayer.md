# CATransformLayer

**Framework**: Core Animation  
**Kind**: class

Objects used to create true 3D layer hierarchies, rather than the flattened hierarchy rendering model used by other layer types.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class CATransformLayer
```

#### Overview

Unlike normal layers, transform layers do not flatten their sublayers into the plane at `Z=0`. Due to this, they do not support many of the features of the `CALayer` class compositing model:

- Only the sublayers of a transform layer are rendered. The `CALayer` properties that are rendered by a layer are ignored, including: `backgroundColor`, `contents`, border style properties, stroke style properties, etc.
- The properties that assume 2D image processing are also ignored, including: `filters`, `backgroundFilters`, `compositingFilter`, `mask`, `masksToBounds`, and shadow style properties.
- The `opacity` property is applied to each sublayer individually, the transform layer does not form a compositing group.
- The [`hitTest(_:)`](calayer/hittest(_:).md) method should never be called on a transform layer as they do not have a 2D coordinate space into which the point can be mapped.

##### Example Displaying Layers in 3d

Because [`CATransformLayer`](catransformlayer.md) creates true 3D layer hierarchies, you can display otherwise hidden layers when applying 3D transforms.

The following code shows three layers with different colors but identical sizes added at the same position to `layer`. The blue layer is visible because it has the highest [`zPosition`](calayer/zposition.md). Defining the layer’s transform rotates the viewpoint in 3D space and, because `layer` is a [`CATransformLayer`](catransformlayer.md), all three layers are visible as illustrated below.

```swift
let layer = CATransformLayer()
     
func layerOfColor(_ color: UIColor, zPosition: CGFloat) -> CALayer {
    let layer = CALayer()
    layer.frame = CGRect(x: 200, y: -200, width: 400, height: 400)
    layer.backgroundColor = color.cgColor
    layer.zPosition = zPosition
    layer.opacity = 0.5
    
    return layer
}
     
layer.addSublayer(layerOfColor(.red, zPosition: 20))
layer.addSublayer(layerOfColor(.green, zPosition: 40))
layer.addSublayer(layerOfColor(.blue, zPosition: 60))
     
var perspective = CATransform3DIdentity
perspective.m34 = -1 / 100
     
layer.transform = CATransform3DRotate(perspective, 0.1, 0, 1, 0)
```

![Hidden layers made visible in 3D with CATransformLayer](https://docs-assets.developer.apple.com/published/8129009096a4ae5306bed60e0990e15d/media-2826921%402x.png)

However, if `layer` is created as a [`CALayer`](calayer.md), the green and red layers, being hidden by the blue layer, are not rendered as illustrated in the following figure.

![Hidden layers remain hidden in 3D with CALayer](https://docs-assets.developer.apple.com/published/72c00676c58725671134abaf6e31e688/media-2826922%402x.png)

## Relationships

### Inherits From
- [CALayer](calayer.md)
### Conforms To
- [CAMediaTiming](camediatiming.md)
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [class CAScrollLayer](cascrolllayer.md)
  A layer that displays scrollable content larger than its own bounds.
- [class CATiledLayer](catiledlayer.md)
  A layer that provides a way to asynchronously provide tiles of the layer’s content, potentially cached at multiple levels of detail.
- [class CAReplicatorLayer](careplicatorlayer.md)
  A layer that creates a specified number of sublayer copies with varying geometric, temporal, and color transformations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/catransformlayer)*