# batchSize

**Framework**: Create ML Components  
**Kind**: property

The number of examples in each training batch.

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
var batchSize: Int
```

#### Discussion

> **Note**: This parameter is only used by the `fitted` method.

## See Also

- [var earlyStoppingIterationCount: Int](lineartimeseriesforecasterconfiguration/earlystoppingiterationcount.md)
  The number of iterations to use when evaluating whether to stop early.
- [var earlyStoppingTolerance: Float](lineartimeseriesforecasterconfiguration/earlystoppingtolerance.md)
  The early-stopping tolerance.
- [var forecastWindowSize: Int](lineartimeseriesforecasterconfiguration/forecastwindowsize.md)
  The number of predicted samples.
- [var inputWindowSize: Int](lineartimeseriesforecasterconfiguration/inputwindowsize.md)
  The number of input samples.
- [var learningRate: Float](lineartimeseriesforecasterconfiguration/learningrate.md)
  The starting learning rate.
- [var maximumIterationCount: Int](lineartimeseriesforecasterconfiguration/maximumiterationcount.md)
  The maximum number of allowed passes through the data.
- [var randomSeed: Int?](lineartimeseriesforecasterconfiguration/randomseed.md)
  A seed to generate reproducible results from random operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/lineartimeseriesforecasterconfiguration/batchsize)*