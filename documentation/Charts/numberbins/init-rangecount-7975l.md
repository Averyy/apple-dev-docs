# init(range:count:)

**Framework**: Swift Charts  
**Kind**: init

Creates the given number of bins for the range.

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
init(range: ClosedRange<Value>, count: Int) where Value : BinaryFloatingPoint
```

## Parameters

- `range`: The range of the bins. The first bin starts at the lower bound of the range, and the last bin ends at the upper bound of the range.
- `count`: The exact number of bins.


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/numberbins/init(range:count:)-7975l)*