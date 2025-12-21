# minimumSequenceLength

**Framework**: Create ML Components  
**Kind**: property

The minimum number of samples required to produce a classification.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
var minimumSequenceLength: Int
```

#### Discussion

This configuration parameter controls the size of the model. Set it to the largest value that is reasonable for your task. For example if your input is accelerometer data sampled at 100Hz and you want to recognize actions, the minimum action duration may be one second, so the minimum sequence length is `100Hz * 1s = 100`. Defaults to 100.

## See Also

- [var batchSize: Int](timeseriesclassifierconfiguration/batchsize.md)
  The number of examples in each training batch.
- [var earlyStoppingIterationCount: Int](timeseriesclassifierconfiguration/earlystoppingiterationcount.md)
  The number of iterations to use when evaluating whether to stop early.
- [var earlyStoppingTolerance: Float](timeseriesclassifierconfiguration/earlystoppingtolerance.md)
  The early-stopping tolerance.
- [var learningRate: Float](timeseriesclassifierconfiguration/learningrate.md)
  The starting learning rate.
- [var maximumIterationCount: Int](timeseriesclassifierconfiguration/maximumiterationcount.md)
  The maximum number of allowed passes through the data.
- [var maximumSequenceLength: Int](timeseriesclassifierconfiguration/maximumsequencelength.md)
  The maximum number of samples that can be classified.
- [var randomSeed: Int?](timeseriesclassifierconfiguration/randomseed.md)
  A seed to generate reproducible results from random operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/timeseriesclassifierconfiguration/minimumsequencelength)*