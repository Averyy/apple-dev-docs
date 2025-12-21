# SCNMatrix4MakeScale(_:_:_:)

**Framework**: SceneKit  
**Kind**: func

Returns a matrix describing a scale transformation.

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
func SCNMatrix4MakeScale(_ sx: CGFloat, _ sy: CGFloat, _ sz: CGFloat) -> SCNMatrix4
```

#### Return Value

A new scale matrix.

## Parameters

- `sx`: The scale factor in the x-axis direction.
- `sy`: The scale factor in the y-axis direction.
- `sz`: The scale factor in the z-axis direction.

## See Also

- [func SCNMatrix4MakeTranslation(Float, Float, Float) -> SCNMatrix4](scnmatrix4maketranslation(_:_:_:).md)
  Returns a matrix describing a translation transformation.
- [func SCNMatrix4MakeRotation(Float, Float, Float, Float) -> SCNMatrix4](scnmatrix4makerotation(_:_:_:_:).md)
  Returns a matrix describing a rotation transformation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnmatrix4makescale(_:_:_:))*