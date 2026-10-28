# maximumIterationCount

**Framework**: Create ML Components  
**Kind**: property  
**Role**: Instance Property

The maximum number of allowed passes through the data.

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
var maximumIterationCount: Int
```

## Discussion

More passes over the data can result in a more accurately trained model. Consider increasing this if the training accuracy is low. Defaults to 25.

> **Note**: This parameter is only used by the `fitted` method. When using the `update` method it’s up to you to decide when to stop.

## See Also

### Getting the properties
- [var batchSize: Int](./batchsize.md)
  The number of examples in each training batch.
- [var earlyStoppingTolerance: Float](./earlystoppingtolerance.md)
  The early-stopping tolerance.
- [var earlyStoppingIterationCount: Int](./earlystoppingiterationcount.md)
  The number of iterations to use when evaluating whether to stop early.
- [var learningRate: Float](./learningrate.md)
  The optimizer learning rate.
- [var randomSeed: Int?](./randomseed.md)
  A seed to generate reproducible results from random operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/multivariatelinearregressorconfiguration/maximumiterationcount)*