# earlyStopIterationCount

**Framework**: Create ML Components  
**Kind**: property

The number of iterations to use when evaluating whether to stop early.

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
var earlyStopIterationCount: Int
```

#### Discussion

The `fitted` method will stop if no significant progress is made for this many iterations. Significant progress happens when the validation error decreases by at least `convergenceThreshold`.

> **Note**: Early stopping only happens when using the `fitted` method with validation data.

Early stopping only happens when using the `fitted` method with validation data.

## See Also

- [var convergenceThreshold: Double](linearregressor/configuration-swift.struct/convergencethreshold.md)
  The convergence threshold.
- [var l1Penalty: Double](linearregressor/configuration-swift.struct/l1penalty.md)
  Weight of the L1 regularization term.
- [var l2Penalty: Double](linearregressor/configuration-swift.struct/l2penalty.md)
  Weight of the L2 regularization term.
- [var maximumIterations: Int](linearregressor/configuration-swift.struct/maximumiterations.md)
  The maximum number of allowed passes through the data.
- [var optimizationStrategy: OptimizationStrategy](linearregressor/configuration-swift.struct/optimizationstrategy.md)
  The optimization strategy.
- [var scaleFeatures: Bool](linearregressor/configuration-swift.struct/scalefeatures.md)
  A Boolean value indicating whether to scale the input features.
- [var stepSize: Double](linearregressor/configuration-swift.struct/stepsize.md)
  The starting step size to use for the solver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/linearregressor/configuration-swift.struct/earlystopiterationcount)*