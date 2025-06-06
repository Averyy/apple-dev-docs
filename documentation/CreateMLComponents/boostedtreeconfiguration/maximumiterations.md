# maximumIterations

**Framework**: Create ML Components  
**Kind**: property

Maximum number of iterations.

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

## See Also

- [var columnSubsample: Double](boostedtreeconfiguration/columnsubsample.md)
  Subsample ratio of the columns in each iteration of tree construction.
- [var earlyStoppingIterationCount: Int?](boostedtreeconfiguration/earlystoppingiterationcount.md)
  Stops training after this number of iterations where the validation metric does not improve.
- [var learningRate: Double](boostedtreeconfiguration/learningrate.md)
  The learning rate.
- [var maximumDepth: Int](boostedtreeconfiguration/maximumdepth.md)
  Maximum tree depth.
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

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/boostedtreeconfiguration/maximumiterations)*