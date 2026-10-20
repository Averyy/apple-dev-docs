# DataDetector.Match.SemanticDetails.Measurement

**Framework**: DataDetection  
**Kind**: struct  
**Role**: Structure

A match that the data detector determines represents a measurement.

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
struct Measurement
```

## Topics

### Values that describe the characteristics of the measurement
- [let possibleDimensions: [Dimension]](./measurement/possibledimensions.md)
  An array of dimensions someone can consider for use in a measurement.
- [func measurement<D>(in: D) -> Measurement<D>](./measurement/measurement%28in%29.md)
  A function that returns a measurement object initialized with the specified dimensions.
- [let value: Double](./measurement/value.md)
  The value the framework returns for a measurement.

## Relationships

### Conforms To
- [Copyable](../../../../Swift/copyable.md)
- [Decodable](../../../../Swift/decodable.md)
- [Encodable](../../../../Swift/encodable.md)
- [Equatable](../../../../Swift/equatable.md)
- [Escapable](../../../../Swift/escapable.md)
- [Hashable](../../../../Swift/hashable.md)
- [Sendable](../../../../Swift/sendable.md)
- [SendableMetatype](../../../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/datadetection/datadetector/match/semanticdetails/measurement)*