# dropoutProbability

**Framework**: Create ML Components  
**Kind**: property

The dropout probability.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 11.0+

## Declaration

```swift
var dropoutProbability: Float
```

#### Discussion

Dropout layers are placed after fully-connected layers to help prevent over-fitting.

Defaults to 0.2.

## See Also

- [var batchSize: Int](fullyconnectednetworkconfiguration/batchsize.md)
  The number of examples to use per mini-batch.
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

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/fullyconnectednetworkconfiguration/dropoutprobability)*