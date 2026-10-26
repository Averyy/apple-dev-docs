# SCNVector3ToGLKVector3(_:)

**Framework**: SceneKit  
**Kind**: func  
**Role**: Function

Returns a three-element GLKit vector structure corresponding to a SceneKit vector structure.

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
func SCNVector3ToGLKVector3(_ vector: SCNVector3) -> GLKVector3
```

```c
static GLKVector3 SCNVector3ToGLKVector3(SCNVector3 vector);
```

#### Return Value

A three-element GLKit vector structure representing the same vector as the input parameter.

## Parameters

- `vector`: A three-element SceneKit vector structure.

## See Also

### Converting Vector Types
- [func SCNVector3FromGLKVector3(GLKVector3) -> SCNVector3](./scnvector3fromglkvector3%28_%29.md)
  Returns a three-element SceneKit vector structure corresponding to a GLKit vector structure.
- [SCNVector3FromFloat3](./scnvector3fromfloat3.md)
- [SCNVector3ToFloat3](./scnvector3tofloat3.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnvector3toglkvector3(_:))*