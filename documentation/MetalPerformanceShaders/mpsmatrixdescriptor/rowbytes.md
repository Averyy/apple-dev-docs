# rowBytes

**Framework**: Metal Performance Shaders  
**Kind**: property

The stride, in bytes, between corresponding elements of consecutive rows in the matrix.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var rowBytes: Int { get set }
```

#### Discussion

This value must be a multiple of the element size.

## See Also

- [var rows: Int](mpsmatrixdescriptor/rows.md)
  The number of rows in the matrix.
- [var columns: Int](mpsmatrixdescriptor/columns.md)
  The number of columns in the matrix.
- [var dataType: MPSDataType](mpsmatrixdescriptor/datatype.md)
  The type of the values in the matrix.
- [enum MPSDataType](mpsdatatype.md)
  A value to specify a type of data.
- [var matrices: Int](mpsmatrixdescriptor/matrices.md)
- [var matrixBytes: Int](mpsmatrixdescriptor/matrixbytes.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsmatrixdescriptor/rowbytes)*