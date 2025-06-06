# earlyStoppingIterationCount

**Framework**: Create ML Components  
**Kind**: property

The number of iterations to use when evaluating whether to stop early.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
var earlyStoppingIterationCount: Int
```

#### Discussion

The `fitted` method will stop if no significant progress is made for this many iterations. Significant progress happens when the validation error decreases by at least `convergenceThreshold`.

> **Note**: Early stopping only happens when using the `fitted` method with validation data.

Early stopping only happens when using the `fitted` method with validation data.

## See Also

- [var batchSize: Int](multivariatelinearregressorconfiguration/batchsize.md)
  The number of examples in each training batch.
- [var maximumIterationCount: Int](multivariatelinearregressorconfiguration/maximumiterationcount.md)
  The maximum number of allowed passes through the data.
- [var earlyStoppingTolerance: Float](multivariatelinearregressorconfiguration/earlystoppingtolerance.md)
  The early-stopping tolerance.
- [var learningRate: Float](multivariatelinearregressorconfiguration/learningrate.md)
  The optimizer learning rate.
- [var randomSeed: Int?](multivariatelinearregressorconfiguration/randomseed.md)
  A seed to generate reproducible results from random operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/multivariatelinearregressorconfiguration/earlystoppingiterationcount)*