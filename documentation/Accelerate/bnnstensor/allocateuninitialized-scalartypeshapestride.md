# allocateUninitialized(scalarType:shape:stride:)

**Framework**: Accelerate  
**Kind**: method

Creates a `BNNSTensor` of the specified data type with allocated memory.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

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