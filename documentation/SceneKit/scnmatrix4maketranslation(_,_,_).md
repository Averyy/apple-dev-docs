# SCNMatrix4MakeTranslation(_:_:_:)

**Framework**: SceneKit  
**Kind**: func  
**Role**: Function

Returns a matrix describing a translation transformation.

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
func SCNMatrix4MakeTranslation(_ tx: Float, _ ty: Float, _ tz: Float) -> SCNMatrix4
```

*macOS*

```swift
func SCNMatrix4MakeTranslation(_ tx: CGFloat, _ ty: CGFloat, _ tz: CGFloat) -> SCNMatrix4
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```c
static SCNMatrix4 SCNMatrix4MakeTranslation(float tx, float ty, float tz);
```

*macOS*

```c
static SCNMatrix4 SCNMatrix4MakeTranslation(CGFloat tx, CGFloat ty, CGFloat tz);
```

#### Return Value

A new translation matrix.

## Parameters

- `tx`: The translation distance in the x-axis direction.
- `ty`: The translation distance in the y-axis direction.
- `tz`: The translation distance in the z-axis direction.

## See Also

### Creating Transform Matrices
- [func SCNMatrix4MakeRotation(Float, Float, Float, Float) -> SCNMatrix4](./scnmatrix4makerotation%28_,_,_,_%29.md)
  Returns a matrix describing a rotation transformation.
- [func SCNMatrix4MakeScale(Float, Float, Float) -> SCNMatrix4](./scnmatrix4makescale%28_,_,_%29.md)
  Returns a matrix describing a scale transformation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnmatrix4maketranslation(_:_:_:))*