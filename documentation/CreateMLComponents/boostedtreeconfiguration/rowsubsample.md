# rowSubsample

**Framework**: Create ML Components  
**Kind**: property

Subsample ratio of the training set in each iteration of tree construction.

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
var rowSubsample: Double
```

#### Discussion

This is called the bagging trick and can usually help prevent overfitting. Setting this to a value of 0.5 results in the model randomly sampling half of the examples (rows) to grow each tree. Must be in the range (0, 1).

## See Also

- [var columnSubsample: Double](boostedtreeconfiguration/columnsubsample.md)
  Subsample ratio of the columns in each iteration of tree construction.
- [var earlyStoppingIterationCount: Int?](boostedtreeconfiguration/earlystoppingiterationcount.md)
  Stops training after this number of iterations where the validation metric does not improve.
- [var learningRate: Double](boostedtreeconfiguration/learningrate.md)
  The learning rate.
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
- [var stepSize: Double](boostedtreeconfiguration/stepsize.md)
  The step size shrinking.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/boostedtreeconfiguration/rowsubsample)*