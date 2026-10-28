# MPSMatrix

**Framework**: Metal Performance Shaders  
**Kind**: class  
**Role**: Class

A 2D array of data that stores the data’s values.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class MPSMatrix
```

```objc
@interface MPSMatrix : NSObject
```

## Overview

[`MPSMatrix`](./mpsmatrix.md) objects serve as inputs and outputs of [`MPSMatrixMultiplication`](./mpsmatrixmultiplication.md) objects. Matrix data is assumed to be stored in row-major order.

> **Note**:  An [`MPSMatrix`](./mpsmatrix.md) object maintains its internal storage using a [`MTLBuffer`](../Metal/mtlbuffer.md) object. Thus, the same rules for maintaining coherency of the buffer’s data between CPU memory and GPU memory also apply to an [`MPSMatrix`](./mpsmatrix.md) object.

## Topics

### Methods
- [init(buffer: any MTLBuffer, descriptor: MPSMatrixDescriptor)](./mpsmatrix/init%28buffer,descriptor%29.md)
  Initializes a matrix with a buffer.
### Properties
- [var device: any MTLDevice](./mpsmatrix/device.md)
  The device on which the matrix will be used.
- [var rows: Int](./mpsmatrix/rows.md)
  The number of rows in the matrix.
- [var columns: Int](./mpsmatrix/columns.md)
  The number of columns in the matrix.
- [var dataType: MPSDataType](./mpsmatrix/datatype.md)
  The type of the values in the matrix.
- [var rowBytes: Int](./mpsmatrix/rowbytes.md)
  The stride, in bytes, between corresponding elements of consecutive rows in the matrix.
- [var data: any MTLBuffer](./mpsmatrix/data.md)
  The buffer that stores the matrix data.
- [var matrices: Int](./mpsmatrix/matrices.md)
- [var matrixBytes: Int](./mpsmatrix/matrixbytes.md)
### Initializers
- [init(buffer: any MTLBuffer, offset: Int, descriptor: MPSMatrixDescriptor)](./mpsmatrix/init%28buffer,offset,descriptor%29.md)
- [init(device: any MTLDevice, descriptor: MPSMatrixDescriptor)](./mpsmatrix/init%28device,descriptor%29.md)
### Instance Properties
- [var offset: Int](./mpsmatrix/offset.md)
### Instance Methods
- [func resourceSize() -> Int](./mpsmatrix/resourcesize%28%29.md)
- [func synchronize(on: any MTLCommandBuffer)](./mpsmatrix/synchronize%28on%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [MPSTemporaryMatrix](./mpstemporarymatrix.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Matrices
- [class MPSMatrixDescriptor](./mpsmatrixdescriptor.md)
  A description of attributes used to create an MPS matrix.
- [class MPSTemporaryMatrix](./mpstemporarymatrix.md)
  A matrix allocated on GPU private memory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsmatrix)*