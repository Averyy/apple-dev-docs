# allocate(initializingFrom:shape:stride:)

**Framework**: Accelerate  
**Kind**: method

Creates a `BNNSTensor` populated with a  of the values in `source`.

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
static func allocate<C>(initializingFrom source: C, shape: [Int], stride: [Int]) -> BNNSTensor where C : AccelerateBuffer, C.Element : BNNSScalar
```

## Parameters

- `source`: The collection that provides the source elements.
- `shape`: The shape of the tensor.
- `stride`: The stride of the tensor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnstensor/allocate(initializingfrom:shape:stride:))*