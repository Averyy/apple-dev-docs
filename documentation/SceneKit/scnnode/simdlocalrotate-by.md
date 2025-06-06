# simdLocalRotate(by:)

**Framework**: SceneKit  
**Kind**: method

Changes the node’s orientation relative to its current orientation.

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
func simdLocalRotate(by rotation: simd_quatf)
```

#### Discussion

This method rotates the node according to its [`simdPivot`](scnnode/simdpivot.md) transform.

The effects of this method are animatable; that is, calling this method during an implicit-animation transaction animates the rotation effect. (See [`Animating SceneKit Content`](animating-scenekit-content.md).)

## Parameters

- `rotation`: The axis and angle of rotation to apply, in node-local space, expressed as a quaternion.

## See Also

- [func localRotate(by: SCNQuaternion)](scnnode/localrotate(by:).md)
  Changes the node’s orientation relative to its current orientation.
- [func simdRotate(by: simd_quatf, aroundTarget: simd_float3)](scnnode/simdrotate(by:aroundtarget:).md)
  Changes the node’s position and orientation, relative to its current transform, through a rotation around the specified point in scene space.
- [func simdLocalTranslate(by: simd_float3)](scnnode/simdlocaltranslate(by:).md)
  Changes the node’s position relative to its current position.
- [func simdLook(at: simd_float3)](scnnode/simdlook(at:).md)
  Changes the node’s orientation so that its local forward vector points toward the specified location.
- [func simdLook(at: simd_float3, up: simd_float3, localFront: simd_float3)](scnnode/simdlook(at:up:localfront:).md)
  Changes the node’s orientation so that the specified forward vector points toward the specified location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnnode/simdlocalrotate(by:))*