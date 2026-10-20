# LinearRegressorModel

**Framework**: Create ML Components  
**Kind**: struct  
**Role**: Structure

A trained linear regressor model.

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
struct LinearRegressorModel<Scalar> where Scalar : MLShapedArrayScalar, Scalar : BinaryFloatingPoint
```

## Topics

### Creating a regressor model
- [init(coefficients: some Sequence<Scalar>)](./linearregressormodel/init%28coefficients%29.md)
  Creates a linear regression model.
### Getting the properties
- [var featureCount: Int](./linearregressormodel/featurecount.md)
  The number of features expected in the input.
- [var coefficients: [Scalar]](./linearregressormodel/coefficients.md)
  The linear coefficients.
### Performing the regression
- [func applied(to: MLShapedArray<Scalar>, eventHandler: EventHandler?) async throws -> Scalar](./linearregressormodel/applied%28to,eventhandler%29.md)
  Performs a regression on a single input.

## Relationships

### Conforms To
- [Regressor](./regressor.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [Transformer](./transformer.md)

## See Also

### Regressors
- [protocol Regressor](./regressor.md)
  A transformer that predicts a float value.
- [struct LinearRegressor](./linearregressor.md)
  A linear regressor.
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
- [struct BoostedTreeRegressor](./boostedtreeregressor.md)
  A gradient boosted decision tree regressor.
- [struct TreeRegressorModel](./treeregressormodel.md)
  A trained tree regressor model.
- [enum OptimizationStrategy](./optimizationstrategy.md)
  A linear optimization strategy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/linearregressormodel)*