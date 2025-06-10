# TimeSeriesClassifierConfiguration

**Framework**: Create ML Components  
**Kind**: struct

The configuration for a time-series classifier.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
struct TimeSeriesClassifierConfiguration
```

## Topics

### Operators
- [static func == (TimeSeriesClassifierConfiguration, TimeSeriesClassifierConfiguration) -> Bool](timeseriesclassifierconfiguration/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Initializers
- [init()](timeseriesclassifierconfiguration/init.md)
  Creates a configuration.
- [init(from: any Decoder) throws](timeseriesclassifierconfiguration/init(from:).md)
  Creates a new instance by decoding from the given decoder.
### Instance Properties
- [var batchSize: Int](timeseriesclassifierconfiguration/batchsize.md)
  The number of examples in each training batch.
- [var earlyStoppingIterationCount: Int](timeseriesclassifierconfiguration/earlystoppingiterationcount.md)
  The number of iterations to use when evaluating whether to stop early.
- [var earlyStoppingTolerance: Float](timeseriesclassifierconfiguration/earlystoppingtolerance.md)
  The early-stopping tolerance.
- [var hashValue: Int](timeseriesclassifierconfiguration/hashvalue.md)
  The hash value.
- [var learningRate: Float](timeseriesclassifierconfiguration/learningrate.md)
  The starting learning rate.
- [var maximumIterationCount: Int](timeseriesclassifierconfiguration/maximumiterationcount.md)
  The maximum number of allowed passes through the data.
- [var maximumSequenceLength: Int](timeseriesclassifierconfiguration/maximumsequencelength.md)
  The maximum number of samples that can be classified.
- [var minimumSequenceLength: Int](timeseriesclassifierconfiguration/minimumsequencelength.md)
  The minimum number of samples required to produce a classification.
- [var randomSeed: Int?](timeseriesclassifierconfiguration/randomseed.md)
  A seed to generate reproducible results from random operations.
### Instance Methods
- [func encode(to: any Encoder) throws](timeseriesclassifierconfiguration/encode(to:).md)
  Encodes this value into the given encoder.
- [func hash(into: inout Hasher)](timeseriesclassifierconfiguration/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](timeseriesclassifierconfiguration/equatable-implementations.md)

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

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
- [struct FullyConnectedNetworkConfiguration](fullyconnectednetworkconfiguration.md)
  A fully connected network configuration.
- [struct TreeClassifierModel](treeclassifiermodel.md)
  A trained tree classifier model.
- [struct TimeSeriesClassifier](timeseriesclassifier.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/timeseriesclassifierconfiguration)*