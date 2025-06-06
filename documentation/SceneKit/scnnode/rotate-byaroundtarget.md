# rotate(by:aroundTarget:)

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
func rotate(by worldRotation: SCNQuaternion, aroundTarget worldTarget: SCNVector3)
```

#### Discussion

The effects of this method are animatable; that is, calling this method during an implicit-animation transaction animates the rotation effect. (See [`Animating SceneKit Content`](animating-scenekit-content.md).)

## Parameters

- `worldRotation`: The axis and angle of rotation to apply, in scene space, expressed as a quaternion.
- `worldTarget`: The center point, in scene space, about which to rotate.

## See Also

- [func simdRotate(by: simd_quatf, aroundTarget: simd_float3)](scnnode/simdrotate(by:aroundtarget:).md)
  Changes the node’s position and orientation, relative to its current transform, through a rotation around the specified point in scene space.
- [func localTranslate(by: SCNVector3)](scnnode/localtranslate(by:).md)
  Changes the node’s position relative to its current position.
- [func localRotate(by: SCNQuaternion)](scnnode/localrotate(by:).md)
  Changes the node’s orientation relative to its current orientation.
- [func look(at: SCNVector3)](scnnode/look(at:).md)
  Changes the node’s orientation so that its local forward vector points toward the specified location.
- [func look(at: SCNVector3, up: SCNVector3, localFront: SCNVector3)](scnnode/look(at:up:localfront:).md)
  Changes the node’s orientation so that the specified forward vector points toward the specified location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnnode/rotate(by:aroundtarget:))*