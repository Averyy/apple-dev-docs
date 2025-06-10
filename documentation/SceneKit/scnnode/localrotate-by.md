# localRotate(by:)

**Framework**: SceneKit  
**Kind**: method

Changes the node’s orientation relative to its current orientation.

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
func localRotate(by rotation: SCNQuaternion)
```

#### Discussion

This method rotates the node according to its [`pivot`](scnnode/pivot.md) transform.

The effects of this method are animatable; that is, calling this method during an implicit-animation transaction animates the rotation effect. (See [`Animating SceneKit Content`](animating-scenekit-content.md).)

## Parameters

- `rotation`: The axis and angle of rotation to apply, in node-local space, expressed as a quaternion.

## See Also

- [func simdLocalRotate(by: simd_quatf)](scnnode/simdlocalrotate(by:).md)
  Changes the node’s orientation relative to its current orientation.
- [func rotate(by: SCNQuaternion, aroundTarget: SCNVector3)](scnnode/rotate(by:aroundtarget:).md)
  Changes the node’s position and orientation, relative to its current transform, through a rotation around the specified point in scene space.
- [func localTranslate(by: SCNVector3)](scnnode/localtranslate(by:).md)
  Changes the node’s position relative to its current position.
- [func look(at: SCNVector3)](scnnode/look(at:).md)
  Changes the node’s orientation so that its local forward vector points toward the specified location.
- [func look(at: SCNVector3, up: SCNVector3, localFront: SCNVector3)](scnnode/look(at:up:localfront:).md)
  Changes the node’s orientation so that the specified forward vector points toward the specified location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnnode/localrotate(by:))*