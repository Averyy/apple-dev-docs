# SCNVector4FromGLKVector4(_:)

**Framework**: SceneKit  
**Kind**: func  
**Role**: Function

Returns a four-element SceneKit vector structure corresponding to a GLKit vector structure.

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
func SCNVector4FromGLKVector4(_ vector: GLKVector4) -> SCNVector4
```

```c
static SCNVector4 SCNVector4FromGLKVector4(GLKVector4 vector);
```

## Return Value

A four-element SceneKit vector structure representing the same vector as the input parameter.

## Parameters

- `vector`: A four-element GLKit vector structure.

## See Also

### Converting Vector Types
- [func SCNVector4ToGLKVector4(SCNVector4) -> GLKVector4](./scnvector4toglkvector4%28_%29.md)
  Returns a four-element GLKit vector structure corresponding to a SceneKit vector structure.
- [SCNVector4FromFloat4](./scnvector4fromfloat4.md)
- [SCNVector4ToFloat4](./scnvector4tofloat4.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnvector4fromglkvector4(_:))*