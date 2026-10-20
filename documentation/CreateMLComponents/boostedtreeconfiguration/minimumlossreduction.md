# minimumLossReduction

**Framework**: Create ML Components  
**Kind**: property  
**Role**: Instance Property

Minimum loss reduction required to further split a node during the tree learning phase.

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
var minimumLossReduction: Double
```

#### Discussion

Larger values can help prevent overfitting by avoiding splits that do not sufficiently reduce the loss function. Defaults to 0.

## See Also

### Inspecting the configuration
- [var columnSubsample: Double](./columnsubsample.md)
  Subsample ratio of the columns in each iteration of tree construction.
- [var earlyStoppingIterationCount: Int?](./earlystoppingiterationcount.md)
  Stops training after this number of iterations where the validation metric does not improve.
- [var learningRate: Double](./learningrate.md)
  The learning rate.
- [var maximumDepth: Int](./maximumdepth.md)
  Maximum tree depth.
- [var maximumIterations: Int](./maximumiterations.md)
  Maximum number of iterations.
- [var minimumChildWeight: Double](./minimumchildweight.md)
  The minimum weight of each leaf node.
- [var parallelTreeCount: Int](./paralleltreecount.md)
  The number of parallel trees constructed during each iteration.
- [var randomSeed: Int](./randomseed.md)
  A seed to generate reproducible results from random operations such as column and row subsampling.
- [var rowSubsample: Double](./rowsubsample.md)
  Subsample ratio of the training set in each iteration of tree construction.
- [var stepSize: Double](./stepsize.md)
  The step size shrinking.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/boostedtreeconfiguration/minimumlossreduction)*