# MultivariateLinearRegressor.Model

**Framework**: Create ML Components  
**Kind**: struct

A trained multivariate linear regressor model.

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
struct Model
```

#### Overview

> **Note**: Only `Float` and `Double` are currently supported as the Scalar type.

## Topics

### Creating a regressor model
- [init(weight: MLShapedArray<Scalar>, bias: MLShapedArray<Scalar>?)](multivariatelinearregressor/model/init(weight:bias:).md)
  Creates a multivariate linear regressor.
### Getting the properties
- [var inputSize: Int](multivariatelinearregressor/model/inputsize.md)
  The input size.
- [var outputSize: Int](multivariatelinearregressor/model/outputsize.md)
  The output size.
- [var weight: MLShapedArray<Scalar>](multivariatelinearregressor/model/weight.md)
  The linear coefficients.
- [var bias: MLShapedArray<Scalar>?](multivariatelinearregressor/model/bias.md)
  The bias coefficients.
### Performing the regression
- [func applied(to: MLShapedArray<Scalar>, eventHandler: EventHandler?) async throws -> MLShapedArray<Scalar>](multivariatelinearregressor/model/applied(to:eventhandler:).md)
  Performs a prediction on a shaped array.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [Transformer](transformer.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/multivariatelinearregressor/model)*