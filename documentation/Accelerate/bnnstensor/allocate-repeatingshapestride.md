# allocate(repeating:shape:stride:)

**Framework**: Accelerate  
**Kind**: method

Creates a `BNNSTensor` filled with the specified scalar value.

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
static func allocate<T>(repeating repeatedValue: T, shape: [Int], stride: [Int]) -> BNNSTensor where T : BNNSScalar
```

## Parameters

- `repeatedValue`: The value that the function uses for a fillable element.
- `shape`: The shape of the tensor.
- `stride`: The stride of the tensor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnstensor/allocate(repeating:shape:stride:))*