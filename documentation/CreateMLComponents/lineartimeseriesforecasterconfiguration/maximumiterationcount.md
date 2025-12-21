# maximumIterationCount

**Framework**: Create ML Components  
**Kind**: property

The maximum number of allowed passes through the data.

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
var maximumIterationCount: Int
```

#### Discussion

More passes over the data can result in a more accurately trained model. Consider increasing this if the training accuracy is low. Defaults to 25.

> **Note**: This parameter is only used by the `fitted` method. When using the `update` method it’s up to you to decide when to stop.

## See Also

- [var batchSize: Int](lineartimeseriesforecasterconfiguration/batchsize.md)
  The number of examples in each training batch.
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
- [var randomSeed: Int?](lineartimeseriesforecasterconfiguration/randomseed.md)
  A seed to generate reproducible results from random operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/lineartimeseriesforecasterconfiguration/maximumiterationcount)*