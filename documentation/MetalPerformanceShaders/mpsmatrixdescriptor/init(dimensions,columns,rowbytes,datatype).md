# init(dimensions:columns:rowBytes:dataType:)

**Framework**: Metal Performance Shaders  
**Kind**: init  
**Role**: Initializer

Creates a matrix descriptor with the specified dimensions and data type.

**Availability**:
- iOS 10.0+ - Deprecated in 11.0
- iPadOS 10.0+ - Deprecated in 11.0
- Mac Catalyst 10.0+ - Deprecated in 11.0
- macOS 10.13+
- tvOS 10.0+ - Deprecated in 11.0
- visionOS 1.0+ - Deprecated in 1.0

## Declaration

```swift
convenience init(dimensions rows: Int, columns: Int, rowBytes: Int, dataType: MPSDataType)
```

```objc
+ (instancetype) matrixDescriptorWithDimensions:(NSUInteger) rows columns:(NSUInteger) columns rowBytes:(NSUInteger) rowBytes dataType:(MPSDataType) dataType;
```

#### Return Value

A valid [`MPSMatrixDescriptor`](../mpsmatrixdescriptor.md) object.

#### Discussion

For performance considerations, the optimal row stride may not necessarily be equal to the number of columns in the matrix. The [`rowBytes(fromColumns:dataType:)`](./rowbytes%28fromcolumns,datatype%29.md) method may be used to help you determine this value.

## Parameters

- `rows`: The number of rows in the matrix.
- `columns`: The number of columns in the matrix.
- `rowBytes`: The stride, in bytes, between corresponding elements of consecutive rows in the matrix.
- `dataType`: The type of the data to be stored in the matrix.

## See Also

### Methods
- [class func rowBytes(fromColumns: Int, dataType: MPSDataType) -> Int](./rowbytes%28fromcolumns,datatype%29.md)
  Determines the recommended matrix row stride, in bytes, for a given number of columns.
- [class func rowBytes(forColumns: Int, dataType: MPSDataType) -> Int](./rowbytes%28forcolumns,datatype%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsmatrixdescriptor/init(dimensions:columns:rowbytes:datatype:))*