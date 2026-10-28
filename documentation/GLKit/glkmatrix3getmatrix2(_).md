# GLKMatrix3GetMatrix2(_:)

**Framework**: GLKit  
**Kind**: func  
**Role**: Function

Returns the upper-left `2x2` section of a `3x3` matrix.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- macOS 10.8+
- tvOS 9.0+

## Declaration

```swift
func GLKMatrix3GetMatrix2(_ matrix: GLKMatrix3) -> GLKMatrix2
```

```c
static GLKMatrix2 GLKMatrix3GetMatrix2(GLKMatrix3 matrix);
```

## Return Value

A new `2x2` matrix.

## Parameters

- `matrix`: A matrix.

## See Also

### Working With Parts of a Matrix
- [func GLKMatrix3GetColumn(GLKMatrix3, Int32) -> GLKVector3](./glkmatrix3getcolumn%28_,_%29.md)
  Retrieves a column from a `3x3` matrix.
- [func GLKMatrix3GetRow(GLKMatrix3, Int32) -> GLKVector3](./glkmatrix3getrow%28_,_%29.md)
  Retrieves a row from a `3x3` matrix.
- [func GLKMatrix3SetColumn(GLKMatrix3, Int32, GLKVector3) -> GLKMatrix3](./glkmatrix3setcolumn%28_,_,_%29.md)
  Returns a new `3x3` matrix with one column replaced by a new vector.
- [func GLKMatrix3SetRow(GLKMatrix3, Int32, GLKVector3) -> GLKMatrix3](./glkmatrix3setrow%28_,_,_%29.md)
  Returns a new `3x3` matrix with one row replaced by a new vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkmatrix3getmatrix2(_:))*