# SCNMatrix4MakeRotation(_:_:_:_:)

**Framework**: SceneKit  
**Kind**: func

Returns a matrix describing a rotation transformation.

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
func SCNMatrix4MakeRotation(_ angle: Float, _ x: Float, _ y: Float, _ z: Float) -> SCNMatrix4
```

#### Return Value

A new rotation matrix.

## Parameters

- `angle`: The amount of rotation, in radians, measured counterclockwise around the rotation axis.
- `x`: The x-component of the rotation axis.
- `y`: The y-component of the rotation axis.
- `z`: The z-component of the rotation axis.

## See Also

- [func SCNMatrix4MakeTranslation(Float, Float, Float) -> SCNMatrix4](scnmatrix4maketranslation(_:_:_:).md)
  Returns a matrix describing a translation transformation.
- [func SCNMatrix4MakeScale(Float, Float, Float) -> SCNMatrix4](scnmatrix4makescale(_:_:_:).md)
  Returns a matrix describing a scale transformation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnmatrix4makerotation(_:_:_:_:))*