# SKTransformNode

**Framework**: SpriteKit  
**Kind**: class

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

#### Overview

`SKTranformNode` adds the ability to rotate nodes across the x and y axes. When combined with `SKNode`’s [`zRotation`](sknode/zrotation.md) property, nodes added as children to a transform node have the ability to rotate in 3D.

## Topics

### Rotating Child Nodes
- [var xRotation: CGFloat](sktransformnode/xrotation.md)
- [var yRotation: CGFloat](sktransformnode/yrotation.md)
- [func setEulerAngles(vector_float3)](sktransformnode/seteulerangles(_:).md)
- [func setQuaternion(simd_quatf)](sktransformnode/setquaternion(_:).md)
- [func setRotationMatrix(matrix_float3x3)](sktransformnode/setrotationmatrix(_:).md)
### Reading the Current Rotation
- [func eulerAngles() -> vector_float3](sktransformnode/eulerangles.md)
- [func quaternion() -> simd_quatf](sktransformnode/quaternion.md)
- [func rotationMatrix() -> matrix_float3x3](sktransformnode/rotationmatrix.md)

## Relationships

### Inherits From
- [SKNode](sknode.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSCopying](../foundation/nscopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)
- [NSStandardKeyBindingResponding](../appkit/nsstandardkeybindingresponding.md)
- [NSTouchBarProvider](../appkit/nstouchbarprovider.md)
- [NSUserActivityRestoring](../appkit/nsuseractivityrestoring.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [UIActivityItemsConfigurationProviding](../uikit/uiactivityitemsconfigurationproviding.md)
- [UICoordinateSpace](../uikit/uicoordinatespace.md)
- [UIFocusEnvironment](../uikit/uifocusenvironment.md)
- [UIFocusItem](../uikit/uifocusitem.md)
- [UIFocusItemContainer](../uikit/uifocusitemcontainer.md)
- [UIPasteConfigurationSupporting](../uikit/uipasteconfigurationsupporting.md)
- [UIResponderStandardEditActions](../uikit/uiresponderstandardeditactions.md)
- [UIUserActivityRestoring](../uikit/uiuseractivityrestoring.md)

## See Also

- [class SKEffectNode](skeffectnode.md)
  A node that renders its children into a separate buffer, optionally applying an effect, before drawing the final result.
- [class SKCropNode](skcropnode.md)
  A node that masks pixels drawn by its children so that only some pixels are seen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/sktransformnode)*