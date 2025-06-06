# init(range:desiredCount:minimumStride:)

**Framework**: Swift Charts  
**Kind**: init

Automatically determine the bins from a range of data.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
nonisolated
init(range: ClosedRange<Value>, desiredCount: Int = 10, minimumStride: Value = 0) where Value : BinaryInteger
```

#### Return Value

The inferred bins.

## Parameters

- `range`: The range the bins should cover.
- `desiredCount`: The desired number of bins for the given data.   If  , infer the number automatically from data.
- `minimumStride`: The minimum allowed bin size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/numberbins/init(range:desiredcount:minimumstride:)-4qxfa)*