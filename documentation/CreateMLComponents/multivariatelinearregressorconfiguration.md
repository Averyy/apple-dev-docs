# MultivariateLinearRegressorConfiguration

**Framework**: Create ML Components  
**Kind**: struct

A linear regressor configuration.

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
struct MultivariateLinearRegressorConfiguration
```

## Topics

### Creating a configuration
- [init()](multivariatelinearregressorconfiguration/init.md)
  Creates a default linear regressor configuration.
### Getting the properties
- [var batchSize: Int](multivariatelinearregressorconfiguration/batchsize.md)
  The number of examples in each training batch.
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

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [protocol Regressor](regressor.md)
  A transformer that predicts a float value.
- [struct LinearRegressor](linearregressor.md)
  A linear regressor.
- [struct LinearRegressorModel](linearregressormodel.md)
  A trained linear regressor model.
- [struct MultivariateLinearRegressor](multivariatelinearregressor.md)
  A multivariate linear regressor.
- [MultivariateLinearRegressor.Model](multivariatelinearregressor/model.md)
  A trained multivariate linear regressor model.
- [struct FullyConnectedNetworkRegressor](fullyconnectednetworkregressor.md)
  A regressor that uses a fully connected network.
- [struct FullyConnectedNetworkRegressorModel](fullyconnectednetworkregressormodel.md)
  A regressor model that uses a fully connected network.
- [struct BoostedTreeRegressor](boostedtreeregressor.md)
  A gradient boosted decision tree regressor.
- [struct TreeRegressorModel](treeregressormodel.md)
  A trained tree regressor model.
- [enum OptimizationStrategy](optimizationstrategy.md)
  A linear optimization strategy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/multivariatelinearregressorconfiguration)*