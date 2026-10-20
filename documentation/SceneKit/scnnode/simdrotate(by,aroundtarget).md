# simdRotate(by:aroundTarget:)

**Framework**: SceneKit  
**Kind**: method  
**Role**: Instance Method

Changes the node’s position and orientation, relative to its current transform, through a rotation around the specified point in scene space.

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

## Declaration

```swift
func simdRotate(by worldRotation: simd_quatf, aroundTarget worldTarget: simd_float3)
```

```objc
- (void) simdRotateBy:(simd_quatf) worldRotation aroundTarget:(simd_float3) worldTarget;
```

#### Discussion

The effects of this method are animatable; that is, calling this method during an implicit-animation transaction animates the rotation effect. (See [Animating SceneKit Content](../animating-scenekit-content.md).)

## Parameters

- `worldRotation`: The axis and angle of rotation to apply, in scene space, expressed as a quaternion.
- `worldTarget`: The center point, in scene space, about which to rotate.

## See Also

### Related Documentation
- [func rotate(by: SCNQuaternion, aroundTarget: SCNVector3)](./rotate%28by,aroundtarget%29.md)
  Changes the node’s position and orientation, relative to its current transform, through a rotation around the specified point in scene space.
### Performing Node-Relative Operations
- [func simdLocalTranslate(by: simd_float3)](./simdlocaltranslate%28by%29.md)
  Changes the node’s position relative to its current position.
- [func simdLocalRotate(by: simd_quatf)](./simdlocalrotate%28by%29.md)
  Changes the node’s orientation relative to its current orientation.
- [func simdLook(at: simd_float3)](./simdlook%28at%29.md)
  Changes the node’s orientation so that its local forward vector points toward the specified location.
- [func simdLook(at: simd_float3, up: simd_float3, localFront: simd_float3)](./simdlook%28at,up,localfront%29.md)
  Changes the node’s orientation so that the specified forward vector points toward the specified location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnnode/simdrotate(by:aroundtarget:))*