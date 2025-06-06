# SCNMatrix4Mult(_:_:)

**Framework**: SceneKit  
**Kind**: func

Returns the product of two matrices.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
func SCNMatrix4Mult(_ a: SCNMatrix4, _ b: SCNMatrix4) -> SCNMatrix4
```

#### Return Value

The matrix product of the `matA` and `matB` parameters.

#### Discussion

Matrix multiplication is not commutative. As a transformation, the result of multiplying a matrix `A` by a matrix `B` is the transformation represented by `B` followed by the transformation represented by `A`.

## Parameters

- `a`: The multiplicand, or left operand of matrix multiplication.
- `b`: The multiplier, or right operand of matrix multiplication.

## See Also

- [func SCNMatrix4Translate(SCNMatrix4, Float, Float, Float) -> SCNMatrix4](scnmatrix4translate(_:_:_:_:).md)
  Returns a new matrix created by concatenating the specified matrix with a translation transformation.
- [func SCNMatrix4Rotate(SCNMatrix4, Float, Float, Float, Float) -> SCNMatrix4](scnmatrix4rotate(_:_:_:_:_:).md)
  Returns a new matrix created by concatenating the specified matrix with a rotation transformation.
- [func SCNMatrix4Scale(SCNMatrix4, Float, Float, Float) -> SCNMatrix4](scnmatrix4scale(_:_:_:_:).md)
  Returns a new matrix created by concatenating the specified matrix with a scale transformation.
- [func SCNMatrix4Invert(SCNMatrix4) -> SCNMatrix4](scnmatrix4invert(_:).md)
  Returns the inverse of the specified matrix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnmatrix4mult(_:_:))*