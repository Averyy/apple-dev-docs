# applied(to:eventHandler:)

**Framework**: Create ML Components  
**Kind**: method

Performs the transformation on an input sequence.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
func applied(to input: some TemporalSequence<MLShapedArray<Scalar>>, eventHandler: EventHandler? = nil) async throws -> AnyTemporalSequence<ClassificationDistribution<Label>>
```

#### Return Value

An temporal sequence of predictions. Each prediction’s shape is `[forecastWindowSize, annotationSize]`.

## Parameters

- `input`: A temporal sequence of features. Each feature’s shape must be  .
- `eventHandler`: An event handler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/timeseriesclassifier/model/applied(to:eventhandler:)-3hpop)*