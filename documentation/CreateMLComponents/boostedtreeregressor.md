# BoostedTreeRegressor

**Framework**: Create ML Components  
**Kind**: struct  
**Role**: Structure

A gradient boosted decision tree regressor.

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
struct BoostedTreeRegressor<Annotation>
```

## Topics

### Creating a regressor
- [init(annotationColumnName: String, featureColumnNames: [String], configuration: BoostedTreeConfiguration)](./boostedtreeregressor/init%28annotationcolumnname,featurecolumnnames,configuration%29.md)
  Creates a boosted tree regressor.
### Getting the properties
- [var annotationColumnID: ColumnID<Annotation>](./boostedtreeregressor/annotationcolumnid.md)
  The annotation column identifier.
- [var configuration: BoostedTreeConfiguration](./boostedtreeregressor/configuration.md)
  Boosted tree configuration.
- [var featureColumnNames: [String]](./boostedtreeregressor/featurecolumnnames.md)
  The names of the columns containing feature values.
### Fitting a regressor model
- [func fitted(to: DataFrame, validateOn: DataFrame?, eventHandler: EventHandler?) async throws -> TreeRegressorModel](./boostedtreeregressor/fitted%28to,validateon,eventhandler%29.md)
  Fits a boosted tree regressor model to a collection of examples.
- [BoostedTreeRegressor.Transformer](./boostedtreeregressor/transformer.md)
  The transformer type created by this estimator.
### Encoding and decoding a regressor
- [func encodeWithOptimizer(TreeRegressorModel, to: inout any EstimatorEncoder) throws](./boostedtreeregressor/encodewithoptimizer%28_,to%29.md)
  Encodes the transformer and optimizer to an encoder.
- [func decodeWithOptimizer(from: inout any EstimatorDecoder) throws -> TreeRegressorModel](./boostedtreeregressor/decodewithoptimizer%28from%29.md)
  Reads the encoded transformer and optimizer with a decoder.
### Default Implementations
- [UpdatableSupervisedTabularEstimator Implementations](./boostedtreeregressor/updatablesupervisedtabularestimator-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/copyable.md)
- [Escapable](../Swift/escapable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [SupervisedTabularEstimator](./supervisedtabularestimator.md)
- [UpdatableSupervisedTabularEstimator](./updatablesupervisedtabularestimator.md)

## See Also

### Regressors
- [protocol Regressor](./regressor.md)
  A transformer that predicts a float value.
- [struct LinearRegressor](./linearregressor.md)
  A linear regressor.
- [struct LinearRegressorModel](./linearregressormodel.md)
  A trained linear regressor model.
- [struct MultivariateLinearRegressor](./multivariatelinearregressor.md)
  A multivariate linear regressor.
- [struct MultivariateLinearRegressorConfiguration](./multivariatelinearregressorconfiguration.md)
  A linear regressor configuration.
- [MultivariateLinearRegressor.Model](./multivariatelinearregressor/model.md)
  A trained multivariate linear regressor model.
- [struct FullyConnectedNetworkRegressor](./fullyconnectednetworkregressor.md)
  A regressor that uses a fully connected network.
- [struct FullyConnectedNetworkRegressorModel](./fullyconnectednetworkregressormodel.md)
  A regressor model that uses a fully connected network.
- [struct TreeRegressorModel](./treeregressormodel.md)
  A trained tree regressor model.
- [enum OptimizationStrategy](./optimizationstrategy.md)
  A linear optimization strategy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/boostedtreeregressor)*