# init(shape:scalars:)

**Framework**: Core ML  
**Kind**: init

Creates a tensor with the specified shape and contiguous scalars in first-major order.

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
init(shape: [Int], scalars: some Collection<Float>)
```

## Parameters

- `shape`: The dimensions of the tensor. The product of the dimensions of the shape must equal the number of scalars.
- `scalars`: The scalar contents of the tensor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mltensor/init(shape:scalars:))*