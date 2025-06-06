# FullyConnectedNetworkRegressor

**Framework**: Create ML Components  
**Kind**: struct

A regressor that uses a fully connected network.

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
struct FullyConnectedNetworkRegressor<Scalar> where Scalar : MLShapedArrayScalar, Scalar : BinaryFloatingPoint
```

## Topics

### Creating the regressor
- [init(configuration: FullyConnectedNetworkConfiguration)](fullyconnectednetworkregressor/init(configuration:).md)
  Creates a fully connected network regressor.
### Getting the configuration
- [var configuration: FullyConnectedNetworkConfiguration](fullyconnectednetworkregressor/configuration.md)
  The fully-connected-network configuration.
### Decoding a regressor
- [func decode(from: inout any EstimatorDecoder) throws -> FullyConnectedNetworkRegressorModel<Scalar>](fullyconnectednetworkregressor/decode(from:).md)
  Decodes the estimator.
### Fitting a regressor
- [func fitted<Input>(to: Input, eventHandler: EventHandler?) async throws -> FullyConnectedNetworkRegressor<Scalar>.Transformer](fullyconnectednetworkregressor/fitted(to:eventhandler:).md)
  Fits a fully connected network regressor model to a sequence of examples.
- [func fitted<Input, Validation>(to: Input, validateOn: Validation, eventHandler: EventHandler?) async throws -> FullyConnectedNetworkRegressorModel<Scalar>](fullyconnectednetworkregressor/fitted(to:validateon:eventhandler:).md)
  Fits a fully connected network regressor model to a sequence of examples.
- [FullyConnectedNetworkRegressor.Annotation](fullyconnectednetworkregressor/annotation.md)
  The annotation type.
- [FullyConnectedNetworkRegressor.Transformer](fullyconnectednetworkregressor/transformer.md)
  The transformer type created by this estimator.
### Default Implementations
- [SupervisedEstimator Implementations](fullyconnectednetworkregressor/supervisedestimator-implementations.md)
- [UpdatableSupervisedEstimator Implementations](fullyconnectednetworkregressor/updatablesupervisedestimator-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Sendable](../Swift/Sendable.md)
- [SupervisedEstimator](supervisedestimator.md)
- [UpdatableSupervisedEstimator](updatablesupervisedestimator.md)

## See Also

- [protocol Regressor](regressor.md)
  A transformer that predicts a float value.
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
- [struct FullyConnectedNetworkRegressorModel](fullyconnectednetworkregressormodel.md)
  A regressor model that uses a fully connected network.
- [struct BoostedTreeRegressor](boostedtreeregressor.md)
  A gradient boosted decision tree regressor.
- [struct TreeRegressorModel](treeregressormodel.md)
  A trained tree regressor model.
- [enum OptimizationStrategy](optimizationstrategy.md)
  A linear optimization strategy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/fullyconnectednetworkregressor)*