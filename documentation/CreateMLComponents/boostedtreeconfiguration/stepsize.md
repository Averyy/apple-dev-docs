# stepSize

**Framework**: Create ML Components  
**Kind**: property  
**Role**: Instance Property

The step size shrinking.

**Availability**:
- iOS 16.0+ - Deprecated in 17.0 (renamed: learningRate)
- iPadOS 16.0+ - Deprecated in 17.0 (renamed: learningRate)
- Mac Catalyst 16.0+ - Deprecated in 17.0 (renamed: learningRate)
- macOS 13.0+ - Deprecated in 14.0 (renamed: learningRate)
- tvOS 16.0+ - Deprecated in 17.0 (renamed: learningRate)
- visionOS 1.0+
- watchOS 11.0+

## Declaration

```swift
var stepSize: Double { get set }
```

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
- [var parallelTreeCount: Int](./paralleltreecount.md)
  The number of parallel trees constructed during each iteration.
- [var randomSeed: Int](./randomseed.md)
  A seed to generate reproducible results from random operations such as column and row subsampling.
- [var rowSubsample: Double](./rowsubsample.md)
  Subsample ratio of the training set in each iteration of tree construction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/boostedtreeconfiguration/stepsize)*