# init(bytesNoCopy:shape:scalarType:deallocator:)

**Framework**: Core ML  
**Kind**: init

Creates a tensor with memory content without copying the bytes.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
init(bytesNoCopy bytes: UnsafeRawBufferPointer, shape: [Int], scalarType: any MLTensorScalar.Type, deallocator: Data.Deallocator)
```

## Parameters

- `bytes`: A pointer to the C-contiguous memory address for the tensor. Expecting the data to be zero-offset, alignment to match   the alignment of the scalar type, and byte count to be equal or greater than the given shape’s contiguous size.
- `shape`: The shape of the tensor.
- `scalarType`: The scalar type.
- `deallocator`: Specifies the mechanism to free the indicated buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mltensor/init(bytesnocopy:shape:scalartype:deallocator:))*