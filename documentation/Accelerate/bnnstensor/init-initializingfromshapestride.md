# init(initializingFrom:shape:stride:)

**Framework**: Accelerate  
**Kind**: init

Returns a `BNNSTensor` structure that’s initialized with every element of the source.

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
init<T>(initializingFrom source: some AccelerateBuffer, shape: [Int], stride: [Int]) where T : BNNSScalar
```

## Parameters

- `source`: A collection of elements that the function uses to initialize the tensor’s storage.
- `shape`: The shape of the tensor.
- `stride`: The stride of the tensor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnstensor/init(initializingfrom:shape:stride:))*