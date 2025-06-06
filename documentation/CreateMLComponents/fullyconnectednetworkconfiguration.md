# FullyConnectedNetworkConfiguration

**Framework**: Create ML Components  
**Kind**: struct

A fully connected network configuration.

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
struct FullyConnectedNetworkConfiguration
```

## Topics

### Creating a network configuration
- [init()](fullyconnectednetworkconfiguration/init.md)
  Creates a default fully-connected-network configuration.
- [init(from: any Decoder) throws](fullyconnectednetworkconfiguration/init(from:).md)
  Creates a new instance by decoding from the given decoder.
### Getting the properties
- [var batchSize: Int](fullyconnectednetworkconfiguration/batchsize.md)
  The number of examples to use per mini-batch.
- [var dropoutProbability: Float](fullyconnectednetworkconfiguration/dropoutprobability.md)
  The dropout probability.
- [var earlyStopIterationCount: Int](fullyconnectednetworkconfiguration/earlystopiterationcount.md)
  The number of iterations to use when evaluating whether to stop early.
- [var earlyStoppingTolerance: Double](fullyconnectednetworkconfiguration/earlystoppingtolerance.md)
  The early-stopping tolerance.
- [var hiddenUnitCounts: [Int]](fullyconnectednetworkconfiguration/hiddenunitcounts.md)
  The number of neurons in each hidden layer.
- [var learningRate: Float](fullyconnectednetworkconfiguration/learningrate.md)
  The learning rate.
- [var maximumIterations: Int](fullyconnectednetworkconfiguration/maximumiterations.md)
  The maximum number of iterations.
- [var randomSeed: Int](fullyconnectednetworkconfiguration/randomseed.md)
  A seed to generate reproducible results from random operations such as column and row subsampling.
### Operators
- [static func == (FullyConnectedNetworkConfiguration, FullyConnectedNetworkConfiguration) -> Bool](fullyconnectednetworkconfiguration/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var hashValue: Int](fullyconnectednetworkconfiguration/hashvalue.md)
  The hash value.
### Instance Methods
- [func encode(to: any Encoder) throws](fullyconnectednetworkconfiguration/encode(to:).md)
  Encodes this value into the given encoder.
- [func hash(into: inout Hasher)](fullyconnectednetworkconfiguration/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](fullyconnectednetworkconfiguration/equatable-implementations.md)

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [protocol Classifier](classifier.md)
  An estimator that predicts classification probabilities.
- [struct LogisticRegressionClassifier](logisticregressionclassifier.md)
  A logistic regression classifier.
- [struct LogisticRegressionClassifierModel](logisticregressionclassifiermodel.md)
  A trained logistic regression classifier model.
- [struct BoostedTreeClassifier](boostedtreeclassifier.md)
  A gradient boosted decision tree classifier.
- [struct BoostedTreeConfiguration](boostedtreeconfiguration.md)
  A boosted tree configuration.
- [struct FullyConnectedNetworkClassifier](fullyconnectednetworkclassifier.md)
  A classifier that uses a fully connected network.
- [struct FullyConnectedNetworkClassifierModel](fullyconnectednetworkclassifiermodel.md)
  A classifier model that uses a fully connected network.
- [struct FullyConnectedNetworkMultiLabelClassifier](fullyconnectednetworkmultilabelclassifier.md)
  A classifier that uses a multi-label fully-connected network.
- [struct FullyConnectedNetworkMultiLabelClassifierModel](fullyconnectednetworkmultilabelclassifiermodel.md)
  A multi-label classifier model that uses a fully-connected network.
- [struct TreeClassifierModel](treeclassifiermodel.md)
  A trained tree classifier model.
- [struct TimeSeriesClassifier](timeseriesclassifier.md)
- [struct TimeSeriesClassifierConfiguration](timeseriesclassifierconfiguration.md)
  The configuration for a time-series classifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/fullyconnectednetworkconfiguration)*