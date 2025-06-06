# GLKMatrix3SetRow(_:_:_:)

**Framework**: GLKit  
**Kind**: func

Returns a new `3x3` matrix with one row replaced by a new vector.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- macOS 10.8+
- tvOS 9.0+

## Declaration

```swift
func GLKMatrix3SetRow(_ matrix: GLKMatrix3, _ row: Int32, _ vector: GLKVector3) -> GLKMatrix3
```

#### Return Value

A new matrix.

## Parameters

- `matrix`: The source matrix.
- `row`: The index of the row to replace, which must be a number between   and  , inclusive.
- `vector`: A vector holding the replacement component values.

## See Also

- [func GLKMatrix3GetMatrix2(GLKMatrix3) -> GLKMatrix2](glkmatrix3getmatrix2(_:).md)
  Returns the upper-left `2x2` section of a `3x3` matrix.
- [func GLKMatrix3GetColumn(GLKMatrix3, Int32) -> GLKVector3](glkmatrix3getcolumn(_:_:).md)
  Retrieves a column from a `3x3` matrix.
- [func GLKMatrix3GetRow(GLKMatrix3, Int32) -> GLKVector3](glkmatrix3getrow(_:_:).md)
  Retrieves a row from a `3x3` matrix.
- [func GLKMatrix3SetColumn(GLKMatrix3, Int32, GLKVector3) -> GLKMatrix3](glkmatrix3setcolumn(_:_:_:).md)
  Returns a new `3x3` matrix with one column replaced by a new vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkmatrix3setrow(_:_:_:))*