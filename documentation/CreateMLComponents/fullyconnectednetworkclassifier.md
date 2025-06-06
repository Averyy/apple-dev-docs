# FullyConnectedNetworkClassifier

**Framework**: Create ML Components  
**Kind**: struct

A classifier that uses a fully connected network.

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
struct FullyConnectedNetworkClassifier<Scalar, Label> where Scalar : MLShapedArrayScalar, Scalar : BinaryFloatingPoint, Label : Comparable, Label : Decodable, Label : Encodable, Label : Hashable
```

## Mentions

- [Creating a multi-label image classifier](creating-a-multi-label-image-classifier.md)

## Topics

### Creating the classifier
- [init(labels: Set<Label>, configuration: FullyConnectedNetworkConfiguration)](fullyconnectednetworkclassifier/init(labels:configuration:).md)
  Creates a fully connected network classifier.
### Getting the properties
- [var labels: Set<Label>](fullyconnectednetworkclassifier/labels.md)
  The set of possible labels.
- [var configuration: FullyConnectedNetworkConfiguration](fullyconnectednetworkclassifier/configuration.md)
  The fully-connected-network configuration.
### Encoding and decoding
- [func encode(Self.Transformer, to: inout any EstimatorEncoder) throws](fullyconnectednetworkclassifier/encode(_:to:).md)
  Encodes a fitted encodable transformer.
- [func decode(from: inout any EstimatorDecoder) throws -> FullyConnectedNetworkClassifierModel<Scalar, Label>](fullyconnectednetworkclassifier/decode(from:).md)
  Decodes the estimator.
### Fitting a classifier
- [func fitted<Input>(to: Input, eventHandler: EventHandler?) async throws -> FullyConnectedNetworkClassifierModel<Scalar, Label>](fullyconnectednetworkclassifier/fitted(to:eventhandler:).md)
  Fits a fully connected network classifier model to a sequence of examples.
- [func fitted<Input, Validation>(to: Input, validateOn: Validation, eventHandler: EventHandler?) async throws -> FullyConnectedNetworkClassifierModel<Scalar, Label>](fullyconnectednetworkclassifier/fitted(to:validateon:eventhandler:).md)
  Fits a fully connected network classifier model to a sequence of examples.
- [FullyConnectedNetworkClassifier.Annotation](fullyconnectednetworkclassifier/annotation.md)
  The annotation type.
- [FullyConnectedNetworkClassifier.Transformer](fullyconnectednetworkclassifier/transformer.md)
  The transformer type created by this estimator.
### Default Implementations
- [SupervisedEstimator Implementations](fullyconnectednetworkclassifier/supervisedestimator-implementations.md)
- [UpdatableSupervisedEstimator Implementations](fullyconnectednetworkclassifier/updatablesupervisedestimator-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Sendable](../Swift/Sendable.md)
- [SupervisedEstimator](supervisedestimator.md)
- [UpdatableSupervisedEstimator](updatablesupervisedestimator.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/fullyconnectednetworkclassifier)*