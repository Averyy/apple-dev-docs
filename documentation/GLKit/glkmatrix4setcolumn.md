# GLKMatrix4SetColumn(_:_:_:)

**Framework**: GLKit  
**Kind**: func

Returns a new `4x4` matrix with one column replaced by a new vector.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- macOS 10.8+
- tvOS 9.0+

## Declaration

```swift
func GLKMatrix4SetColumn(_ matrix: GLKMatrix4, _ column: Int32, _ vector: GLKVector4) -> GLKMatrix4
```

#### Return Value

A new matrix.

#### Discussion

The first three components of column `3` provide the translation values `tx`, `ty` and `tz`.

## Parameters

- `matrix`: The source matrix.
- `column`: The index of the column to replace, which must be a number between   and  , inclusive.
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
- [func GLKMatrix4SetRow(GLKMatrix4, Int32, GLKVector4) -> GLKMatrix4](glkmatrix4setrow(_:_:_:).md)
  Returns a new `4x4` matrix with one row replaced by a new vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkmatrix4setcolumn(_:_:_:))*