# maximumIterations

**Framework**: Create ML Components  
**Kind**: property  
**Role**: Instance Property

The maximum number of allowed passes through the data.

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
var maximumIterations: Int
```

## Discussion

More passes over the data can result in a more accurately trained model. Consider increasing this if the training accuracy is low. Defaults to 25.

> **Note**: This parameter is only used by the `fitted` method. When using the `update` method it’s up to you to decide when to stop.

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
- [var optimizationStrategy: OptimizationStrategy](./optimizationstrategy.md)
  The optimization strategy.
- [var scaleFeatures: Bool](./scalefeatures.md)
  A Boolean value indicating whether to scale the input features.
- [var stepSize: Double](./stepsize.md)
  The starting step size to use for the solver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/linearregressor/configuration-swift.struct/maximumiterations)*