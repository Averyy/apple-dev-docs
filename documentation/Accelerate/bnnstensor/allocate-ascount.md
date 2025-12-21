# allocate(as:count:)

**Framework**: Accelerate  
**Kind**: method

Allocates a tensor with existing size and stride populated by `Context.tensor(forFunction:argument:fillKnownDynamicShapes:)`.

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
mutating func allocate<T>(as scalarType: T.Type, count: Int) where T : BNNSScalar
```

## Parameters

- `scalarType`: The data type.
- `count`: The allocation size represented by the count of   elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnstensor/allocate(as:count:))*