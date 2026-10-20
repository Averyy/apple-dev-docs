# look(at:up:localFront:)

**Framework**: SceneKit  
**Kind**: method

Changes the node’s orientation so that the specified forward vector points toward the specified location.

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
func look(at worldTarget: SCNVector3, up worldUp: SCNVector3, localFront: SCNVector3)
```

#### Discussion

The effects of this method are animatable; that is, calling this method during an implicit-animation transaction animates the rotation effect. (See [`Animating SceneKit Content`](animating-scenekit-content.md).)

## Parameters

- `worldTarget`: The point, in world space, to face the node toward.
- `worldUp`: The direction vector, in world space, that should appear as “up” from the rotated node’s point of view.
- `localFront`: The direction vector, in the node’s local space, that should orient toward the target point.

## See Also

- [func simdLook(at: simd_float3, up: simd_float3, localFront: simd_float3)](scnnode/simdlook(at:up:localfront:).md)
  Changes the node’s orientation so that the specified forward vector points toward the specified location.
- [func rotate(by: SCNQuaternion, aroundTarget: SCNVector3)](scnnode/rotate(by:aroundtarget:).md)
  Changes the node’s position and orientation, relative to its current transform, through a rotation around the specified point in scene space.
- [func localTranslate(by: SCNVector3)](scnnode/localtranslate(by:).md)
  Changes the node’s position relative to its current position.
- [func localRotate(by: SCNQuaternion)](scnnode/localrotate(by:).md)
  Changes the node’s orientation relative to its current orientation.
- [func look(at: SCNVector3)](scnnode/look(at:).md)
  Changes the node’s orientation so that its local forward vector points toward the specified location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnnode/look(at:up:localfront:))*