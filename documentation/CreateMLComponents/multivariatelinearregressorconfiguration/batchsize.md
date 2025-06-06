# batchSize

**Framework**: Create ML Components  
**Kind**: property

The number of examples in each training batch.

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
var batchSize: Int
```

#### Discussion

> **Note**: This parameter is only used by the `fitted` method.

This parameter is only used by the `fitted` method.

## See Also

- [var maximumIterationCount: Int](multivariatelinearregressorconfiguration/maximumiterationcount.md)
  The maximum number of allowed passes through the data.
- [var earlyStoppingTolerance: Float](multivariatelinearregressorconfiguration/earlystoppingtolerance.md)
  The early-stopping tolerance.
- [var earlyStoppingIterationCount: Int](multivariatelinearregressorconfiguration/earlystoppingiterationcount.md)
  The number of iterations to use when evaluating whether to stop early.
- [var learningRate: Float](multivariatelinearregressorconfiguration/learningrate.md)
  The optimizer learning rate.
- [var randomSeed: Int?](multivariatelinearregressorconfiguration/randomseed.md)
  A seed to generate reproducible results from random operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/multivariatelinearregressorconfiguration/batchsize)*