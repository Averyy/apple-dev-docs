# convergenceThreshold

**Framework**: Create ML Components  
**Kind**: property

The convergence threshold.

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
var convergenceThreshold: Double
```

#### Discussion

When the residual is within the convergence threshold of the objective, training stops. The threshold is also used by the `fitted` method to decide when progress is no longer being made, in which case the training process will stop before convergence and before the specified maximum number of iterations (known as early stopping).

Consider reducing this value for a more accurately trained model. But beware of overfitting if the it is set to a very low value. Defaults to 0.01.

## See Also

- [var earlyStopIterationCount: Int](logisticregressionclassifier/configuration-swift.struct/earlystopiterationcount.md)
  The number of iterations to use when evaluating whether to stop early.
- [var l1Penalty: Double](logisticregressionclassifier/configuration-swift.struct/l1penalty.md)
  Weight of the L1 regularization term.
- [var l2Penalty: Double](logisticregressionclassifier/configuration-swift.struct/l2penalty.md)
  Weight of the L2 regularization term.
- [var maximumIterations: Int](logisticregressionclassifier/configuration-swift.struct/maximumiterations.md)
  The maximum number of allowed passes through the data.
- [var optimizationStrategy: OptimizationStrategy](logisticregressionclassifier/configuration-swift.struct/optimizationstrategy.md)
  The optimization strategy.
- [var scaleFeatures: Bool](logisticregressionclassifier/configuration-swift.struct/scalefeatures.md)
  A Boolean value indicating whether to scale the input features.
- [var stepSize: Double](logisticregressionclassifier/configuration-swift.struct/stepsize.md)
  The starting step size to use for the solver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/logisticregressionclassifier/configuration-swift.struct/convergencethreshold)*