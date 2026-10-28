# earlyStopIterationCount

**Framework**: Create ML Components  
**Kind**: property  
**Role**: Instance Property

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

## Discussion

The `fitted` method will stop if no significant progress is made for this many iterations. Significant progress happens when the validation error decreases by at least `convergenceThreshold`.

> **Note**: Early stopping only happens when using the `fitted` method with validation data.

## See Also

### Getting the properties
- [var convergenceThreshold: Double](./convergencethreshold.md)
  The convergence threshold.
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
- [var stepSize: Double](./stepsize.md)
  The starting step size to use for the solver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/linearregressor/configuration-swift.struct/earlystopiterationcount)*