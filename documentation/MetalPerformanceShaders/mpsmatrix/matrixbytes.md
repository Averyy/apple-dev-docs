# matrixBytes

**Framework**: Metal Performance Shaders  
**Kind**: property  
**Role**: Instance Property

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var matrixBytes: Int { get }
```

```objc
@property (nonatomic, readonly) NSUInteger matrixBytes;
```

## See Also

### Properties
- [var device: any MTLDevice](./device.md)
  The device on which the matrix will be used.
- [var rows: Int](./rows.md)
  The number of rows in the matrix.
- [var columns: Int](./columns.md)
  The number of columns in the matrix.
- [var dataType: MPSDataType](./datatype.md)
  The type of the values in the matrix.
- [var rowBytes: Int](./rowbytes.md)
  The stride, in bytes, between corresponding elements of consecutive rows in the matrix.
- [var data: any MTLBuffer](./data.md)
  The buffer that stores the matrix data.
- [var matrices: Int](./matrices.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsmatrix/matrixbytes)*