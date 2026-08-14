# SCNMorpher

**Framework**: SceneKit  
**Kind**: class

An object that manages smooth transitions between a node’s base geometry and one or more target geometries.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
class SCNMorpher
```

#### Overview

![None](/images/com.apple.scenekit/media-2929789@2x.png)

You control these transitions by associating an [`SCNMorpher`](scnmorpher.md) object with a node using its [`morpher`](scnnode/morpher.md) property. The morpher maintains an array of target geometries and a set of weights associated with each. When all weights are zero, the surface takes the form of the base geometry (from the node’s [`geometry`](scnnode/geometry.md) property). When you use the [`setWeight(_:forTargetAt:)`](scnmorpher/setweight(_:fortargetat:).md) method to increase a weight to `1.0`, the surface takes the form of the geometry at the corresponding index in the morpher’s [`targets`](scnmorpher/targets.md) array. If you use a variety of weight values for several targets, the surface takes a form that proportionally interpolates between the target geometries.

You can also animate weights implicitly or explicitly using keypath animations. For example, the following code creates a morph animation that transitions one target weight back and forth repeatedly:

```objc
CABasicAnimation *animation = [CABasicAnimation animationWithKeyPath:@"morpher.weights[0]"];
animation.fromValue = @0.0;
animation.toValue = @1.0;
animation.autoreverses = YES;
animation.repeatCount = INFINITY;
animation.duration = 5;
[node addAnimation:animation forKey:nil];
```

A morpher and its target geometries may be loaded from a scene file or created programmatically. The base geometry and all target geometries must be topologically identical—that is, they must contain the same number and structural arrangement of vertices.

## Topics

### Specifying Morph Targets
- [var targets: [SCNGeometry]](scnmorpher/targets.md)
  The array of target geometries to morph between.
### Blending between Morph Targets
- [func weight(forTargetAt: Int) -> CGFloat](scnmorpher/weight(fortargetat:).md)
  Returns the weight value for the specified target index.
- [func setWeight(CGFloat, forTargetAt: Int)](scnmorpher/setweight(_:fortargetat:).md)
  Specifies a weight value at a specified target index.
### Changing Interpolation Mode
- [var calculationMode: SCNMorpherCalculationMode](scnmorpher/calculationmode.md)
  The interpolation formula for blending between target geometries.
### Constants
- [enum SCNMorpherCalculationMode](scnmorphercalculationmode.md)
  The interpolation formulas for blending between target geometries.
### Initializers
- [init?(coder: NSCoder)](scnmorpher/init(coder:).md)
### Instance Properties
- [var unifiesNormals: Bool](scnmorpher/unifiesnormals.md)
- [var weights: [NSNumber]](scnmorpher/weights.md)
### Instance Methods
- [func setWeight(CGFloat, forTargetNamed: String)](scnmorpher/setweight(_:fortargetnamed:).md)
- [func weight(forTargetNamed: String) -> CGFloat](scnmorpher/weight(fortargetnamed:).md)

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)
- [SCNAnimatable](scnanimatable.md)

## See Also

- [Animation](animation.md)
  Create declarative animations that move elements of a scene in predetermined ways, or manage animations imported with external authoring tools.
- [Constraints](constraints.md)
  Automatically adjust the position or orientation of a node based on specified rules.
- [class SCNSkinner](scnskinner.md)
  An object that manages the relationship between skeletal animations and the nodes and geometries they animate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnmorpher)*