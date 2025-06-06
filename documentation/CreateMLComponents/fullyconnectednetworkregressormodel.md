# FullyConnectedNetworkRegressorModel

**Framework**: Create ML Components  
**Kind**: struct

A regressor model that uses a fully connected network.

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
struct FullyConnectedNetworkRegressorModel<Scalar> where Scalar : MLShapedArrayScalar, Scalar : BinaryFloatingPoint
```

## Topics

### Creating a regressor model
- [init(from: any Decoder) throws](fullyconnectednetworkregressormodel/init(from:).md)
  Creates a new instance by decoding from the given decoder.
### Performing a regression
- [func applied(to: MLShapedArray<Scalar>, eventHandler: EventHandler?) async throws -> FullyConnectedNetworkRegressorModel<Scalar>.Target](fullyconnectednetworkregressormodel/applied(to:eventhandler:).md)
  Performs regression on a shaped array.
- [FullyConnectedNetworkRegressorModel.Target](fullyconnectednetworkregressormodel/target.md)
### Type Aliases
- [FullyConnectedNetworkRegressorModel.Input](fullyconnectednetworkregressormodel/input.md)
  The input type.
- [FullyConnectedNetworkRegressorModel.Output](fullyconnectednetworkregressormodel/output.md)
  The output type.
### Default Implementations
- [CustomDebugStringConvertible Implementations](fullyconnectednetworkregressormodel/customdebugstringconvertible-implementations.md)
- [Decodable Implementations](fullyconnectednetworkregressormodel/decodable-implementations.md)
- [Encodable Implementations](fullyconnectednetworkregressormodel/encodable-implementations.md)
- [Regressor Implementations](fullyconnectednetworkregressormodel/regressor-implementations.md)
- [Transformer Implementations](fullyconnectednetworkregressormodel/transformer-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Regressor](regressor.md)
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
- [MultivariateLinearRegressor.Model](multivariatelinearregressor/model.md)
  A trained multivariate linear regressor model.
- [struct FullyConnectedNetworkRegressor](fullyconnectednetworkregressor.md)
  A regressor that uses a fully connected network.
- [struct BoostedTreeRegressor](boostedtreeregressor.md)
  A gradient boosted decision tree regressor.
- [struct TreeRegressorModel](treeregressormodel.md)
  A trained tree regressor model.
- [enum OptimizationStrategy](optimizationstrategy.md)
  A linear optimization strategy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/fullyconnectednetworkregressormodel)*