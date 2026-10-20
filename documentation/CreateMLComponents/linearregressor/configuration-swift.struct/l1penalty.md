# l1Penalty

**Framework**: Create ML Components  
**Kind**: property  
**Role**: Instance Property

Weight of the L1 regularization term.

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
var l1Penalty: Double
```

#### Discussion

Like the l2 penalty, the higher the l1 penalty, the more the estimated coefficients shrink toward 0. The l1 penalty, however, completely zeros out sufficiently small coefficients, automatically indicating features that are not useful for the model. The default weight of 0 prevents any features from being discarded.

## See Also

### Getting the properties
- [var convergenceThreshold: Double](./convergencethreshold.md)
  The convergence threshold.
- [var earlyStopIterationCount: Int](./earlystopiterationcount.md)
  The number of iterations to use when evaluating whether to stop early.
- [var l2Penalty: Double](./l2penalty.md)
  Weight of the L2 regularization term.
- [var maximumIterations: Int](./maximumiterations.md)
  The maximum number of allowed passes through the data.
- [var optimizationStrategy: OptimizationStrategy](./optimizationstrategy.md)
  The optimization strategy.
- [var scaleFeatures: Bool](./scalefeatures.md)
  A Boolean value indicating whether to scale the input features.
- [var stepSize: Double](./stepsize.md)
  The starting step size to use for the solver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/linearregressor/configuration-swift.struct/l1penalty)*