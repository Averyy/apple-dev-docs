# SCNMatrix4Mult(_:_:)

**Framework**: SceneKit  
**Kind**: func  
**Role**: Function

Returns the product of two matrices.

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
func SCNMatrix4Mult(_ a: SCNMatrix4, _ b: SCNMatrix4) -> SCNMatrix4
```

```c
extern SCNMatrix4 SCNMatrix4Mult(SCNMatrix4 a, SCNMatrix4 b);
```

## Return Value

The matrix product of the `matA` and `matB` parameters.

## Discussion

Matrix multiplication is not commutative. As a transformation, the result of multiplying a matrix `A` by a matrix `B` is the transformation represented by `B` followed by the transformation represented by `A`.

## Parameters

- `a`: The multiplicand, or left operand of matrix multiplication.
- `b`: The multiplier, or right operand of matrix multiplication.

## See Also

### Performing Matrix Operations
- [func SCNMatrix4Translate(SCNMatrix4, Float, Float, Float) -> SCNMatrix4](./scnmatrix4translate%28_,_,_,_%29.md)
  Returns a new matrix created by concatenating the specified matrix with a translation transformation.
- [func SCNMatrix4Rotate(SCNMatrix4, Float, Float, Float, Float) -> SCNMatrix4](./scnmatrix4rotate%28_,_,_,_,_%29.md)
  Returns a new matrix created by concatenating the specified matrix with a rotation transformation.
- [func SCNMatrix4Scale(SCNMatrix4, Float, Float, Float) -> SCNMatrix4](./scnmatrix4scale%28_,_,_,_%29.md)
  Returns a new matrix created by concatenating the specified matrix with a scale transformation.
- [func SCNMatrix4Invert(SCNMatrix4) -> SCNMatrix4](./scnmatrix4invert%28_%29.md)
  Returns the inverse of the specified matrix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnmatrix4mult(_:_:))*