# SCNMatrix4MakeScale(_:_:_:)

**Framework**: SceneKit  
**Kind**: func  
**Role**: Function

Returns a matrix describing a scale transformation.

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

## Declaration

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```swift
func SCNMatrix4MakeScale(_ sx: Float, _ sy: Float, _ sz: Float) -> SCNMatrix4
```

*macOS*

```swift
func SCNMatrix4MakeScale(_ sx: CGFloat, _ sy: CGFloat, _ sz: CGFloat) -> SCNMatrix4
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```c
static SCNMatrix4 SCNMatrix4MakeScale(float sx, float sy, float sz);
```

*macOS*

```c
static SCNMatrix4 SCNMatrix4MakeScale(CGFloat sx, CGFloat sy, CGFloat sz);
```

#### Return Value

A new scale matrix.

## Parameters

- `sx`: The scale factor in the x-axis direction.
- `sy`: The scale factor in the y-axis direction.
- `sz`: The scale factor in the z-axis direction.

## See Also

### Creating Transform Matrices
- [func SCNMatrix4MakeTranslation(Float, Float, Float) -> SCNMatrix4](./scnmatrix4maketranslation%28_,_,_%29.md)
  Returns a matrix describing a translation transformation.
- [func SCNMatrix4MakeRotation(Float, Float, Float, Float) -> SCNMatrix4](./scnmatrix4makerotation%28_,_,_,_%29.md)
  Returns a matrix describing a rotation transformation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnmatrix4makescale(_:_:_:))*