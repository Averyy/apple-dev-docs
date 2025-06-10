# BNNSDataLayoutRowMajorMatrix

**Framework**: Accelerate  
**Kind**: var

A constant that represents a 2D row-major matrix.

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
var BNNSDataLayoutRowMajorMatrix: BNNSDataLayout { get }
```

#### Discussion

The value `(row, col)` is at index `col * stride[0] + row * stride[1]`.

- `size[0]` is the number of columns.
- `size[1]` is the number of rows.

## See Also

- [var BNNSDataLayoutColumnMajorMatrix: BNNSDataLayout](bnnsdatalayoutcolumnmajormatrix.md)
  A constant that represents a 2D column-major matrix.
- [var BNNSDataLayout2DFirstMajor: BNNSDataLayout](bnnsdatalayout2dfirstmajor.md)
  A constant that represents a 2D first-major matrix.
- [var BNNSDataLayout2DLastMajor: BNNSDataLayout](bnnsdatalayout2dlastmajor.md)
  A constant that represents a 2D last-major matrix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsdatalayoutrowmajormatrix)*