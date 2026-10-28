# parallelTreeCount

**Framework**: Create ML Components  
**Kind**: property  
**Role**: Instance Property

The number of parallel trees constructed during each iteration.

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
var parallelTreeCount: Int
```

## Discussion

Use a value greater than one to train a boosted random forest.

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
- [var minimumLossReduction: Double](./minimumlossreduction.md)
  Minimum loss reduction required to further split a node during the tree learning phase.
- [var randomSeed: Int](./randomseed.md)
  A seed to generate reproducible results from random operations such as column and row subsampling.
- [var rowSubsample: Double](./rowsubsample.md)
  Subsample ratio of the training set in each iteration of tree construction.
- [var stepSize: Double](./stepsize.md)
  The step size shrinking.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/boostedtreeconfiguration/paralleltreecount)*