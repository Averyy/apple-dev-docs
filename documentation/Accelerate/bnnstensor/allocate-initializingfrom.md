# allocate(initializingFrom:)

**Framework**: Accelerate  
**Kind**: method

Allocates and initializes a tensor with existing size and stride populated by `Context.tensor(forFunction:argument:fillKnownDynamicShapes:)`.

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
mutating func allocate<T>(initializingFrom source: some AccelerateBuffer) where T : BNNSScalar
```

#### Discussion

This function copies the data in `source` to the tensor and sets the tensor’s `data_type` property to that of the source collection’s elements.

## Parameters

- `source`: The collection that provides the source elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnstensor/allocate(initializingfrom:))*