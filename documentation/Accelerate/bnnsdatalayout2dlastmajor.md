# BNNSDataLayout2DLastMajor

**Framework**: Accelerate  
**Kind**: var

A constant that represents a 2D last-major matrix.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
var BNNSDataLayout2DLastMajor: BNNSDataLayout { get }
```

#### Discussion

The value `(i, j)` is at index `i * stride[0] + j * stride[1]`.

- `size[0]` is the size of the first dimension (`i`).
- `size[1]` is the size of the second dimension (`j`).

This is the BLAS/LAPACK column-major equivalent.

## See Also

- [var BNNSDataLayoutColumnMajorMatrix: BNNSDataLayout](bnnsdatalayoutcolumnmajormatrix.md)
  A constant that represents a 2D column-major matrix.
- [var BNNSDataLayoutRowMajorMatrix: BNNSDataLayout](bnnsdatalayoutrowmajormatrix.md)
  A constant that represents a 2D row-major matrix.
- [var BNNSDataLayout2DFirstMajor: BNNSDataLayout](bnnsdatalayout2dfirstmajor.md)
  A constant that represents a 2D first-major matrix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsdatalayout2dlastmajor)*