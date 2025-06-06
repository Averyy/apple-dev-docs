# LogisticRegressionClassifier

**Framework**: Create ML Components  
**Kind**: struct

A logistic regression classifier.

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
struct LogisticRegressionClassifier<Scalar, Label> where Scalar : MLShapedArrayScalar, Scalar : BinaryFloatingPoint, Label : Comparable, Label : Decodable, Label : Encodable, Label : Hashable
```

## Topics

### Creating a classifier
- [init(labels: Set<Label>, configuration: LogisticRegressionClassifier<Scalar, Label>.Configuration)](logisticregressionclassifier/init(labels:configuration:).md)
  Creates a logistic regression classifier.
- [LogisticRegressionClassifier.Configuration](logisticregressionclassifier/configuration-swift.struct.md)
  A logistic regression classifier configuration.
### Getting the properties
- [var configuration: LogisticRegressionClassifier<Scalar, Label>.Configuration](logisticregressionclassifier/configuration-swift.property.md)
  The logistic regression classifier configuration.
- [var labels: Set<Label>](logisticregressionclassifier/labels.md)
  The set of possible labels.
### Encoding and decoding
- [func encode(LogisticRegressionClassifierModel<Scalar, Label>, to: inout any EstimatorEncoder) throws](logisticregressionclassifier/encode(_:to:).md)
  Encodes a fitted transformer.
- [func decode(from: inout any EstimatorDecoder) throws -> LogisticRegressionClassifierModel<Scalar, Label>](logisticregressionclassifier/decode(from:).md)
  Decodes a previously fitted transformer.
### Fitting
- [func fitted<Input>(to: Input, eventHandler: EventHandler?) async throws -> LogisticRegressionClassifier<Scalar, Label>.Transformer](logisticregressionclassifier/fitted(to:eventhandler:).md)
  Fits a logistic regression classifier model to a sequence of examples while validating with a validation sequence.
- [func fitted<Input, Validation>(to: Input, validateOn: Validation, eventHandler: EventHandler?) async throws -> LogisticRegressionClassifierModel<Scalar, Label>](logisticregressionclassifier/fitted(to:validateon:eventhandler:).md)
  Fits a logistic regression classifier model to a sequence of examples.
- [LogisticRegressionClassifier.Annotation](logisticregressionclassifier/annotation.md)
  The annotation type.
- [LogisticRegressionClassifier.Transformer](logisticregressionclassifier/transformer.md)
  The transformer type created by this estimator.
### Default Implementations
- [SupervisedEstimator Implementations](logisticregressionclassifier/supervisedestimator-implementations.md)
- [UpdatableSupervisedEstimator Implementations](logisticregressionclassifier/updatablesupervisedestimator-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Sendable](../Swift/Sendable.md)
- [SupervisedEstimator](supervisedestimator.md)
- [UpdatableSupervisedEstimator](updatablesupervisedestimator.md)

## See Also

- [protocol Classifier](classifier.md)
  An estimator that predicts classification probabilities.
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
- [struct TimeSeriesClassifierConfiguration](timeseriesclassifierconfiguration.md)
  The configuration for a time-series classifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/logisticregressionclassifier)*