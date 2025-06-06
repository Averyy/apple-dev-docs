# MultivariateLinearRegressor

**Framework**: Create ML Components  
**Kind**: struct

A multivariate linear regressor.

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
struct MultivariateLinearRegressor<Scalar> where Scalar : MLShapedArrayScalar, Scalar : BinaryFloatingPoint
```

#### Overview

Unlike a [`LinearRegressor`](linearregressor.md), a [`MultivariateLinearRegressor`](multivariatelinearregressor.md) supports shaped array outputs with any number of elements. It also provides a wider range of training options better suited for large multi-dimensional regression.

> **Note**: Only `Float` and `Double` are currently supported as the Scalar type. You may get faster training when using `Float`.

Only `Float` and `Double` are currently supported as the Scalar type. You may get faster training when using `Float`.

## Topics

### Creating a regressor
- [init(configuration: MultivariateLinearRegressor<Scalar>.Configuration)](multivariatelinearregressor/init(configuration:).md)
  Creates a multivariate linear regressor.
### Getting the configuration
- [var configuration: MultivariateLinearRegressor<Scalar>.Configuration](multivariatelinearregressor/configuration-swift.property.md)
  The linear regressor configuration.
### Fitting
- [func fitted(to: some Sequence<AnnotatedFeature<MLShapedArray<Scalar>, MLShapedArray<Scalar>>>, eventHandler: EventHandler?) async throws -> MultivariateLinearRegressor<Scalar>.Model](multivariatelinearregressor/fitted(to:eventhandler:).md)
  Fits a linear regressor model to a sequence of annotated features.
- [func fitted(to: some Sequence<AnnotatedFeature<MLShapedArray<Scalar>, MLShapedArray<Scalar>>>, validateOn: some Sequence<AnnotatedFeature<MLShapedArray<Scalar>, MLShapedArray<Scalar>>>, eventHandler: EventHandler?) async throws -> MultivariateLinearRegressor<Scalar>.Model](multivariatelinearregressor/fitted(to:validateon:eventhandler:)-9bluu.md)
  Fits a linear regressor model to a sequence of annotated features.
- [func fitted(to: AnnotatedBatch<Scalar>, validateOn: AnnotatedBatch<Scalar>?, eventHandler: EventHandler?) async throws -> MultivariateLinearRegressor<Scalar>.Model](multivariatelinearregressor/fitted(to:validateon:eventhandler:)-82szq.md)
  Fits a linear regressor model to shaped arrays of features and annotations.
### Fitting Progressively
- [func makeTransformer() -> MultivariateLinearRegressor<Scalar>.Model](multivariatelinearregressor/maketransformer.md)
  Creates a default-initialized model suitable for incremental fitting.
- [func update(inout MultivariateLinearRegressor<Scalar>.Model, with: some Sequence<AnnotatedFeature<MLShapedArray<Scalar>, MLShapedArray<Scalar>>>, eventHandler: EventHandler?) async throws](multivariatelinearregressor/update(_:with:eventhandler:).md)
  Updates a model with a new sequence of examples.
- [func update(inout MultivariateLinearRegressor<Scalar>.Model, with: AnnotatedBatch<Scalar>) async throws -> Scalar](multivariatelinearregressor/update(_:with:).md)
  Updates a model with a new shaped array of examples.
### Encoding and decoding
- [func encode(MultivariateLinearRegressor<Scalar>.Model, to: inout any EstimatorEncoder) throws](multivariatelinearregressor/encode(_:to:).md)
  Encodes a fitted transformer.
- [func decode(from: inout any EstimatorDecoder) throws -> MultivariateLinearRegressor<Scalar>.Model](multivariatelinearregressor/decode(from:).md)
  Decodes a previously fitted transformer.
- [func encodeWithOptimizer(MultivariateLinearRegressor<Scalar>.Model, to: inout any EstimatorEncoder) throws](multivariatelinearregressor/encodewithoptimizer(_:to:).md)
  Encodes the model and optimizer to an encoder.
- [func decodeWithOptimizer(from: inout any EstimatorDecoder) throws -> MultivariateLinearRegressor<Scalar>.Model](multivariatelinearregressor/decodewithoptimizer(from:).md)
  Reads the encoded model and optimizer with a decoder.
### Structures
- [MultivariateLinearRegressor.Model](multivariatelinearregressor/model.md)
  A trained multivariate linear regressor model.
### Type Aliases
- [MultivariateLinearRegressor.Annotation](multivariatelinearregressor/annotation.md)
  The annotation type.
- [MultivariateLinearRegressor.Configuration](multivariatelinearregressor/configuration-swift.typealias.md)
- [MultivariateLinearRegressor.Feature](multivariatelinearregressor/feature.md)
  The feature type.
- [MultivariateLinearRegressor.Transformer](multivariatelinearregressor/transformer.md)
  The transformer type created by this estimator.
### Default Implementations
- [SupervisedEstimator Implementations](multivariatelinearregressor/supervisedestimator-implementations.md)
- [UpdatableSupervisedEstimator Implementations](multivariatelinearregressor/updatablesupervisedestimator-implementations.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/multivariatelinearregressor)*