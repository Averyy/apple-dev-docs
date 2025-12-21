# allocate(initializingFrom:shape:stride:)

**Framework**: Accelerate  
**Kind**: method

Creates a `BNNSTensor` populated with a  of the values in `source`.

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
static func allocate<C>(initializingFrom source: C, shape: [Int], stride: [Int]) -> BNNSTensor where C : AccelerateBuffer, C.Element : BNNSScalar
```

## Parameters

- `source`: The collection that provides the source elements.
- `shape`: The shape of the tensor.
- `stride`: The stride of the tensor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnstensor/allocate(initializingfrom:shape:stride:))*