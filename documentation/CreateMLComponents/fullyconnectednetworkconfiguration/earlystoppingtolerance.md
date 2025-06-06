# earlyStoppingTolerance

**Framework**: Createmlcomponents  
**Kind**: property

The early-stopping tolerance.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 11.0+

## Declaration

```swift
var earlyStoppingTolerance: Double
```

#### Discussion

The tolerance is used by the `fitted` method to decide when progress is no longer being made, in which case the training process will stop before the specified maximum number of iterations (known as early stopping). Significant progress happens when the validation loss decreases by at least the tolerance.

Defaults to 0.01.

> **Note**: Early stopping only happens when using the `fitted` method with validation data.

## See Also

- [var batchSize: Int](fullyconnectednetworkconfiguration/batchsize.md)
  The number of examples to use per mini-batch.
- [var dropoutProbability: Float](fullyconnectednetworkconfiguration/dropoutprobability.md)
  The dropout probability.
- [var earlyStopIterationCount: Int](fullyconnectednetworkconfiguration/earlystopiterationcount.md)
  The number of iterations to use when evaluating whether to stop early.
- [var hiddenUnitCounts: [Int]](fullyconnectednetworkconfiguration/hiddenunitcounts.md)
  The number of neurons in each hidden layer.
- [var learningRate: Float](fullyconnectednetworkconfiguration/learningrate.md)
  The learning rate.
- [var maximumIterations: Int](fullyconnectednetworkconfiguration/maximumiterations.md)
  The maximum number of iterations.
- [var randomSeed: Int](fullyconnectednetworkconfiguration/randomseed.md)
  A seed to generate reproducible results from random operations such as column and row subsampling.


---

*[View on Apple Developer](https://developer.apple.com/documentation/CreateMLComponents/fullyconnectednetworkconfiguration/earlystoppingtolerance)*