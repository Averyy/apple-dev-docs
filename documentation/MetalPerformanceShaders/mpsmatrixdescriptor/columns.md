# columns

**Framework**: Metal Performance Shaders  
**Kind**: property  
**Role**: Instance Property

The number of columns in the matrix.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var columns: Int { get set }
```

```objc
@property (nonatomic, readwrite) NSUInteger columns;
```

## See Also

### Properties
- [var rows: Int](./rows.md)
  The number of rows in the matrix.
- [var dataType: MPSDataType](./datatype.md)
  The type of the values in the matrix.
- [enum MPSDataType](../mpsdatatype.md)
  A value to specify a type of data.
- [var rowBytes: Int](./rowbytes.md)
  The stride, in bytes, between corresponding elements of consecutive rows in the matrix.
- [var matrices: Int](./matrices.md)
- [var matrixBytes: Int](./matrixbytes.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsmatrixdescriptor/columns)*