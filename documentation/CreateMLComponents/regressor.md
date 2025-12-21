# Regressor

**Framework**: Create ML Components  
**Kind**: protocol

A transformer that predicts a float value.

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
protocol Regressor : Transformer where Self.Output : FloatingPoint
```

## Topics

### Performing the prediction
- [func prediction(from:)](regressor/prediction(from:).md)
  Performs a prediction from a single input.

## Relationships

### Inherits From
- [Transformer](transformer.md)
### Conforming Types
- [FullyConnectedNetworkRegressorModel](fullyconnectednetworkregressormodel.md)
- [LinearRegressorModel](linearregressormodel.md)
- [MLModelRegressorAdaptor](mlmodelregressoradaptor.md)

## See Also

- [struct LinearRegressor](linearregressor.md)
  A linear regressor.
- [struct LinearRegressorModel](linearregressormodel.md)
  A trained linear regressor model.
- [struct MultivariateLinearRegressor](multivariatelinearregressor.md)
  A multivariate linear regressor.
- [struct MultivariateLinearRegressorConfiguration](multivariatelinearregressorconfiguration.md)
  A linear regressor configuration.
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

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/regressor)*