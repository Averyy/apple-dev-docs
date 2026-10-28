# stepSize

**Framework**: Create ML Components  
**Kind**: property  
**Role**: Instance Property

The starting step size to use for the solver.

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
var stepSize: Double
```

## Discussion

Defaults to 1.0. If the first iteration takes a considerable amount of time, reducing this parameter may speed up model training.

## See Also

### Getting the properties
- [var convergenceThreshold: Double](./convergencethreshold.md)
  The convergence threshold.
- [var earlyStopIterationCount: Int](./earlystopiterationcount.md)
  The number of iterations to use when evaluating whether to stop early.
- [var l1Penalty: Double](./l1penalty.md)
  Weight of the L1 regularization term.
- [var l2Penalty: Double](./l2penalty.md)
  Weight of the L2 regularization term.
- [var maximumIterations: Int](./maximumiterations.md)
  The maximum number of allowed passes through the data.
- [var optimizationStrategy: OptimizationStrategy](./optimizationstrategy.md)
  The optimization strategy.
- [var scaleFeatures: Bool](./scalefeatures.md)
  A Boolean value indicating whether to scale the input features.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/logisticregressionclassifier/configuration-swift.struct/stepsize)*