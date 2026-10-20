# SKTransformNode

**Framework**: SpriteKit  
**Kind**: class  
**Role**: Class

A node that allows its children to rotate in 3D.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
class SKTransformNode
```

```objc
@interface SKTransformNode : SKNode
```

#### Overview

`SKTranformNode` adds the ability to rotate nodes across the x and y axes. When combined with `SKNode`’s [`zRotation`](./sknode/zrotation.md) property, nodes added as children to a transform node have the ability to rotate in 3D.

## Topics

### Rotating Child Nodes
- [var xRotation: CGFloat](./sktransformnode/xrotation.md)
- [var yRotation: CGFloat](./sktransformnode/yrotation.md)
- [func setEulerAngles(vector_float3)](./sktransformnode/seteulerangles%28_%29.md)
- [func setQuaternion(simd_quatf)](./sktransformnode/setquaternion%28_%29.md)
- [func setRotationMatrix(matrix_float3x3)](./sktransformnode/setrotationmatrix%28_%29.md)
### Reading the Current Rotation
- [func eulerAngles() -> vector_float3](./sktransformnode/eulerangles%28%29.md)
- [func quaternion() -> simd_quatf](./sktransformnode/quaternion%28%29.md)
- [func rotationMatrix() -> matrix_float3x3](./sktransformnode/rotationmatrix%28%29.md)

## Relationships

### Inherits From
- [SKNode](./sknode.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)
- [NSStandardKeyBindingResponding](../AppKit/nsstandardkeybindingresponding.md)
- [NSTouchBarProvider](../AppKit/nstouchbarprovider.md)
- [NSUserActivityRestoring](../AppKit/nsuseractivityrestoring.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [UIActivityItemsConfigurationProviding](../UIKit/uiactivityitemsconfigurationproviding.md)
- [UICoordinateSpace](../UIKit/uicoordinatespace.md)
- [UIFocusEnvironment](../UIKit/uifocusenvironment.md)
- [UIFocusItem](../UIKit/uifocusitem.md)
- [UIFocusItemContainer](../UIKit/uifocusitemcontainer.md)
- [UIPasteConfigurationSupporting](../UIKit/uipasteconfigurationsupporting.md)
- [UIResponderStandardEditActions](../UIKit/uiresponderstandardeditactions.md)
- [UIUserActivityRestoring](../UIKit/uiuseractivityrestoring.md)

## See Also

### Nodes that Modify Drawing
- [class SKEffectNode](./skeffectnode.md)
  A node that renders its children into a separate buffer, optionally applying an effect, before drawing the final result.
- [class SKCropNode](./skcropnode.md)
  A node that masks pixels drawn by its children so that only some pixels are seen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/sktransformnode)*