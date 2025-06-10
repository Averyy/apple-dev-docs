# simdLocalTranslate(by:)

**Framework**: SceneKit  
**Kind**: method

Changes the node’s position relative to its current position.

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
func simdLocalTranslate(by translation: simd_float3)
```

#### Discussion

The effects of this method are animatable; that is, calling this method during an implicit-animation transaction animates the move. (See [`Animating SceneKit Content`](animating-scenekit-content.md).)

## Parameters

- `translation`: The distance, in node-local space, by which to move the node.

## See Also

- [func localTranslate(by: SCNVector3)](scnnode/localtranslate(by:).md)
  Changes the node’s position relative to its current position.
- [func simdRotate(by: simd_quatf, aroundTarget: simd_float3)](scnnode/simdrotate(by:aroundtarget:).md)
  Changes the node’s position and orientation, relative to its current transform, through a rotation around the specified point in scene space.
- [func simdLocalRotate(by: simd_quatf)](scnnode/simdlocalrotate(by:).md)
  Changes the node’s orientation relative to its current orientation.
- [func simdLook(at: simd_float3)](scnnode/simdlook(at:).md)
  Changes the node’s orientation so that its local forward vector points toward the specified location.
- [func simdLook(at: simd_float3, up: simd_float3, localFront: simd_float3)](scnnode/simdlook(at:up:localfront:).md)
  Changes the node’s orientation so that the specified forward vector points toward the specified location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnnode/simdlocaltranslate(by:))*