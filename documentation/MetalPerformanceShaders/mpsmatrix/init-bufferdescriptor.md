# init(buffer:descriptor:)

**Framework**: Metal Performance Shaders  
**Kind**: init

Initializes a matrix with a buffer.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
init(buffer: any MTLBuffer, descriptor: MPSMatrixDescriptor)
```

#### Return Value

A valid [`MPSMatrix`](mpsmatrix.md) object or `nil`, if failure.

#### Discussion

The dimensions and stride of the matrix are specified by the [`MPSMatrixDescriptor`](mpsmatrixdescriptor.md) object. The size of the provided [`MTLBuffer`](https://developer.apple.com/documentation/Metal/MTLBuffer) object must be large enough to store the following amount of bytes:

`(descriptor.rows-1) * descriptor.rowBytes + descriptor.columns * (element size)`

## Parameters

- `buffer`: The buffer that stores the matrix data.
- `descriptor`: The matrix descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsmatrix/init(buffer:descriptor:))*