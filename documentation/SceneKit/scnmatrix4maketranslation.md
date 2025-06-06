# SCNMatrix4MakeTranslation(_:_:_:)

**Framework**: SceneKit  
**Kind**: func

Returns a matrix describing a translation transformation.

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
func SCNMatrix4MakeTranslation(_ tx: CGFloat, _ ty: CGFloat, _ tz: CGFloat) -> SCNMatrix4
```

#### Return Value

A new translation matrix.

## Parameters

- `tx`: The translation distance in the x-axis direction.
- `ty`: The translation distance in the y-axis direction.
- `tz`: The translation distance in the z-axis direction.

## See Also

- [func SCNMatrix4MakeRotation(Float, Float, Float, Float) -> SCNMatrix4](scnmatrix4makerotation(_:_:_:_:).md)
  Returns a matrix describing a rotation transformation.
- [func SCNMatrix4MakeScale(Float, Float, Float) -> SCNMatrix4](scnmatrix4makescale(_:_:_:).md)
  Returns a matrix describing a scale transformation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnmatrix4maketranslation(_:_:_:))*