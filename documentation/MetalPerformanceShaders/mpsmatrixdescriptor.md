# MPSMatrixDescriptor

**Framework**: Metal Performance Shaders  
**Kind**: class  
**Role**: Class

A description of attributes used to create an MPS matrix.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class MPSMatrixDescriptor
```

```objc
@interface MPSMatrixDescriptor : NSObject
```

#### Overview

Matrix data is assumed to be stored in row-major order.

## Topics

### Initializers
- [convenience init(rows: Int, columns: Int, matrices: Int, rowBytes: Int, matrixBytes: Int, dataType: MPSDataType)](./mpsmatrixdescriptor/init%28rows,columns,matrices,rowbytes,matrixbytes,datatype%29.md)
- [convenience init(rows: Int, columns: Int, rowBytes: Int, dataType: MPSDataType)](./mpsmatrixdescriptor/init%28rows,columns,rowbytes,datatype%29.md)
### Methods
- [convenience init(dimensions: Int, columns: Int, rowBytes: Int, dataType: MPSDataType)](./mpsmatrixdescriptor/init%28dimensions,columns,rowbytes,datatype%29.md)
  Creates a matrix descriptor with the specified dimensions and data type.
- [class func rowBytes(fromColumns: Int, dataType: MPSDataType) -> Int](./mpsmatrixdescriptor/rowbytes%28fromcolumns,datatype%29.md)
  Determines the recommended matrix row stride, in bytes, for a given number of columns.
- [class func rowBytes(forColumns: Int, dataType: MPSDataType) -> Int](./mpsmatrixdescriptor/rowbytes%28forcolumns,datatype%29.md)
### Properties
- [var rows: Int](./mpsmatrixdescriptor/rows.md)
  The number of rows in the matrix.
- [var columns: Int](./mpsmatrixdescriptor/columns.md)
  The number of columns in the matrix.
- [var dataType: MPSDataType](./mpsmatrixdescriptor/datatype.md)
  The type of the values in the matrix.
- [enum MPSDataType](./mpsdatatype.md)
  A value to specify a type of data.
- [var rowBytes: Int](./mpsmatrixdescriptor/rowbytes.md)
  The stride, in bytes, between corresponding elements of consecutive rows in the matrix.
- [var matrices: Int](./mpsmatrixdescriptor/matrices.md)
- [var matrixBytes: Int](./mpsmatrixdescriptor/matrixbytes.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Matrices
- [class MPSMatrix](./mpsmatrix.md)
  A 2D array of data that stores the data’s values.
- [class MPSTemporaryMatrix](./mpstemporarymatrix.md)
  A matrix allocated on GPU private memory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsmatrixdescriptor)*