# simdRotate(by:aroundTarget:)

**Framework**: SceneKit  
**Kind**: method

Changes the node’s position and orientation, relative to its current transform, through a rotation around the specified point in scene space.

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
func simdRotate(by worldRotation: simd_quatf, aroundTarget worldTarget: simd_float3)
```

#### Discussion

The effects of this method are animatable; that is, calling this method during an implicit-animation transaction animates the rotation effect. (See [`Animating SceneKit Content`](animating-scenekit-content.md).)

## Parameters

- `worldRotation`: The axis and angle of rotation to apply, in scene space, expressed as a quaternion.
- `worldTarget`: The center point, in scene space, about which to rotate.

## See Also

- [func rotate(by: SCNQuaternion, aroundTarget: SCNVector3)](scnnode/rotate(by:aroundtarget:).md)
  Changes the node’s position and orientation, relative to its current transform, through a rotation around the specified point in scene space.
- [func simdLocalTranslate(by: simd_float3)](scnnode/simdlocaltranslate(by:).md)
  Changes the node’s position relative to its current position.
- [func simdLocalRotate(by: simd_quatf)](scnnode/simdlocalrotate(by:).md)
  Changes the node’s orientation relative to its current orientation.
- [func simdLook(at: simd_float3)](scnnode/simdlook(at:).md)
  Changes the node’s orientation so that its local forward vector points toward the specified location.
- [func simdLook(at: simd_float3, up: simd_float3, localFront: simd_float3)](scnnode/simdlook(at:up:localfront:).md)
  Changes the node’s orientation so that the specified forward vector points toward the specified location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnnode/simdrotate(by:aroundtarget:))*