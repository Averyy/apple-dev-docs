# batchSize

**Framework**: Create ML Components  
**Kind**: property

The number of examples to use per mini-batch.

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
var batchSize: Int
```

#### Discussion

A larger batch size will speed up computation when training, as long as the batch fits in memory.

> **Note**: This parameter is only used by the `fitted` method. When using the `update` method it’s up to you to do batching.

This parameter is only used by the `fitted` method. When using the `update` method it’s up to you to do batching.

## See Also

- [var dropoutProbability: Float](fullyconnectednetworkconfiguration/dropoutprobability.md)
  The dropout probability.
- [var earlyStopIterationCount: Int](fullyconnectednetworkconfiguration/earlystopiterationcount.md)
  The number of iterations to use when evaluating whether to stop early.
- [var earlyStoppingTolerance: Double](fullyconnectednetworkconfiguration/earlystoppingtolerance.md)
  The early-stopping tolerance.
- [var hiddenUnitCounts: [Int]](fullyconnectednetworkconfiguration/hiddenunitcounts.md)
  The number of neurons in each hidden layer.
- [var learningRate: Float](fullyconnectednetworkconfiguration/learningrate.md)
  The learning rate.
- [var maximumIterations: Int](fullyconnectednetworkconfiguration/maximumiterations.md)
  The maximum number of iterations.
- [var randomSeed: Int](fullyconnectednetworkconfiguration/randomseed.md)
  A seed to generate reproducible results from random operations such as column and row subsampling.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/fullyconnectednetworkconfiguration/batchsize)*