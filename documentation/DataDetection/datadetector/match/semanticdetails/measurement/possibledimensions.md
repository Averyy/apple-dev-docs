# possibleDimensions

**Framework**: DataDetection  
**Kind**: property

An array of dimensions someone can consider for use in a measurement.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
let possibleDimensions: [Dimension]
```

#### Discussion

There’s typically only one measurement, unless the original string is ambiguous and open to interpretation in more than one way. For example, a measurement of “10 degrees” is ambiguous without additional context.

## See Also

- [func measurement<D>(in: D) -> Measurement<D>](datadetector/match/semanticdetails/measurement/measurement(in:).md)
  A function that returns a measurement object initialized with the specified dimensions.
- [let value: Double](datadetector/match/semanticdetails/measurement/value.md)
  The value the framework returns for a measurement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/datadetection/datadetector/match/semanticdetails/measurement/possibledimensions)*