# measurement(in:)

**Framework**: DataDetection  
**Kind**: method

A function that returns a measurement object initialized with the specified dimensions.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
func measurement<D>(in dimension: D) -> Measurement<D> where D : Dimension
```

## See Also

- [let possibleDimensions: [Dimension]](datadetector/match/semanticdetails/measurement/possibledimensions.md)
  An array of dimensions someone can consider for use in a measurement.
- [let value: Double](datadetector/match/semanticdetails/measurement/value.md)
  The value the framework returns for a measurement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/datadetection/datadetector/match/semanticdetails/measurement/measurement(in:))*