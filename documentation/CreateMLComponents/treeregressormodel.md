# TreeRegressorModel

**Framework**: Create ML Components  
**Kind**: struct

A trained tree regressor model.

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
struct TreeRegressorModel
```

## Topics

### Getting the column names
- [var featureColumnNames: [String]](treeregressormodel/featurecolumnnames.md)
  The names of the columns containing feature values.
- [var predictionColumnName: String](treeregressormodel/predictioncolumnname.md)
  The name of the column containing the predicted values.
### Applying
- [func applied(to: DataFrame, eventHandler: EventHandler?) async throws -> DataFrame](treeregressormodel/applied(to:eventhandler:).md)
  Performs a regression on a data frame.
### Type Aliases
- [TreeRegressorModel.Input](treeregressormodel/input.md)
  The input type.
- [TreeRegressorModel.Output](treeregressormodel/output.md)
  The output type.
### Default Implementations
- [CustomDebugStringConvertible Implementations](treeregressormodel/customdebugstringconvertible-implementations.md)
- [TabularTransformer Implementations](treeregressormodel/tabulartransformer-implementations.md)
- [Transformer Implementations](treeregressormodel/transformer-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [Sendable](../Swift/Sendable.md)
- [TabularTransformer](tabulartransformer.md)
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
- [struct FullyConnectedNetworkRegressorModel](fullyconnectednetworkregressormodel.md)
  A regressor model that uses a fully connected network.
- [struct BoostedTreeRegressor](boostedtreeregressor.md)
  A gradient boosted decision tree regressor.
- [enum OptimizationStrategy](optimizationstrategy.md)
  A linear optimization strategy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/treeregressormodel)*