# l2Penalty

**Framework**: Create ML Components  
**Kind**: property

Weight of the L2 regularization term.

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
var l2Penalty: Double
```

#### Discussion

The larger this weight, the more the model coefficients shrink toward 0. This introduces bias into the model but decreases variance, potentially leading to better predictions. The default value is 0.01; setting this parameter to 0 corresponds to unregularized logistic regression.

## See Also

- [var convergenceThreshold: Double](linearregressor/configuration-swift.struct/convergencethreshold.md)
  The convergence threshold.
- [var earlyStopIterationCount: Int](linearregressor/configuration-swift.struct/earlystopiterationcount.md)
  The number of iterations to use when evaluating whether to stop early.
- [var l1Penalty: Double](linearregressor/configuration-swift.struct/l1penalty.md)
  Weight of the L1 regularization term.
- [var maximumIterations: Int](linearregressor/configuration-swift.struct/maximumiterations.md)
  The maximum number of allowed passes through the data.
- [var optimizationStrategy: OptimizationStrategy](linearregressor/configuration-swift.struct/optimizationstrategy.md)
  The optimization strategy.
- [var scaleFeatures: Bool](linearregressor/configuration-swift.struct/scalefeatures.md)
  A Boolean value indicating whether to scale the input features.
- [var stepSize: Double](linearregressor/configuration-swift.struct/stepsize.md)
  The starting step size to use for the solver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/linearregressor/configuration-swift.struct/l2penalty)*