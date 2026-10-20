# scaleFeatures

**Framework**: Create ML Components  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether to scale the input features.

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
var scaleFeatures: Bool
```

#### Discussion

Scaling the features reduces numerical errors.

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
- [var stepSize: Double](./stepsize.md)
  The starting step size to use for the solver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/logisticregressionclassifier/configuration-swift.struct/scalefeatures)*