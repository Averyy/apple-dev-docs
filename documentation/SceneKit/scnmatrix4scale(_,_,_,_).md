# SCNMatrix4Scale(_:_:_:_:)

**Framework**: SceneKit  
**Kind**: func  
**Role**: Function

Returns a new matrix created by concatenating the specified matrix with a scale transformation.

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
func SCNMatrix4Scale(_ m: SCNMatrix4, _ sx: Float, _ sy: Float, _ sz: Float) -> SCNMatrix4
```

*macOS*

```swift
func SCNMatrix4Scale(_ m: SCNMatrix4, _ sx: CGFloat, _ sy: CGFloat, _ sz: CGFloat) -> SCNMatrix4
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```c
extern SCNMatrix4 SCNMatrix4Scale(SCNMatrix4 m, float sx, float sy, float sz);
```

*macOS*

```c
extern SCNMatrix4 SCNMatrix4Scale(SCNMatrix4 m, CGFloat sx, CGFloat sy, CGFloat sz);
```

#### Return Value

A new matrix.

#### Discussion

The resulting transformation consists of the specified scale followed by the transformation represented by the `mat` parameter.

## Parameters

- `m`: The matrix to be combined with a translation.
- `sx`: The scale factor in the x-axis direction.
- `sy`: The scale factor in the y-axis direction.
- `sz`: The scale factor in the z-axis direction.

## See Also

### Performing Matrix Operations
- [func SCNMatrix4Translate(SCNMatrix4, Float, Float, Float) -> SCNMatrix4](./scnmatrix4translate%28_,_,_,_%29.md)
  Returns a new matrix created by concatenating the specified matrix with a translation transformation.
- [func SCNMatrix4Rotate(SCNMatrix4, Float, Float, Float, Float) -> SCNMatrix4](./scnmatrix4rotate%28_,_,_,_,_%29.md)
  Returns a new matrix created by concatenating the specified matrix with a rotation transformation.
- [func SCNMatrix4Invert(SCNMatrix4) -> SCNMatrix4](./scnmatrix4invert%28_%29.md)
  Returns the inverse of the specified matrix.
- [func SCNMatrix4Mult(SCNMatrix4, SCNMatrix4) -> SCNMatrix4](./scnmatrix4mult%28_,_%29.md)
  Returns the product of two matrices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnmatrix4scale(_:_:_:_:))*