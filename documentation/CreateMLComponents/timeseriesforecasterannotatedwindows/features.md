# features

**Framework**: Create ML Components  
**Kind**: property  
**Role**: Instance Property

The original features.

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
let features: MLShapedArray<Scalar>
```

## See Also

### Inspecting a time series forecaster annotated window
- [let annotations: MLShapedArray<Scalar>](./annotations.md)
  The original annotations.
- [let forecastWindowSize: Int](./forecastwindowsize.md)
  The prediction sample count.
- [let inputWindowSize: Int](./inputwindowsize.md)
  The input sample count.
- [var shufflesElements: Bool](./shuffleselements.md)
  A Boolean value indicating whether to shuffle the elements.
- [var stride: Int](./stride.md)
  The number of samples between windows.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/timeseriesforecasterannotatedwindows/features)*