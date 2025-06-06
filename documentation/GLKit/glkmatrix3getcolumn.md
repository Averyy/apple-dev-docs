# GLKMatrix3GetColumn(_:_:)

**Framework**: GLKit  
**Kind**: func

Retrieves a column from a `3x3` matrix.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- macOS 10.8+
- tvOS 9.0+

## Declaration

```swift
func GLKMatrix3GetColumn(_ matrix: GLKMatrix3, _ column: Int32) -> GLKVector3
```

#### Return Value

A vector representing the column retrieved from the matrix.

## Parameters

- `matrix`: A   matrix.
- `column`: The column index, which must be a number between   and  , inclusive.

## See Also

- [func GLKMatrix3GetMatrix2(GLKMatrix3) -> GLKMatrix2](glkmatrix3getmatrix2(_:).md)
  Returns the upper-left `2x2` section of a `3x3` matrix.
- [func GLKMatrix3GetRow(GLKMatrix3, Int32) -> GLKVector3](glkmatrix3getrow(_:_:).md)
  Retrieves a row from a `3x3` matrix.
- [func GLKMatrix3SetColumn(GLKMatrix3, Int32, GLKVector3) -> GLKMatrix3](glkmatrix3setcolumn(_:_:_:).md)
  Returns a new `3x3` matrix with one column replaced by a new vector.
- [func GLKMatrix3SetRow(GLKMatrix3, Int32, GLKVector3) -> GLKMatrix3](glkmatrix3setrow(_:_:_:).md)
  Returns a new `3x3` matrix with one row replaced by a new vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkmatrix3getcolumn(_:_:))*