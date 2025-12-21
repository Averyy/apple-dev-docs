# allocateUninitialized(scalarType:shape:stride:)

**Framework**: Accelerate  
**Kind**: method

Creates a `BNNSTensor` of the specified data type with allocated memory.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
static func allocateUninitialized(scalarType: any BNNSScalar.Type, shape: [Int], stride: [Int]) -> BNNSTensor
```

## Parameters

- `scalarType`: The data type.
- `shape`: The shape of the tensor.
- `stride`: The stride of the tensor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnstensor/allocateuninitialized(scalartype:shape:stride:))*