# OptimizationStrategy

**Framework**: Create ML Components  
**Kind**: enum

A linear optimization strategy.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 11.0+

## Declaration

```swift
enum OptimizationStrategy
```

## Topics

### Optimization strategies
- [OptimizationStrategy.automatic](optimizationstrategy/automatic.md)
  Chooses the best optimization strategy based on the problem size and configuration.
- [OptimizationStrategy.fast](optimizationstrategy/fast.md)
  An optimization strategy that minimizes computation time.
- [OptimizationStrategy.lowMemory](optimizationstrategy/lowmemory.md)
  An optimization strategy that minimizes memory use.
- [OptimizationStrategy.nonSmooth](optimizationstrategy/nonsmooth.md)
  An optimization strategy that can handle non-smooth problems.
### Creating an optimization strategy
- [init(from: any Decoder) throws](optimizationstrategy/init(from:).md)
  Creates a new instance by decoding from the given decoder.
### Operators
- [static func == (OptimizationStrategy, OptimizationStrategy) -> Bool](optimizationstrategy/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var hashValue: Int](optimizationstrategy/hashvalue.md)
  The hash value.
### Instance Methods
- [func encode(to: any Encoder) throws](optimizationstrategy/encode(to:).md)
  Encodes this value into the given encoder.
- [func hash(into: inout Hasher)](optimizationstrategy/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](optimizationstrategy/equatable-implementations.md)

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/optimizationstrategy)*