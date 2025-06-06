# learningRate

**Framework**: Create ML Components  
**Kind**: property

The learning rate.

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
var learningRate: Double { get set }
```

#### Discussion

The learning rate controls the step size shrinkage. A smaller learning rate makes the learning process more conservative. Must be in the range [0, 1]. Defaults to 0.3.

## See Also

- [var columnSubsample: Double](boostedtreeconfiguration/columnsubsample.md)
  Subsample ratio of the columns in each iteration of tree construction.
- [var earlyStoppingIterationCount: Int?](boostedtreeconfiguration/earlystoppingiterationcount.md)
  Stops training after this number of iterations where the validation metric does not improve.
- [var maximumDepth: Int](boostedtreeconfiguration/maximumdepth.md)
  Maximum tree depth.
- [var maximumIterations: Int](boostedtreeconfiguration/maximumiterations.md)
  Maximum number of iterations.
- [var minimumChildWeight: Double](boostedtreeconfiguration/minimumchildweight.md)
  The minimum weight of each leaf node.
- [var minimumLossReduction: Double](boostedtreeconfiguration/minimumlossreduction.md)
  Minimum loss reduction required to further split a node during the tree learning phase.
- [var parallelTreeCount: Int](boostedtreeconfiguration/paralleltreecount.md)
  The number of parallel trees constructed during each iteration.
- [var randomSeed: Int](boostedtreeconfiguration/randomseed.md)
  A seed to generate reproducible results from random operations such as column and row subsampling.
- [var rowSubsample: Double](boostedtreeconfiguration/rowsubsample.md)
  Subsample ratio of the training set in each iteration of tree construction.
- [var stepSize: Double](boostedtreeconfiguration/stepsize.md)
  The step size shrinking.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/boostedtreeconfiguration/learningrate)*