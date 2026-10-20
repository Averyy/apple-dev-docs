# SCNMatrix4Translate(_:_:_:_:)

**Framework**: SceneKit  
**Kind**: func  
**Role**: Function

Returns a new matrix created by concatenating the specified matrix with a translation transformation.

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
func SCNMatrix4Translate(_ m: SCNMatrix4, _ tx: Float, _ ty: Float, _ tz: Float) -> SCNMatrix4
```

*macOS*

```swift
func SCNMatrix4Translate(_ m: SCNMatrix4, _ tx: CGFloat, _ ty: CGFloat, _ tz: CGFloat) -> SCNMatrix4
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```c
static SCNMatrix4 SCNMatrix4Translate(SCNMatrix4 m, float tx, float ty, float tz);
```

*macOS*

```c
static SCNMatrix4 SCNMatrix4Translate(SCNMatrix4 m, CGFloat tx, CGFloat ty, CGFloat tz);
```

#### Return Value

A new matrix.

#### Discussion

The resulting transformation consists of the specified translation followed by the transformation represented by the `mat` parameter.

## Parameters

- `m`: The matrix to be combined with a translation.
- `tx`: The translation distance in the x-axis direction.
- `ty`: The translation distance in the y-axis direction.
- `tz`: The translation distance in the z-axis direction.

## See Also

### Performing Matrix Operations
- [func SCNMatrix4Rotate(SCNMatrix4, Float, Float, Float, Float) -> SCNMatrix4](./scnmatrix4rotate%28_,_,_,_,_%29.md)
  Returns a new matrix created by concatenating the specified matrix with a rotation transformation.
- [func SCNMatrix4Scale(SCNMatrix4, Float, Float, Float) -> SCNMatrix4](./scnmatrix4scale%28_,_,_,_%29.md)
  Returns a new matrix created by concatenating the specified matrix with a scale transformation.
- [func SCNMatrix4Invert(SCNMatrix4) -> SCNMatrix4](./scnmatrix4invert%28_%29.md)
  Returns the inverse of the specified matrix.
- [func SCNMatrix4Mult(SCNMatrix4, SCNMatrix4) -> SCNMatrix4](./scnmatrix4mult%28_,_%29.md)
  Returns the product of two matrices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnmatrix4translate(_:_:_:_:))*