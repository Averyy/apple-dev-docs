# look(at:)

**Framework**: SceneKit  
**Kind**: method

Changes the node’s orientation so that its local forward vector points toward the specified location.

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
func look(at worldTarget: SCNVector3)
```

#### Discussion

Using this method is equivalent to calling the [`look(at:up:localFront:)`](scnnode/look(at:up:localfront:).md) method and passing the node’s [`worldUp`](scnnode/worldup.md) and [`localFront`](scnnode/localfront.md) vectors for the corresponding parameters.

The effects of this method are animatable; that is, calling this method during an implicit-animation transaction animates the rotation effect. (See [`Animating SceneKit Content`](animating-scenekit-content.md).)

## Parameters

- `worldTarget`: The point, in world space, to face the node toward.

## See Also

- [func simdLook(at: simd_float3)](scnnode/simdlook(at:).md)
  Changes the node’s orientation so that its local forward vector points toward the specified location.
- [func rotate(by: SCNQuaternion, aroundTarget: SCNVector3)](scnnode/rotate(by:aroundtarget:).md)
  Changes the node’s position and orientation, relative to its current transform, through a rotation around the specified point in scene space.
- [func localTranslate(by: SCNVector3)](scnnode/localtranslate(by:).md)
  Changes the node’s position relative to its current position.
- [func localRotate(by: SCNQuaternion)](scnnode/localrotate(by:).md)
  Changes the node’s orientation relative to its current orientation.
- [func look(at: SCNVector3, up: SCNVector3, localFront: SCNVector3)](scnnode/look(at:up:localfront:).md)
  Changes the node’s orientation so that the specified forward vector points toward the specified location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnnode/look(at:))*