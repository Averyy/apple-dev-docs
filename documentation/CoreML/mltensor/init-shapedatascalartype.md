# init(shape:data:scalarType:)

**Framework**: Core ML  
**Kind**: init

Creates a tensor by copying the given block of data.

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
init(shape: [Int], data: Data, scalarType: any MLTensorScalar.Type)
```

## Parameters

- `shape`: The shape of the tensor.
- `data`: The block of data that holds the contents of the tensor whose data is expected to zero-offset, stored in a C-contiguous   (aka row major) way, and alignment to match the alignment of the scalar type.
- `scalarType`: The scalar type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mltensor/init(shape:data:scalartype:))*