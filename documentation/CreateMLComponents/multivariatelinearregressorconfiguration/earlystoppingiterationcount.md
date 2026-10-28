# earlyStoppingIterationCount

**Framework**: Create ML Components  
**Kind**: property  
**Role**: Instance Property

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

## Discussion

The `fitted` method will stop if no significant progress is made for this many iterations. Significant progress happens when the validation error decreases by at least `convergenceThreshold`.

> **Note**: Early stopping only happens when using the `fitted` method with validation data.

## See Also

### Getting the properties
- [var batchSize: Int](./batchsize.md)
  The number of examples in each training batch.
- [var maximumIterationCount: Int](./maximumiterationcount.md)
  The maximum number of allowed passes through the data.
- [var earlyStoppingTolerance: Float](./earlystoppingtolerance.md)
  The early-stopping tolerance.
- [var learningRate: Float](./learningrate.md)
  The optimizer learning rate.
- [var randomSeed: Int?](./randomseed.md)
  A seed to generate reproducible results from random operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/multivariatelinearregressorconfiguration/earlystoppingiterationcount)*