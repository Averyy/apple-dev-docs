# look(at:)

**Framework**: SceneKit  
**Kind**: method  
**Role**: Instance Method

Changes the node’s orientation so that its local forward vector points toward the specified location.

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
func look(at worldTarget: SCNVector3)
```

```objc
- (void) lookAt:(SCNVector3) worldTarget;
```

## Discussion

Using this method is equivalent to calling the [`look(at:up:localFront:)`](./look%28at,up,localfront%29.md) method and passing the node’s [`worldUp`](./worldup.md) and [`localFront`](./localfront.md) vectors for the corresponding parameters.

The effects of this method are animatable; that is, calling this method during an implicit-animation transaction animates the rotation effect. (See [Animating SceneKit Content](../animating-scenekit-content.md).)

## Parameters

- `worldTarget`: The point, in world space, to face the node toward.

## See Also

### Related Documentation
- [func simdLook(at: simd_float3)](./simdlook%28at%29.md)
  Changes the node’s orientation so that its local forward vector points toward the specified location.
### Performing Node-Relative Operations (SceneKit Types)
- [func rotate(by: SCNQuaternion, aroundTarget: SCNVector3)](./rotate%28by,aroundtarget%29.md)
  Changes the node’s position and orientation, relative to its current transform, through a rotation around the specified point in scene space.
- [func localTranslate(by: SCNVector3)](./localtranslate%28by%29.md)
  Changes the node’s position relative to its current position.
- [func localRotate(by: SCNQuaternion)](./localrotate%28by%29.md)
  Changes the node’s orientation relative to its current orientation.
- [func look(at: SCNVector3, up: SCNVector3, localFront: SCNVector3)](./look%28at,up,localfront%29.md)
  Changes the node’s orientation so that the specified forward vector points toward the specified location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnnode/look(at:))*