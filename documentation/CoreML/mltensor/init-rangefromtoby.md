# init(rangeFrom:to:by:)

**Framework**: Core ML  
**Kind**: init

Creates a one-dimensional tensor representing a sequence from a starting value to, but not including, an end value, stepping by the specified amount.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
init(rangeFrom start: Float, to end: Float, by stride: Float.Stride)
```

## Parameters

- `start`: The starting value to use for the sequence. If the sequence contains any values, the first one is  .
- `end`: An end value to limit the sequence.   is never an element of the resulting sequence.
- `stride`: The amount to step by with each iteration.   must be positive.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mltensor/init(rangefrom:to:by:))*