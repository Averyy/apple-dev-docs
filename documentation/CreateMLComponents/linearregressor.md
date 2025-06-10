# LinearRegressor

**Framework**: Create ML Components  
**Kind**: struct

A linear regressor.

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
struct LinearRegressor<Scalar> where Scalar : MLShapedArrayScalar, Scalar : BinaryFloatingPoint
```

## Topics

### Creating a regressor
- [init(configuration: LinearRegressor<Scalar>.Configuration)](linearregressor/init(configuration:).md)
  Creates a linear regressor.
- [LinearRegressor.Configuration](linearregressor/configuration-swift.struct.md)
  A linear regressor configuration.
### Getting the configuration
- [var configuration: LinearRegressor<Scalar>.Configuration](linearregressor/configuration-swift.property.md)
  The linear regressor configuration.
### Encoding and decoding
- [func encode(LinearRegressorModel<Scalar>, to: inout any EstimatorEncoder) throws](linearregressor/encode(_:to:).md)
  Encodes a fitted transformer.
- [func decode(from: inout any EstimatorDecoder) throws -> LinearRegressorModel<Scalar>](linearregressor/decode(from:).md)
  Decodes a previously fitted transformer.
### Fitting
- [func fitted<Input>(to: Input, eventHandler: EventHandler?) async throws -> LinearRegressorModel<Scalar>](linearregressor/fitted(to:eventhandler:).md)
  Fits a linear regressor model to a sequence of examples.
- [func fitted<Input, Validation>(to: Input, validateOn: Validation, eventHandler: EventHandler?) async throws -> LinearRegressorModel<Scalar>](linearregressor/fitted(to:validateon:eventhandler:).md)
  Fits a linear regressor model to a sequence of examples.
- [LinearRegressor.Annotation](linearregressor/annotation.md)
  The annotation type.
- [LinearRegressor.Transformer](linearregressor/transformer.md)
  The transformer type created by this estimator.
### Default Implementations
- [SupervisedEstimator Implementations](linearregressor/supervisedestimator-implementations.md)
- [UpdatableSupervisedEstimator Implementations](linearregressor/updatablesupervisedestimator-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SupervisedEstimator](supervisedestimator.md)
- [UpdatableSupervisedEstimator](updatablesupervisedestimator.md)

## See Also

- [protocol Regressor](regressor.md)
  A transformer that predicts a float value.
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

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/linearregressor)*