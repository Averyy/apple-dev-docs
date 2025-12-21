# allocate(repeating:shape:stride:)

**Framework**: Accelerate  
**Kind**: method

Creates a `BNNSTensor` filled with the specified scalar value.

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
static func allocate<T>(repeating repeatedValue: T, shape: [Int], stride: [Int]) -> BNNSTensor where T : BNNSScalar
```

## Parameters

- `repeatedValue`: The value that the function uses for a fillable element.
- `shape`: The shape of the tensor.
- `stride`: The stride of the tensor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnstensor/allocate(repeating:shape:stride:))*