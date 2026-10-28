# learningRate

**Framework**: Create ML Components  
**Kind**: property  
**Role**: Instance Property

The starting learning rate.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
var learningRate: Float
```

## Discussion

Defaults to 0.005.

## See Also

### Inspecting a time series classifier configuration
- [var batchSize: Int](./batchsize.md)
  The number of examples in each training batch.
- [var earlyStoppingIterationCount: Int](./earlystoppingiterationcount.md)
  The number of iterations to use when evaluating whether to stop early.
- [var earlyStoppingTolerance: Float](./earlystoppingtolerance.md)
  The early-stopping tolerance.
- [var maximumIterationCount: Int](./maximumiterationcount.md)
  The maximum number of allowed passes through the data.
- [var maximumSequenceLength: Int](./maximumsequencelength.md)
  The maximum number of samples that can be classified.
- [var minimumSequenceLength: Int](./minimumsequencelength.md)
  The minimum number of samples required to produce a classification.
- [var randomSeed: Int?](./randomseed.md)
  A seed to generate reproducible results from random operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/timeseriesclassifierconfiguration/learningrate)*