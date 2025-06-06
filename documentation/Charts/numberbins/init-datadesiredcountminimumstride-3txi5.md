# init(data:desiredCount:minimumStride:)

**Framework**: Swift Charts  
**Kind**: init

Automatically determine the bins from data.

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
init(data: [Value], desiredCount: Int? = nil, minimumStride: Value = 0) where Value : BinaryFloatingPoint
```

#### Return Value

The inferred bins.

## Parameters

- `data`: The given data values.
- `desiredCount`: The desired number of bins for the given data.   If  , infer the number of bins automatically from data using   capped at 200.
- `minimumStride`: The minimum allowed bin size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/numberbins/init(data:desiredcount:minimumstride:)-3txi5)*