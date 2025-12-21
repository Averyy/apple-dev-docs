# earlyStoppingTolerance

**Framework**: Create ML Components  
**Kind**: property

The early-stopping tolerance.

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
var earlyStoppingTolerance: Float
```

#### Discussion

The tolerance is used by the `fitted` method to decide when progress is no longer being made, in which case the training process will stop before the specified maximum number of iterations (known as early stopping). Significant progress happens when the validation loss decreases by at least the tolerance.

Defaults to 0.01.

> **Note**: Early stopping only happens when using the `fitted` method with validation data.

## See Also

- [var batchSize: Int](lineartimeseriesforecasterconfiguration/batchsize.md)
  The number of examples in each training batch.
- [var earlyStoppingIterationCount: Int](lineartimeseriesforecasterconfiguration/earlystoppingiterationcount.md)
  The number of iterations to use when evaluating whether to stop early.
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

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/lineartimeseriesforecasterconfiguration/earlystoppingtolerance)*