# SCNMatrix4MakeScale(_:_:_:)

**Framework**: SceneKit  
**Kind**: func

Returns a matrix describing a scale transformation.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
func SCNMatrix4MakeScale(_ sx: Float, _ sy: Float, _ sz: Float) -> SCNMatrix4
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