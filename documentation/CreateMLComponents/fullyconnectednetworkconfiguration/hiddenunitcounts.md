# hiddenUnitCounts

**Framework**: Create ML Components  
**Kind**: property  
**Role**: Instance Property

The number of neurons in each hidden layer.

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
var hiddenUnitCounts: [Int]
```

#### Discussion

Defaults to a single hidden layer with 100 neurons.

## See Also

### Getting the properties
- [var batchSize: Int](./batchsize.md)
  The number of examples to use per mini-batch.
- [var dropoutProbability: Float](./dropoutprobability.md)
  The dropout probability.
- [var earlyStopIterationCount: Int](./earlystopiterationcount.md)
  The number of iterations to use when evaluating whether to stop early.
- [var earlyStoppingTolerance: Double](./earlystoppingtolerance.md)
  The early-stopping tolerance.
- [var learningRate: Float](./learningrate.md)
  The learning rate.
- [var maximumIterations: Int](./maximumiterations.md)
  The maximum number of iterations.
- [var randomSeed: Int](./randomseed.md)
  A seed to generate reproducible results from random operations such as column and row subsampling.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/fullyconnectednetworkconfiguration/hiddenunitcounts)*