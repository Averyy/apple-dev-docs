# inputWindowSize

**Framework**: Create ML Components  
**Kind**: property  
**Role**: Instance Property

The number of input samples.

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
var inputWindowSize: Int { get }
```

## See Also

### Inspecting the model
- [var annotationSize: Int](./annotationsize.md)
  The number of annotations per sample.
- [var bias: MLShapedArray<Scalar>?](./bias.md)
  The bias coefficients.
- [var featureSize: Int](./featuresize.md)
  The number of features per sample.
- [var forecastWindowSize: Int](./forecastwindowsize.md)
  The number of prediction samples.
- [var stride: Int](./stride.md)
  The number of samples between windows.
- [var weight: MLShapedArray<Scalar>](./weight.md)
  The linear coefficients.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/lineartimeseriesforecaster/model/inputwindowsize)*