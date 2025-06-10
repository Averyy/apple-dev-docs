# init(data:shape:stride:dataType:)

**Framework**: Accelerate  
**Kind**: init

Creates a `BNNSTensor` that references the same memory as the specified `UnsafeMutableRawBufferPointer`.

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
init(data: UnsafeMutableRawBufferPointer, shape: [Int], stride: [Int], dataType: BNNSDataType)
```

## Parameters

- `data`: A pointer to the source data.
- `shape`: The shape of the tensor.
- `stride`: The stride of the tensor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnstensor/init(data:shape:stride:datatype:))*