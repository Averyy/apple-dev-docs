# GLKMatrix4SetRow(_:_:_:)

**Framework**: GLKit  
**Kind**: func

Returns a new `4x4` matrix with one row replaced by a new vector.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- macOS 10.8+
- tvOS 9.0+

## Declaration

```swift
func GLKMatrix4SetRow(_ matrix: GLKMatrix4, _ row: Int32, _ vector: GLKVector4) -> GLKMatrix4
```

#### Return Value

A new matrix.

#### Discussion

The last component of rows `0` through `2` correspond to the translation values `tx`, `ty`, and `tz`, respectively.

## Parameters

- `matrix`: The source matrix.
- `row`: The index of the row to replace, which must be a number between   and  , inclusive.
- `vector`: A vector holding the replacement component values.

## See Also

- [func GLKMatrix4GetMatrix2(GLKMatrix4) -> GLKMatrix2](glkmatrix4getmatrix2(_:).md)
  Returns the upper-left `2x2` section of a `4x4` matrix.
- [func GLKMatrix4GetMatrix3(GLKMatrix4) -> GLKMatrix3](glkmatrix4getmatrix3(_:).md)
  Returns the upper-left `3x3` section of a `4x4` matrix.
- [func GLKMatrix4GetColumn(GLKMatrix4, Int32) -> GLKVector4](glkmatrix4getcolumn(_:_:).md)
  Retrieves a column from a `4x4` matrix.
- [func GLKMatrix4GetRow(GLKMatrix4, Int32) -> GLKVector4](glkmatrix4getrow(_:_:).md)
  Retrieves a row from a `4x4` matrix.
- [func GLKMatrix4SetColumn(GLKMatrix4, Int32, GLKVector4) -> GLKMatrix4](glkmatrix4setcolumn(_:_:_:).md)
  Returns a new `4x4` matrix with one column replaced by a new vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkmatrix4setrow(_:_:_:))*