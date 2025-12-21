# earlyStoppingIterationCount

**Framework**: Create ML Components  
**Kind**: property

The number of iterations to use when evaluating whether to stop early.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
var earlyStoppingIterationCount: Int
```

#### Discussion

The `fitted` method will stop if no significant progress is made for this many iterations. Significant progress happens when the validation error decreases by at least `convergenceThreshold`.

> **Note**: Early stopping only happens when using the `fitted` method with validation data.

## See Also

- [var batchSize: Int](timeseriesclassifierconfiguration/batchsize.md)
  The number of examples in each training batch.
- [var earlyStoppingTolerance: Float](timeseriesclassifierconfiguration/earlystoppingtolerance.md)
  The early-stopping tolerance.
- [var learningRate: Float](timeseriesclassifierconfiguration/learningrate.md)
  The starting learning rate.
- [var maximumIterationCount: Int](timeseriesclassifierconfiguration/maximumiterationcount.md)
  The maximum number of allowed passes through the data.
- [var maximumSequenceLength: Int](timeseriesclassifierconfiguration/maximumsequencelength.md)
  The maximum number of samples that can be classified.
- [var minimumSequenceLength: Int](timeseriesclassifierconfiguration/minimumsequencelength.md)
  The minimum number of samples required to produce a classification.
- [var randomSeed: Int?](timeseriesclassifierconfiguration/randomseed.md)
  A seed to generate reproducible results from random operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/timeseriesclassifierconfiguration/earlystoppingiterationcount)*