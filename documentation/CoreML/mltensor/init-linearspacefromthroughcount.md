# init(linearSpaceFrom:through:count:)

**Framework**: Core ML  
**Kind**: init

Creates a one-dimensional tensor representing a sequence from a starting value, up to and including an end value, spaced evenly to generate the number of values specified.

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
init(linearSpaceFrom start: Float, through end: Float, count: Int)
```

## Parameters

- `start`: The starting value to use for the sequence. If the sequence contains any values, the first one is  .
- `end`: An end value to limit the sequence.   is the last element of the resulting sequence.
- `count`: The number of values in the resulting sequence.   must be positive and greater than  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mltensor/init(linearspacefrom:through:count:))*